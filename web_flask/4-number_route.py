#!/usr/bin/python3
"""
This module starts a Flask web application with multiple routes.
Each route displays a different message
with one route checking if a parameter is an integer.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Returns a greeting message at the root route. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Returns 'HBNB' at the '/hbnb' route. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by custom text.
    Replaces underscores in 'text' with spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python ' followed by the custom text or a default.
    Replaces underscores in 'text' with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_check(n):
    """
    Displays a message confirming 'n' is a number if it's an integer.
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    # Runs the application on the specified host and port.
    app.run(host='0.0.0.0', port=5000)
