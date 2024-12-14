from functions.govee_functions import govee_function_schemas, govee_function_mappings
from functions.example_functions import example_function_schemas, example_function_mappings

def load_functions():
    """Load all schemas and mappings from multiple function files."""
    schemas = govee_function_schemas + example_function_schemas
    mappings = {**govee_function_mappings, **example_function_mappings}
    return {"schemas": schemas, "mappings": mappings}
