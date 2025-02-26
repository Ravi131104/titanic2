from transformers import pipeline
import streamlit as st

# ✅ Load Hugging Face API Key securely
huggingface_api_key = st.secrets["HUGGINGFACE_API_KEY"]

# ✅ Load Mistral 7B Model
hf_pipeline = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-v0.1",  # ✅ Public model
    token=huggingface_api_key
)

# ✅ Function to Query Mistral 7B
def ask_agent(query: str):
    try:
        response = hf_pipeline(query, max_length=200, do_sample=True)
        return response[0]["generated_text"]
    except Exception as e:
        return f"❌ Error: {str(e)}"
