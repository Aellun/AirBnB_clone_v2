#!/usr/bin/python3
"""This script Starts a flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when the route is queried
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
