import os
import json
import streamlit as st
from google.cloud import storage  # Example Cloud API

# Load Service Account JSON from Streamlit Secrets
service_info = json.loads(st.secrets["GCP_SERVICE_ACCOUNT_JSON"])
with open("service_account.json", "w") as f:
    json.dump(service_info, f)

# Tell Python where to find it
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

# Example: Cloud Storage client
storage_client = storage.Client()

def list_buckets():
    return [bucket.name for bucket in storage_client.list_buckets()]
