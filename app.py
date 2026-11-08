import streamlit as st
from groq import Groq

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Education For All",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .hero {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 35px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 18px;
    }

    .card {
        background: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }

    .card h3 {
        color: #4f46e5;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        padding: 25px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎓 AI Education For All</h1>
    <p>Learn smarter. Understand better. Ask anything.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# API Key
# -----------------------------
api_key = st.secrets.get("GROQ_API_KEY", "")

if not api_key:
    st.error("⚠️ Groq API key is not configured.")
    st.info("Please add GROQ_API_KEY in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 AI Education For All")

st.sidebar.markdown("""
### 📚 Learning Tools

Choose what you want to do:
""")

option = st.sidebar.radio(
    "Select an option:",
    [
        "🏠 Home",
        "🤖 AI Study Assistant",
        "📝 Homework Assistance",
        "❓ Question & Answer",
        "📖 Explain a Topic",
        "🎯 Personalized Learning"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI Education For All helps students learn, understand difficult topics, "
    "solve questions, and improve their knowledge."
)

# -----------------------------
# AI Function
# -----------------------------
def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI education assistant. "
                        "Explain answers clearly and simply for students. "
                        "Use examples when useful. "
                        "Do not make answers unnecessarily complicated."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"


# -----------------------------
# HOME
# -----------------------------
if option == "🏠 Home":

    st.subheader("Welcome to AI Education For All 👋")

    st.write(
        "An intelligent educational assistant that helps students "
        "learn faster and understand difficult topics."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🤖 AI Study Assistant</h3>
            <p>Ask AI about your studies and get clear explanations.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📝 Homework Help</h3>
            <p>Get step-by-step help with your homework questions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📖 Learn Topics</h3>
            <p>Understand difficult topics using simple explanations.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🚀 How to Use")

    st.write("1. Select a learning tool from the sidebar.")
    st.write("2. Enter your question or topic.")
    st.write("3. Click the button.")
    st.write("4. Get your AI-generated learning support.")

# -----------------------------
# AI STUDY ASSISTANT
# -----------------------------
elif option == "🤖 AI Study Assistant":

    st.subheader("🤖 AI Study Assistant")

    question = st.text_area(
        "What would you like to learn?",
        placeholder="Example: Explain photosynthesis in simple words."
    )

    if st.button("✨ Ask AI"):

        if question.strip():
            with st.spinner("AI is thinking..."):
                answer = ask_ai(
                    f"Help the student with this study question:\n\n{question}"
                )

            st.markdown("### 📚 AI Answer")
            st.write(answer)

        else:
            st.warning("Please enter a question first.")

# -----------------------------
# HOMEWORK
# -----------------------------
elif option == "📝 Homework Assistance":

    st.subheader("📝 Homework Assistance")

    subject = st.selectbox(
        "Select Subject",
        [
            "Mathematics",
            "Science",
            "English",
            "Computer Science",
            "Pakistan Studies",
            "General Knowledge",
            "Other"
        ]
    )

    homework = st.text_area(
        "Enter your homework question:",
        placeholder="Write your homework question here..."
    )

    if st.button("📘 Solve Homework"):

        if homework.strip():

            prompt = f"""
Subject: {subject}

Homework Question:
{homework}

Help the student understand and solve this question.
Give the answer clearly and explain the important steps.
"""

            with st.spinner("Solving..."):
                answer = ask_ai(prompt)

            st.markdown("### ✅ Solution")
            st.write(answer)

        else:
            st.warning("Please enter your homework question.")

# -----------------------------
# QUESTION & ANSWER
# -----------------------------
elif option == "❓ Question & Answer":

    st.subheader("❓ Question & Answer")

    question = st.text_input(
        "Ask any educational question:",
        placeholder="Example: What is Artificial Intelligence?"
    )

    if st.button("🔍 Get Answer"):

        if question.strip():

            with st.spinner("Finding answer..."):

                answer = ask_ai(
                    f"""
Answer this educational question clearly:

{question}

Give a simple explanation suitable for a student.
"""
                )

            st.markdown("### 💡 Answer")
            st.write(answer)

        else:
            st.warning("Please enter a question.")

# -----------------------------
# EXPLAIN TOPIC
# -----------------------------
elif option == "📖 Explain a Topic":

    st.subheader("📖 Explain a Difficult Topic")

    topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Newton's Laws of Motion"
    )

    level = st.selectbox(
        "Select your learning level:",
        [
            "Beginner",
            "School Student",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("📚 Explain Topic"):

        if topic.strip():

            prompt = f"""
Explain the following topic:

Topic: {topic}
Student Level: {level}

Explain it in simple language.
Include:
1. Definition
2. Main concept
3. Simple example
4. Important points
5. Short summary
"""

            with st.spinner("Preparing explanation..."):
                answer = ask_ai(prompt)

            st.markdown("### 📖 Topic Explanation")
            st.write(answer)

        else:
            st.warning("Please enter a topic.")

# -----------------------------
# PERSONALIZED LEARNING
# -----------------------------
elif option == "🎯 Personalized Learning":

    st.subheader("🎯 Personalized Learning Support")

    name = st.text_input("Student Name")

    subject = st.selectbox(
        "Choose your subject:",
        [
            "Mathematics",
            "Science",
            "English",
            "Computer Science",
            "General Knowledge"
        ]
    )

    level = st.selectbox(
        "Your Level:",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    goal = st.text_area(
        "What do you want to improve?",
        placeholder="Example: I want to improve my Mathematics."
    )

    if st.button("🎯 Create Learning Plan"):

        if goal.strip():

            prompt = f"""
Create a personalized learning plan.

Student Name: {name}
Subject: {subject}
Level: {level}
Goal: {goal}

Create:
1. Learning goals
2. Topics to study
3. Daily practice suggestions
4. Revision strategy
5. Helpful tips

Keep the plan simple and practical.
"""

            with st.spinner("Creating your learning plan..."):
                answer = ask_ai(prompt)

            st.markdown("### 🎓 Your Personalized Learning Plan")
            st.write(answer)

        else:
            st.warning("Please tell us what you want to improve.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    <p>🎓 AI Education For All</p>
    <p>Powered by Python • Streamlit • Groq • GitHub</p>
</div>
""", unsafe_allow_html=True)
