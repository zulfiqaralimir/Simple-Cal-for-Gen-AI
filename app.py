import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app code
def main():
    st.title("Simple Calculator")

    # Input numbers
    num1 = st.number_input("Enter the first number", format="%.2f")
    num2 = st.number_input("Enter the second number", format="%.2f")

    # Dropdown menu for operation selection
    operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

    # When the user clicks the button
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)

        # Display the result
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
