from datetime import datetime


prediction_history = []


def add_prediction(message, prediction, confidence):
    """
    Add a prediction to the history.
    """

    record = {
        "message": message,
        "prediction": prediction,
        "confidence": confidence,
        "time": datetime.now().strftime("%H:%M:%S")
    }

    prediction_history.append(record)


def get_history():
    """
    Return all prediction history.
    """

    return prediction_history


def clear_history():
    """
    Clear all prediction history.
    """

    prediction_history.clear()