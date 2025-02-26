from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import requests
import streamlit as st

# ✅ Hugging Face API Key
huggingface_api_key = st.secrets["HUGGINGFACE_API_KEY"]

# ✅ Use Hugging Face's hosted API instead of loading Mistral locally
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
headers = {"Authorization": f"Bearer {huggingface_api_key}"}

def ask_agent(query: str):
    payload = {"inputs": query}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]
