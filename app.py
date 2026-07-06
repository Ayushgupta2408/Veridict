# app.py

import streamlit as st
from dotenv import load_dotenv
from crew import legal_assistant_crew

load_dotenv()

st.set_page_config(page_title="AI Legal Assistant", page_icon="🧠", layout="wide")

st.markdown("""
<h1 style="margin-bottom:0;">
    ⚖️ Veridict
</h1>
<h5 style="margin-top:0; color:#808080; font-weight:400;">
    Personal AI Legal Assistant
</h5>
""", unsafe_allow_html=True)
st.markdown(
    "Enter a legal problem in plain English. This assistant will help you:\n"
    "- Understand the legal issue\n"
    "- Find applicable IPC sections\n"
    "- Retrieve matching precedent cases\n"
    "- Generate a formal legal document"
)

with st.form("legal_form"):
    user_input = st.text_area("📝 Describe your legal issue:", height=250)
    submitted = st.form_submit_button("🔍 Run Legal Assistant")

if submitted:
    if not user_input.strip():
        st.warning("Please enter a legal issue to analyze.")
    else:
        with st.spinner("🔎 Analyzing your case and preparing legal output..."):
            result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

        st.success("✅ Legal Assistant completed the workflow!")

        # Display final result
        st.subheader("📄 Final Output")
        st.markdown(result if isinstance(result, str) else str(result))

        # Optional: Expand sections if intermediate steps are structured (later enhancement)
