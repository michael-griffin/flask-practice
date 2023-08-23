from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def add_page():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{add(a, b)}"

@app.get('/sub')
def sub_page():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{sub(a, b)}"

@app.get('/mult')
def mult_page():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{mult(a, b)}"

@app.get('/div')
def div_page():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f"{div(a, b)}"

@app.get('/math/<operation>')
def calc_page(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    #TODO:could use data strucutre (dict) here where key is what you are
    #looking for
    match operation:
        case 'add':
            return f"{add(a, b)}"
        case 'sub':
            return f"{sub(a, b)}"
        case 'mult':
            return f"{mult(a, b)}"
        case 'div':
            return f"{sub(a, b)}"

