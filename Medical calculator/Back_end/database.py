import json
import os
from pathlib import Path

# This ensures accounts.json is always inside the Back_end folder
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "accounts.json"
HISTORY_FILE = BASE_DIR / "history.json"

def save_account(username, password):
    data = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError: # Handles empty file error
                data = {}
    
    if username in data:
        return False, "Username already exists!"
    
    data[username] = password
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4) # indent=4 makes it pretty and easy to read
    return True, "Account created successfully!"

def check_login(username, password):
    if not os.path.exists(DB_FILE):
        return False
    
    with open(DB_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return False
    
    return data.get(username) == password

def save_to_history(username, calculation_type, inputs, result):
    history_data = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history_data = json.load(f)
            except json.JSONDecodeError:
                history_data = []

    new_entry = {
        "username": username,
        "type": calculation_type,
        "inputs": inputs,
        "result": result
    }

    history_data.insert(0, new_entry) 
    history_data = history_data[:20]

    with open(HISTORY_FILE, "w") as f:
        json.dump(history_data, f, indent=4)

def get_history(username):
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            data = json.load(f)
            return [entry for entry in data if entry["username"] == username]
        except:
            return []