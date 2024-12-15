import json
from functions.functions_loader import load_functions
from utils.messages import get_system_message, get_developer_message

def run_interactive_conversation(openai_client, govee_api_key):
    
    functions_data = load_functions()
    functions = functions_data["schemas"]
    function_mappings = functions_data["mappings"]
    messages = [
        get_system_message(),
        get_developer_message()
    ]
    print("Welcome to the Govee Assistant! Type your commands below.")
    print("Type 'exit' to end the session.\n")

    while True:
        user_message = input("You: ").strip()
        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_message})
        
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            functions=functions,
            function_call="auto"
        )
        current_message = response.choices[0].message
        messages.append(current_message)
        
        while current_message.function_call:
            function_name = current_message.function_call.name
            arguments = json.loads(current_message.function_call.arguments)
            if function_name in function_mappings:
                function_to_call = function_mappings[function_name]
                try:
                    result = function_to_call(**arguments, api_key=govee_api_key)
                except Exception as e:
                    result = {"status": "error", "message": str(e)}
            else:
                result = {"status": "error", "message": f"Unknown function: {function_name}"}

            messages.append({"role": "assistant", "name": function_name, "content": str(result)})
            follow_up_response = openai_client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                functions=functions,
                function_call="auto"
            )
            current_message = follow_up_response.choices[0].message
            messages.append(current_message)

        print(f"Assistant: {current_message.content}")

def run_conversation(user_message, openai_client, govee_api_key, messages):
    functions_data = load_functions()
    functions = functions_data["schemas"]
    function_mappings = functions_data["mappings"]

    
    if not messages:
        messages.extend([get_system_message(), get_developer_message()])
    messages.append({"role": "user", "content": user_message})
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        function_call="auto"
    )
    current_message = response.choices[0].message
    messages.append(current_message)

    while current_message.function_call:
        function_name = current_message.function_call.name
        arguments = json.loads(current_message.function_call.arguments)
        if function_name in function_mappings:
            function_to_call = function_mappings[function_name]
            result = function_to_call(**arguments, api_key=govee_api_key)
        else:
            result = {"status": "error", "message": f"Unknown function: {function_name}"}

        messages.append({"role": "assistant", "name": function_name, "content": str(result)})
        follow_up_response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            functions=functions,
            function_call="auto"
        )
        current_message = follow_up_response.choices[0].message
        messages.append(current_message)

    return current_message.content
