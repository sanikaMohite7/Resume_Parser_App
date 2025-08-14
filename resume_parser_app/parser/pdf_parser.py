from typing import Tuple
import fitz  # PyMuPDF

def extract_text_from_pdf(path: str) -> Tuple[str, int]:
    """Extract text and page count from a PDF file."""
    doc = fitz.open(path)
    texts = []
    for page in doc:
        texts.append(page.get_text())
    text = "\n".join(texts)
    return text, len(doc)