# ingest/chunker.py
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize a recursive splitter that breaks text on paragraph/sentence boundaries
_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=1200,          # target characters per chunk (~700–900 words)
    chunk_overlap=150,        # overlap to preserve context
    separators=["\n\n", "\n", ". ", ", ", " "]
)

def normalize_text(t: str) -> str:
    """
    Cleans text: removes extra spaces and line breaks.
    """
    t = re.sub(r"\s+", " ", t)
    return t.strip()

def chunk_docs(items):
    """
    Splits raw text pages into smaller overlapping chunks.

    Args:
        items (list[dict]): Output from loader.py, each with doc_id, page, text.

    Returns:
        List[dict]: Each dict has chunk_id, doc_id, page, text.
    """
    chunks = []
    for it in items:
        text = normalize_text(it["text"])
        pieces = _SPLITTER.split_text(text)
        for j, piece in enumerate(pieces):
            chunks.append({
                "chunk_id": f"{it['doc_id']}::p{it['page']}::c{j}",
                "doc_id": it['doc_id'],
                "page": it['page'],
                "text": piece
            })
    print(f"✅ Created {len(chunks)} chunks from {len(items)} pages.")
    return chunks
