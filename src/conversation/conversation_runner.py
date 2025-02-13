"""
    UltraAgent is an AI agent with real-world powers to control many applications.
    Copyright (C) 2024  Olav "Olavorw" Sharma - 4934 Tech

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import os
from src.commands.command_registry import CommandRegistry
from src.utils.messages import get_system_message, get_developer_message

def initialize_command_registry(api_keys: dict) -> CommandRegistry:
    """Initialize the command registry with all available commands"""
    # Create registry and load commands first
    commands_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "commands")
    registry = CommandRegistry.load_commands_from_directory(commands_dir)
    
    # Then register API keys
    for key_name, key_value in api_keys.items():
        if key_value:  # Only register non-None API keys
            registry.register_api_key(key_name, key_value)
    
    return registry

def run_interactive_conversation(openai_client, api_keys: dict):
    registry = initialize_command_registry(api_keys)
    messages = [
        get_system_message(),
        get_developer_message()
    ]
    print("Welcome to UltraAgent! Type your commands below.")
    print("Type 'exit' to end the session.\n")

    while True:
        user_message = input("You: ").strip()
        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_message})
        
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            functions=registry.get_command_schemas(),
            function_call="auto"
        )
        current_message = response.choices[0].message
        messages.append(current_message)
        
        while current_message.function_call:
            function_name = current_message.function_call.name
            arguments = json.loads(current_message.function_call.arguments)
            
            command = registry.get_command(function_name)
            if command:
                try:
                    # Validate API keys before execution
                    if not registry.validate_command_api_keys(command):
                        missing_keys = [key for key in command.required_api_keys if key not in api_keys or not api_keys[key]]
                        result = {"status": "error", "message": f"Missing required API keys: {missing_keys}"}
                    else:
                        result = command.execute(**arguments, api_key=api_keys.get(command.required_api_keys[0]))
                except Exception as e:
                    result = {"status": "error", "message": str(e)}
            else:
                result = {"status": "error", "message": f"Unknown command: {function_name}"}

            messages.append({"role": "assistant", "name": function_name, "content": str(result)})
            follow_up_response = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                functions=registry.get_command_schemas(),
                function_call="auto"
            )
            current_message = follow_up_response.choices[0].message
            messages.append(current_message)

        print(f"Assistant: {current_message.content}")

def execute_command(command, arguments, api_keys):
    """Execute a command with proper API key handling"""
    try:
        # Get all required API keys for the command
        command_api_keys = {key: api_keys.get(key) for key in command.required_api_keys}
        if not all(command_api_keys.values()):
            missing_keys = [key for key in command.required_api_keys if not api_keys.get(key)]
            return {"status": "error", "message": f"Missing required API keys: {missing_keys}"}
            
        # Execute command with all required API keys
        return command.execute(**arguments, **command_api_keys)
    except Exception as e:
        return {"status": "error", "message": str(e)}

def run_conversation(user_message, openai_client, api_keys: dict, messages):
    registry = initialize_command_registry(api_keys)
    
    if not messages:
        messages.extend([get_system_message(), get_developer_message()])
    messages.append({"role": "user", "content": user_message})
    
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        functions=registry.get_command_schemas(),
        function_call="auto"
    )
    current_message = response.choices[0].message
    messages.append(current_message)

    while current_message.function_call:
        function_name = current_message.function_call.name
        arguments = json.loads(current_message.function_call.arguments)
        
        command = registry.get_command(function_name)
        if command:
            result = execute_command(command, arguments, api_keys)
        else:
            result = {"status": "error", "message": f"Unknown command: {function_name}"}

        messages.append({"role": "assistant", "name": function_name, "content": str(result)})
        follow_up_response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            functions=registry.get_command_schemas(),
            function_call="auto"
        )
        current_message = follow_up_response.choices[0].message
        messages.append(current_message)

    return current_message.content
