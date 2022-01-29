#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ DISPLAY Hello HBNB!!! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ DISPLAY HBNB!!! """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c/text route"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """python/text route"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

if __name__ == '__main__':
    app.run()
