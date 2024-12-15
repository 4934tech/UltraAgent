"""
    UltraAgent is an AI agent with real-world powers to control many applications.
    Copyright (C) 2024  Olav Sharma - 4934.tech

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

def example_function(param1, param2):
    return {"status": "success", "param1": param1, "param2": param2}

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

example_function_mappings = {
    "example_function": example_function
}
