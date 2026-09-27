from src.predictor import predict_message


def test_spam_message():
    message = "Congratulations! You have won a free prize. Click now to claim."

    prediction, confidence = predict_message(message)

    assert prediction == "spam"
    assert confidence > 0


def test_ham_message():
    message = "Hey, are you coming to class tomorrow?"

    prediction, confidence = predict_message(message)

    assert prediction == "ham"
    assert confidence > 0


def test_empty_message():
    try:
        predict_message("")
        assert False
    except ValueError as error:
        assert str(error) == "Message cannot be empty."