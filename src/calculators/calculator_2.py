from typing import Dict, List
from flask import request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driverhandler = driver_handler

    def calculate(self, request) -> Dict:
        body = request.json
        input_data = self.__validade_body(body)
        result = self.__process_data(input_data)
        formated_response = self.__formated_response(result)
        return formated_response

    def __validade_body(self, body) -> List:
        if 'numbers' not in body:
            raise Exception('Body mal formatado')
        input_data = body['numbers']
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process = [(num * 11) **0.95 for num in input_data]
        result = self.__driverhandler.standard_derivation(first_process)
        return 1/result

    def __formated_response(self, result: float ) -> Dict:
        return {
            'data': {
                'Calculator': 2,
                'result': round(result, 2)
            }
        }
    
