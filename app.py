import streamlit as st
from parser import parse_file
from ocr import image_to_text
from extractor import extract_values
from analyzer import analyze
from chatbot import explain


# Page configuration
st.set_page_config(
    page_title="AI Medical Report Analyzer",
    page_icon="🧬",
    layout="wide"
)

# Header
st.title("🧬 AI Medical Report Analyzer")
st.markdown(
    """
Upload your **medical report** and this system will automatically:

✔ Extract important medical parameters  
✔ Detect possible health conditions  
✔ Provide medical explanations  
"""
)

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "png", "jpg", "jpeg", "txt", "csv"]
)

# If file uploaded
if uploaded_file:

    st.success("Report uploaded successfully")

    # Detect file type
    if uploaded_file.name.endswith(("png", "jpg", "jpeg")):
        text = image_to_text(uploaded_file)
    else:
        text = parse_file(uploaded_file)

    # Layout columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Extracted Report Text")
        st.text_area("Report Content", text, height=350)

    # Extract values
    values = extract_values(text)

    with col2:
        st.subheader("🧪 Detected Medical Parameters")

        if values:
            st.json(values)
        else:
            st.warning("No medical parameters detected.")

    st.divider()

    # Analyze report
    results = analyze(values)

    st.subheader("⚕ Health Analysis")

    if results:

        for r in results:
            st.error(r)

    else:
        st.success("No major abnormalities detected")

    st.divider()

    # Explanation button
    if st.button("🧠 Generate Health Explanation"):

        explanations = explain(values, results)

        st.subheader("📋 AI Health Explanation")

        if explanations:

            for e in explanations:
                st.info(e)

        else:
            st.success("All parameters appear within healthy range.")

else:

    st.info("Please upload a medical report to begin analysis.")
