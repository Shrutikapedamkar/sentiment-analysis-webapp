import streamlit as st
from textblob import TextBlob

from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Sentiment Analysis App",layout="wide")

with st.container():
    st.title("Sentiment Analysis!")

text = st.text_area("Please enter your comment here...")

if st.button("Analyze the Sentiment"):
    blob = TextBlob(text)
    result = blob.sentiment
    polarity = result.polarity
    subjectivity = result.subjectivity
    if polarity<0:
        st.warning("The comment has negative sentiments "+str(polarity))
        rain(
            emoji="😫",
            font_size=50,
            falling_speed=3,
            animation_length="infinite",
        )
    if polarity>0:
        st.success("The comment has positive sentiments "+str(polarity))
        rain(
            emoji="😁",
            font_size=50,
            falling_speed=3,
            animation_length="infinite",
        )
    st.success(result)