from app.rag_pipeline import generate_answer

query = "What does the document say about rekha or data science?"
response = generate_answer(query)

print("\nAnswer:\n", response['answer'])
print("\nCitations:\n", response['citations'])



