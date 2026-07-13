import streamlit as st
from chatbot import ask_chatbot
st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support Chatbot")

st.write("Welcome! Ask me any question.")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    answer = ask_chatbot(question)
    st.write(answer)