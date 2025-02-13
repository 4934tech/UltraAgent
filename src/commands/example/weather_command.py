"""
    Example weather command implementation for UltraAgent.
"""

from typing import Dict, Any, List
from src.commands.base_command import BaseCommand

class GetWeatherCommand(BaseCommand):
    @property
    def name(self) -> str:
        return "get_weather"

    @property
    def description(self) -> str:
        return "Get the current weather for a location"

    @property
    def schema(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The city to get weather for"},
                    "country": {"type": "string", "description": "The country code (e.g., US, UK)"}
                },
                "required": ["city", "country"]
            }
        }

    @property
    def required_api_keys(self) -> List[str]:
        return ["WEATHER_API_KEY"]

    def execute(self, **kwargs) -> Dict[str, Any]:
        # This is just a mock implementation
        # In a real implementation, you would call a weather API
        city = kwargs.get("city")
        country = kwargs.get("country")
        return {
            "status": "success",
            "weather": {
                "location": f"{city}, {country}",
                "temperature": "22°C",
                "condition": "Sunny",
                "humidity": "65%"
            }
        }

def register_commands():
    """Register all example commands"""
    return [GetWeatherCommand()] 