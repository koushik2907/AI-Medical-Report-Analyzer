# 🧬 AI Medical Report Analyzer

An intelligent web application that analyzes medical reports and provides automated health insights.
The system extracts medical parameters from reports, detects potential health conditions, visualizes health data, and answers user questions through a medical chatbot.

Built using **Python, Streamlit, and data analysis tools**, this project demonstrates how AI-driven systems can assist in **automated medical report interpretation**.

---

# 🚀 Features

### 📄 Medical Report Parsing

Supports multiple report formats:

* PDF
* TXT
* CSV

The system extracts report text and processes it automatically.

---

### 🧪 Medical Parameter Extraction

The application detects key medical parameters such as:

* Hemoglobin
* WBC (White Blood Cells)
* Platelets
* Cholesterol
* LDL
* HDL
* Triglycerides
* Vitamin D
* Vitamin B12
* Thyroid (TSH)
* Blood Sugar (Glucose)
* Creatinine
* Uric Acid
* Liver Enzymes (ALT)

---

### ⚕ Health Condition Detection

Based on medical ranges, the system identifies possible conditions such as:

* Anemia
* Infection
* Low Platelet Count
* High Cholesterol
* High LDL (Heart Risk)
* Low HDL
* High Triglycerides
* Vitamin D Deficiency
* Vitamin B12 Deficiency
* Hypothyroidism
* Diabetes Risk
* Kidney Function Issues
* High Uric Acid
* Liver Function Issues

---

### 📊 Medical Dashboard

The application generates visualizations showing detected medical values.

Features include:

* Medical parameter bar charts
* Health data visualization
* Quick overview of report metrics

---

### 🚨 Health Risk Prediction

The system estimates a health risk level based on detected abnormalities:

* Low Health Risk
* Moderate Health Risk
* High Health Risk

This provides a quick summary of the user's health status.

---

### 💬 Medical Chatbot

An interactive chatbot allows users to ask questions about their health report.

Example questions:

* Should I do exercise now?
* How can I reduce cholesterol?
* What food helps Vitamin D deficiency?
* How to control diabetes?
* Why is my uric acid high?

The chatbot provides health guidance and lifestyle suggestions.

---

# 🏗 System Architecture

```
User Uploads Report
        │
        ▼
Report Parser (PDF / TXT / CSV)
        │
        ▼
Text Extraction
        │
        ▼
Medical Parameter Detection
        │
        ▼
Health Condition Analyzer
        │
        ▼
Explanation Engine
        │
        ▼
Streamlit Dashboard + Chatbot
```

---

# 🛠 Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Core programming language    |
| Streamlit  | Web application framework    |
| Pandas     | Data processing              |
| Matplotlib | Data visualization           |
| Regex      | Medical parameter extraction |

---

# 📂 Project Structure

```
AI-Medical-Report-Analyzer

app.py
parser.py
extractor.py
analyzer.py
chatbot.py

requirements.txt
README.md
```

### File Description

| File             | Description                        |
| ---------------- | ---------------------------------- |
| app.py           | Main Streamlit application         |
| parser.py        | Parses PDF, TXT, and CSV reports   |
| extractor.py     | Extracts medical parameters        |
| analyzer.py      | Detects possible health conditions |
| chatbot.py       | Provides health explanations       |
| requirements.txt | Project dependencies               |

---

# ⚙ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Medical-Report-Analyzer.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd AI-Medical-Report-Analyzer
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Live Deployment

The application can be deployed using **Streamlit Cloud**.

Steps:

1. Push the project to GitHub
2. Connect repository to Streamlit Cloud
3. Select `app.py` as the entry file
4. Deploy the application

---

# 🎯 Use Cases

This system can be used for:

* Medical report interpretation
* Health monitoring applications
* AI healthcare research
* Medical data analysis tools
* Educational healthcare platforms

---

# ⚠ Disclaimer

This application is designed for **educational purposes only**.
It does **not replace professional medical diagnosis or consultation**.

Always consult a qualified healthcare professional for medical advice.

---
