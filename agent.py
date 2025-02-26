import requests
import streamlit as st

# ✅ Hugging Face API Key
huggingface_api_key = st.secrets["HUGGINGFACE_API_KEY"]

# ✅ Use Hugging Face API instead of running locally
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
headers = {"Authorization": f"Bearer {huggingface_api_key}"}

def ask_agent(query: str):
    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload)

    # ✅ Handle API errors
    if response.status_code != 200:
        return f"❌ Error: {response.status_code} - {response.json()}"

    try:
        return response.json()[0]["generated_text"]
    except (KeyError, IndexError, TypeError) as e:
        return f"❌ API Response Error: {e}\nFull response: {response.json()}"
