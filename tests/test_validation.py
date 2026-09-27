from src.validation import validate_message


def test_valid_message():
    valid, message = validate_message("Hello, how are you?")

    assert valid is True
    assert message == "Valid message."


def test_empty_message():
    valid, message = validate_message("")

    assert valid is False
    assert message == "Message cannot be empty."


def test_short_message():
    valid, message = validate_message("A")

    assert valid is False
    assert message == "Message is too short."


def test_non_string_message():
    valid, message = validate_message(None)

    assert valid is False
    assert message == "Message must be text."