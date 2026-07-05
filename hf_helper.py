import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

def analyze_resume(text):

    prompt = f"""
    Analyze this resume and provide:

    1. Strengths
    2. Weaknesses
    3. Missing Skills
    4. Career Suggestions

    Resume:
    {text}
    """

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]

    return str(result)