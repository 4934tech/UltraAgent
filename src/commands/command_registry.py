"""
    Command registry system for UltraAgent.
    Handles registration and management of command modules.
"""

import importlib
import os
from typing import Dict, Type, List
from src.commands.base_command import BaseCommand

class CommandRegistry:
    def __init__(self):
        self._commands: Dict[str, BaseCommand] = {}
        self._api_keys: Dict[str, str] = {}

    def register_command(self, command_instance: BaseCommand) -> None:
        """Register a command module"""
        if not isinstance(command_instance, BaseCommand):
            raise ValueError(f"Command must inherit from BaseCommand: {command_instance}")
        
        # Register command regardless of API key status
        self._commands[command_instance.name] = command_instance

    def register_api_key(self, key_name: str, key_value: str) -> None:
        """Register an API key"""
        if key_value:  # Only register non-None API keys
            self._api_keys[key_name] = key_value

    def get_command(self, name: str) -> BaseCommand:
        """Get a command by name"""
        return self._commands.get(name)

    def get_all_commands(self) -> Dict[str, BaseCommand]:
        """Get all registered commands"""
        return self._commands.copy()

    def get_command_schemas(self) -> List[Dict]:
        """Get OpenAI function schemas for all commands"""
        return [cmd.schema for cmd in self._commands.values()]

    def validate_command_api_keys(self, command: BaseCommand) -> bool:
        """Validate that a command has all required API keys"""
        return command.validate_api_keys(self._api_keys)

    @classmethod
    def load_commands_from_directory(cls, directory: str) -> 'CommandRegistry':
        """
        Load all command modules from a directory.
        Each module should have a register_commands() function that returns a list of command instances.
        """
        registry = cls()
        
        # Get all Python files in the directory
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    try:
                        # Convert file path to module path
                        module_path = os.path.relpath(root, os.path.dirname(os.path.dirname(directory)))
                        module_path = os.path.join(module_path, file[:-3]).replace(os.path.sep, '.')
                        
                        # Import the module
                        module = importlib.import_module(module_path)
                        
                        # If module has register_commands, call it
                        if hasattr(module, 'register_commands'):
                            commands = module.register_commands()
                            for command in commands:
                                registry.register_command(command)
                    except Exception as e:
                        print(f"Warning: Could not load commands from {module_path}: {e}")
        
        return registry 