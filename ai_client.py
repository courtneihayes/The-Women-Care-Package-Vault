import os
from google.cloud import aiplatform

def generate_ai_response(prompt: str):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    client = aiplatform.gapic.PredictionServiceClient()
    
    project = "womens-care-ai-sa"  # replace with your GCP Project ID
    location = "us-central1"
    model = "text-bison-001"

    endpoint = client.endpoint_path(project=project, location=location, endpoint=model)

    response = client.predict(
        endpoint=endpoint,
        instances=[{"content": prompt}],
        parameters={}
    )
    return response.predictions[0]["content"]
