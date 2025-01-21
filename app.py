from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import os

app = Flask(__name__)

# Global variables to store data and model
uploaded_data = None
model = None
label_encoder = None

@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_data, label_encoder

    if 'file' not in request.files:
        return jsonify({"error": "No file provided."}), 400

    file = request.files['file']

    try:
        # Read the CSV file
        uploaded_data = pd.read_csv(file)

        # Encode categorical column 'Machine_ID'
        label_encoder = LabelEncoder()
        uploaded_data['Machine_ID_Encoded'] = label_encoder.fit_transform(uploaded_data['Machine_ID'])

        return jsonify({"message": "File uploaded and processed successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/train', methods=['POST'])
def train():
    global uploaded_data, model

    if uploaded_data is None:
        return jsonify({"error": "No data uploaded. Please upload a dataset first."}), 400

    try:
        # Features (X) and target (y)
        X = uploaded_data[['Machine_ID_Encoded', 'Temperature', 'Run_Time']]
        y = uploaded_data['Downtime_Flag']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the Decision Tree Classifier
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        return jsonify({
            "accuracy": accuracy,
            "classification_report": report
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    global model, label_encoder

    if model is None:
        return jsonify({"error": "No model trained. Please train the model first."}), 400

    try:
        # Parse the input JSON
        input_data = request.get_json()
        temperature = input_data.get("Temperature")
        run_time = input_data.get("Run_Time")
        machine_id = input_data.get("Machine_ID")

        if temperature is None or run_time is None or machine_id is None:
            return jsonify({"error": "Missing required fields (Temperature, Run_Time, Machine_ID)."}), 400

        # Encode the Machine_ID
        machine_id_encoded = label_encoder.transform([machine_id])[0]

        # Prepare the input for prediction
        input_features = [[machine_id_encoded, temperature, run_time]]

        # Make prediction
        prediction = model.predict(input_features)
        probability = model.predict_proba(input_features)[0][1]  # Probability for class "1" (Downtime: Yes)
        downtime = "Yes" if prediction[0] == 1 else "No"

        return jsonify({"Downtime": downtime, "Confidence": round(probability, 2)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
