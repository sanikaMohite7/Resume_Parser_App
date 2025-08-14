from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_similarity(resume_text: str, jd_text: str) -> float:
    if not resume_text or not jd_text:
        return 0.0
    vect = TfidfVectorizer(ngram_range=(1,2), min_df=1)
    tfidf = vect.fit_transform([resume_text, jd_text])
    sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return float(sim)

def skill_overlap_score(resume_skills: List[str], jd_skills: List[str]) -> float:
    rs = set([s.lower() for s in resume_skills])
    js = set([s.lower() for s in jd_skills])
    if not js:
        return 0.0 if not rs else 1.0
    overlap = len(rs & js)
    return overlap / max(1, len(js))