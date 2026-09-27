import pandas as pd


def load_dataset(file_path):
    """
    Load the SMS Spam Collection dataset.

    The dataset is tab-separated:
    first column  = label
    second column = message
    """

    data = pd.read_csv(
        file_path,
        sep="\t",
        header=None,
        names=["label", "message"],
        encoding="utf-8",
        on_bad_lines="skip"
    )

    return data


def prepare_dataset(data):
    """
    Clean and prepare the dataset for machine learning.
    """

    # Remove missing values
    data = data.dropna()

    # Convert labels to lowercase
    data["label"] = data["label"].str.lower()

    # Keep only spam and ham
    data = data[data["label"].isin(["spam", "ham"])]

    # Reset row numbers
    data = data.reset_index(drop=True)

    return data