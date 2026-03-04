import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from parser import parse_file
from ocr import image_to_text
from extractor import extract_values
from analyzer import analyze
from chatbot import explain


# -------------------------------
# Page Settings
# -------------------------------

st.set_page_config(
    page_title="AI Medical Report Analyzer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 AI Medical Report Analyzer")

st.markdown("""
Upload your **medical report** and the system will:

✔ Extract medical parameters  
✔ Detect health conditions  
✔ Generate explanations  
✔ Display health dashboard  
✔ Predict health risks  
✔ Allow medical chatbot queries  
""")

st.divider()


# -------------------------------
# Upload Report
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf","png","jpg","jpeg","txt","csv"]
)


if uploaded_file:

    st.success("Report uploaded successfully")

    if uploaded_file.name.endswith(("png","jpg","jpeg")):
        text = image_to_text(uploaded_file)
    else:
        text = parse_file(uploaded_file)

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("📄 Extracted Report Text")
        st.text_area("Report",text,height=350)

    values = extract_values(text)

    with col2:
        st.subheader("🧪 Detected Medical Parameters")
        st.json(values)

    st.divider()


# -------------------------------
# Health Analysis
# -------------------------------

    results = analyze(values)

    st.subheader("⚕ Health Analysis")

    if results:
        for r in results:
            st.error(r)
    else:
        st.success("No abnormal conditions detected")


# -------------------------------
# AI Explanation
# -------------------------------

    st.subheader("📋 AI Health Explanation")

    explanations = explain(values,results)

    for e in explanations:
        st.info(e)


# -------------------------------
# Medical Dashboard
# -------------------------------

    st.divider()
    st.subheader("📊 Medical Dashboard")

    df = pd.DataFrame(list(values.items()),columns=["Parameter","Value"])

    fig,ax = plt.subplots()

    ax.bar(df["Parameter"],df["Value"])
    ax.set_ylabel("Values")
    ax.set_title("Medical Parameter Overview")

    plt.xticks(rotation=45)

    st.pyplot(fig)


# -------------------------------
# Risk Prediction
# -------------------------------

    st.divider()
    st.subheader("🚨 Health Risk Prediction")

    risk_score = len(results)

    if risk_score <= 2:
        st.success("Low Health Risk")

    elif risk_score <= 5:
        st.warning("Moderate Health Risk")

    else:
        st.error("High Health Risk – Medical Consultation Recommended")



# -------------------------------
# Chatbot UI
# -------------------------------

    st.divider()
    st.subheader("💬 Medical Chatbot")

    user_question = st.text_input("Ask a medical question")

    if user_question:

        question = user_question.lower()

        if "cholesterol" in question:
            st.write("High cholesterol can result from unhealthy diet, lack of exercise, smoking, and genetics.")

        elif "vitamin d" in question:
            st.write("Foods rich in Vitamin D include fatty fish, egg yolks, fortified milk, and sunlight exposure.")

        elif "diabetes" in question:
            st.write("Diabetes occurs when blood sugar levels remain elevated. Healthy diet and exercise can help manage it.")

        elif "kidney" in question:
            st.write("Kidney issues may arise from high blood pressure, diabetes, or dehydration.")

        else:
            st.write("Please consult a healthcare professional for personalized medical advice.")



else:

    st.info("Upload a medical report to begin analysis.")
