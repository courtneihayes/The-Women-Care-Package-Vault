import os
import json
import streamlit as st

# Read secret JSON
service_info = json.loads(st.secrets["GCP_SERVICE_ACCOUNT_JSON"])

# Write to a local file for Google AI authentication
with open("service_account.json", "w") as f:
    json.dump(service_info, f)

# Tell Python where to find it
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
"

def generate_ai_response(prompt: str):
    setup_google_credentials()
    
    client = aiplatform.gapic.PredictionServiceClient()
    
    project = "womens-care-ai-vault"  # Your Google Cloud Project ID (string)
    location = "us-central1"
    model = "text-bison-001"

    endpoint = client.endpoint_path(project=project, location=location, endpoint=model)
    
    response = client.predict(
        endpoint=endpoint,
        instances=[{"content": prompt}],
        parameters={}
    )
    
    return response.predictions[0]["content"]

