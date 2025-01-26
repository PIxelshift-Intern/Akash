from typing import Optional, List, Any, Dict
import json
import os
from datetime import datetime

# Helper function to read existing database
def read_database() -> list:
    try:
        with open("./db/database.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Helper function to write to database
def write_database(data: List[Any], filepath: str = "./db/database.json"):
    """
    Write data to a JSON database, creating directories and file if needed
    
    Args:
        data (List[Any]): Data to write to database
        filepath (str, optional): Path to the database file
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4, default=str)
    except Exception as e:
        print(f"Error writing to database: {e}")
        raise

def log(message: str, data: Any = None, filepath: str = "./logs/app.log"):
    """
    Log messages with optional data to a specified log file
    
    Args:
        message (str): Log message
        data (Any, optional): Additional data to log
        filepath (str, optional): Path to log file
    """
    # Ensure directory exists
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Convert data to string if not None
    log_data = json.dumps(data, default=str) if data is not None else ""
    
    # Write log entry
    with open(filepath, "a") as log_file:
        timestamp = datetime.now().isoformat()
        log_entry = f"{timestamp} - {message}: {log_data}\n"
        log_file.write(log_entry)