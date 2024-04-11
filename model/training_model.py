import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('heart_disease_data.csv')

# Define predictors (X) and target variable (Y)
predictors = data.drop("target", axis=1)
target = data["target"]

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(predictors, target, test_size=0.20, random_state=0)

# Initialize the Logistic Regression model
lr = LogisticRegression(max_iter=10000)

# Train the model using the training sets
lr.fit(X_train, Y_train)

# Make predictions using the testing set
Y_pred_lr = lr.predict(X_test)

# Calculate the accuracy score
score_lr = round(accuracy_score(Y_pred_lr, Y_test) * 100, 2)

print("The accuracy score achieved using Logistic Regression is: " + str(score_lr) + " %")

joblib.dump(lr, 'logistic_regression_model.sav')
