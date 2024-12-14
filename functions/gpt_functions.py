functions = [
    {
        "name": "govee_list_devices",
        "description": "List all Govee devices connected to the account",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "govee_turn_light",
        "description": "Control a Govee light",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The Govee device ID"},
                "device_model": {"type": "string", "description": "The Govee device model"},
                "action": {"type": "string", "description": "Action: 'on' or 'off'"}
            },
            "required": ["device_id", "device_model", "action"]
        }
    }
]