TOPICS = {
    "python": "Python basics and functions",
    "sql": "SQL queries, joins and aggregation",
    "excel": "Excel formulas and pivot tables",
    "pandas": "Pandas for data cleaning and analysis",
    "power bi": "Build a Power BI dashboard",
    "tableau": "Tableau basics and dashboards",
    "statistics": "Descriptive statistics and probability",
    "data visualization": "Charts with Matplotlib and Plotly",
    "machine learning": "Core ML algorithms and model evaluation",
    "scikit-learn": "Build models with scikit-learn",
    "fastapi": "FastAPI basics, then deploy an ML model",
    "docker": "Docker fundamentals",
    "numpy": "NumPy arrays and operations",
    "mlflow": "MLflow experiment tracking",
    "deep learning": "Neural networks fundamentals",
    "llm": "Working with large language models",
    "rag": "Build a simple RAG app",
    "apis": "Calling and building REST APIs",
    "pytorch": "PyTorch basics and training loops",
    "nlp": "Text preprocessing and NLP basics",
    "transformers": "Transformer models",
    "hugging face": "Hugging Face pipelines",
    "spacy": "spaCy entities and phrase extraction",
    "opencv": "Image processing with OpenCV",
    "cnn": "Convolutional neural networks",
    "yolo": "Object detection with YOLO",
    "tensorflow": "TensorFlow and Keras basics",
}


def make_roadmap(missing_skills):
    steps = []
    for i, skill in enumerate(missing_skills, start=1):
        steps.append(f"Week {i}: {TOPICS.get(skill, 'Learn ' + skill)}")
    return steps