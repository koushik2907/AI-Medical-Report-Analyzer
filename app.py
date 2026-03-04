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

    response = "Please consult a healthcare professional for personalized medical advice."

    # exercise questions
    if "exercise" in question or "workout" in question or "gym" in question:
        response = "Regular moderate exercise like walking, cycling, or yoga can improve heart health, control cholesterol, and regulate blood sugar."

    # diet questions
    elif "diet" in question or "food" in question or "eat" in question:
        response = "A balanced diet including vegetables, fruits, whole grains, and lean protein helps maintain healthy cholesterol and blood sugar levels."

    # vitamin D
    elif "vitamin d" in question or "sunlight" in question:
        response = "Vitamin D levels improve with sunlight exposure and foods like fish, eggs, and fortified milk."

    # cholesterol
    elif "cholesterol" in question:
        response = "High cholesterol can be improved with exercise, fiber-rich foods, and reducing fried or fatty foods."

    # diabetes / sugar
    elif "diabetes" in question or "sugar" in question:
        response = "Maintaining a healthy diet, regular exercise, and weight control helps manage blood sugar levels."

    # thyroid
    elif "thyroid" in question:
        response = "Thyroid imbalance can cause fatigue and weight changes. Regular medical monitoring is recommended."

    # kidney
    elif "kidney" in question or "creatinine" in question:
        response = "Kidney health improves with proper hydration, balanced diet, and controlling blood pressure."

    # uric acid
    elif "uric acid" in question:
        response = "Reducing red meat, alcohol, and sugary drinks can help control uric acid levels."

    # anemia
    elif "anemia" in question or "hemoglobin" in question:
        response = "Iron-rich foods such as spinach, lentils, beans, and red meat can help improve hemoglobin levels."

    # sleep
    elif "sleep" in question:
        response = "Adequate sleep (7-8 hours) helps regulate metabolism, hormones, and overall health."

    st.write(response)


# ---------------------------------------------------
# If No File Uploaded
# ---------------------------------------------------

else:

    st.info("Upload a medical report to begin analysis.")
