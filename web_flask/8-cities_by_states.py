#!/usr/bin/python3
"""Cities by states"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states_list():
    """render HTML cities"""
    return render_template('8-cities_by_states.html', burger=storage.all(State).values())


@app.teardown_appcontext
def use_teardown(exception):
    """Close SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
