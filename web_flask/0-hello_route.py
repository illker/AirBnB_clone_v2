#!/usr/bin/python3
"""Hello Flask!"""

from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route("/")
def hello():
    """display hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
