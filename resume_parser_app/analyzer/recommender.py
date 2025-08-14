from typing import List, Dict

def missing_skills(resume_skills: List[str], jd_skills: List[str]) -> List[str]:
    rs = set([s.lower() for s in resume_skills])
    js = set([s.lower() for s in jd_skills])
    return sorted(list(js - rs))

def recommendations(resume_skills: List[str], jd_skills: List[str]) -> Dict[str, List[str]]:
    missing = missing_skills(resume_skills, jd_skills)
    recs = []
    for s in missing:
        recs.append(f"Consider adding or improving: {s}")
    return {"missing_skills": missing, "actions": recs}