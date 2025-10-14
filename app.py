import streamlit as st
from transformers import pipeline

# Title and description
st.title("🤖 GenAI Text Summarizer & Q&A Assistant")
st.write("Upload or paste text, and let AI summarize it or answer your questions.")

# Load models (cached)
@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    qa = pipeline("question-answering", model="deepset/roberta-base-squad2")
    return summarizer, qa

summarizer, qa = load_models()

# Input text
text = st.text_area("📜 Paste your text here:", height=250)

if text:
    if st.button("🧾 Summarize Text"):
        summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
        st.subheader("🧠 Summary:")
        st.write(summary[0]['summary_text'])

    question = st.text_input("💬 Ask a question about the text:")
    if question:
        answer = qa(question=question, context=text)
        st.subheader("🗣️ Answer:")
        st.write(answer["answer"])
