import re
import pandas as pd

SKILLS = {
    "python": "programming", "java": "programming", "c++": "programming",
    "sql": "databases", "mysql": "databases", "postgresql": "databases",
    "mongodb": "databases",
    "excel": "tools", "power bi": "tools", "tableau": "tools", "git": "tools",
    "docker": "cloud", "fastapi": "cloud", "mlflow": "cloud", "aws": "cloud",
    "apis": "cloud",
    "pandas": "data", "numpy": "data", "statistics": "data",
    "data visualization": "data",
    "machine learning": "ml", "deep learning": "ml", "scikit-learn": "ml",
    "tensorflow": "ml", "pytorch": "ml", "nlp": "ml", "transformers": "ml",
    "hugging face": "ml", "spacy": "ml", "opencv": "ml", "cnn": "ml",
    "yolo": "ml", "llm": "ml", "rag": "ml",
}


def load_skills():
    return pd.DataFrame(list(SKILLS.items()), columns=["skill", "category"])


def extract_skills(clean_resume_text, skills_df):
    found = []
    for skill in skills_df["skill"]:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"
        if re.search(pattern, clean_resume_text):
            found.append(skill)
    return found