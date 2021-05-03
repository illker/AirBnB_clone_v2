#!/usr/bin/python3
"""Number template"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """display hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello2():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is(text):
    """display C followed by args"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def py_is(text='is cool'):
    """display Py is cool"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def n_is(n):
    """display Py is cool"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def n_template(n):
    """HTML page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
