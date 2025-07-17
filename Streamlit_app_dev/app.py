import streamlit as st

# Set page config
st.set_page_config(page_title="Welcome to Python Tutorial", page_icon="🐍")

# App Title
st.title("👋 Welcome to Your Python Streamlit Journey!")

# Input for name
name = st.text_input("Enter your name:")

# Know More button
if st.button("🚀 Know More"):
    if name.strip() == "":
        st.warning("⚠️ Please enter your name before proceeding.")
    else:
        st.success(f"🎉 {name}, you are successfully registered!")
        st.write("✅ This is your **first step** into the world of **digital creation**. Let's build something amazing together!")
