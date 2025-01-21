# Create a JSON file for prediction input
import json

# Example input data
prediction_data = {
    "Machine_ID": "M3",
    "Temperature": 80,
    "Run_Time": 120
}

# Save to a JSON file
json_path = "prediction_input.json"
with open(json_path, "w") as json_file:
    json.dump(prediction_data, json_file, indent=4)
json_path
