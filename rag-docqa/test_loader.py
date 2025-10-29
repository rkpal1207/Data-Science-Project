from ingest.loader import load_docs

# Load all PDFs from docs folder
items = load_docs(["docs"])

print("Pages extracted:", len(items))

# Preview first 400 characters of first page
if items:
    print("\nSample text from first page:\n")
    print(items[0]['text'][:400])
