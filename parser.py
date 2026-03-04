import pandas as pd
import fitz

def parse_file(uploaded_file):

    name = uploaded_file.name.lower()

    if name.endswith(".txt"):
        text = uploaded_file.read().decode()

    elif name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        text = df.to_string()

    elif name.endswith(".pdf"):

        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""

        for page in pdf:
            text += page.get_text()

    else:
        text = ""

    return text
