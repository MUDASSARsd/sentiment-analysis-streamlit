import streamlit as st
import pickle as pk

st.set_page_config(page_title="Movie Sentiment Analysis", page_icon="🎬")

st.title("🎬 Movie Review Sentiment Analysis")
st.write("Enter a movie review below and click **Predict**.")

model = pk.load(open("model.pkl", "rb"))
vectorizer = pk.load(open("scaler.pkl", "rb"))

review = st.text_area("Movie Review")

if st.button("Predict"):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)

    if prediction[0] == 1:
        st.success("😊 Positive Review")
    else:
        st.error("😞 Negative Review")