#!/usr/bin/python3
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define route for the homepage
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Define route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'

if __name__ == '__main__':
    # Run the app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
