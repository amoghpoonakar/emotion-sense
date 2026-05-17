import streamlit as st
import pickle

from responses import responses

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page title
st.title("Emotion Detection Chat App")

# User input
user_input = st.text_input("Type your message")

if user_input:

    # Convert text
    transformed_text = vectorizer.transform([user_input])

    # Predict emotion
    prediction = model.predict(transformed_text)[0]

    st.subheader("Detected Emotion:")
    st.success(f"Detected Emotion: {prediction}")

    # Bot reply
    bot_reply = responses.get(
        prediction,
        "I understand."
    )

    st.subheader("Bot Reply:")
    st.write(bot_reply)
    
    