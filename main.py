import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Review Analyzer", layout="wide")

st.title("🧠 Smart Review Analyzer")
st.write("Upload a CSV file with customer reviews to get started.")

uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    def analyze_sentiment(text):
        if not isinstance(text, str):
            return "neutral"
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return "positive +"
        elif polarity < 0:
            return "negative -"
        else:
            return "neutral ~"

    # Apply sentiment analysis to each review
    df["sentiment"] = df["review_text"].apply(analyze_sentiment)

    st.subheader("Reviews with Sentiment")
    st.write(df.head())

    st.subheader("Preview of Uploaded Reviews")
    st.write(df.head())  # show the first few rows
else:
    st.info("Please upload a CSV file to begin.")

# Filter by sentiment
sentiment_options = df["sentiment"].unique().tolist()
sentiment_filter = st.multiselect(
    "Filter by Sentiment",
    options=sentiment_options,
    default=sentiment_options  # Show all by default
)

# Apply filter
filtered_df = df[df["sentiment"].isin(sentiment_filter)]

st.subheader("Filtered Reviews")
st.write(filtered_df)
# Offer CSV download of filtered data
csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download Filtered Results as CSV",
    data=csv,
    file_name='filtered_reviews.csv',
    mime='text/csv',
)

# Count sentiment values
sentiment_counts = df["sentiment"].value_counts()

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures pie is a circle

st.subheader("Sentiment Distribution")
st.pyplot(fig)

# Bar chart version
fig, ax = plt.subplots()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'], ax=ax)
ax.set_title("Sentiment Distribution")
ax.set_xlabel("Sentiment")
ax.set_ylabel("Count")
st.pyplot(fig)

# Move sentiment filter to sidebar
with st.sidebar:
    st.header("🔍 Filter Options")
    sentiment_filter = st.multiselect(
        "Select Sentiments",
        options=sentiment_options,
        default=sentiment_options
    )

    st.markdown("---")
    st.markdown("📄 [Download Filtered CSV above in main view]")

# Apply filter
filtered_df = df[df["sentiment"].isin(sentiment_filter)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sentiment Chart")
    st.pyplot(fig)

with col2:
    st.subheader("Filtered Reviews")
    st.write(filtered_df)

