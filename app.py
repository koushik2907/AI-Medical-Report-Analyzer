import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from parser import parse_file
from ocr import image_to_text
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
✔ Allow health chatbot queries  
""")

st.divider()


# ---------------------------------------------------
# Upload File
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf", "png", "jpg", "jpeg", "txt", "csv"]
)


# ---------------------------------------------------
# If File Uploaded
# ---------------------------------------------------

if uploaded_file:

    st.success("Report uploaded successfully")

    if uploaded_file.name.endswith(("png","jpg","jpeg")):
        text = image_to_text(uploaded_file)
    else:
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
# Smart Medical Chatbot
# ---------------------------------------------------

    st.divider()
    st.subheader("💬 Medical Chatbot")

    user_question = st.text_input("Ask a question about your health report")

    if user_question:

        question = user_question.lower()

        response = "Please consult a healthcare professional for personalized advice."

        if "cholesterol" in question:
            response = "High cholesterol may be caused by fatty foods, lack of exercise, smoking, obesity, or genetics. Eating fiber-rich foods and exercising regularly can help."

        elif "ldl" in question:
            response = "LDL is known as bad cholesterol. High LDL levels can lead to plaque buildup in arteries and increase heart disease risk."

        elif "hdl" in question:
            response = "HDL is good cholesterol. Higher HDL levels help remove bad cholesterol from the bloodstream."

        elif "triglyceride" in question:
            response = "High triglycerides are often linked to obesity, diabetes, and high sugar diets. Exercise and healthy eating can help lower them."

        elif "vitamin d" in question:
            response = "Vitamin D deficiency can occur due to lack of sunlight exposure or poor diet. Sunlight, fatty fish, fortified milk, and supplements help increase Vitamin D."

        elif "vitamin b12" in question or "b12" in question:
            response = "Vitamin B12 deficiency may lead to fatigue, weakness, and nerve problems. Foods like meat, dairy, eggs, and supplements can help."

        elif "anemia" in question or "hemoglobin" in question:
            response = "Anemia occurs when hemoglobin levels are low. Iron-rich foods like spinach, lentils, red meat, and iron supplements can help."

        elif "thyroid" in question or "tsh" in question:
            response = "High TSH levels may indicate hypothyroidism. Symptoms include fatigue, weight gain, and cold sensitivity."

        elif "diabetes" in question or "blood sugar" in question:
            response = "High blood sugar levels may indicate diabetes. A balanced diet, exercise, and weight management help control blood sugar."

        elif "kidney" in question or "creatinine" in question:
            response = "High creatinine levels may indicate kidney dysfunction. Hydration and controlling blood pressure and diabetes are important."

        elif "uric acid" in question:
            response = "High uric acid levels may cause gout, leading to joint pain. Reducing red meat, alcohol, and sugary drinks can help."

        elif "liver" in question or "alt" in question:
            response = "High ALT levels may indicate liver inflammation. Avoid alcohol, maintain healthy weight, and eat a balanced diet."

        elif "platelet" in question:
            response = "Low platelet count may increase bleeding risk. It may occur due to infections or bone marrow conditions."

        elif "wbc" in question:
            response = "High WBC count may indicate infection, inflammation, or immune response."

        st.write(response)


# ---------------------------------------------------
# If No File Uploaded
# ---------------------------------------------------

else:

    st.info("Upload a medical report to begin analysis.")
