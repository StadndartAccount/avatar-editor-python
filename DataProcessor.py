import json
import os
from AvatarLayer import Layer
import uuid


def save_object(object):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory_name = 'History'
    history_directory_path = os.path.join(current_directory, directory_name)
    os.makedirs(history_directory_path, exist_ok=True)

    filename = f"{str(uuid.uuid4())}.json"

    file_path = os.path.join(history_directory_path, filename)

    with open(file_path, 'w') as file:
        json.dump(object, file)


def load_object(unique_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    history_directory_path = os.path.join(current_directory, "History")

    filename = f"{unique_id}.json"
    file_path = os.path.join(history_directory_path, filename)
    
    if not os.path.exists(file_path):
        print(f"Файл {filename} не найден.")
        return None
    
    with open(file_path, 'r') as file:
        object_data = json.load(file)
        return object_data


def remove_object(unique_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    history_directory_path = os.path.join(current_directory, "History")

    filename = f"{unique_id}.json"
    file_path = os.path.join(history_directory_path, filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл {filename} успешно удален.")
    else:
        print("Файл не найден.")