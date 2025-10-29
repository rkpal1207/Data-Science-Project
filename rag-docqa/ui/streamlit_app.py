import streamlit as st
from app.rag_pipeline import generate_answer

st.title("📚 Document Search & QA (RAG System)")
query = st.text_input("Ask a question:")
if st.button("Search"):
    with st.spinner("Retrieving answer..."):
        result = generate_answer(query)
        st.write("### Answer:")
        st.write(result["answer"])
        st.write("### Citations:")
        st.write(", ".join(result["citations"]))
