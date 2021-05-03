#!/usr/bin/python3
"""States and State"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def states_by_id(id=None):
    """render HTML states - cities"""
    bu = storage.all(State)
    if id:
        id = "State." + id
    return render_template('9-states.html', burger=bu, id=id)


@app.teardown_appcontext
def use_teardown(exception):
    """Close SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
