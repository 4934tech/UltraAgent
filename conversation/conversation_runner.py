import json
from api.govee_client import govee_list_devices, govee_turn_light
from utils.messages import system_message, developer_message  # Import the messages
from functions.gpt_functions import functions  # Import the GPT-4 function schemas

def run_conversation(user_message, openai_client, govee_api_key):
    messages = [
        system_message,
        developer_message,
        {"role": "user", "content": user_message}
    ]

    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        function_call="auto"
    )

    current_message = response.choices[0].message

    while current_message.function_call:
        function_name = current_message.function_call.name
        arguments = json.loads(current_message.function_call.arguments)

        if function_name == "govee_list_devices":
            result = govee_list_devices(govee_api_key)
        elif function_name == "govee_turn_light":
            result = govee_turn_light(
                arguments["device_id"],
                arguments["device_model"],
                arguments["action"],
                govee_api_key
            )
        else:
            result = {"status": "error", "message": "Unknown function"}

        messages.append({"role": "assistant", "name": function_name, "content": str(result)})
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            functions=functions,
            function_call="auto"
        )
        current_message = response.choices[0].message

    return current_message.content
