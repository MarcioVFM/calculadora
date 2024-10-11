from typing import Dict, List
from flask import request
from src.drivers.numpy_handler import NumptHandler

class Calculator2:
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
        numpy_handler = NumptHandler()
        first_process = [(num * 11) **0.95 for num in input_data]
        result = numpy_handler.standard_derivation(first_process)
        return 1/result

    def __formated_response(self, result: float ) -> Dict:
        return {
            'data': {
                'Calculator': 1,
                'result': round(result, 2)
            }
        }
    
