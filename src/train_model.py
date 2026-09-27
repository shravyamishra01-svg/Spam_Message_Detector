import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from src.dataset_loader import load_dataset, prepare_dataset
from src.preprocessing import clean_text


# File paths
DATASET_PATH = "data/SMSSpamCollection"
MODEL_PATH = "models/spam_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


def train_model():
    print("Loading dataset...")

    # Load dataset
    data = load_dataset(DATASET_PATH)
    data = prepare_dataset(data)

    print(f"Dataset loaded: {len(data)} messages")

    # Clean messages
    data["message"] = data["message"].apply(clean_text)

    # Separate input and output
    X = data["message"]
    y = data["label"]

    # Split dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print(f"Training messages: {len(X_train)}")
    print(f"Testing messages: {len(X_test)}")

    # Convert text into numerical features
    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )

    X_train_vectors = vectorizer.fit_transform(X_train)

    # Train Naive Bayes model
    model = MultinomialNB()

    model.fit(X_train_vectors, y_train)

    # Create models directory if it doesn't exist
    os.makedirs("models", exist_ok=True)

    # Save model and vectorizer
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print("\nModel training completed!")
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Vectorizer saved to: {VECTORIZER_PATH}")


if __name__ == "__main__":
    train_model()
