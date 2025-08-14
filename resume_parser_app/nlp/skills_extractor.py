from typing import List, Set, Dict
from config.settings import DEFAULT_SKILLS

def normalize_token(tok: str) -> str:
    return tok.strip().lower()

def build_skill_set() -> Set[str]:
    all_skills: Set[str] = set()
    for group in DEFAULT_SKILLS.values():
        for s in group:
            all_skills.add(normalize_token(s))
    return all_skills

def extract_skills(text: str, extra_skills: Dict[str, list] | None = None) -> List[str]:
    """Extract skills by keyword matching (case-insensitive)."""
    skills_ref = build_skill_set()
    if extra_skills:
        for group in extra_skills.values():
            for s in group:
                skills_ref.add(normalize_token(s))
    found = set()
    # naive membership; improve with tokenization if needed
    for skill in skills_ref:
        if skill in text:
            found.add(skill)
    return sorted(found)