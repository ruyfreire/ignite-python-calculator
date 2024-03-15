from flask import request as FlaskRequest
from typing import Dict, List, Union
from src.errors.http_bad_request import HttpBadRequestError


class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        average = self.__calculate_average(input_data)
        formatted_response = self.__format_response(average)

        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpBadRequestError("body deve conter o campo 'numbers'")

        numbers = body["numbers"]
        if not isinstance(numbers, list) or \
           not all(isinstance(n, (int, float)) for n in numbers):
            raise HttpBadRequestError("numbers deve ser uma lista de números")

        return numbers

    def __calculate_average(self, numbers: List[Union[int, float]]) -> float:
        average = sum(numbers) / len(numbers)
        return average

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": round(average, 2)
            }
        }
