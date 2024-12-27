from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a GET endpoint for Hello World
@app.route('/hellodeji', methods=['GET'])
def say_hello():
    return jsonify({"message": "Hello, World!"}), 200

