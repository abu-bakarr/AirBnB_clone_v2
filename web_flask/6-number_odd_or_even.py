#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ DISPLAY Hello HBNB!!! """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ DISPLAY HBNB!!! """
    return ("HBNB")


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


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """number/n route"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ Display a HTML page. """
    if type(n) == int:
        return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_HBNB(n):
    if n % 2 == 0:
        val = "even"
    else:
        val = "odd"
    return render_template('6-number_odd_or_even.html', num=n, val=val)


if __name__ == '__main__':
    app.run()
