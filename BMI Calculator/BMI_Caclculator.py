import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your Height(in cm): ", 100, 250, 175 )
weight = st.slider("Enter yur Weight (in Kg)", 40, 200 , 70)

bmi = weight / ((height/100) **2)

st.write(f"Your BM is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5 or less")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI between 30 or greater")