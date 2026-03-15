import streamlit as st
import pickle

# load model
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

st.title("Fake News Detection")

news = st.text_area("Enter News")

if st.button("Predict"):

    vec = vectorizer.transform([news])
    result = model.predict(vec)

    if result[0] == 0:
        st.error("Fake News")
    else:
        st.success("Real News")