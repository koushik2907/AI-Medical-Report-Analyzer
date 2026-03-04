import pytesseract
from PIL import Image
import streamlit as st


def image_to_text(uploaded_file):

    try:

        img = Image.open(uploaded_file)

        text = pytesseract.image_to_string(img)

        return text

    except:

        st.error("OCR engine not available on cloud deployment. Please upload PDF, TXT, or CSV reports.")

        return ""
