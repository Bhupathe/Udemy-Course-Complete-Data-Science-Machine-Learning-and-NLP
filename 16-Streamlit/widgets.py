import streamlit as st
import pandas as pd

st.title('Streamllit Text input')

name = st.text_input('Enter you name: ')
age = st.slider('Select your age:', 0, 100, 22) ## start, end, default

options =['Python', 'Java', 'C++', "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)


if name and age and choice:
    st.write(f"Hello, {name}")
    st.write(f'Your age is {age}')
    st.write(f"Your favorite language: {choice}")

uploaded_file = st.file_uploader("choose a CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)