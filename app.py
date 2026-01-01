import streamlit as st
from src.resources import RESOURCES
from src.ai_client import generate_ai_response

st.set_page_config(page_title="Women's Care Package Vault", layout="centered")
st.title("Women's Care Package Vault")

# Track which step user is on
if "step" not in st.session_state:
    st.session_state.step = 1

step = st.session_state.step
resources = RESOURCES.get(step, [])

st.subheader(f"Step {step}")
for r in resources:
    st.markdown(f"- **{r['name']}**: [Link]({r['link']})")

# Generate AI guidance for current step
prompt = f"Explain simply why these resources are helpful: {', '.join([r['name'] for r in resources])}"
ai_text = generate_ai_response(prompt)
st.markdown(f"**AI Guidance:** {ai_text}")

# Button to go to the next step
if st.button("Next Step"):
    st.session_state.step += 1
    st.experimental_rerun()

