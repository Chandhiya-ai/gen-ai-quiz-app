import streamlit as st

st.set_page_config(page_title="Gen AI Quiz")

if 'user_name' not in st.session_state or st.session_state.user_name == '':
    st.warning("Please go to the Home page and enter your name & email first.")
    st.stop()

st.title("🧠 Generative AI Quiz")

score = 0
total = 5

# Quiz Questions
q1 = st.radio("1. What does 'LLM' stand for in Generative AI?",
              ["Large Language Model", "Limited Learning Model", "Logical Language Machine"])
if q1 == "Large Language Model":
    score += 1

q2 = st.radio("2. Which company developed ChatGPT?",
              ["Google", "Meta", "OpenAI"])
if q2 == "OpenAI":
    score += 1

q3 = st.radio("3. Which of the following is a text-to-image model?",
              ["GPT-4", "DALL·E", "BERT"])
if q3 == "DALL·E":
    score += 1

q4 = st.radio("4. What is a typical use case of Generative AI?",
              ["Spreadsheets", "Email composing", "Wi-Fi setup"])
if q4 == "Email composing":
    score += 1

q5 = st.radio("5. What is 'prompt engineering' in Gen AI?",
              ["Fixing bugs in code", "Designing machines", "Crafting effective inputs for AI models"])
if q5 == "Crafting effective inputs for AI models":
    score += 1

# Submit
if st.button("Submit Quiz"):
    st.success(f"🎉 Thank you, {st.session_state.user_name}!")
    st.write(f"✅ Your Score: **{score}/{total}**")

    if score == total:
        st.balloons()
        st.info("Excellent! You're a Gen AI Pro! 🎉")
    elif score >= 3:
        st.info("Good job! Keep learning.")
    else:
        st.warning("Nice try! Keep exploring Gen AI.")

