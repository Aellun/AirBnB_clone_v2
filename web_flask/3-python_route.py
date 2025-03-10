#!/usr/bin/python3
"""This script starts flask  web application with 4 routings"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns string when the route is queried"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns string when the route is queried"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return predefined reformatted text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable predefined = cool"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
