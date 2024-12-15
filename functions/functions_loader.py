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

from functions.govee_functions import govee_function_schemas, govee_function_mappings
from functions.example_functions import example_function_schemas, example_function_mappings

def load_functions():
    schemas = govee_function_schemas + example_function_schemas
    mappings = {**govee_function_mappings, **example_function_mappings}
    return {"schemas": schemas, "mappings": mappings}
