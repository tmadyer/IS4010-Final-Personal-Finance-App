import json
import os

def load_data(file_path):
    """
    Loads transaction data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of transactions. Returns an empty list if the file doesn't exist.
    
    Raises:
        ValueError: If the file is corrupted and cannot be decoded.
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("The data file is corrupted and cannot be read.")

def save_data(file_path, data):
    """
    Saves transaction data to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (list): The list of transactions to save.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
