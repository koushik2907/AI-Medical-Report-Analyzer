import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use correct model name
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def explain(text, values, results):

    prompt = f"""
You are a medical AI assistant.

Medical Report:
{text}

Detected Values:
{values}

Health Issues:
{results}

Explain clearly:
1. What each abnormal value means
2. Possible diseases
3. Lifestyle suggestions
4. When to consult a doctor

Keep explanation simple.
"""

    response = model.generate_content(prompt)

    return response.text
