import re

def extract_values(text):

    patterns = {
        "Hemoglobin": r"Hemoglobin.*?(\d+\.?\d*)",
        "WBC": r"WBC.*?(\d+\.?\d*)",
        "Platelets": r"Platelets.*?(\d+\.?\d*)",
        "Cholesterol": r"Cholesterol.*?(\d+\.?\d*)",
        "LDL": r"LDL.*?(\d+\.?\d*)",
        "HDL": r"HDL.*?(\d+\.?\d*)",
        "Triglycerides": r"Triglycerides.*?(\d+\.?\d*)",
        "Vitamin D": r"Vitamin D.*?(\d+\.?\d*)",
        "Vitamin B12": r"B12.*?(\d+\.?\d*)",
        "Thyroid": r"TSH.*?(\d+\.?\d*)",
        "Blood Sugar": r"Glucose.*?(\d+\.?\d*)",
        "Creatinine": r"Creatinine.*?(\d+\.?\d*)",
        "Uric Acid": r"Uric.*?(\d+\.?\d*)",
        "Liver Enzymes": r"ALT.*?(\d+\.?\d*)"
    }

    values = {}

    for key, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            values[key] = float(match.group(1))

    return values
