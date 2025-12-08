import streamlit as st

st.title("Simple Calculator")

# Take user inputs safely
n1 = st.text_input("Enter first number:")
n2 = st.text_input("Enter second number:")

# Button to calculate
if st.button("Calculate"):
    try:
        # Convert inputs to numbers
        num1 = float(n1)
        num2 = float(n2)

        # Perform operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Handle division by zero
        if num2 == 0:
            division = "Error: Cannot divide by zero"
        else:
            division = num1 / num2

        # Display results
        st.success(f"Addition: {addition}")
        st.success(f"Subtraction: {subtraction}")
        st.success(f"Multiplication: {multiplication}")
        st.success(f"Division: {division}")

    except ValueError:
        st.error("Invalid input! Please enter numeric values only.")
