from fastapi import FastAPI, Query
from app.rag_pipeline import generate_answer

app = FastAPI(title="Document Search & QA API")

@app.get("/ask")
def ask(query: str = Query(..., description="User question")):
    return generate_answer(query)
