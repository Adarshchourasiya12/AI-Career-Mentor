import streamlit as st
from pypdf import PdfReader
import matplotlib.pyplot as plt

st.title("AI Career Mentor")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type="pdf"
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    required_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "AI",
        "Git",
        "LangChain"
    ]

    found_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in text.lower():
            found_skills.append(skill)

        else:
            missing_skills.append(skill)

    score = int(
        (len(found_skills) /
         len(required_skills)) * 100
    )

    st.subheader("AI Engineer Report")

    st.write(f"Resume Score: {score}/100")

    st.progress(score)

    st.subheader("Skills Found")

    for skill in found_skills:
        st.success(skill)

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.error(skill)

    st.subheader("Suggestions")

    if score < 50:
        st.warning(
            "Add Python, SQL, Deep Learning, Git and LangChain skills to improve your AI Engineer profile."
        )

    elif score < 80:
        st.info(
            "Good profile. Add more AI projects and advanced skills."
        )

    else:
        st.success(
            "Excellent AI Engineer profile!"
        )

    st.subheader("ATS Rating")

    if score < 40:
        st.error("Poor")

    elif score < 70:
        st.warning("Average")

    else:
        st.success("Excellent")

    st.subheader("Career Roadmap")

    st.write("""
Month 1: Learn Python

Month 2: Learn SQL and Git

Month 3: Machine Learning

Month 4: Deep Learning

Month 5: LangChain and RAG

Month 6: Build AI Projects
""")

    st.subheader("Resume Statistics")

    st.write(f"Skills Found: {len(found_skills)}")
    st.write(f"Skills Missing: {len(missing_skills)}")
    labels = ["Found Skills", "Missing Skills"]
    sizes = [len(found_skills), len(missing_skills)]

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    st.pyplot(fig)  
    if score >= 70:
        st.balloons()