import anthropic
import streamlit as st

client = anthropic.Anthropic()

st.set_page_config(page_title="🎯TechYard CV Scorer")
st.markdown("""
    <style>
    .stButton > button {
        background-color: #dd762e;
        color: white;
        border: none;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #c4651f;
        color: white;
    }
    h1, h2, h3 {
    color: #dd762e !important;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://img.icons8.com/fluency/96/goal.png", width=60)
st.title("TechYard CV Scorer")
st.write("Powered by AI — score any candidate against a role in seconds.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Job description")
    job_description = st.text_area("", height=300, placeholder="Paste the job description here...")

with col2:
    st.subheader("Candidate CV")
    cv_text = st.text_area("", height=300, placeholder="Paste the CV text here...")

st.divider()

if st.button("Score this candidate", use_container_width=True):
    if job_description and cv_text:
        with st.spinner("Analysing candidate fit..."):
            prompt = "Score this CV against this job description from 1-10 and explain why.\n\nJob:\n" + job_description + "\n\nCV:\n" + cv_text
            message = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            st.divider()
            st.subheader("Assessment result")
            st.markdown(message.content[0].text)
    else:
        st.warning("Please paste both a job description and a CV before scoring.")