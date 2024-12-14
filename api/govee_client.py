import requests

# Base URL for Govee API
BASE_URL = "https://developer-api.govee.com/v1"

def govee_list_devices(api_key):
    """List all devices connected to the user's Govee account."""
    url = f"{BASE_URL}/devices"
    headers = {"Govee-API-Key": api_key}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}

def govee_turn_light(device_id, device_model, action, api_key):
    """Turn a Govee light on or off."""
    url = f"{BASE_URL}/devices/control"
    headers = {
        "Govee-API-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "device": device_id,
        "model": device_model,
        "cmd": {"name": "turn", "value": action}
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}

def govee_set_brightness(device_id, device_model, brightness, api_key):
    """Set the brightness of a Govee light."""
    url = f"{BASE_URL}/devices/control"
    headers = {
        "Govee-API-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "device": device_id,
        "model": device_model,
        "cmd": {"name": "brightness", "value": brightness}
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}

def govee_set_color(device_id, device_model, color, api_key):
    """Set the color of a Govee light (RGB values)."""
    url = f"{BASE_URL}/devices/control"
    headers = {
        "Govee-API-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "device": device_id,
        "model": device_model,
        "cmd": {"name": "color", "value": color}
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}

def govee_set_color_temperature(device_id, device_model, temperature, api_key):
    """Set the color temperature of a Govee light."""
    url = f"{BASE_URL}/devices/control"
    headers = {
        "Govee-API-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "device": device_id,
        "model": device_model,
        "cmd": {"name": "colorTem", "value": temperature}
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}

def govee_get_device_state(device_id, device_model, api_key):
    """Retrieve the current state of a specific Govee device."""
    url = f"{BASE_URL}/devices/state"
    headers = {
        "Govee-API-Key": api_key,
        "Content-Type": "application/json"
    }
    params = {
        "device": device_id,
        "model": device_model
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}
