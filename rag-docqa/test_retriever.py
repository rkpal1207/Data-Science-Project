from retriever.hybrid import hybrid_retrieve

query = "What does the document say about rekha or data science?"
results = hybrid_retrieve(query, k=3)

print("\nTop results:\n")
for r in results:
    print(f"[{r['meta']['doc_id']} p.{r['meta']['page']}] (score={r['score']:.2f})")
    print(r['text'][:300], "\n")
