#!/usr/bin/python3
"""
Flask web application that demonstrates basic routing.
This module defines routes for '/', '/hbnb', and '/c/<text>'.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """ Returns a greeting message at the root route. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Returns 'HBNB' at the '/hbnb' route. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Displays 'C ' followed by custom text.
    Underscores in 'text' are replaced with spaces.
    """
    formatted_text = text.replace('_', ' ')
    return 'C ' + formatted_text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
