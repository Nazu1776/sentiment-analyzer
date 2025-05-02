import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.title("🧠 Sentiment Analyzer")
st.write("Analyze the sentiment of your text as **Positive**, **Negative**, or **Neutral**.")

# Text Input
user_input = st.text_area("Enter your review or sentence here:")

# Sentiment Function
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Button and Output
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentiment = get_sentiment(user_input)
        st.success(f"Sentiment: **{sentiment}**")

# Optional: Test Multiple Examples
st.markdown("---")
st.subheader("📊 Example Sentiment Chart")

sample_data = [
    "I love this movie!",
    "This is the worst service ever.",
    "Absolutely fantastic!",
    "Not bad, but could be better.",
    "Terrible experience. Do not recommend.",
    "Great job, very satisfied!"
]

df = pd.DataFrame(sample_data, columns=["Text"])
df["Sentiment"] = df["Text"].apply(get_sentiment)

# Plotting
fig, ax = plt.subplots()
sns.countplot(x="Sentiment", data=df, palette="pastel", ax=ax)
plt.title("Sentiment Distribution (Sample Data)")
st.pyplot(fig)
