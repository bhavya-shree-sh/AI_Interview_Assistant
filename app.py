
import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Assistant Interview", layout="centered")

st.title("AI Interview Assistant")
st.caption("Launched By Bhavyashree")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API Key is missing. Add it in Advanced Settings.")
    st.stop()

role = st.selectbox(
    "Job Title",
    ["Machine Learning Engineer", "Senior Software Engineer",
     "DevOps Engineer", "Data Analyst", "Other"]
)

if role == "Other":
    role = st.text_input("Enter your Job Title", "XXXXXXX")

gen_model = st.selectbox(
    "Model",
    ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
)

level = st.selectbox(
    "Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

mode = st.radio(
    "Activity",
    ["Generate Questions", "Generate Code Questions",
     "Evaluate Answers", "Improve Answers"]
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

if st.button("Generate AI Response", type="primary"):

    if mode in ["Evaluate Answers", "Improve Answers"]:
        if not questions.strip() or not answer.strip():
            st.warning("Please enter a valid Question and Answer.")
            st.stop()

    background = (
        "Job role: " + role +
        ". Difficulty level: " + level + ". "
    )

    if mode == "Generate Questions":
        task = (
            "Generate " + str(count) +
            " frequently asked interview questions. "
            "Include theory and scenario-based questions. "
            "Do not give answers. Give hints."
        )

    elif mode == "Generate Code Questions":
        task = (
            "Generate " + str(count) +
            " frequently asked coding questions on topic " + topic +
            ". Include hints to solve them. Be accurate."
        )

    elif mode == "Evaluate Answers":
        task = (
            "Question: " + questions +
            "\nMy answer: " + answer +
            "\nEvaluate based on concept, relevance, communication "
            "and length of answer. Give each rating out of 5."
        )

    elif mode == "Improve Answers":
        task = (
            "Question: " + questions +
            "\nMy answer: " + answer +
            "\nImprove the answer based on choice of words "
            "and provide a better version."
        )

    with st.spinner("Generating your answer..."):
        try:
            response = client.chat.completions.create(
                model=gen_model,
                messages=[
                    {
                        "role": "system",
                        "content": "Act as a senior interviewer and HR and technical expert."
                    },
                    {
                        "role": "user",
                        "content": background + task
                    }
                ],
                temperature=0.7,
                max_tokens=1800
            )

            output = response.choices[0].message.content

            st.subheader("AI Response")
            st.write(output)

            st.download_button(
                "Download Response",
                output,
                file_name="Interview_Response.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error("API connection was unsuccessful.")
            st.info("Please check your API key and rate limits.")
            st.caption("Powered by Streamlit, GitHub and Groq API.")
```
