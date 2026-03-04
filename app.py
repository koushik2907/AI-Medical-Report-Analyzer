import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from parser import parse_file
from extractor import extract_values
from analyzer import analyze
from chatbot import explain


# ---------------------------------------------------
# Page Settings
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Medical Report Analyzer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 AI Medical Report Analyzer")

st.markdown("""
Upload your **medical report** and this system will:

✔ Extract medical parameters  
✔ Detect possible health conditions  
✔ Generate medical explanations  
✔ Display health dashboard  
✔ Predict health risks  
✔ Allow chatbot queries  
""")

st.divider()


# ---------------------------------------------------
# Upload File
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "txt", "csv"]  # Images removed
)

st.caption("Supported formats: PDF, TXT, CSV")


# ---------------------------------------------------
# If File Uploaded
# ---------------------------------------------------

if uploaded_file:

    st.success("Report uploaded successfully")

    text = parse_file(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Extracted Report Text")
        st.text_area("Report Content", text, height=350)

    values = extract_values(text)

    with col2:
        st.subheader("🧪 Detected Medical Parameters")

        if values:
            st.json(values)
        else:
            st.warning("No medical parameters detected")

    st.divider()


# ---------------------------------------------------
# Health Analysis
# ---------------------------------------------------

    results = analyze(values)

    st.subheader("⚕ Health Analysis")

    if results:
        for r in results:
            st.error(r)
    else:
        st.success("No abnormal conditions detected")


# ---------------------------------------------------
# Explanation Engine
# ---------------------------------------------------

    st.subheader("📋 AI Health Explanation")

    explanations = explain(values, results)

    if explanations:
        for e in explanations:
            st.info(e)
    else:
        st.success("All parameters appear within healthy range")


# ---------------------------------------------------
# Medical Dashboard
# ---------------------------------------------------

    if values:

        st.divider()
        st.subheader("📊 Medical Dashboard")

        df = pd.DataFrame(list(values.items()), columns=["Parameter", "Value"])

        fig, ax = plt.subplots()

        ax.bar(df["Parameter"], df["Value"])

        ax.set_title("Medical Parameter Overview")
        ax.set_ylabel("Measured Value")

        plt.xticks(rotation=45)

        st.pyplot(fig)


# ---------------------------------------------------
# Health Risk Prediction
# ---------------------------------------------------

    st.divider()
    st.subheader("🚨 Health Risk Prediction")

    risk_score = len(results)

    if risk_score == 0:
        st.success("Low Health Risk")

    elif risk_score <= 4:
        st.warning("Moderate Health Risk")

    else:
        st.error("High Health Risk – Medical Consultation Recommended")


# ---------------------------------------------------
# Chatbot
# ---------------------------------------------------

    st.divider()
    st.subheader("💬 Medical Chatbot")

    user_question = st.text_input("Ask a question about your health report")

    if user_question:

        question = user_question.lower()

        response = "Please consult a healthcare professional for personalized advice."

        if "cholesterol" in question:
            response = "High cholesterol may be caused by fatty foods, lack of exercise, smoking, obesity, or genetics."

        elif "vitamin d" in question:
            response = "Vitamin D deficiency may occur due to lack of sunlight. Sun exposure and fortified foods help."

        elif "diabetes" in question or "sugar" in question:
            response = "High blood sugar may indicate diabetes. Diet control and exercise help manage it."

        elif "thyroid" in question:
            response = "High TSH may indicate hypothyroidism causing fatigue and weight gain."

        elif "uric acid" in question:
            response = "High uric acid may lead to gout and joint pain."

        elif "kidney" in question or "creatinine" in question:
            response = "High creatinine levels may indicate kidney function issues."

        st.write(response)


# ---------------------------------------------------
# If No File Uploaded
# ---------------------------------------------------

else:

    st.info("Upload a medical report to begin analysis.")
