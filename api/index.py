from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


# Load the trained model
model = joblib.load("random_forest_model.joblib")

# Initialize Flask app
app = Flask(__name__)

# Define the API endpoint for prediction


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON data
        input_data = request.get_json()

        # Convert input JSON to DataFrame (expecting a list of records)
        data = pd.DataFrame(input_data)

        # Ensure the data contains the required features as per the model
        required_features = model.feature_names_in_
        if not all(feature in data.columns for feature in required_features):
            return jsonify({
                "error": f"Input data must include the following features: {list(required_features)}"
            }), 400

        # Predict using the model
        predictions = model.predict(data)
        # Probability of class 1 (stroke)
        probabilities = model.predict_proba(data)[:, 1]

        # Format the response
        response = {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist()
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a health check endpoint


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running"}), 200
