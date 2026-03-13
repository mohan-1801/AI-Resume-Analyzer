import streamlit as st
import re
from dotenv import load_dotenv

from resume_parser import extract_text
from analyzer import analyze_resume

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume to get AI-powered ATS feedback and suggestions.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    if not text:
        st.error("Could not extract text from the PDF.")
    else:
        st.subheader("Resume Analysis")

        try:
            with st.spinner("Analyzing resume with AI..."):
                result = analyze_resume(text)

            # Display result
            st.write(result)

            # Extract ATS score
            match = re.search(r"Resume Score:\s*(\d+)", result)

            if match:
                score = int(match.group(1))

                st.subheader("ATS Score")
                st.progress(score / 100)
                st.metric("Score", f"{score}/100")

            # Download button
            st.download_button(
                label="Download Analysis",
                data=result,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Analysis failed: {e}")