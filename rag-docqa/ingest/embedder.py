# ingest/embedder.py
import numpy as np
from sentence_transformers import SentenceTransformer

_model = None  # cached global model

def get_model():
    """
    Loads the embedding model once and caches it.
    """
    global _model
    if _model is None:
        print("🔄 Loading embedding model (BAAI/bge-small-en-v1.5)...")
        _model = SentenceTransformer("BAAI/bge-small-en-v1.5")
    return _model

def embed_chunks(chunks):
    """
    Encodes text chunks into dense embeddings.
    Args:
        chunks (list[dict]): output from chunk_docs()
    Returns:
        np.ndarray: shape [N, embedding_dim]
    """
    model = get_model()
    texts = [c["text"] for c in chunks]
    embs = model.encode(texts, batch_size=64, normalize_embeddings=True)
    print(f"✅ Created embeddings: {embs.shape}")
    return np.asarray(embs, dtype=np.float32)
