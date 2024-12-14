import json
from functions.functions_loader import load_functions
from utils.messages import get_system_message, get_developer_message

def run_interactive_conversation(openai_client, govee_api_key):
    # Load schemas and mappings dynamically
    functions_data = load_functions()
    functions = functions_data["schemas"]
    function_mappings = functions_data["mappings"]

    # Initialize message history
    messages = [
        get_system_message(),
        get_developer_message()
    ]

    print("Welcome to the Govee Assistant! Type your commands below.")
    print("Type 'exit' to end the session.\n")

    while True:
        # Get user input
        user_message = input("You: ").strip()
        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        # Add user message to history
        messages.append({"role": "user", "content": user_message})

        # Get GPT-4 response
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            functions=functions,
            function_call="auto"
        )
        current_message = response.choices[0].message
        messages.append(current_message)

        # Process function calls
        while current_message.function_call:
            function_name = current_message.function_call.name
            arguments = json.loads(current_message.function_call.arguments)

            if function_name in function_mappings:
                # Dynamically call the function
                function_to_call = function_mappings[function_name]
                try:
                    result = function_to_call(**arguments, api_key=govee_api_key)
                except Exception as e:
                    result = {"status": "error", "message": str(e)}
            else:
                result = {"status": "error", "message": f"Unknown function: {function_name}"}

            # Add result to messages and get follow-up response
            messages.append({"role": "assistant", "name": function_name, "content": str(result)})
            follow_up_response = openai_client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                functions=functions,
                function_call="auto"
            )
            current_message = follow_up_response.choices[0].message
            messages.append(current_message)

        # Print the assistant's final response
        print(f"Assistant: {current_message.content}")

def run_conversation(user_message, openai_client, govee_api_key, messages):
    """Run a single conversation turn."""
    # Load schemas and mappings dynamically
    functions_data = load_functions()
    functions = functions_data["schemas"]
    function_mappings = functions_data["mappings"]

    # Initialize messages if empty
    if not messages:
        messages.extend([get_system_message(), get_developer_message()])

    # Add user message to history
    messages.append({"role": "user", "content": user_message})

    # Get GPT-4 response
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        function_call="auto"
    )
    current_message = response.choices[0].message
    messages.append(current_message)

    # Process function calls if any
    while current_message.function_call:
        function_name = current_message.function_call.name
        arguments = json.loads(current_message.function_call.arguments)

        if function_name in function_mappings:
            # Dynamically call the function
            function_to_call = function_mappings[function_name]
            result = function_to_call(**arguments, api_key=govee_api_key)
        else:
            result = {"status": "error", "message": f"Unknown function: {function_name}"}

        # Add result and follow-up to messages
        messages.append({"role": "assistant", "name": function_name, "content": str(result)})
        follow_up_response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            functions=functions,
            function_call="auto"
        )
        current_message = follow_up_response.choices[0].message
        messages.append(current_message)

    # Return the assistant's final response content
    return current_message.content
