"""
    Govee command implementations for UltraAgent.
"""

from typing import Dict, Any, List
from src.commands.base_command import BaseCommand
from src.api.govee_client import (
    govee_list_devices,
    govee_turn_light,
    govee_set_brightness,
    govee_set_color,
    govee_set_color_temperature,
    govee_get_device_state
)

class GoveeListDevicesCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "govee_list_devices"

    @property
    def description(self) -> str:
        return "List all Govee devices connected to the account"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {"type": "object", "properties": {}}
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["GOVEE_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        api_key = kwargs.get("api_key")
        return govee_list_devices(api_key)

class GoveeTurnLightCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "govee_turn_light"

    @property
    def description(self) -> str:
        return "Turn a Govee light on or off"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {"type": "string", "description": "The Govee device ID"},
                    "device_model": {"type": "string", "description": "The Govee device model"},
                    "action": {"type": "string", "description": "'on' or 'off'"}
                },
                "required": ["device_id", "device_model", "action"]
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["GOVEE_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        api_key = kwargs.pop("api_key")
        return govee_turn_light(**kwargs, api_key=api_key)

class GoveeSetBrightnessCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "govee_set_brightness"

    @property
    def description(self) -> str:
        return "Set the brightness of a Govee light"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {"type": "string", "description": "The Govee device ID"},
                    "device_model": {"type": "string", "description": "The Govee device model"},
                    "brightness": {"type": "integer", "description": "Brightness level (0-100)"}
                },
                "required": ["device_id", "device_model", "brightness"]
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["GOVEE_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        api_key = kwargs.pop("api_key")
        return govee_set_brightness(**kwargs, api_key=api_key)

class GoveeSetColorCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "govee_set_color"

    @property
    def description(self) -> str:
        return "Set the color of a Govee light (RGB values)"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
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
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["GOVEE_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        api_key = kwargs.pop("api_key")
        return govee_set_color(**kwargs, api_key=api_key)

class GoveeSetColorTemperatureCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "govee_set_color_temperature"

    @property
    def description(self) -> str:
        return "Set the color temperature of a Govee light"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {"type": "string", "description": "The Govee device ID"},
                    "device_model": {"type": "string", "description": "The Govee device model"},
                    "temperature": {"type": "integer", "description": "Color temperature in Kelvin"}
                },
                "required": ["device_id", "device_model", "temperature"]
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["GOVEE_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        api_key = kwargs.pop("api_key")
        return govee_set_color_temperature(**kwargs, api_key=api_key)

class GoveeGetDeviceStateCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "govee_get_device_state"

    @property
    def description(self) -> str:
        return "Retrieve the current state of a specific Govee device"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "device_id": {"type": "string", "description": "The Govee device ID"},
                    "device_model": {"type": "string", "description": "The Govee device model"}
                },
                "required": ["device_id", "device_model"]
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["GOVEE_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        api_key = kwargs.pop("api_key")
        return govee_get_device_state(**kwargs, api_key=api_key)

def register_commands():
    """Register all Govee commands"""
    return [
        GoveeListDevicesCommand(),
        GoveeTurnLightCommand(),
        GoveeSetBrightnessCommand(),
        GoveeSetColorCommand(),
        GoveeSetColorTemperatureCommand(),
        GoveeGetDeviceStateCommand()
    ] 