from typing import Tuple
import docx

def extract_text_from_docx(path: str) -> Tuple[str, int]:
    """Extract text and a pseudo page count (1) from a DOCX file."""
    document = docx.Document(path)
    text = "\n".join([p.text for p in document.paragraphs])
    return text, 1