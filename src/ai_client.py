import streamlit as st
from google import genai

# Pull key from Streamlit Secrets
api_key = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

def generate_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=prompt
    )
    return response.text
