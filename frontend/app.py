import streamlit as st
import requests

st.title("📄 AI Resume Skill Analyzer")

st.write("Paste your CV or resume text below:")

text = st.text_area("Resume Input")

if st.button("Analyze Skills"):
    if text.strip() != "":
        response = requests.post(
            "http://127.0.0.1:8000/extract",
            json={"text": text}
        )

        data = response.json()

        st.subheader("🔍 Extracted Skills")

        for skill in data["skills"]:
            st.write("•", skill)
    else:
        st.warning("Please enter text")