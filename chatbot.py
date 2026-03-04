def explain(values, results):

    explanations = []

    for condition in results:

        if condition == "Possible Anemia":
            explanations.append(
                "Low hemoglobin suggests anemia. Symptoms may include fatigue, weakness, and dizziness."
            )

        elif condition == "Possible Infection":
            explanations.append(
                "Elevated white blood cell count may indicate infection or inflammation."
            )

        elif condition == "Low Platelet Count":
            explanations.append(
                "Low platelet count may increase bleeding risk and may be caused by infections or bone marrow issues."
            )

        elif condition == "High Cholesterol":
            explanations.append(
                "High cholesterol increases the risk of heart disease and stroke."
            )

        elif condition == "High LDL (Heart Risk)":
            explanations.append(
                "LDL is considered bad cholesterol and high levels can cause artery blockage."
            )

        elif condition == "Low HDL":
            explanations.append(
                "Low HDL reduces protection against heart disease."
            )

        elif condition == "High Triglycerides":
            explanations.append(
                "High triglycerides may increase risk of heart disease and metabolic syndrome."
            )

        elif condition == "Vitamin D Deficiency":
            explanations.append(
                "Vitamin D deficiency can cause fatigue, bone pain, and weakened immunity."
            )

        elif condition == "Vitamin B12 Deficiency":
            explanations.append(
                "Low B12 levels can lead to nerve damage, fatigue, and memory issues."
            )

        elif condition == "Possible Hypothyroidism":
            explanations.append(
                "High TSH may indicate hypothyroidism which can cause weight gain, fatigue, and cold intolerance."
            )

        elif condition == "Possible Diabetes":
            explanations.append(
                "High blood sugar levels may indicate diabetes. Lifestyle and diet changes are recommended."
            )

        elif condition == "Possible Kidney Issue":
            explanations.append(
                "Elevated creatinine may indicate reduced kidney function."
            )

        elif condition == "High Uric Acid":
            explanations.append(
                "High uric acid levels may cause gout and joint pain."
            )

        elif condition == "Possible Liver Issue":
            explanations.append(
                "Elevated ALT may indicate liver inflammation or damage."
            )

    return explanations
