import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data set
df = pd.read_csv('heart_disease.csv')

# Split the data into training and test sets
X = df.drop(columns=['target'])
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.svm import SVC

# Train a linear SVM
model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# Evaluate the model on the test data
y_pred = model.predict(X_test)
accuracy = (y_pred == y_test).mean()
print('Accuracy:', accuracy)

# Diagnose a new patient
patient_data = [65, 1, 0, 170, 256, 0, 1, 1, 1]
patient_data = [patient_data]  # SVM expects a 2D array as input
patient_label = model.predict(patient_data)
print('Predicted label:', patient_label)