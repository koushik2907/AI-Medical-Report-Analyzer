import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyAAN0mUDHJV7wwSL3qncjWrgUYYZNzHN3A"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def explain(text, values, results):

    prompt = f"""
You are a medical AI assistant.

Report Data:
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
"""

    response = model.generate_content(prompt)

    return response.text
