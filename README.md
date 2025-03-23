# 📐 Drawing Review Assistant

A Streamlit app for analyzing architectural and engineering drawings (PDF and DXF), generating a GPT-powered technical summary, and downloading it as a Word document.

## 🚀 Features
- Upload PDF or DXF drawing files
- Extract raw text from drawings
- Send drawing text to GPT-4 for analysis
- Receive structured technical summary
- Download result as Word doc

## 🛠 Installation
```bash
pip install -r requirements.txt
streamlit run drawing_review_app.py
```

## 🔐 API Key
Set your OpenAI API key using Streamlit Cloud’s Secrets Manager or a local `.streamlit/secrets.toml` file:

```toml
OPENAI_API_KEY = "sk-..."
```
