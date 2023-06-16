import datetime


def separate_account_details(acc_det):
    """
    Separates account name from account number
    :param acc_det: string with card name and number
    :return: account_name, account_number
    """
    acc_det_spl = acc_det.split()
    acc_name = ''
    acc_number = ''

    for spl in acc_det_spl:
        if spl.isdigit():
            acc_number = spl
        else:
            acc_name += ' ' + spl

    return acc_name, acc_number


def print_operation(operation):
    """
    Prints one operation in a specific format
    :param operation: operation
    :return: None
    """
    transaction_date = datetime.datetime.fromisoformat(operation['date']).strftime('%d.%m.%Y')
    description = operation['description']
    from_name, from_number = separate_account_details(operation['from'])
    to_name, to_number = separate_account_details(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    print(f'''{transaction_date} {description}
{from_name} {from_number[:4]} {from_number[4:6]} ** ** ** {from_number[-4:]}' -> {to_name} **{to_number[-4:]}
{amount} {currency}
''')
