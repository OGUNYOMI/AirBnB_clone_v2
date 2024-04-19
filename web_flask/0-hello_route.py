#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)

# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app, listening on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
