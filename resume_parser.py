from pypdf import PdfReader
from docx import Document


def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    text = ""

    if name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += (page.extract_text() or "") + "\n"

    elif name.endswith(".docx"):
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text