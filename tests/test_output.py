from utils import output
OPERATION = {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}


def test_separate_account_details():
    assert output.separate_account_details("Счет 64686473678894779589") == ('Счет', '64686473678894779589')


def test_print_operation():
    assert output.print_operation(OPERATION) is None
