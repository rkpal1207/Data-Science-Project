# ingest/loader.py
from pypdf import PdfReader
import os

def load_docs(paths):
    """
    Reads PDF files and extracts text from each page.

    Args:
        paths (list[str]): List of file paths or a folder path.

    Returns:
        List[dict]: Each dict has {'doc_id', 'page', 'text'}.
    """
    items = []

    # Allow folder path
    file_list = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                for f in files:
                    if f.lower().endswith(".pdf"):
                        file_list.append(os.path.join(root, f))
        else:
            file_list.append(p)

    for p in file_list:
        try:
            reader = PdfReader(p)
            for i, page in enumerate(reader.pages):
                text = (page.extract_text() or "").strip()
                if text:
                    items.append({
                        "doc_id": os.path.basename(p),
                        "page": i + 1,
                        "text": text
                    })
        except Exception as e:
            print(f"⚠️ Skipped {p} due to error: {e}")

    print(f"✅ Loaded {len(file_list)} files, extracted {len(items)} pages.")
    return items
