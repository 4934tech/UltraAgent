"""
    Base command module interface for UltraAgent.
    All command modules should inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseCommand(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the command module"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what the command module does"""
        pass

    @property
    @abstractmethod
    def schema(self) -> Dict[str, Any]:
        """JSON schema for the command's parameters"""
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute the command with given parameters"""
        pass

    @property
    def required_api_keys(self) -> List[str]:
        """List of required API keys for this command"""
        return []

    def validate_api_keys(self, api_keys: Dict[str, str]) -> bool:
        """Validate that all required API keys are present"""
        return all(key in api_keys for key in self.required_api_keys) 