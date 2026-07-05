import streamlit as st
from pypdf import PdfReader
import matplotlib.pyplot as plt
# from hf_helper import analyze_resume

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
    st.subheader("AI Resume Analysis")

    #with st.spinner("Analyzing Resume..."):
    #        result = analyze_resume(text)

    #st.write(result)

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

    st.subheader("Recommended Career Roles")
    roles = []
    if "Python" in found_skills:
        roles.append("Python Developer")

    if "Machine Learning" in found_skills:
        roles.append("Machine Learning Engineer")

    if "Deep Learning" in found_skills:
        roles.append("AI Engineer")

    if "SQL" in found_skills:
        roles.append("Data Analyst")

    if "LangChain" in found_skills:
        roles.append("Generative AI Engineer")

    if roles:
        for role in roles:
            st.success(role)
    else:
        st.warning(
            "Add more technical skills to get career recommendations."
        )
    
    st.subheader("Resume Level")

    if score < 40:
        st.error("Beginner")
    elif score < 70:
        st.warning("Intermediate")
    else:
        st.success("Advanced")

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
    st.subheader("Resume Preview")
    st.subheader("Skill Match Progress")

    for skill in required_skills:

        if skill in found_skills:
            st.write(f"{skill} ✅")
            st.progress(100)

        else:
            st.write(f"{skill} ❌")
            st.progress(0)

    st.text_area(
        "Extracted Resume Text",
        text,
        height=250
    )
    st.subheader("Resume Strength")

    if score >= 80:
        st.success("Strong Resume 💪")
    elif score >= 60:
        st.warning("Moderate Resume ⚡")
    else:
        st.error("Weak Resume ❌")
    st.subheader("Keyword Frequency")

    for skill in required_skills:
        count = text.lower().count(skill.lower())
        st.write(f"{skill}: {count}")
        if "cnn" in text.lower() and "Deep Learning" not in found_skills:
         found_skills.append("Deep Learning")

        if "Deep Learning" in missing_skills:
            missing_skills.remove("Deep Learning")

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
    report = f"""
Resume Score: {score}/100

Skills Found:
{', '.join(found_skills)}

Skills Missing:
{', '.join(missing_skills)}

ATS Rating:
{"Excellent" if score >= 70 else "Average" if score >= 40 else "Poor"}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )
    st.subheader("Career Readiness")

    if score >= 80:
        st.success("You are Job Ready 🚀")
    elif score >= 60:
        st.warning("You are Almost Ready ⚡")
    else:
        st.error("Need More Skills 📚")


    st.subheader("Learning Recommendations")

    if "Deep Learning" in missing_skills:
        st.info(
            "Deep Learning → Learn Neural Networks, TensorFlow and PyTorch"
        )

    if "LangChain" in missing_skills:
        st.info(
            "LangChain → Learn RAG, Vector Databases and AI Agents"
        )

    if "SQL" in missing_skills:
        st.info(
            "SQL → Learn Database Queries and Data Analysis"
        )

    if "Git" in missing_skills:
        st.info(
            "Git → Learn GitHub, Branching and Version Control"
        )

    if "Machine Learning" in missing_skills:
        st.info(
            "Machine Learning → Learn Scikit-Learn, Regression and Classification"
        )


    st.subheader("Skill Gap Analysis")

    gap = len(missing_skills)
    total = len(required_skills)

    gap_percent = int((gap / total) * 100)

    st.write(f"Skill Gap: {gap_percent}%")
    st.progress(100 - gap_percent)


    st.subheader("Action Plan")

    if missing_skills:

        st.write("Focus on these skills first:")

        for skill in missing_skills:
            st.write(f"• Learn {skill}")

    else:
        st.success(
            "Great! All required skills are present."
        )


    st.subheader("Performance Dashboard")

    skills_score = score
    ats_score = min(score + 10, 100)
    readiness_score = min(score + 5, 100)

    overall_score = int(
        (skills_score + ats_score + readiness_score) / 3
    )

    st.write(f"Skills Score: {skills_score}%")
    st.write(f"ATS Score: {ats_score}%")
    st.write(f"Career Readiness: {readiness_score}%")
    st.write(f"Overall Score: {overall_score}%")

    if score >= 70:
        st.balloons()