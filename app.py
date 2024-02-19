import streamlit as st
from PyMyPDF import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.
    """
    doc_text = ''
    # Ensure the uploaded file is read as bytes
    if pdf_file is not None:
        pdf_bytes = pdf_file.getvalue()
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                doc_text += page.get_text()
    return doc_text

def count_words_in_text(text):
    """
    Count words in a text.
    """
    words = text.split()
    return len(words)

st.title("PDF Text Extractor")

uploaded_file = st.file_uploader("Choose your PDF file", type="pdf")

if uploaded_file is not None:
    extracted_text = extract_text_from_pdf(uploaded_file)
    word_count = count_words_in_text(extracted_text)
    st.text_area("Extracted Text", extracted_text, height=300)
    st.write(f"Word count: {word_count}")
else:
    st.write("Please upload a PDF file to extract text.")
