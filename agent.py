from transformers import pipeline
import streamlit as st

# ✅ Load Hugging Face API Key
huggingface_api_key = st.secrets["HUGGINGFACE_API_KEY"]

# ✅ Use a lighter model (Falcon-7B is faster than Mistral)
hf_pipeline = pipeline(
    "text-generation",
    model="tiiuae/falcon-7b-instruct",
    token=huggingface_api_key
)

def ask_agent(query: str):
    try:
        response = hf_pipeline(query, max_length=200, do_sample=True)
        return response[0]["generated_text"]
    except Exception as e:
        return f"❌ Error: {str(e)}"
