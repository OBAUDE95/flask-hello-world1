from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a POST endpoint for greeting
@app.route('/greet', methods=['POST'])
def greet_user():
    try:
        # Get JSON data from the request
        input_data = request.get_json()

        # Check if the input contains 'name'
        if not input_data or 'name' not in input_data:
            return jsonify({"error": "Missing 'name' in input data"}), 400

        # Extract the name
        name = input_data['name']

        # Create a greeting message
        greeting = f"Hello, {name}! Welcome to the API."

        # Return the greeting message
        return jsonify({"message": greeting}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running"}), 200

