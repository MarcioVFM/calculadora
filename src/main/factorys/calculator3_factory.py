from src.drivers.numpy_handler import NumptHandler
from src.calculators.calculator_3 import Calculator3

def calculator3_factory():
    nunpy_handler = NumptHandler()
    calculator_3 = Calculator3(nunpy_handler)
    return calculator_3
