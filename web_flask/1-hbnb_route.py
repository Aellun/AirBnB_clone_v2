#!/usr/bin/python3
"""This script Start flask web-application with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when the route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when the  route is queried
    """
    return 'HBNB'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
