import pandas as pd
import numpy as np

# Generate synthetic data for columns Machine_ID, Temperature, Run_Time, Downtime_Flag
np.random.seed(42)

# Number of rows of data
num_rows = 1000

# Machine IDs (e.g., M1, M2, ..., M10)
machine_ids = [f'M{i}' for i in range(1, 11)]

# Temperature range (e.g., 30 to 100°C)
temperature = np.random.uniform(30, 100, num_rows)

# Run time (e.g., 0 to 12 hours)
run_time = np.random.uniform(0, 12, num_rows)

# Downtime flag (0 = no downtime, 1 = downtime)
downtime_flag = np.random.choice([0, 1], num_rows, p=[0.9, 0.1])

# Assign machine ID to each row randomly
machine_ids_col = np.random.choice(machine_ids, num_rows)

# Create the DataFrame
df = pd.DataFrame({
    'Machine_ID': machine_ids_col,
    'Temperature': temperature,
    'Run_Time': run_time,
    'Downtime_Flag': downtime_flag
})

print(df)


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Encode categorical column 'Machine_ID' to numerical values
label_encoder = LabelEncoder()
df['Machine_ID_Encoded'] = label_encoder.fit_transform(df['Machine_ID'])

# Features (X) and target (y)
X = df[['Machine_ID_Encoded', 'Temperature', 'Run_Time']]
y = df['Downtime_Flag']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("################################")
print(report)
print("################################")
print(accuracy)
print("################################")