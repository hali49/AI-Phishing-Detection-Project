import mailbox
import email
import os
from gensim.parsing.preprocessing import preprocess_string, strip_tags, strip_punctuation, strip_multiple_whitespaces, strip_numeric, remove_stopwords
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources if not already downloaded
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
custom_stopwords = stop_words.union({"nbsp", "font", "click", "account"})  # Add more domain-specific words as needed

# Define custom preprocessing filters
CUSTOM_FILTERS = [
    lambda x: x.lower(), strip_tags, strip_punctuation, strip_multiple_whitespaces, strip_numeric,
    remove_stopwords, lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split() if word not in custom_stopwords])
]

def get_body_from_email(msg):
    """
    Extracts the body text from an email message.
    Handles both multipart and single-part messages.
    Returns the decoded email body as a UTF-8 string.
    """
    body = None
    try:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    break  # Only get the first text part
        else:
            body = msg.get_payload(decode=True)
        return body.decode('utf-8', errors="ignore") if body else ""
    except Exception as e:
        print(f"Error processing message body: {e}")
        return ""

def load_emails_from_mbox(file_path):
    """
    Loads emails from an mbox file and extracts the body of each message.
    Returns a list of email bodies (strings).
    """
    emails = []
    try:
        mbox = mailbox.mbox(file_path)
        for msg in mbox:
            email_body = get_body_from_email(msg)
            if email_body:
                emails.append(email_body)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error loading emails from mbox: {e}")
    return emails

def load_emails_from_folder(folder_path):
    """
    Loads emails from a folder with .eml files and extracts the body of each message.
    Returns a list of email bodies (strings).
    """
    emails = []
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".eml"):
                with open(os.path.join(folder_path, filename), 'rb') as f:
                    msg = email.message_from_bytes(f.read())
                    email_body = get_body_from_email(msg)
                    if email_body:
                        emails.append(email_body)
    except FileNotFoundError:
        print(f"Error: Folder not found at {folder_path}")
    except Exception as e:
        print(f"Error loading emails from folder: {e}")
    return emails

def preprocess_email_content(emails):
    """
    Preprocesses a list of email bodies using custom filters.
    Applies tokenization, lowercasing, stopword removal, and lemmatization.
    """
    return [preprocess_string(email, CUSTOM_FILTERS) for email in emails]
"""
preprocessing.py
This file handles loading emails and applying preprocessing functions, including HTML handling, stopwords, lemmatization, and tokenization.


"""
