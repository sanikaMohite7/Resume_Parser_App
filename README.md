# AI-Powered Resume Parser & Analyzer (Streamlit)  
**Created by Sanika Mohite**  

This project is a **production-ready starter** for parsing resumes (**PDF/DOCX**), extracting **skills, work experience, education, and named entities**, and matching them against a given **Job Description (JD)**.  
It also performs **ATS (Applicant Tracking System) compatibility checks** and generates **interactive visual dashboards** — all built with **Streamlit**.  

---

## 🚀 Features
- **Multi-format resume parsing** — Supports PDF & DOCX.  
- **Skill extraction & tagging** — Detects both hard and soft skills.  
- **JD Matching** — Compares extracted skills with job requirements.  
- **ATS Compliance Check** — Flags missing keywords, formatting issues, and structural problems.  
- **Interactive Dashboard** — Visualizes skill gaps and keyword matches.  
- **Exportable Reports** — Save results to CSV or JSON.  

---

## 🔧 Quickstart
```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the Streamlit app
streamlit run app.py

📁 Project Structure
resume_parser_analyzer/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── utils/
│   ├── parser.py           # Resume parsing logic
│   ├── jd_matcher.py       # JD matching & skill comparison
│   ├── ats_checker.py      # ATS compliance checks
│   ├── visualizer.py       # Dashboard rendering
│
├── data/
│   ├── sample_resume.pdf   # Example resume
│   ├── sample_jd.txt       # Example job description
│
└── README.md               # Documentation

📌 Notes

Replace sample data with real resumes and JDs.

Enhance skill extraction using spaCy or Hugging Face Transformers.

Integrate with ATS APIs for live recruitment pipelines.

Deploy to Streamlit Cloud or Heroku for remote access.
