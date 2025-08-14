import streamlit as st
from pathlib import Path
from typing import List, Dict

from config.settings import UPLOAD_DIR, JD_DIR, DEFAULT_SKILLS, WEIGHTS
from utils.file_handler import save_upload, read_text_file, split_ext
from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx
from parser.text_cleaner import clean_text
from nlp.ner_extractor import extract_entities
from nlp.skills_extractor import extract_skills
from analyzer.matcher import tfidf_similarity, skill_overlap_score
from analyzer.scorer import overall_score
from analyzer.ats_checker import ats_flags
from analyzer.recommender import recommendations
from utils.visualizer import bar_skill_match, gauge_score

st.set_page_config(page_title="Resume Parser & Analyzer", layout="wide")

st.title("🧠 AI Resume Parser & Analyzer")
st.caption("Upload a resume (PDF/DOCX), paste or upload a Job Description, and get an ATS-style analysis.")

with st.sidebar:
    st.header("🔧 Settings")
    st.write("Adjust scoring weights (optional)")
    skill_w = st.slider("Skill Overlap Weight", 0.0, 1.0, WEIGHTS["skill_overlap"], 0.05)
    tfidf_w = st.slider("TF-IDF Similarity Weight", 0.0, 1.0, WEIGHTS["tfidf_similarity"], 0.05)
    total = skill_w + tfidf_w
    if total == 0:
        st.warning("At least one weight must be > 0")
    st.write(f"Sum of weights: **{total:.2f}** (normalized internally)")

col1, col2 = st.columns(2)
with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
with col2:
    jd_source = st.radio("📌 Job Description Source", ["Paste text", "Upload .txt"], horizontal=True)
    jd_text = ""
    if jd_source == "Paste text":
        jd_text = st.text_area("Paste JD here", height=200, placeholder="Paste the job description...")
    else:
        jd_upload = st.file_uploader("Upload JD (.txt)", type=["txt"], key="jd_upload")
        if jd_upload:
            jd_text = jd_upload.getvalue().decode("utf-8", errors="ignore")

st.divider()

if resume_file and jd_text.strip():
    # Save resume
    path = save_upload(UPLOAD_DIR, resume_file)
    stem, ext = split_ext(path)

    raw_text = ""
    pages = 1
    try:
        if ext == ".pdf":
            raw_text, pages = extract_text_from_pdf(str(path))
        elif ext == ".docx":
            raw_text, pages = extract_text_from_docx(str(path))
        else:
            st.error("Unsupported file type.")
            st.stop()
    except Exception as e:
        st.error(f"Failed to parse file: {e}")
        st.stop()

    cleaned_resume = clean_text(raw_text)
    cleaned_jd = clean_text(jd_text)

    # Entities & Skills
    entities = extract_entities(cleaned_resume)
    resume_skills = extract_skills(cleaned_resume)
    # Derive JD skills by keyword matching against catalog as a baseline
    jd_skills = extract_skills(cleaned_jd)

    # Similarities
    sim_tfidf = tfidf_similarity(cleaned_resume, cleaned_jd)
    overlap = skill_overlap_score(resume_skills, jd_skills)

    # Re-weight with user sliders (normalized to sum=1 if needed)
    if (skill_w + tfidf_w) == 0:
        weights = {"skill_overlap": 1.0, "tfidf_similarity": 0.0}
    else:
        s = skill_w + tfidf_w
        weights = {"skill_overlap": skill_w/s, "tfidf_similarity": tfidf_w/s}

    scores = {
        "skill_overlap": overlap,
        "tfidf_similarity": sim_tfidf,
    }
    # Temporarily patch global WEIGHTS for computation
    from analyzer import scorer
    orig = scorer.WEIGHTS.copy() if hasattr(scorer, "WEIGHTS") else {}
    scorer.WEIGHTS = weights
    final_score = overall_score(scores)
    scorer.WEIGHTS = orig if orig else scorer.WEIGHTS

    # ATS
    ats = ats_flags(raw_text, pages)

    # Recommendations
    recs = recommendations(resume_skills, jd_skills)

    # UI Layout
    a, b = st.columns([1,1])
    with a:
        st.subheader("👤 Candidate")
        st.write({
            "email": entities.get("email", ""),
            "phone": entities.get("phone", ""),
        })
        st.subheader("🧩 Extracted Skills")
        st.write(", ".join(resume_skills) or "—")

        st.subheader("📌 JD Skills (detected)")
        st.write(", ".join(jd_skills) or "—")

        st.subheader("⚠️ ATS Flags")
        st.write(ats)

    with b:
        st.subheader("📈 Scores")
        st.metric("Skill Overlap", f"{overlap*100:.1f}%")
        st.metric("TF-IDF Similarity", f"{sim_tfidf*100:.1f}%")
        st.metric("Overall Match", f"{final_score*100:.1f}%")

        st.plotly_chart(gauge_score(final_score), use_container_width=True)

        # build a dict of JD skills -> 1/0 presence
        present_map = {s: (1 if s in set(resume_skills) else 0) for s in jd_skills}
        if present_map:
            st.plotly_chart(bar_skill_match(present_map), use_container_width=True)

    st.divider()
    st.subheader("📝 Recommendations")
    if recs["actions"]:
        for r in recs["actions"]:
            st.write("- ", r)
    else:
        st.success("Great! Your skills align well with the JD. Consider tailoring achievements for impact.")

else:
    st.info("Upload a resume and provide a JD to begin.")