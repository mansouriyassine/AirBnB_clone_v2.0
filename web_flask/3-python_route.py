#!/usr/bin/python3
"""
Flask web application demonstrating more complex routing.
Includes routes for '/', '/hbnb', '/c/<text>', and '/python/<text>'.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ Returns a greeting at the root route. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """ Returns 'HBNB' at the '/hbnb' route. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """
    Displays 'C ' followed by the custom text.
    Replaces underscores in 'text' with spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text):
    """
    Displays 'Python ' followed by the custom text or a default.
    Replaces underscores in 'text' with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    # Runs the application on the specified host and port.
    app.run(host='0.0.0.0', port=5000)
