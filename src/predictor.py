import joblib

from src.preprocessing import clean_text


MODEL_PATH = "models/spam_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


def load_model():
    """
    Load the trained spam detection model and TF-IDF vectorizer.
    """

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer


def predict_message(message):
    """
    Predict whether a message is Spam or Ham.
    """

    if not isinstance(message, str):
        raise ValueError("Message must be a string.")

    if not message.strip():
        raise ValueError("Message cannot be empty.")

    # Clean the message
    cleaned_message = clean_text(message)

    # Load model and vectorizer
    model, vectorizer = load_model()

    # Convert message into TF-IDF features
    message_vector = vectorizer.transform([cleaned_message])

    # Make prediction
    prediction = model.predict(message_vector)[0]

    # Get prediction confidence
    probabilities = model.predict_proba(message_vector)[0]

    confidence = max(probabilities) * 100

    return prediction, confidence


if __name__ == "__main__":

    message = input("Enter a message: ")

    try:
        prediction, confidence = predict_message(message)

        print("\nPrediction:", prediction.upper())
        print(f"Confidence: {confidence:.2f}%")

    except ValueError as error:
        print("Error:", error)