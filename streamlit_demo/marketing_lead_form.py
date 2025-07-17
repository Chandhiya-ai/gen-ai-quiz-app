import streamlit as st
import datetime

# ---- Branding ----
st.set_page_config(page_title="📈 Get Marketing Help", page_icon="🚀")

st.title("🚀 Let's Grow Your Business With Digital Marketing!")
st.write("Answer a few quick questions so I can understand your business better.")

st.markdown("---")

# ---- Form ----
with st.form("lead_form", clear_on_submit=False):
    business_name = st.text_input("🧾 Business Name", placeholder="e.g., FitMonkey Gym")
    phone = st.text_input("📞 Phone Number", placeholder="e.g., 9876543210")

    budget = st.slider("💸 Monthly Marketing Budget (₹)", 1000, 100000, step=1000)
    
    goals = st.text_area("🎯 What is your main goal with marketing?", placeholder="e.g., Get more local leads, brand visibility...")

    submitted = st.form_submit_button("📤 Submit")

# ---- Action ----
if submitted:
    if business_name and phone:
        st.success("✅ Details received! I will contact you shortly.")
        
        st.write("**Here's what you submitted:**")
        st.write(f"📌 **Business Name**: {business_name}")
        st.write(f"📞 **Phone**: {phone}")
        st.write(f"💰 **Budget**: ₹{budget}")
        st.write(f"🎯 **Goal**: {goals}")

        # Save to a simple text file (you can change this to a DB later)
        with open("leads.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | {business_name} | {phone} | ₹{budget} | {goals}\n")

    else:
        st.error("❌ Please fill in both business name and phone number.")
