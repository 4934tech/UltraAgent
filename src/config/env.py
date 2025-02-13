"""
    UltraAgent is an AI agent with real-world powers to control many applications.
    Copyright (C) 2024  Olav "Olavorw" Sharma - 4934 Tech

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

import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

def find_project_root() -> Path:
    """Find the project root directory"""
    current_dir = Path(__file__).resolve().parent
    while current_dir.name != "UltraAgent" and current_dir.parent != current_dir:
        current_dir = current_dir.parent
    return current_dir

def load_environment():
    """Load environment variables from .env file"""
    # Try multiple possible locations for .env
    project_root = find_project_root()
    possible_env_paths = [
        Path(__file__).parent / '.env',  # src/config/.env
        project_root / '.env',           # /UltraAgent/.env
        project_root / 'src/config/.env' # /UltraAgent/src/config/.env
    ]

    # Print debug information
    print("Looking for .env file in:", file=sys.stderr)
    for path in possible_env_paths:
        print(f"  - {path} {'(exists)' if path.exists() else '(not found)'}", file=sys.stderr)

    # First try find_dotenv() which searches parent directories
    env_path = find_dotenv()
    if not env_path:
        # If find_dotenv() fails, try our explicit paths
        for path in possible_env_paths:
            if path.exists():
                env_path = str(path)
                break

    if not env_path:
        print("Warning: No .env file found!", file=sys.stderr)
        return False

    print(f"Loading .env from: {env_path}", file=sys.stderr)
    return load_dotenv(dotenv_path=env_path, override=True)

# Load environment variables
load_environment()

def get_env_var(var_name: str) -> str:
    """Get an environment variable or raise an error if it's not set"""
    value = os.getenv(var_name)
    if value is None:
        print(f"Error: Environment variable {var_name} is not set!", file=sys.stderr)
        print("Available environment variables:", file=sys.stderr)
        for key, value in os.environ.items():
            if any(secret in key.lower() for secret in ['key', 'secret', 'token', 'password']):
                print(f"  - {key}: {'*' * 8}", file=sys.stderr)
            else:
                print(f"  - {key}: {value}", file=sys.stderr)
        raise ValueError(f"Environment variable {var_name} is not set")
    return value

# API Keys
OPENAI_API_KEY = get_env_var("OPENAI_API_KEY")
GOVEE_API_KEY = get_env_var("GOVEE_API_KEY")
ELEVENLABS_API_KEY = get_env_var("ELEVENLABS_API_KEY")

# Spotify Configuration
SPOTIFY_CLIENT_ID = get_env_var("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = get_env_var("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = get_env_var("SPOTIFY_REDIRECT_URI")

