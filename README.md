# Flask API for Manufacturing Data Predictions

## Overview
This API allows users to:
1. Upload a CSV file containing manufacturing data.
2. Train a Decision Tree model on the uploaded dataset.
3. Predict downtime based on provided input parameters such as temperature, runtime, and machine ID.

## Requirements
- Python 3.7+
- Flask
- Pandas
- Scikit-learn

## Setup Instructions

1. **Clone the repository:**
   git clone <repository-url>
   cd <repository-folder>

### Install dependencies:
`pip install flask pandas scikit-learn`


2. **Run the application:**

python app.py
Access the API: The application will be available at http://127.0.0.1:5000 by default.

3. **Endpoints**

**1. Upload Endpoint**

`1. POST /upload`
Uploads a CSV file containing manufacturing data.

Request:
File: A CSV file with the following columns: Machine_ID, Temperature, Run_Time, Downtime_Flag.
Example:
`curl -X POST -F "file=@manufacturing_data.csv" http://127.0.0.1:5000/upload`

`Response:
{
    "message": "File uploaded and processed successfully."
}`


**2. Train Endpoint**
`POST /train`
Trains a Decision Tree model on the uploaded dataset and evaluates its performance.

Request: No additional input required.

Example:
`curl -X POST http://127.0.0.1:5000/train`

`Response:
{
    "accuracy": 0.95,
    "classification_report": {
        "0": {
            "precision": 0.96,
            "recall": 0.94,
            "f1-score": 0.95,
            "support": 20
        },
        "1": {
            "precision": 0.90,
            "recall": 0.95,
            "f1-score": 0.92,
            "support": 10
        },
        "accuracy": 0.95,
        "macro avg": {
            "precision": 0.93,
            "recall": 0.95,
            "f1-score": 0.94,
            "support": 30
        },
        "weighted avg": {
            "precision": 0.95,
            "recall": 0.95,
            "f1-score": 0.95,
            "support": 30
        }
    }
}`

**3. Predict Endpoint**

`POST /predict`
Predicts downtime based on input parameters.

`Request:
{
    "Machine_ID": "M3",
    "Temperature": 80,
    "Run_Time": 120
}`

Example:
`curl -X POST -H "Content-Type: application/json" -d '{"Machine_ID": "M3", "Temperature": 80, "Run_Time": 120}' http://127.0.0.1:5000/predict`

`Response:
{
    "Downtime": "No",
    "Confidence": 0.85
}`

## Example Workflow
**1. Upload the dataset:**
`curl -X POST -F "file=@manufacturing_data.csv" http://127.0.0.1:5000/upload`
**2. Train the model:**
`curl -X POST http://127.0.0.1:5000/train`
**3. Predict downtime:**
`curl -X POST -H "Content-Type: application/json" -d '{"Machine_ID": "M3", "Temperature": 80, "Run_Time": 120}' http://127.0.0.1:5000/predict`
