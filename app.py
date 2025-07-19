import streamlit as st
from llm_engine import explain_topic
from quiz_generator import generate_quiz
from study_plan import create_study_plan
from db import init_db, log_interaction, get_history

st.set_page_config(page_title="EduMentor AI", layout="centered")
st.sidebar.title("EduMentor AI")
option = st.sidebar.radio("Choose a feature:", ["Topic Explainer", "Quiz Generator", "Study Plan Creator"])

with st.sidebar:
    api_key = st.text_input("Enter your OpenAI API Key", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar.")
    st.stop()

init_db()
st.title("EduMentor AI: Smart Study Assistant")

if option == "Topic Explainer":
    topic = st.text_input("Enter a topic (e.g., Binary Trees):")
    level = st.selectbox("Select your level:", ["Beginner", "Intermediate", "Advanced"])
    if st.button("Explain") and topic:
        with st.spinner("Explaining topic..."):
            explanation = explain_topic(api_key, topic, level)
        st.markdown(f"### Explanation for {topic} ({level})")
        st.write(explanation)
        log_interaction("Topic Explainer", topic, level)

elif option == "Quiz Generator":
    topic = st.text_input("Enter a topic to generate a quiz:")
    if st.button("Generate Quiz") and topic:
        with st.spinner("Generating quiz..."):
            quiz = generate_quiz(api_key, topic)
        st.markdown("### Quiz")
        for idx, q in enumerate(quiz):
            st.markdown(f"**Q{idx+1}. {q['question']}**")
            for opt in q['options']:
                st.markdown(f"- {opt}")
        log_interaction("Quiz Generator", topic, "3 MCQs generated")

elif option == "Study Plan Creator":
    subject = st.text_input("Enter your subject (e.g., Operating Systems):")
    days = st.slider("Number of days to prepare:", 1, 30, 7)
    if st.button("Create Study Plan") and subject:
        with st.spinner("Creating your study plan..."):
            plan = create_study_plan(api_key, subject, days)
        st.markdown("### Personalized Study Plan")
        st.write(plan)
        log_interaction("Study Plan Creator", subject, f"{days} days")

with st.expander("📜 View Recent History"):
    history = get_history()
    for h in history:
        st.markdown(f"**[{h[0]}]**: *{h[1]}* → `{h[2]}` at `{h[3]}`")
