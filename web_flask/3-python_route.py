#!/usr/bin/python3
"""Python is cool!"""

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


@app.route('/c/<text>', , methods=['GET'])
def c_is(text):
    """display C followed by args"""
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>', , methods=['GET'])
def py_is(text='is cool'):
    """display Py is cool"""
    return 'Pysthon %s' % escape(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
