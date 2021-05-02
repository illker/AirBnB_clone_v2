#!/usr/bin/python3
"""C is fun!"""

from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route("/")
def hello():
    """display hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello2():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', methods=['GET'])
def c_is(text):
    """display C followed by args"""
    return 'C {%s}' format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
