from src.calculators.calculator_4 import Calculator4
from typing import Dict
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2.6, 3, 2.8]})
    calc = Calculator4()

    response = calc.calculate(mock_request)

    assert response == {'data': {
        'Calculator': 4,
        'value': 2.35
        }
    }


def test_calculate_with_body_error():
    mock_request = MockRequest({"numbers": [1, 'a', 3, 4, 5]})
    calc = Calculator4()
    with raises(Exception) as excinfo:
        calc.calculate(mock_request)

    assert str(excinfo.value) == 'numbers deve ser uma lista de números'
