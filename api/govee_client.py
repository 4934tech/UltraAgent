import requests

def govee_list_devices(api_key):
    url = "https://developer-api.govee.com/v1/devices"
    headers = {"Govee-API-Key": api_key}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {"status": "error", "error": response.text}

def govee_turn_light(device_id, device_model, action, api_key):
    url = "https://developer-api.govee.com/v1/devices/control"
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