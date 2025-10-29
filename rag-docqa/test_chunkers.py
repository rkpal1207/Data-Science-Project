from ingest.loader import load_docs
from ingest.chunker import chunk_docs

# Step 1: Load PDFs
items = load_docs(["docs"])
# Step 2: Chunk them
chunks = chunk_docs(items)

print("Total chunks created:", len(chunks))
print("\nExample chunk:\n")
print(chunks[0]['text'][:400])
