import requests
import os

# unitary/toxic-bert is a multi-label classifier with 6 categories
API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
HF_TOKEN = os.getenv("HF_API_KEY", "")

# The model returns scores in this order for each label
LABEL_ORDER = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

def predict_toxicity(text):
    if not HF_TOKEN:
        print("Warning: HF_API_KEY not found. API calls may be limited.")
    
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": text, "options": {"wait_for_model": True}}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()
        
        # Log the raw response so we can debug in Docker/Render logs
        print(f"HF API Raw Response: {data}")

        result = {}

        # unitary/toxic-bert returns a list of lists:
        # [[{label: 'toxic', score: X}, {label: 'non-toxic', score: Y}],
        #  [{label: 'obscene', score: X}, {label: 'non-toxic', score: Y}], ...]
        # Each inner list corresponds to one toxicity category in LABEL_ORDER order.
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
            for i, category_scores in enumerate(data):
                if i >= len(LABEL_ORDER):
                    break
                label_name = LABEL_ORDER[i]
                # Find the 'toxic' score (not 'non-toxic') for this category
                toxic_score = next(
                    (item['score'] for item in category_scores 
                     if item['label'].lower() not in ['non-toxic', 'non_toxic', 'label_0']),
                    0.0
                )
                result[label_name] = toxic_score
            return result

        # Flat list format: [{'label': 'toxic', 'score': 0.9}, ...]
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            return {item['label']: item['score'] for item in data}

        # Error from HF
        if isinstance(data, dict) and "error" in data:
            print(f"HF API Error: {data['error']}")

        raise Exception(f"Unexpected API response structure: {data}")

    except Exception as e:
        print(f"Exception during API call: {e}")
        return {label: 0.0 for label in LABEL_ORDER}
