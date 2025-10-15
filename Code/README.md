# 🤖 GenAI Text Summarizer & Q&A Assistant

An AI-powered web app that **summarizes research papers, articles, and long-form text** using transformer models — and can also **answer questions** based on the content.

Built with **Hugging Face Transformers** and **Streamlit** by [Bharath S](https://github.com/bharath3010).

---

## 🌟 Demo

🚀 **Live App:** [https://bharath3010-genai-summarizer.streamlit.app](#) *(Add after deployment)*  
💻 **GitHub Repo:** [https://github.com/bharath3010/genai-text-summarizer-and-qa-assistant](#)

---

## 📸 Preview

![App Screenshot](https://raw.githubusercontent.com/bharath3010/genai-text-summarizer-and-qa-assistant/main/preview.png)

*(You can take a screenshot after deployment and name it `preview.png`)*

---

## 🧠 Features

- ✨ Summarize any long text instantly  
- 💬 Ask natural language questions and get answers  
- ⚡ Powered by **BART** and **RoBERTa** transformer models  
- 🖥️ Streamlit web interface (no setup complexity)

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend UI | Streamlit |
| AI Models | Hugging Face Transformers |
| NLP Models Used | `facebook/bart-large-cnn`, `deepset/roberta-base-squad2` |
| Language | Python |
| Hosting | Streamlit Cloud |

---

## 🚀 Quick Start

Clone the repo and run locally:

```bash
git clone https://github.com/bharath3010/genai-text-summarizer-and-qa-assistant.git
cd genai-text-summarizer-and-qa-assistant
pip install -r requirements.txt
streamlit run app.py
