# app/rag_pipeline.py
from dotenv import load_dotenv
load_dotenv()

import os
from retriever.hybrid import hybrid_retrieve
from app.prompts import build_prompt

# ------------------ Configuration ------------------
USE_OLLAMA = bool(int(os.getenv("USE_OLLAMA", "0")))
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:8b")  # Default local model

# Initialize the right client
if not USE_OLLAMA:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
else:
    import ollama


def generate_answer(query: str):
    """
    Main RAG pipeline:
    1. Retrieve top chunks
    2. Build prompt with context
    3. Call LLM (OpenAI or Ollama)
    4. Return answer + citations
    """
    # ------------------ Step 1: Retrieve context ------------------
    retrieved = hybrid_retrieve(query, k=5)

    # ------------------ Step 2: Build RAG prompt ------------------
    prompt = build_prompt(query, retrieved)

    # ------------------ Step 3: Generate answer ------------------
    if USE_OLLAMA:
        print(f"🧠 Using local Ollama model ({OLLAMA_MODEL})...")
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response["message"]["content"]
    else:
        print("🧠 Using OpenAI GPT model...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Or "gpt-3.5-turbo" if preferred
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        answer = response.choices[0].message.content

    # ------------------ Step 4: Format citations ------------------
    citations = [
        f"[{r['meta']['doc_id']} p.{r['meta']['page']}]"
        for r in retrieved
    ]

    return {"answer": answer.strip(), "citations": citations}

"""
# app/rag_pipeline.py
from dotenv import load_dotenv
load_dotenv()

import os
from retriever.hybrid import hybrid_retrieve
from app.prompts import build_prompt

# For either OpenAI or Ollama
USE_OLLAMA = bool(int(os.getenv("USE_OLLAMA", "0")))

if not USE_OLLAMA:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
else:
    import ollama

def generate_answer(query: str):
    
    #Main RAG pipeline:
    #- Retrieve top chunks
    #- Build prompt with context
    #- Call LLM (OpenAI or Ollama)
    #- Return answer + citations
    
    # Step 1: Retrieve context
    retrieved = hybrid_retrieve(query, k=5)

    # Step 2: Build the RAG prompt
    prompt = build_prompt(query, retrieved)

    # Step 3: Generate answer
    if USE_OLLAMA:
        print("🧠 Using local Ollama model (llama3)...")
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        answer = response["message"]["content"]
    else:
        print("🧠 Using OpenAI GPT model...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        answer = response.choices[0].message.content

    # Step 4: Format citations
    citations = [
        f"[{r['meta']['doc_id']} p.{r['meta']['page']}]"
        for r in retrieved
    ]
    return {"answer": answer.strip(), "citations": citations}


"""