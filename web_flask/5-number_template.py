#!/usr/bin/python3
"""This script starts flask web application with six routings"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns string when the  route is queried"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns string when the route is queried"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Returns predefined reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable predefined text=cool"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve the html template for request"""
    path = '5-number.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
