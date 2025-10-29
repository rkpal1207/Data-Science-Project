# app/prompts.py
def build_prompt(query, retrieved_chunks):
    """
    Combines retrieved context and user question into a single prompt.
    """
    context = "\n\n".join([
        f"Source: {r['meta']['doc_id']} (page {r['meta']['page']})\n{r['text']}"
        for r in retrieved_chunks
    ])

    prompt = f"""
You are a helpful AI assistant that answers questions strictly based on the provided context.
If the answer is not in the context, say "The information is not available in the provided documents."

### Context:
{context}

### Question:
{query}

### Answer:
"""
    return prompt.strip()
