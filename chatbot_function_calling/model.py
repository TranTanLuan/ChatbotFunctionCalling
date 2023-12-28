from dotenv import load_dotenv
import os
import openai
import json

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
def get_provided_services():
    print("Function calling is used!")
    provided_services = {
        "provided_topics": ["General cleaning", "Specialized cleaning"],
    }
    return json.dumps(provided_services)
functions = [
    {
        "name": "get_provided_services",
        "description": "Get list of provided service names which you provide",
    }
]
def chat(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": query}],
        functions=functions,
    )
    message = response["choices"][0]["message"]
    return message

def model_pipeline(query: str):
    # query = "What services do you provide?"
    # query = "what is the capital of Viet Nam?"
    message = chat(query)

    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        function_response = get_provided_services()

        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": query},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        output = second_response["choices"][0]["message"]["content"]
    else:
        output = message['content']

    return output
