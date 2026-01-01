import os
import os
from google import genai

# Tell Python where your credential is (local)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../service_account.json"

# Create the AI client
client = genai.Client()

# Function to call AI
def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=prompt
    )
    return response.text

