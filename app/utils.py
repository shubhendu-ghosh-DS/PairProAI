import json

def create_prompt(code, option, target_language, error=None):
    instruction = get_instructions(option, target_language, error)
    
    prompt_template = f"""
    Act as an expert programmer. Your task is to generate a solution based on the instructions.

    Instruction: {instruction}

    Code:
    {code}

    **Important:** If the above text in 'Code:' is not actual code, return:
    'This tool is only for Pair Programming. Paste only code in the code box.'

    Please explain changes in JSON format:
    ```{{
        "code": "(your generated code)",
        "explanation": "(your explanation in markdown format. return with proper heeading, subheading and bulllet point)"
    }}```
    """

    return prompt_template

def get_instructions(option, target_language=None, error=None):
    options_map = {
        "Code Translation": f"Translate the given code to {target_language}.",
        "Debug Your Code": f"Debug the given code. Error: {error}" if error else "Error message required.",
        "Code Improvements": "Improve the given code.",
        "Simplify Code": "Simplify the given code.",
        "Write Test Cases": "Generate test cases for the given code.",
        "Improve Efficiency": "Optimize the given code for efficiency."
    }
    return options_map.get(option, "Invalid option selected.")

def separate_code_and_explanation(json_text):
    try:
        json_data = json_text[json_text.find("{"): json_text.rfind("}") + 1]
        data = json.loads(json_data)
        return data["code"], data["explanation"]
    except json.JSONDecodeError:
        raise Exception("Invalid response format.")
