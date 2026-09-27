from src.dataset_loader import load_dataset, prepare_dataset


def test_dataset_loading():
    data = load_dataset("data/SMSSpamCollection")

    assert len(data) > 0
    assert "label" in data.columns
    assert "message" in data.columns


def test_dataset_preparation():
    data = load_dataset("data/SMSSpamCollection")
    data = prepare_dataset(data)

    assert len(data) > 0
    assert set(data["label"].unique()).issubset({"spam", "ham"})
    