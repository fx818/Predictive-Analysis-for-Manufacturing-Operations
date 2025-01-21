import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.read_csv("manufacturing_data.csv")

print(df)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['Machine_ID_Encoded'] = label_encoder.fit_transform(df['Machine_ID'])

X = df[['Machine_ID_Encoded', 'Temperature', 'Run_Time']]
y = df['Downtime_Flag']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("################################")
print(report)
print("################################")
print(accuracy)
print("################################")