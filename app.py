import streamlit as st
from utils.planner import plan_task
from utils.browser import run_task

st.set_page_config(page_title="AI Browser Agent", layout="wide")

st.title("🌐 AI Browser Automation Agent")

st.write("Give a task and let AI perform it on the web.")

task = st.text_input("Enter your task (e.g., search iPhone on Amazon):")

if st.button("Run Task"):
    if task:
        with st.spinner("Planning..."):
            plan = plan_task(task)

        st.subheader("🧠 AI Plan")
        st.write(plan)

        with st.spinner("Executing task..."):
            result = run_task(task)

        st.subheader("📊 Results")
        st.write(result)
