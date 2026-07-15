import streamlit as st

from modules.parser import extract_text_from_pdf
from modules.extractor import extract_resume_details
from modules.ats import calculate_ats_score
from modules.roadmap import recommend_career
from modules.projects import recommend_projects
from modules.interview import get_interview_questions


st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.subheader("Your Personalized Career Guidance Platform")

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    details = extract_resume_details(resume_text)

    ats_score, ats_comments = calculate_ats_score(details,resume_text)

    career = recommend_career(details["Skills"])

    projects = recommend_projects(career["career"])

    st.success("Resume Uploaded Successfully!")

    st.header("📄 Resume Details")

    import pandas as pd

    resume_df = pd.DataFrame({
    "Field": [
        "👤 Name",
        "📧 Email",
        "📱 Phone",
        "🔗 LinkedIn",
        "💻 GitHub",
        "🛠 Skills",
        "🎓 Education"
    ],
    "Value": [
        details["Name"],
        details["Email"],
        details["Phone"],
        details["LinkedIn"],
        details["GitHub"],
        ", ".join(details["Skills"]),
        ", ".join(details["Education"])
    ]
    })

    st.table(resume_df)

    st.divider()

    st.header("📊 ATS Score")

    col1, col2 = st.columns([8,1])

    with col1:
     st.progress(ats_score/100)

    with col2:
     st.markdown(f"## {ats_score}%")

    if ats_score >= 85:
     st.success("🟢 Excellent Resume")
    elif ats_score >= 70:
     st.warning("🟡 Good Resume")
    else:
     st.error("🔴 Needs Improvement")

    st.divider()

    st.header("🎯 Career Recommendation")

    st.success(career["career"])

    st.subheader("Career Roadmap")

    for step in career["roadmap"]:
        st.write("➡", step)

    st.subheader("Recommended Certifications")

    for cert in career["certifications"]:
        st.write("🏆", cert)

    st.divider()

    st.header("💼 Recommended Projects")

    for project in projects:

        st.subheader(project["title"])

        st.write("Difficulty :", project["difficulty"])

        st.write("Skills Required")

        for skill in project["skills"]:
            st.write("✔", skill)

        st.divider()
    st.header("🎤 Interview Preparation Assistant")

    questions = get_interview_questions(career["career"])

    for i, q in enumerate(questions, start=1):

      with st.expander(f"Question {i}"):

        st.write("### ❓ Question")
        st.write(q["question"])

        st.write("### ✅ Answer")
        st.write(q["answer"])