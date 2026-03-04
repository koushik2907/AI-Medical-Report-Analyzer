def analyze(values):

    results = []

    if "Hemoglobin" in values and values["Hemoglobin"] < 12:
        results.append("Possible Anemia")

    if "WBC" in values and values["WBC"] > 11000:
        results.append("Possible Infection")

    if "Platelets" in values and values["Platelets"] < 150000:
        results.append("Low Platelet Count")

    if "Cholesterol" in values and values["Cholesterol"] > 200:
        results.append("High Cholesterol")

    if "LDL" in values and values["LDL"] > 130:
        results.append("High LDL (Heart Risk)")

    if "HDL" in values and values["HDL"] < 40:
        results.append("Low HDL")

    if "Triglycerides" in values and values["Triglycerides"] > 150:
        results.append("High Triglycerides")

    if "Vitamin D" in values and values["Vitamin D"] < 30:
        results.append("Vitamin D Deficiency")

    if "Vitamin B12" in values and values["Vitamin B12"] < 200:
        results.append("Vitamin B12 Deficiency")

    if "Thyroid" in values and values["Thyroid"] > 4:
        results.append("Possible Hypothyroidism")

    if "Blood Sugar" in values and values["Blood Sugar"] > 126:
        results.append("Possible Diabetes")

    if "Creatinine" in values and values["Creatinine"] > 1.3:
        results.append("Possible Kidney Issue")

    if "Uric Acid" in values and values["Uric Acid"] > 7:
        results.append("High Uric Acid")

    if "Liver Enzymes" in values and values["Liver Enzymes"] > 40:
        results.append("Possible Liver Issue")

    return results
