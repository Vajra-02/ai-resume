from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROLES = {
    "Data Analyst": ["python", "sql", "excel", "pandas", "power bi",
                     "statistics", "data visualization", "tableau"],
    "Machine Learning Engineer": ["python", "machine learning", "scikit-learn",
                                  "fastapi", "docker", "pandas", "numpy", "mlflow"],
    "AI Engineer": ["python", "deep learning", "llm", "rag", "apis",
                    "pytorch", "fastapi", "docker"],
    "NLP Engineer": ["python", "nlp", "transformers", "hugging face", "spacy",
                     "pytorch", "machine learning", "deep learning"],
    "Computer Vision Engineer": ["python", "opencv", "cnn", "yolo",
                                 "deep learning", "pytorch", "numpy", "tensorflow"],
}


def match_roles(found_skills):
    names = list(ROLES.keys())
    if not found_skills:
        return [(n, 0.0) for n in names]

    docs = [";".join(ROLES[n]) for n in names]
    resume_doc = ";".join(found_skills)

    vec = TfidfVectorizer(tokenizer=lambda t: t.split(";"),
                          token_pattern=None, lowercase=False)
    matrix = vec.fit_transform(docs + [resume_doc])
    scores = cosine_similarity(matrix[-1], matrix[:-1])[0] * 100

    results = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
    return [(n, round(float(s), 1)) for n, s in results]


def skill_gap(found_skills, role):
    required = ROLES[role]
    have = [s for s in required if s in found_skills]
    missing = [s for s in required if s not in found_skills]
    return have, missing