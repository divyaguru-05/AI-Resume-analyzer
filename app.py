import streamlit as st
import PyPDF2

st.title("AI Resume Skill Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

skills_list = [
    "python","java","c++","html","css",
    "javascript","verilog","c","vhdl","vlsi"
]

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.lower()

    detected_skills = []
    missing_skills = []

    for skill in skills_list:
        if skill in text:
            detected_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_skills = len(skills_list)
    found_skills = len(detected_skills)

    score = int((found_skills / total_skills) * 100)

    st.subheader("Detected Skills")
    st.write(detected_skills)

    st.subheader("Missing Skills")
    st.write(missing_skills)

    st.subheader("Resume Score")
    st.progress(score)
    st.write(score, "% Skill Match")

    st.subheader("Suggested Learning Areas")
    st.write(missing_skills[:3])

