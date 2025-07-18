import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.recommender import extract_text_from_pdf, recommend_roles

st.set_page_config(page_title="AI Job Recommender", layout="centered")

st.title("AI Job Recommender")
st.markdown("Upload your resume and specify your career goal to get AI-powered job role suggestions.")

# Upload PDF
resume_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
career_goal = st.text_input("Your career goal (e.g. 'Computer Vision Engineer')")

if st.button("Get Recommendations"):
    if resume_file and career_goal:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(resume_file)
            suggestions = recommend_roles(resume_text, career_goal)
        st.success("Here are your recommended roles:")
        st.markdown(f"📝 **Career Goal**: {career_goal}")
        st.markdown("### ✅ Suggested Roles:")
        st.markdown(suggestions)
    else:
        st.warning("Please upload a PDF resume and enter your career goal.")
