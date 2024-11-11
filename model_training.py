from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(X, y):
    """
    Trains a Random Forest classifier and returns the trained model, test features, and test labels.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model, X_test, y_test

def save_model(model, path="random_forest_phishing_model.joblib"):
    """
    Saves the trained model to a file.
    """
    joblib.dump(model, path)

def load_model(path="random_forest_phishing_model.joblib"):
    """
    Loads a saved model from a file.
    """
    return joblib.load(path)

"""
model_training.py
This file trains a Random Forest classifier on the extracted features and includes methods for saving and loading the model.
"""