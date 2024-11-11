from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def extract_features_tfidf(emails, max_features=1000):
    """
    Extracts TF-IDF features from a list of emails.
    """
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(emails).toarray()
    return X, vectorizer

def save_vectorizer(vectorizer, path="tfidf_vectorizer.joblib"):
    """
    Saves the TF-IDF vectorizer to a file.
    """
    joblib.dump(vectorizer, path)

def load_vectorizer(path="tfidf_vectorizer.joblib"):
    """
    Loads a saved TF-IDF vectorizer from a file.
    """
    return joblib.load(path)
"""
feature_processing.py
This file extracts features from preprocessed emails using TF-IDF. It includes methods for saving and loading the vectorizer.
"""