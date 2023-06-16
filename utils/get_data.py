import json

OPERATION_KEYS = ['id', 'date', 'state', 'operationAmount', 'description', 'from', 'to']


def read_json(file_path):
    """
    Reads data from a json file and returns a list
    :param file_path: path to the json file
    :return: list of data
    """
    with open(file=file_path, mode='r', encoding='utf-8') as json_file:
        list_of_data = json.load(json_file)
    return list_of_data


def clear_operations(operations):
    """
    Removes broken operations
    :param operations: list of operations
    :return: cleared list of operations
    """
    cleared_operations = []
    for operation in operations:
        try:
            for key in OPERATION_KEYS:
                operation[f'{key}']
        except KeyError:
            continue
        cleared_operations.append(operation)

    return cleared_operations


def sort_operations_by_time(operations):
    """
    Sorts operations by time
    :param operations: list of operations
    :return: list of sorted operations
    """
    sorted_operations = sorted(operations, key=lambda k: k['date'])
    return sorted_operations


def get_operations(file_path):
    """
    Gets operations from json, clears them from broken ones and returns a list of operations sorted by time
    :param file_path: path to json file with  operations
    :return: list of operations sorted by time
    """
    operations = read_json(file_path)
    cleared_operations = clear_operations(operations)
    sorted_operations = sort_operations_by_time(cleared_operations)

    return sorted_operations
