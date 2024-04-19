#!/usr/bin/python3
<<<<<<< HEAD

=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
>>>>>>> 22b01ee835343cfeb0083226eac6a2f4c868d80e
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app, listening on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
=======

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 22b01ee835343cfeb0083226eac6a2f4c868d80e
