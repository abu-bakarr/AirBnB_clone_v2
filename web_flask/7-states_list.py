#!/usr/bin/python3
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    state_obj = storage.all("State")
    states = list()
    for state, value in state_obj.items():
        states.append(value)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def home_teradown(exit):
    storage.close()


if __name__ == '__main__':
    app.run()