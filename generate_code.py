import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import sys

sys.tracebacklimit = 0

load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel(model_name='gemini-1.5-flash')



def generate_code(code, option, target_language=None, error=None):
    try:
        prompt = create_prompt(code, option, target_language, error)

        response = model.generate_content(prompt)
        code, explaination = seperate_code_and_explaination(response.text)
        return code, explaination
    except Exception as e:
        raise Exception(f"We are Sorry. We failed to solve your problem. Please try again later. Or with a different problem.")
    

def create_prompt(code, option, target_language, error=None):
    prompt_template = """
    Act as an expert programmer. your task is to follow the instruction given below by the user and based on that generate a solution.

    instruction: {instruction}
    
    Below is the code. 
    Code: {code}
    **Important** If the above text in 'Code:' is not an actual piece of code, please do not go further. just return
    'This tool is only for Pair Programming. paste only code in the code box. i can not answer your question. i can only help you writing better code.'

    {suffix}

    """
    instruction = get_instructions(option, target_language, error)
    suffix = """Please explain what you did or changed in detail. put your solution into a json. 
    the json should be in this format so that it can be loaded using json.loads().
    ```{
        "code": "(your code)",
        "explaination": "(your explaination in nice markdown format)"
    }```
    Do not write anything else. just the json in correct format. do not even write json in the response
    """
    prompt = prompt_template.format(instruction=instruction,
                                    code=code,
                                    suffix=suffix)
    
    return prompt


def get_instructions(option, target_language=None, error=None):
    if option == "Code Translation":
        if target_language:
            instruction = f"Please translate the given code to the language {target_language}. keep the structure intact."
        else:
            raise Exception("Please chose your target language.")
    elif option == "Debug Your Code":
        if error:
            instruction = f"Please debug the given code. here is the error {error}"
        else:
            raise Exception("Please paste your exception or error in the box below.")
    elif option == "Code Improvements":
        instruction = f"I don't think this is the right way to write the code. please help me to improve it?"
    elif option == "Simplify Code":
        instruction = f"Can you please help me simplify the code below?"
    elif option == "Write Test Cases":
        instruction = f"Can you please create test cases in code for the code below?"
    elif option == "Improve Efficiency":
        instruction = f"Can you please make this code more efficient?"
    
    return instruction

def seperate_code_and_explaination(json_text):
    try:
        start_idx = json_text.find('{')
        end_idx = json_text.rfind('}') + 1
        json_data = json_text[start_idx:end_idx]
        data = json.loads(json_data)
        code = data['code']
        explaination = data['explaination']
        return code, explaination
    except Exception as e:
        raise Exception(f"Failed to show you the code. We are sorry for this. Please try again later.")