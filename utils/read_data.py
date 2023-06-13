import json


def read_json(file_path):
    with open(file=file_path, mode='r', encoding='utf-8') as json_file:
        operations = json.load(json_file)
    return operations
