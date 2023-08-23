from flask import Flask

app = Flask(__name__)


# /welcome
#     Returns “welcome”
# /welcome/home
#     Returns “welcome home”
# /welcome/back
#     Return “welcome back”
@app.get('/welcome')
def show_welcome():
    return "<h1>welcome</h1>"

@app.get('/welcome/home')
def show_home():
    return "<h1>welcome home</h1>"

@app.get('/welcome/back')
def show_back():
    return "<h1>welcome back</h1>"