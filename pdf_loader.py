# pdf_loader.py

import streamlit as st
from pypdf import PdfReader

@st.cache_data(show_spinner=False)
def load_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text
