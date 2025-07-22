import streamlit as st

st.title("📏 Rectangle Math Party")

# Inputs: Length and Breadth
length = st.number_input("Enter the length of the rectangle:", min_value=0.0)
breadth = st.number_input("Enter the breadth of the rectangle:", min_value=0.0)

# Option to select what to calculate
options = st.multiselect(
    "What would you like to calculate?",
    ["Area", "Perimeter"]
)

# Calculate results
if st.button("Calculate"):
    if "Area" in options:
        area = length * breadth
        st.success(f"Area: {area:.2f} square units")

    if "Perimeter" in options:
        perimeter = 2 * (length + breadth)
        st.success(f"Perimeter: {perimeter:.2f} units")

    if not options:
        st.warning("Please select at least one option.")
