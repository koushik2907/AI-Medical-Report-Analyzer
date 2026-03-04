import pytesseract
from PIL import Image

def image_to_text(uploaded_file):

    img = Image.open(uploaded_file)

    text = pytesseract.image_to_string(img)

    return text
