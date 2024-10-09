from typing import Dict
from flask import request

class Calculator1:
    def calculate(self, request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3
        
        firs_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        result = firs_process_result + second_process_result + splited_number
        return self.to_dict(result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception('Body mal formatado')
        
        input_data = body['number']
        return input_data
    
    def __first_process(self, first_number:float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = (second_number **2.212)
        second_part = (first_part / 5) + 1
        return second_part
    
    def to_dict(self, calc_result: float) -> Dict:
        return {
            'data': {
                'Calculator': 1,
                'result': round(calc_result, 2)
            }
        }