from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a GET endpoint for Hello World
@app.route('/', methods=['GET'])
def say_hello():
    return "deji"
