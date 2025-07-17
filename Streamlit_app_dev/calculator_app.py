import streamlit as st

# Set page configuration
st.set_page_config(page_title="🧮 Simple Calculator", page_icon="📟")

# App title
st.title("🧮 Simple & Safe Calculator App")

# Input numbers
num1 = st.text_input("Enter the first number:")
num2 = st.text_input("Enter the second number:")

# Select operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# When user clicks the Calculate button
if st.button("Calculate"):
    # Validate inputs
    if not num1.strip() or not num2.strip():
        st.warning("⚠️ Please enter both numbers.")
    else:
        try:
            a = float(num1)
            b = float(num2)

            # Perform operation
            if operation == "Add":
                result = a + b
            elif operation == "Subtract":
                result = a - b
            elif operation == "Multiply":
                result = a * b
            elif operation == "Divide":
                if b == 0:
                    st.error("❌ Cannot divide by zero.")
                    result = None
                else:
                    result = a / b
            else:
                result = None

            if result is not None:
                st.success(f"✅ Result: {result}")

        except ValueError:
            st.error("❌ Please enter valid numeric values.")
