import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load your dataset
data = pd.read_csv('heart_disease_data.csv')

# Preprocessing (handle missing values, encode categorical variables, scale features if needed)
# Assuming X contains features and y contains the target variable

# Split data into features (X) and target variable (y)
X = data.drop('target', axis=1)
y = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=10000)  # Increase max_iter to 1000
model.fit(X_train_scaled, y_train)

# Evaluate the model
accuracy = model.score(X_test_scaled, y_test)
print(f"Model Accuracy: {accuracy}")


# Save the model using joblib
joblib.dump(model, 'heart_disease_model_m.sav')
