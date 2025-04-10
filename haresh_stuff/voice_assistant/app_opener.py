import json
import subprocess
import os

# Load the systems.json file
SYSTEMS_FILE = "d:\\coding\\Python\\voice_assistant\\systems.json"

def load_systems():
    """Load the systems.json file and return the data."""
    try:
        with open(SYSTEMS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {SYSTEMS_FILE} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {SYSTEMS_FILE}.")
        return {}

def open_app(app_name):
    """Open an application by its name."""
    systems = load_systems()
    app_name = app_name.upper()  # Convert input to uppercase for matching
    if app_name in systems:
        app_path = systems[app_name]
        try:
            subprocess.Popen(app_path, shell=True)  # Open the application
            return f"Opening {app_name}..."
        except Exception as e:
            return f"Failed to open {app_name}: {e}"
    else:
        return f"{app_name} not found in the system list."
