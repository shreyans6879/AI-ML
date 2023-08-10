import streamlit as st
import joblib

st.title("Underweight/ Overweight/ Normal Predictor")
weight = st.slider('What is your weight?',0,100,25)
height = st.slider('What is your height?',0,200,25)
model = joblib.load('model_new')
result =  model.predict([[weight,height]])[0]

if st.button("Predict"):
  st.write(f"You are {result}")
