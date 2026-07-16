import os
from pathlib import Path

import streamlit as st

from src.utils import save_uploaded_file
from src.parser import read_document
from src.preprocess import preprocess_text
from src.similarity import calculate_similarity
from src.skills import extract_skills, load_skills
from src.scoring import (
    calculate_skill_score,
    calculate_final_score,
    interpret_score,
)

st.set_page_config(
    page_title="Resume Keyword Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Resume Keyword Analyzer")

st.write(
    "Upload a resume and a job description to evaluate the overall match, "
    "skill coverage, and missing skills."
)

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx", "txt"],
)

jd_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "docx", "txt"],
)

if resume_file and jd_file:

    with st.spinner("Analyzing resume..."):

        resume_path = save_uploaded_file(resume_file)
        jd_path = save_uploaded_file(jd_file)

        try:
            # Read and preprocess
            resume_text = preprocess_text(read_document(resume_path))
            jd_text = preprocess_text(read_document(jd_path))

            # Load skill database
            skills_path = Path("data") / "skills.txt"
            skill_set = load_skills(skills_path)

            # Extract skills
            resume_skills = extract_skills(resume_text, skill_set)
            jd_skills = extract_skills(jd_text, skill_set)

            matched = resume_skills & jd_skills
            missing = jd_skills - resume_skills

            # Calculate scores
            similarity = calculate_similarity(resume_text, jd_text)
            skill_score = calculate_skill_score(matched, jd_skills)
            final_score = calculate_final_score(similarity, skill_score)

            st.success("Analysis completed successfully!")

            st.divider()

            st.subheader("📊 Analysis Results")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Similarity", f"{similarity * 100:.2f}%")

            with col2:
                st.metric("Skill Match", f"{skill_score * 100:.2f}%")

            with col3:
                st.metric("Final Score", f"{final_score * 100:.2f}%")

            st.info(f"Interpretation: {interpret_score(final_score)}")

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("✅ Matched Skills")

                if matched:
                    for skill in sorted(matched):
                        st.write(f"• {skill}")
                else:
                    st.write("No matched skills found.")

            with col2:
                st.subheader("❌ Missing Skills")

                if missing:
                    for skill in sorted(missing):
                        st.write(f"• {skill}")
                else:
                    st.write("No missing skills.")

        except Exception as e:
            st.error(f"An error occurred while analyzing the documents.\n\n{e}")

        finally:
            # Remove temporary files
            if resume_path.exists():
                os.remove(resume_path)

            if jd_path.exists():
                os.remove(jd_path)