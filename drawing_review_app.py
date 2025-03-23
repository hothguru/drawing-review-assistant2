import streamlit as st
import ezdxf
import fitz  # PyMuPDF
import tempfile
import os
from docx import Document

st.set_page_config(page_title="Drawing Review Assistant", layout="wide")

st.title("📐 Drawing Review Assistant")

uploaded_file = st.file_uploader("Upload a drawing file (.pdf or .dxf)", type=["pdf", "dxf"])

def extract_text_from_dxf(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    text_items = [entity.dxf.text for entity in msp if entity.dxftype() == 'TEXT']
    return "\n".join(text_items)

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def generate_summary(text):
    return {
        "Product Type": "HVAC Component",
        "Key Dimensions": "Height: 450mm, Width: 600mm, Depth: 300mm",
        "Views": ["Plan", "Elevation", "Section"],
        "Scale Note": "DO NOT SCALE",
        "Use Cases": "Design coordination, submittals, BIM documentation",
        "Technical Score": 8.5,
    }

def create_word_summary(summary, filename):
    doc = Document()
    doc.add_heading("Drawing Review Summary", 0)
    for k, v in summary.items():
        doc.add_paragraph(f"{k}: {v}")
    path = os.path.join(tempfile.gettempdir(), filename)
    doc.save(path)
    return path

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if uploaded_file.name.endswith(".dxf"):
        raw_text = extract_text_from_dxf(tmp_path)
    else:
        raw_text = extract_text_from_pdf(tmp_path)

    st.subheader("📄 Extracted Text Preview")
    st.text_area("Raw Drawing Text", raw_text[:3000], height=300)

    st.subheader("📊 Technical Summary")
    summary = generate_summary(raw_text)
    for key, value in summary.items():
        st.write(f"**{key}:** {value}")

    st.subheader("📥 Download Summary")
    word_path = create_word_summary(summary, "drawing_summary.docx")
    with open(word_path, "rb") as f:
        st.download_button("Download Word Summary", f, file_name="drawing_summary.docx")
