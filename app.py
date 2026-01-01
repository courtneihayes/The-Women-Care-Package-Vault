import streamlit as st
from src.resources import RESOURCES
from src.ai_client import generate_ai_response

# Simple theme
st.set_page_config(page_title="Women's Care Package Vault", layout="centered")
st.title("Women's Care Package Vault")

# Step tracking
if "step" not in st.session_state:
    st.session_state.step = 1

step = st.session_state.step
resources = RESOURCES.get(step, [])

st.subheader(f"Step {step}")
for r in resources:
    st.markdown(f"- **{r['name']}**: [Link]({r['link']})")

# AI guidance
prompt = f"Explain simply why these resources are helpful: {', '.join([r['name'] for r in resources])}"
ai_response = generate_ai_response(prompt)
st.markdown(f"**AI Guidance:** {ai_response}")

# Next step button
if st.button("Next Step"):
    st.session_state.step += 1
    st.experimental_rerun()

