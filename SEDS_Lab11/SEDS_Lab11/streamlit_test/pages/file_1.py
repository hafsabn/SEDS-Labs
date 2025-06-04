import streamlit as st
from transformers import pipeline

text = st.text_input("Enter text to analyze")

@st.cache_resource()
def get_model():
    return pipeline("sentiment-analysis")
model = get_model()

if text:
    result = model(text)
    st.write("sentiment: ",result[0]["label"])
    st.write("Confidence: ",result[0]["score"])