from src.drivers.numpy_handler import NumptHandler
from src.calculators.calculator_2 import Calculator2

def calculator2_factory():
    numpy_handler = NumptHandler()
    calc = Calculator2(numpy_handler)
    return calc