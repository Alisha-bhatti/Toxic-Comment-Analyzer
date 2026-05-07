import requests
import os
import time

API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
# Fallback to a placeholder if no key is provided, but user should provide one
HF_TOKEN = os.getenv("HF_API_KEY", "")

def predict_toxicity(text):
    if not HF_TOKEN:
        print("Warning: HF_API_KEY not found. API calls may be limited.")
    
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": text, "options": {"wait_for_model": True}}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        # If model is loading, it returns 503. Handled by wait_for_model: True
        data = response.json()
        
        # Hugging Face returns a list of lists of dicts for this model
        # [[{'label': 'toxic', 'score': 0.001}, ...]]
        if isinstance(data, list) and len(data) > 0:
            results = data[0]
            # Convert list of dicts to a single flat dict
            return {item['label']: item['score'] for item in results}
        
        raise Exception(f"Unexpected API response: {data}")

    except Exception as e:
        print(f"API Error: {e}")
        # Return zeros as fallback
        labels = ["toxic","severe_toxic","obscene","threat","insult","identity_hate"]
        return {label: 0.0 for label in labels}
