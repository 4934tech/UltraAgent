functions = [
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
        "description": "Set the color of a Govee light using RGB values",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"},
                "color": {
                    "type": "object",
                    "properties": {
                        "r": {"type": "integer", "description": "Red value (0-255)"},
                        "g": {"type": "integer", "description": "Green value (0-255)"},
                        "b": {"type": "integer", "description": "Blue value (0-255)"}
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
                "temperature": {"type": "integer", "description": "Color temperature (2000-9000K)"}
            },
            "required": ["device_id", "device_model", "temperature"]
        }
    },
    {
        "name": "govee_get_device_state",
        "description": "Retrieve the current state of a Govee device",
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
