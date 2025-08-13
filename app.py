import streamlit as st
from transformers import pipeline

# Load the summarization model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Streamlit UI
st.set_page_config(page_title="AI Chat Summarizer", page_icon="📝", layout="centered")

st.title("📝 AI Chat Summarizer")
st.write("Paste any text, article, or chat transcript and get a concise summary!")

# Input text area
text_input = st.text_area("Enter your text here:", height=250)

# Summary length sliders
min_len = st.slider("Minimum Summary Length", 20, 200, 50)
max_len = st.slider("Maximum Summary Length", 50, 500, 150)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(text_input, max_length=max_len, min_length=min_len, do_sample=False)
            st.subheader("📌 Summary:")
            st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
