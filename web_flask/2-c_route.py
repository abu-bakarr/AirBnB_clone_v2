#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Main page rout"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route def"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c/text route"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run()
