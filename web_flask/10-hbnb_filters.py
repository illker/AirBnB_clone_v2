#!/usr/bin/python3
"""HBNB filters"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """render filters web static"""
    bu = storage.all(State).values()
    bee = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', burger=bu, beer=bee)


@app.teardown_appcontext
def use_teardown(exception):
    """Close SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
