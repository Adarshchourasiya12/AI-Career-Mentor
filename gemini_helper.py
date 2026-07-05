import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(text):

    prompt = f"""
    Analyze this resume.

    Give:

    1. Strengths
    2. Weaknesses
    3. Missing Skills
    4. Career Suggestions

    Resume:

    {text}
    """

    response = model.generate_content(prompt)

    return response.text