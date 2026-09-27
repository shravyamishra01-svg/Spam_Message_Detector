def format_prediction(prediction):
    """
    Convert the model prediction into a user-friendly label.
    """

    if prediction == "spam":
        return "SPAM"

    return "NOT SPAM"


def get_prediction_message(prediction):
    """
    Return a descriptive message for the prediction.
    """

    if prediction == "spam":
        return "This message appears to be a spam message."

    return "This message appears to be a legitimate message."