import streamlit as st
import pandas as pd
import time
from agent import ask_agent  # ✅ Uses Mistral 7B from Hugging Face

st.set_page_config(page_title="Titanic Chatbot", page_icon="🚢", layout="wide")

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

st.title("🛳️ Titanic Dataset Chatbot")
st.markdown("### 🤖 Ask me anything about the Titanic dataset!")

with st.expander("🔍 View Titanic Dataset (Top 5 Rows)"):
    st.dataframe(df.head())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, text in st.session_state.chat_history:
    st.chat_message(role).markdown(text)

user_input = st.text_input("Type your question here...")

if st.button("Ask 🚀") and user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    with st.spinner("Thinking... 🤔"):
        time.sleep(1)
        response = ask_agent(user_input)  # ✅ Now using Mistral 7B

    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append(("assistant", response))

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
