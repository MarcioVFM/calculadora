from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request
from typing import Dict, List

class Calculator3:
    def __init__(self, driver_handle: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handle

    def calculate(self, request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)
        formated_response = self.__formated_response(variance)
        return formated_response


    def __validate_body(self, body) -> List:
        if 'numbers' not in body:
            raise Exception('Body mal formatado')
        input_data = body['numbers']
        return input_data
    
    def __calculate_variance(self, numbers: List) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception('Falha no processo: Variância menos que multiplicação')
        
    def __formated_response(self, variance: float ) -> Dict:
        return {
            'data': {
                'Calculator': 3,
                'Variance': variance,
                'Success': True
            }
        }