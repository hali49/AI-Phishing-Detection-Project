from preprocessing import load_emails_from_mbox, load_emails_from_folder, preprocess_email_content
from feature_processing import extract_features_tfidf, save_vectorizer
from model_training import train_model, save_model
from evaluate import evaluate_model

# Paths to phishing and benign datasets
phishing_paths = ["path/to/phishing_data1.mbox", "path/to/phishing_data2.mbox"]
benign_paths = ["path/to/benign_data_folder"]

# Load and preprocess phishing emails
phishing_emails = []
for path in phishing_paths:
    phishing_emails.extend(load_emails_from_mbox(path))
phishing_processed = preprocess_email_content(phishing_emails)

# Load and preprocess benign emails
benign_emails = []
for path in benign_paths:
    benign_emails.extend(load_emails_from_folder(path))
benign_processed = preprocess_email_content(benign_emails)

# Combine and label data
all_emails = phishing_processed + benign_processed
all_labels = [1] * len(phishing_processed) + [0] * len(benign_processed)

# Extract features
X, vectorizer = extract_features_tfidf([" ".join(email) for email in all_emails])
save_vectorizer(vectorizer)

# Train model
rf_model, X_test, y_test = train_model(X, all_labels)
save_model(rf_model)

# Evaluate model
evaluate_model(rf_model, X_test, y_test)
