import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Interview Assistant",
    layout="centered"
)

st.title("AI Interview Assistant")
st.caption("Practice and Prepare for your Placements here")

# Connect to Groq API
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

except Exception as e:
    st.error("API Key is missing or incorrect. Check Streamlit Secrets.")
    st.stop()

# Job Title
role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Senior Software",
        "DevOps Engineer",
        "Data Analyst",
        "Other"
    ]
)

if role == "Other":
    role = st.text_input("Enter your Job Title")

# Model selection
model = st.selectbox(
    "Model",
    ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
)

# Difficulty
level = st.selectbox(
    "Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

# Activity
mode = st.radio(
    "Activity",
    [
        "Generate Questions",
        "Generate Code Questions",
        "Evaluate Answers",
        "Improve Answers"
    ]
)

if mode == "Generate Questions":
    count = st.slider("Number of Questions", 1, 10, 5)

elif mode == "Generate Code Questions":
    topic = st.selectbox(
        "Topics",
        ["SQL", "AIML", "Python", "DSA", "Java", "C/C++"]
    )
    count = st.slider("Number of Questions", 1, 10, 5)

else:
    questions = st.text_area("Enter Interview Questions here")
    answer = st.text_area("Enter your answer", height=160)

st.write("Your selections are ready!")
