"""Return the pathname of the KOS root directory."""

from flask import Flask
from flask import request

app = Flask(__name__)

# class Calculator:
#     def __init__(self, op1: float, op2: float):
#        self.op1 = op1
#        self.op2 = op2
#
#     def sum(self):
#         return self.op1 + self.op2
#
#     def subtract(self):
#         return self.op1 - self.op2
#
# class TestCalculator:
#     def test_sum(self):
#         calc = Calculator(1, 2)
#         assert calc.sum() == 3


# calc = Calculator(4, 4)
# print(calc.op1)
# print(calc.sum())

@app.route('/calculate')
def calculate():  # put application's code here
    """Return the pathname of the KOS root directory."""
    op   = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=float)
    arg2 = request.args.get('arg2', type=float)
    output = ""
    op_string = ""
    if op=="sum":
        output = arg1 + arg2
        op_string = "+"
    elif op=="-":
        output = arg1 - arg2
        op_string = "-"

    return f"<h1 class='margin: auto;text-align: center;vertical-align: middle;'>{arg1} {op_string} {arg2} = {output}</h1>"


if __name__ == '__main__':
     app.run()
