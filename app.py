from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a POST endpoint to greet the user
@app.route('/greet', methods=['POST'])
def greet_user():
    try:
        # Parse the JSON data from the request
        data = request.get_json()
        
        # Extract the name from the JSON payload
        name = data.get('name', None)
        
        if not name:
            return jsonify({"error": "Name is required"}), 400

        # Create a personalized greeting
        return jsonify({"message": f"Hello, {name}!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
