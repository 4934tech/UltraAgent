from api.govee_client import (
    govee_list_devices,
    govee_turn_light,
    govee_set_brightness,
    govee_set_color,
    govee_set_color_temperature,
    govee_get_device_state
)

govee_function_schemas = [
    {
        "name": "govee_list_devices",
        "description": "List all Govee devices connected to the account",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "govee_turn_light",
        "description": "Turn a Govee light on or off",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"},
                "action": {"type": "string", "description": "'on' or 'off'"}
            },
            "required": ["device_id", "device_model", "action"]
        }
    },
    {
        "name": "govee_set_brightness",
        "description": "Set the brightness of a Govee light",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"},
                "brightness": {"type": "integer", "description": "Brightness level (0-100)"}
            },
            "required": ["device_id", "device_model", "brightness"]
        }
    },
    {
        "name": "govee_set_color",
        "description": "Set the color of a Govee light (RGB values)",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"},
                "color": {
                    "type": "object",
                    "description": "RGB values (e.g., {'r': 255, 'g': 255, 'b': 255})",
                    "properties": {
                        "r": {"type": "integer", "minimum": 0, "maximum": 255},
                        "g": {"type": "integer", "minimum": 0, "maximum": 255},
                        "b": {"type": "integer", "minimum": 0, "maximum": 255}
                    },
                    "required": ["r", "g", "b"]
                }
            },
            "required": ["device_id", "device_model", "color"]
        }
    },
    {
        "name": "govee_set_color_temperature",
        "description": "Set the color temperature of a Govee light",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"},
                "temperature": {"type": "integer", "description": "Color temperature in Kelvin"}
            },
            "required": ["device_id", "device_model", "temperature"]
        }
    },
    {
        "name": "govee_get_device_state",
        "description": "Retrieve the current state of a specific Govee device",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"}
            },
            "required": ["device_id", "device_model"]
        }
    }
]

govee_function_mappings = {
    "govee_list_devices": govee_list_devices,
    "govee_turn_light": govee_turn_light,
    "govee_set_brightness": govee_set_brightness,
    "govee_set_color": govee_set_color,
    "govee_set_color_temperature": govee_set_color_temperature,
    "govee_get_device_state": govee_get_device_state,
}
