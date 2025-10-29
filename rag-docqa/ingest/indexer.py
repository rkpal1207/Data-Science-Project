# ingest/indexer.py
import chromadb
from rank_bm25 import BM25Okapi
import pickle, os

CHROMA_PATH = os.getenv("CHROMA_PATH", ".chroma")
BM25_PATH = os.path.join(CHROMA_PATH, "bm25.pkl")

# persistent client = stores vectors on disk
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(name="docs", metadata={"hnsw:space": "cosine"})

def index_to_stores(chunks, embs):
    """
    Saves embeddings to Chroma and builds BM25 keyword index.
    """
    ids = [c["chunk_id"] for c in chunks]
    metas = [{"doc_id": c["doc_id"], "page": c["page"]} for c in chunks]
    texts = [c["text"] for c in chunks]

    # Add to Chroma
    collection.add(ids=ids, metadatas=metas, documents=texts, embeddings=embs)
    print(f"✅ Stored {len(ids)} embeddings in Chroma ({CHROMA_PATH})")

    # Build BM25 (for keyword retrieval)
    tokenized = [t.split() for t in texts]
    bm25 = BM25Okapi(tokenized)
    os.makedirs(CHROMA_PATH, exist_ok=True)
    with open(BM25_PATH, "wb") as f:
        pickle.dump({"bm25": bm25, "ids": ids, "texts": texts, "metas": metas}, f)
    print(f"✅ Saved BM25 index → {BM25_PATH}")
 