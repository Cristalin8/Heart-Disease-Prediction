import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('data/heart_disease_data.csv')

predictors = data.drop("target", axis=1)
target = data["target"]

X_train, X_test, Y_train, Y_test = train_test_split(predictors, target, test_size=0.20, random_state=0)

lr = LogisticRegression(max_iter=10000)

lr.fit(X_train, Y_train)

Y_pred_lr = lr.predict(X_test)

score_lr = round(accuracy_score(Y_pred_lr, Y_test) * 100, 2)

print("Scorul de acuratețe obținut cu ajutorul modelului Logistic Regression este: " + str(score_lr) + " %")

joblib.dump(lr, 'models/logistic_regression_model.sav')


dt = DecisionTreeClassifier()

dt.fit(X_train, Y_train)

Y_pred_dt = dt.predict(X_test)

score_dt = round(accuracy_score(Y_pred_dt, Y_test) * 100, 2)

print("Scorul de acuratețe obținut cu ajutorul modelului Decision Tree este: " + str(score_dt) + " %")

joblib.dump(dt, 'models/decision_tree_model.sav')


rf = RandomForestClassifier(n_estimators=100)

rf.fit(X_train, Y_train)

Y_pred_rf = rf.predict(X_test)

score_rf = round(accuracy_score(Y_pred_rf, Y_test) * 100, 2)

print("Scorul de acuratețe obținut cu ajutorul modelului Random Forest este: " + str(score_rf) + " %")

joblib.dump(rf, 'models/random_forest_model.sav')
