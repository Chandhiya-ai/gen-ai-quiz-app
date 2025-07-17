import streamlit as st

st.set_page_config(page_title="Gen AI Quiz App", page_icon="🧠")

#st.image("logo.png", width=100)  # Optional logo

st.title("🤖 Welcome to the Generative AI Quiz App")
st.write("Please enter your details before starting the quiz.")

# Session state initialization
if 'user_name' not in st.session_state:
    st.session_state.user_name = ''
if 'email' not in st.session_state:
    st.session_state.email = ''

# Collect user input
with st.form("user_form"):
    st.session_state.user_name = st.text_input("Your Name")
    st.session_state.email = st.text_input("Your Email")
    submitted = st.form_submit_button("Start Quiz")

    if submitted:
        if st.session_state.user_name and st.session_state.email:
            st.success("You can now go to the Quiz page using the sidebar ➡️")
        else:
            st.error("Please fill in both your name and email.")
