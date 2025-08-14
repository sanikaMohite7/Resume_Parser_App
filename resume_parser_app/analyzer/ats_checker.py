from typing import Dict

PROBLEM_HINTS = [
    "table", "image", "graphics", "text box", "header", "footer",
    "columns", "chart", "diagram"
]

def ats_flags(text: str, page_count: int) -> Dict[str, bool | int | list]:
    flags = {
        "too_long": page_count > 2,
        "problem_hints_found": [],
    }
    lower = text.lower()
    for hint in PROBLEM_HINTS:
        if hint in lower:
            flags["problem_hints_found"].append(hint)
    return flags