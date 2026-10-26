import streamlit as st
import plotly.express as px
from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import load_skills, extract_skills
from job_matcher import ROLES, match_roles, skill_gap
from roadmap_generator import make_roadmap

st.title("AI Resume Analyzer")

file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if file:
    raw = extract_text(file)
    cleaned = clean_text(raw)

    if not cleaned:
        st.error("No text found. Try a DOCX or a text-based PDF.")
    else:
        found = extract_skills(cleaned, load_skills())

        st.subheader("Skills found")
        st.write(", ".join(found) if found else "No skills detected")

        results = match_roles(found)

        st.subheader("Top 3 recommended roles")
        for i, (role, score) in enumerate(results[:3], start=1):
            st.write(f"{i}. **{role}** - {score}%")

        fig = px.bar(x=[r for r, _ in results], y=[s for _, s in results],
                     labels={"x": "Role", "y": "Match score (%)"})
        st.plotly_chart(fig)

        st.subheader("Skill gap for a target role")
        target = st.selectbox("Choose a target role", list(ROLES.keys()))
        have, missing = skill_gap(found, target)

        st.write("Skills you have:", ", ".join(have) if have else "None")
        st.write("Missing skills:", ", ".join(missing) if missing else "None")

        if missing:
            st.subheader("Learning roadmap")
            for step in make_roadmap(missing):
                st.write(step)

        report = f"""AI RESUME ANALYSIS REPORT
File: {file.name}

Skills found: {", ".join(found)}

Top roles:
""" + "\n".join(f"{i}. {r} - {s}%" for i, (r, s) in enumerate(results[:3], 1)) + f"""

Target role: {target}
Skills you have: {", ".join(have)}
Missing skills: {", ".join(missing)}

Roadmap:
""" + "\n".join(make_roadmap(missing)) + """

Note: match scores are estimates, not recruiter decisions.
A missing keyword does not always mean a missing ability.
"""

        st.download_button("Download report", report, file_name="resume_report.txt")

        st.caption("Match scores are estimates, not recruiter decisions. "
                   "A missing keyword does not always mean a missing ability.")