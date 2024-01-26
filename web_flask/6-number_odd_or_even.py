#!/usr/bin/python3
"""
Flask web application with several routes including
one that determines if a number is odd or even.
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Returns 'Hello HBNB!' at the root. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Returns 'HBNB' at the '/hbnb' route. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays 'C ' followed by the custom text. """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ Displays 'Python ' followed by the custom text or default. """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Confirms that 'n' is a number if it's an integer. """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Renders a HTML page displaying 'n' if it's an integer. """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Renders a HTML page displaying if 'n' is odd or even. """
    parity = "odd" if n % 2 else "even"
    return render_template(
        '6-number_odd_or_even.html', number=n, parity=parity
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
