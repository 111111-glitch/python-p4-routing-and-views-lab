#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
   return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    if parameter < 1:
        return "Error: Parameter must be a positive integer greater than 0."
    else:
        numbers = '\n'.join(str(num) for num in range(1, parameter + 1))
        return f'<pre>{numbers}</pre>'


@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2

    elif operation == '-':
        result = num1 - num2

    elif operation == '*':
        result = num1 * num2

    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"    
    elif operation == '%':
        num1 % num2

    if result != None :
        return f'{num1} {operation} {num2} = {result}'
    else :
        return 'Invalid operation!'   
    

      
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)