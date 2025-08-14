import re

def clean_text(text: str) -> str:
    text = text.replace('\x00', ' ')  # remove nulls if any
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()