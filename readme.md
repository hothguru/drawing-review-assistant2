# 📐 Drawing Review Assistant

A Streamlit-based web app to review and summarize architectural and engineering drawing files (PDF and DXF).

## 🚀 Features
- Upload DXF or PDF files
- Extract raw text from drawings
- Auto-generate a technical summary:
  - Product type
  - Key dimensions
  - Detected views (Plan, Elevation, etc.)
  - Scale warnings
  - Suggested use-cases
- Download a Word summary
- Clean and simple interface

## 🛠️ Tech Stack
- Python
- Streamlit
- ezdxf, PyMuPDF
- python-docx, pandas

## 📦 Installation (Local)
```bash
pip install -r requirements.txt
streamlit run drawing_review_app.py
