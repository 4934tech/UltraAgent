"""Utility to validate .env file format"""

import os
from pathlib import Path

def validate_env_file(env_path: Path) -> bool:
    """Validate the format of a .env file"""
    if not env_path.exists():
        print(f"Error: {env_path} does not exist")
        return False
    
    print(f"\nValidating {env_path}:")
    valid = True
    with open(env_path, 'r') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if '=' not in line:
                print(f"Line {i}: Missing '=' character: {line}")
                valid = False
                continue
                
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            if not key:
                print(f"Line {i}: Empty key: {line}")
                valid = False
            
            if not value:
                print(f"Line {i}: Empty value: {line}")
                valid = False
            
            # Check for common formatting issues
            if value.startswith("'") != value.endswith("'") or \
               value.startswith('"') != value.endswith('"'):
                print(f"Line {i}: Mismatched quotes: {line}")
                valid = False
            
            if ' ' in key:
                print(f"Line {i}: Key contains spaces: {line}")
                valid = False
    
    if valid:
        print("✓ .env file format is valid")
    return valid

if __name__ == '__main__':
    config_dir = Path(__file__).parent
    env_path = config_dir / '.env'
    validate_env_file(env_path) 