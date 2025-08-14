from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
JD_DIR = BASE_DIR / "job_descriptions"

# Primary knobs for scoring
WEIGHTS = {
    "skill_overlap": 0.6,   # overlap of extracted skills with required skills
    "tfidf_similarity": 0.4 # cosine similarity between resume text and JD
}

# A lightweight default skills catalog (expand freely)
DEFAULT_SKILLS = {
    "programming": [
        "python", "java", "c++", "javascript", "typescript", "go", "rust"
    ],
    "data": [
        "pandas", "numpy", "matplotlib", "plotly", "scikit-learn",
        "tensorflow", "pytorch", "sql", "power bi", "excel"
    ],
    "cloud_devops": [
        "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "linux", "ci/cd"
    ],
    "web": [
        "html", "css", "react", "node", "express", "django", "flask", "streamlit", "bootstrap"
    ],
    "soft": [
        "communication", "leadership", "teamwork", "problem solving", "agile", "scrum"
    ]
}