import json
import os

def get_config(name=None):
    """
    Get configuration settings from JSON files in the same directory as this script.

    Args:
        name (str, optional): The name of a specific configuration file to retrieve. Defaults to None.

    Returns:
        dict: A dictionary containing configuration settings loaded from JSON files.
    """

    config = {}
    filepath = os.path.dirname(__file__)
    
    config_files = [filename for filename in os.listdir(filepath) if filename.endswith(".json")]
    
    if name:
        
        if name.endswith(".json"):
            with open(name, "r") as f:
                config = json.load(f)
        elif name in config_files:
            with open(os.path.join(filepath, f"{name}.json"), "r") as f:
                config = json.load(f)
        else:
            raise FileNotFoundError(f"Configuration file '{name}' not found.")
            
    for filename in config_files:
        with open(os.path.join(filepath, filename), "r") as f:
            filename = os.path.splitext(filename)[0]
            config[filename] = json.load(f)
    return config