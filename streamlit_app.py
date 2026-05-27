
import streamlit as st
import math

st.title("🚀 My Super Calculator")

# Pick what kind of math to do
mode = st.selectbox("What should I calculate?", ["Math", "Money", "Science"])

if mode == "Math":
    n1 = st.number_input("Number 1")
    n2 = st.number_input("Number 2")
    if st.button("Add"): st.write(f"Answer: {n1 + n2}")
    if st.button("Multiply"): st.write(f"Answer: {n1 * n2}")

elif mode == "Money":
    amount = st.number_input("Amount of Dollars")
    rate = st.number_input("Tax Rate (in %)")
    if st.button("Calculate Tax"):
        st.write(f"Tax is: ${amount * (rate/100)}")

elif mode == "Science":
    num = st.number_input("Enter a number")
    if st.button("Find Square Root"):
        st.write(f"The square root is: {math.sqrt(num)}")
