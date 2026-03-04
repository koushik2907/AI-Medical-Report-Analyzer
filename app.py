import streamlit as st
from parser import parse_file
from ocr import image_to_text
from extractor import extract_values
from analyzer import analyze
from chatbot import explain

st.set_page_config(page_title="AI Medical Report Analyzer", layout="wide")

st.title("🧬 AI Medical Report Analyzer")

st.write("Upload your medical report and get AI-powered health insights.")

uploaded_file = st.file_uploader(
    "Upload Report",
    type=["pdf","png","jpg","jpeg","txt","csv"]
)

if uploaded_file:

    if uploaded_file.name.endswith(("png","jpg","jpeg")):
        text = image_to_text(uploaded_file)
    else:
        text = parse_file(uploaded_file)

    st.subheader("Extracted Report Text")
    st.text_area("", text, height=200)

    values = extract_values(text)

    st.subheader("Detected Medical Parameters")
    st.write(values)

    results = analyze(values)

    st.subheader("Health Analysis")

    if results:
        for r in results:
            st.error(r)
    else:
        st.success("No major issues detected")

    if st.button("Explain with AI Doctor"):

        explanation = explain(text, values, results)

        st.subheader("AI Doctor Explanation")

        st.write(explanation)
