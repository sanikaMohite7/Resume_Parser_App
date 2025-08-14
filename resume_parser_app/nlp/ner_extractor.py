import re
from typing import Dict

EMAIL_RE = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
PHONE_RE = re.compile(r'(\+\d{1,3}[\s-]?)?\b\d{10}\b')

def extract_entities(text: str) -> Dict[str, str]:
    """Very lightweight entity extraction using regex and heuristics."""
    entities = {}
    email_match = EMAIL_RE.search(text)
    phone_match = PHONE_RE.search(text)

    if email_match:
        entities['email'] = email_match.group(0)
    if phone_match:
        entities['phone'] = phone_match.group(0)

    # Name heuristic: first two capitalized words at start of doc before a line break
    # (only works if original casing; if text already lowercased, skip)
    # For this demo we return empty name because we lowercase text in cleaner.
    entities['name'] = ''

    return entities