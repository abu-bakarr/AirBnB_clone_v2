#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ DISPLAY Hello HBNB!!! """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ DISPLAY HBNB!!! """
    return ("HBNB")


@app.route('/c/<phrase>', strict_slashes=False)
def c(phrase):
    """ C + Phrases!!! """
    return 'C {}'.format(phrase.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<phrase>', strict_slashes=False)
def python(phrase='is cool'):
    """ Python + phrases!!!(is cool by default) """
    return 'Python {}'.format(phrase.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def number(num):
    """ It's a number! """
    if type(num) == int:
        return ("{} is a number".format(num))


if __name__ == '__main__':
    app.run()
