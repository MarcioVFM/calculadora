from typing import Dict
from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculator():
    mock_request = MockRequest(body={'numbers': [1.234, 2.433, 3.0]})

    calculator_2 = Calculator2()
    formated_number = calculator_2.calculate(mock_request)

    assert isinstance(formated_number, dict) #verifica se o formated_number e um dict