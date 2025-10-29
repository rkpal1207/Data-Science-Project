# retriever/hybrid.py
import numpy as np
import os
import pickle
import chromadb
from sentence_transformers import CrossEncoder

# ------------------ Load Chroma + BM25 ------------------
CHROMA_PATH = os.getenv("CHROMA_PATH", ".chroma")
BM25_PATH = os.path.join(CHROMA_PATH, "bm25.pkl")

TOP_K = int(os.getenv("TOP_K", 8))
VECTOR_WEIGHT = float(os.getenv("VECTOR_WEIGHT", 0.65))
BM25_WEIGHT = float(os.getenv("BM25_WEIGHT", 0.35))

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(name="docs")

# Load BM25 model + metadata
with open(BM25_PATH, "rb") as f:
    bm25_pack = pickle.load(f)

bm25 = bm25_pack["bm25"]
ids = bm25_pack["ids"]
texts = bm25_pack["texts"]
metas = bm25_pack["metas"]

# ------------------ Optional Reranker ------------------
reranker = CrossEncoder("BAAI/bge-reranker-base")  # good balance speed/accuracy


def vector_search(query: str, k: int):
    """Search vector DB (semantic similarity)."""
    res = collection.query(query_texts=[query], n_results=k * 2)
    items = []
    for i in range(len(res["ids"][0])):
        score = 1 - res["distances"][0][i]  # convert cosine distance to similarity
        items.append({
            "chunk_id": res["ids"][0][i],
            "text": res["documents"][0][i],
            "meta": res["metadatas"][0][i],
            "vector_score": float(score)
        })
    return items


def bm25_search(query: str, k: int):
    """Search BM25 index (keyword overlap)."""
    tokenized_query = query.lower().split()
    scores = bm25.get_scores(tokenized_query)
    top_idx = np.argsort(scores)[::-1][:k * 2]
    items = []
    for i in top_idx:
        items.append({
            "chunk_id": ids[i],
            "text": texts[i],
            "meta": metas[i],
            "bm25_score": float(scores[i])
        })
    return items


def hybrid_retrieve(query: str, k: int = TOP_K):
    """Combine vector + BM25 results, merge and rerank."""
    vector_results = vector_search(query, k)
    bm25_results = bm25_search(query, k)

    combined = {}

    # Merge scores
    for item in vector_results:
        cid = item["chunk_id"]
        combined[cid] = {
            "text": item["text"],
            "meta": item["meta"],
            "score": VECTOR_WEIGHT * item["vector_score"]
        }

    for item in bm25_results:
        cid = item["chunk_id"]
        if cid not in combined:
            combined[cid] = {"text": item["text"], "meta": item["meta"], "score": 0}
        combined[cid]["score"] += BM25_WEIGHT * item["bm25_score"]

    # Prepare candidates for reranker
    candidates = list(combined.items())
    candidates = sorted(candidates, key=lambda x: x[1]["score"], reverse=True)[:k * 4]

    # Deep reranking using CrossEncoder
    pairs = [(query, c[1]["text"]) for c in candidates]
    ce_scores = reranker.predict(pairs)

    for (cid, data), ce in zip(candidates, ce_scores):
        data["rerank_score"] = float(ce)

    # Final top-k results
    top = sorted(candidates, key=lambda x: x[1]["rerank_score"], reverse=True)[:k]
    results = [
        {
            "chunk_id": cid,
            "text": d["text"],
            "meta": d["meta"],
            "score": d["rerank_score"]
        }
        for cid, d in top
    ]

    print(f"✅ Retrieved {len(results)} chunks for query: {query}")
    return results
