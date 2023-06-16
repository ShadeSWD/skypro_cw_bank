from utils import get_data
from utils import output


if __name__ == "__main__":
    operations = get_data.get_operations("data/operations.json")
    operations_total = len(operations)
    last_operations = []
    for operation in operations:
        if len(last_operations) >= 5 or len(last_operations) >= operations_total:
            break
        else:
            if operation['state'] == "EXECUTED":
                last_operations.append(operation)

    for operation in last_operations:
        output.print_operation(operation)
