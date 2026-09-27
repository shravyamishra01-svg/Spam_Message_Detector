def validate_message(message):
    """
    Validate a message before prediction.
    """

    if not isinstance(message, str):
        return False, "Message must be text."

    if not message.strip():
        return False, "Message cannot be empty."

    if len(message.strip()) < 2:
        return False, "Message is too short."

    if len(message) > 5000:
        return False, "Message is too long."

    return True, "Valid message."