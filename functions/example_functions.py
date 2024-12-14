# example_functions.py

def example_function(param1, param2):
    """Example function for demonstration purposes."""
    return {"status": "success", "param1": param1, "param2": param2}

# Function schemas for Example API
example_function_schemas = [
    {
        "name": "example_function",
        "description": "An example function to demonstrate extensibility",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string", "description": "First parameter"},
                "param2": {"type": "string", "description": "Second parameter"}
            },
            "required": ["param1", "param2"]
        }
    }
]

# Function mappings for Example API
example_function_mappings = {
    "example_function": example_function
}
