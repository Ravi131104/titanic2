import requests
import streamlit as st

# ✅ Load Hugging Face API Key
huggingface_api_key = st.secrets["HUGGINGFACE_API_KEY"]

# ✅ Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
headers = {"Authorization": f"Bearer {huggingface_api_key}"}

def ask_agent(query: str):
    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload)

    # ✅ Handle empty response
    if not response.text.strip():  # Checks if response is completely empty
        return "❌ API returned an empty response. Model may still be loading."

    # ✅ Print response for debugging
    print("Response Status:", response.status_code)
    print("Raw Response Content:", response.text)

    # ✅ Handle non-JSON responses
    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError:
        return f"❌ API returned invalid JSON: {response.text}"

    # ✅ Handle API errors
    if response.status_code != 200:
        return f"❌ API Error {response.status_code}: {response_json}"

    # ✅ Return model-generated text
    try:
        return response_json[0]["generated_text"]
    except (KeyError, IndexError, TypeError) as e:
        return f"❌ API Response Error: {e}\nFull response: {response_json}"
