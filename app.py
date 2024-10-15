import streamlit as st
import PyPDF2
from docx import Document
from fpdf import FPDF
import pandas as pd
from bs4 import BeautifulSoup
import re  # For text sanitization

# Function to clean the text by removing non-XML compatible characters
def sanitize_text(text):
    return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)

# Streamlit App Interface
st.title("Text Converter into TXT")

# Upload the file in various formats
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx", "csv", "html"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1]  # Get the file extension
    original_text = ""
    converted_text = ""

    # Process txt files
    if file_type == "txt":
        original_text = uploaded_file.read().decode("utf-8")
        converted_text = original_text.upper()  # Example conversion: convert text to uppercase

    # Process pdf files
    elif file_type == "pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            original_text += page.extract_text()
        converted_text = original_text.upper()

    # Process docx files
    elif file_type == "docx":
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            original_text += para.text
        converted_text = original_text.upper()

    # Process csv files
    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        original_text = df.to_string()
        converted_text = original_text.upper()

    # Process html files
    elif file_type == "html":
        html_content = uploaded_file.read()
        soup = BeautifulSoup(html_content, "html.parser")
        original_text = soup.get_text()
        converted_text = original_text.upper()

    # Sanitize
