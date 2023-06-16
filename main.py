from utils import get_data
from utils import output


if __name__ == "__main__":
    operations = get_data.get_operations("data/operations.json")
    print(operations)
    output.print_operation(operations[8])
