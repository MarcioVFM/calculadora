from flask import jsonify, request, Blueprint
from src.calculators.calculator_1 import Calculator1

calc_routes_bp = Blueprint('calc_routes', __name__)

@calc_routes_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    response = calc.calculate(request)
    
    return jsonify(response), 200 