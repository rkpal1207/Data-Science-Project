print("Step 1: Importing modules...")

from ingest.loader import load_docs
from ingest.chunker import chunk_docs
from ingest.embedder import embed_chunks
from ingest.indexer import index_to_stores

print("Step 2: Loading PDFs...")
docs = load_docs(["docs"])
print(" -> Loaded:", len(docs), "pages")

print("Step 3: Chunking text...")
chunks = chunk_docs(docs)
print(" -> Created:", len(chunks), "chunks")

print("Step 4: Generating embeddings...")
embs = embed_chunks(chunks)
print(" -> Embeddings shape:", embs.shape)

print("Step 5: Indexing to vector DB...")
index_to_stores(chunks, embs)

print("✅ All steps completed successfully!")
