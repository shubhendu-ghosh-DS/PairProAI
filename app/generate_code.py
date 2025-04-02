import google.generativeai as genai
import json
from app.config import Config
from app.utils import create_prompt, extract_code_and_explanation

genai.configure(api_key=Config.API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_code(code, option, target_language=None, error=None):
    try:
        prompt = create_prompt(code, option, target_language, error)
        response = model.generate_content(prompt)
        return extract_code_and_explanation(response.text)
    except Exception as e:
        raise Exception(f"AI Processing Failed: {e}")
