import json

def create_prompt(code, option, target_language, error=None):
    instructions = get_instructions(option, target_language, error)
    
    return f"""
    Act as an expert programmer. Follow the instructions below to generate a solution.

    **Instruction**: {instructions}

    **Code**:
    ```{code}```

    If the above is not actual code, return: 
    'This tool is only for Pair Programming. Please paste only code.'

    **Output Format**:
    ```json
    {{
        "code": "(your code)",
        "explanation": "(your explanation in markdown)"
    }}
    ```
    """

def get_instructions(option, target_language=None, error=None):
    instructions = {
        "Code Translation": f"Translate the given code to {target_language} while keeping the structure intact.",
        "Debug Your Code": f"Debug the given code. Error provided: {error}",
        "Code Improvements": "Improve the given code for better readability and efficiency.",
        "Simplify Code": "Simplify the given code without changing its functionality.",
        "Write Test Cases": "Generate unit test cases for the given code.",
        "Improve Efficiency": "Optimize the given code for better performance.",
    }
    return instructions.get(option, "Invalid Option")

def extract_code_and_explanation(response_text):
    try:
        json_data = response_text[response_text.find('{'):response_text.rfind('}')+1]
        parsed = json.loads(json_data)
        return parsed["code"], parsed["explanation"]
    except Exception as e:
        raise Exception("Failed to parse AI response. Try again.")
