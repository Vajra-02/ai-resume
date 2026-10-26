import re


def clean_text(text):
    text = text.lower()
    # keep letters, numbers, spaces and symbols used in skills like c++, c#, .net
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()