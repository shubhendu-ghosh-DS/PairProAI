import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from app.utils import create_prompt, separate_code_and_explanation

# Load API Key
load_dotenv()
#genai.configure(api_key=os.getenv("API_KEY"))
genai.configure(api_key="AIzaSyDu0ijBcvRVGfRrw5MzXUDVJjNoi231ZUc")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_code(code, option, target_language=None, error=None):
    try:
        prompt = create_prompt(code, option, target_language, error)
        response = model.generate_content(prompt)
        return separate_code_and_explanation(response.text)
    except Exception:
        raise Exception("Failed to generate response. Please try again later.")
