import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

from sklearn.model_selection import train_test_split

from src.dataset_loader import load_dataset, prepare_dataset
from src.preprocessing import clean_text


DATASET_PATH = "data/SMSSpamCollection"
MODEL_PATH = "models/spam_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


def evaluate_model():
    print("Loading dataset...")

    # Load and prepare dataset
    data = load_dataset(DATASET_PATH)
    data = prepare_dataset(data)

    # Clean messages
    data["message"] = data["message"].apply(clean_text)

    X = data["message"]
    y = data["label"]

    # Use the same train/test split used during training
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Load trained model and vectorizer
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    # Convert test messages into TF-IDF features
    X_test_vectors = vectorizer.transform(X_test)

    # Make predictions
    predictions = model.predict(X_test_vectors)

    # Calculate metrics
    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        pos_label="spam"
    )

    recall = recall_score(
        y_test,
        predictions,
        pos_label="spam"
    )

    f1 = f1_score(
        y_test,
        predictions,
        pos_label="spam"
    )

    print("\n===== MODEL EVALUATION =====")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    # Confusion matrix
    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=["ham", "spam"]
    )

    print("\nConfusion Matrix:")
    print(matrix)

    # Display confusion matrix
    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=["Ham", "Spam"]
    )

    display.plot()
    plt.title("Spam Message Detector - Confusion Matrix")
    plt.tight_layout()

    plt.savefig("models/confusion_matrix.png")

    print("\nConfusion matrix saved to:")
    print("models/confusion_matrix.png")


if __name__ == "__main__":
    evaluate_model()