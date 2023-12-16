import json
import re
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
from prompts import assess_research_topic, generate_dystopia

load_dotenv()
client = OpenAI()

GPT_MODEL = "gpt-4-1106-preview"#"gpt-3.5-turbo"#

def extract_json(text):
    print(text)
    try:
        # Find the starting index of JSON structure
        start_index = text.find('{')
        # Find the ending index of JSON structure
        end_index = text.rfind('}') + 1

        # Extract the JSON string
        json_str = text[start_index:end_index]

        # Parse the JSON string into a Python dictionary
        return json.loads(json_str)
    except (ValueError, json.JSONDecodeError) as e:
        # Handle parsing errors (e.g., if the JSON is malformed)
        print("Error parsing JSON:", e)
        return None


def get_json_completion(messages): 
        
        response = client.chat.completions.create(
            model = GPT_MODEL,
            response_format={ "type": "json_object" },
            messages=messages,
            stream=False
        )
        return(response)

def get_completion(messages):
    response = client.chat.completions.create(
        model = GPT_MODEL,
        messages=messages,
        stream=False
    )
    return(response)

def get_email_for_topic(proposal):
        
    messages = [{"role": "system", "content": assess_research_topic},
                {"role": "user", "content": proposal}]
    email_json = get_json_completion(messages)
    print(email_json)
    email_json = email_json.choices[0].message.content
    return(extract_json(email_json))

def get_description(proposal):
    messages = [{"role": "system", "content": generate_dystopia},
        {"role": "user", "content": proposal}]
    print("$$DEBUG$$")
    print(messages)
    if len(proposal)>10:
        description = get_completion(messages)
    return(description.choices[0].message.content)