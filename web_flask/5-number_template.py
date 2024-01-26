#!/usr/bin/python3
"""
This module starts a Flask web application with enhanced routing and rendering.
Includes routes for '/', '/hbnb', '/c/<text>', '/python/<text>', '/number/<n>',
and '/number_template/<n>'.
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main_page():
    """ Returns 'Hello HBNB!' at the root route. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """ Returns 'HBNB' at the '/hbnb' route. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'C ' followed by the custom text.
    Replaces underscores in 'text' with spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Displays 'Python ' followed by the custom text or a default.
    Replaces underscores in 'text' with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays a message confirming 'n' is a number if it's an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML page displaying 'n' if it's an integer.
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
