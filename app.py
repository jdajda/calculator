"""Return the pathname of the KOS root directory."""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/calculate')
def calculate():  # put application's code here
    """Return the pathname of the KOS root directory."""
    op   = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    output = ""
    op_string = ""
    if op=="sum":
        output = arg1 + arg2
        op_string = "+"
    elif op=="-":
        output = arg1 - arg2
        op_string = "-"

    return f"<h1>{arg1} {op_string} {arg2} = {output}</h1>"


if __name__ == '__main__':
    app.run()
