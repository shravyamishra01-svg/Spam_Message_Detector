# Spam Message Detector System Using Machine Learning

A machine learning based web application that analyzes text messages and classifies them as **Spam** or **Not Spam (Ham)**.

## 1. Project Overview

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, misleading information, or suspicious links.

This project provides an automated system that analyzes the content of a text message and predicts whether it is spam or legitimate.

The system uses:

* Text preprocessing
* TF-IDF feature extraction
* Multinomial Naive Bayes classification
* Model evaluation
* Input validation
* Prediction history
* Streamlit web interface
* Automated testing

---

## 2. Features

### Message Detection

Users can enter a text message and receive a Spam or Not Spam prediction.

### Text Preprocessing

Messages are cleaned before being passed to the machine learning model.

The preprocessing includes:

* Lowercase conversion
* URL removal
* Email address removal
* Special character removal
* Extra-space removal

### Machine Learning Classification

The system uses:

* **TF-IDF Vectorizer** for converting text into numerical features
* **Multinomial Naive Bayes** for classification

### Confidence Score

The system displays the confidence associated with each prediction.

### Prediction History

The application maintains the messages checked during the current session and displays their predictions.

### Input Validation

The system validates user input before prediction.

### Model Evaluation

The trained model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Automated Testing

The project includes automated tests using Pytest.

---

## 3. Project Architecture

```text
User
  |
  v
Streamlit Web Interface
  |
  v
Input Validation
  |
  v
Text Preprocessing
  |
  v
TF-IDF Vectorizer
  |
  v
Naive Bayes Model
  |
  v
Spam / Ham Prediction
  |
  +----> Confidence Score
  |
  +----> Prediction History
```

---

## 4. Project Structure

```text
Spam_Message_Detector/
│
├── data/
│   └── SMSSpamCollection
│
├── models/
│   ├── spam_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── confusion_matrix.png
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── dataset_loader.py
│   ├── train_model.py
│   ├── evaluation.py
│   ├── predictor.py
│   ├── utils.py
│   ├── history.py
│   └── validation.py
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_dataset_loader.py
│   ├── test_predictor.py
│   └── test_validation.py
│
├── app.py
├── requirements.txt
├── statement.md
├── README.md
└── .gitignore
```

---

## 5. Technologies Used

| Technology              | Purpose                   |
| ----------------------- | ------------------------- |
| Python                  | Core programming language |
| Pandas                  | Dataset processing        |
| Scikit-learn            | Machine learning          |
| TF-IDF                  | Text feature extraction   |
| Multinomial Naive Bayes | Message classification    |
| Joblib                  | Model persistence         |
| Matplotlib              | Evaluation visualization  |
| Streamlit               | Web application           |
| Pytest                  | Automated testing         |
| Git/GitHub              | Version control           |

---

## 6. Dataset

The project uses the **SMS Spam Collection** dataset.

The dataset contains SMS messages labelled as either:

* `spam`
* `ham`

The dataset is used to train and evaluate the machine learning model.

---

## 7. Machine Learning Workflow

```text
SMS Dataset
     |
     v
Load Dataset
     |
     v
Prepare Dataset
     |
     v
Clean Text
     |
     v
Train/Test Split
     |
     v
TF-IDF Feature Extraction
     |
     v
Multinomial Naive Bayes
     |
     v
Model Evaluation
     |
     v
Save Model
     |
     v
Predict New Messages
```

---

## 8. Model Evaluation

The current model was evaluated using a test set created with an 80/20 train-test split.

Current results:

| Metric    |  Result |
| --------- | ------: |
| Accuracy  |  96.86% |
| Precision | 100.00% |
| Recall    |  76.51% |
| F1 Score  |  86.69% |

The project also generates a confusion matrix:

```text
models/confusion_matrix.png
```

---

## 9. Installation

### Step 1: Clone the repository

```bash
git clone <repository-url>
```

### Step 2: Open the project folder

```bash
cd Spam_Message_Detector
```

### Step 3: Create a virtual environment

```bash
py -m venv venv
```

### Step 4: Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\activate
```

### Step 5: Install dependencies

```powershell
py -m pip install -r requirements.txt
```

---

## 10. Train the Model

Run:

```powershell
py -m src.train_model
```

This creates:

```text
models/spam_model.pkl
models/tfidf_vectorizer.pkl
```

---

## 11. Evaluate the Model

Run:

```powershell
py -m src.evaluation
```

This displays the evaluation metrics and creates:

```text
models/confusion_matrix.png
```

---

## 12. Run Automated Tests

Run:

```powershell
py -m pytest
```

The current project contains automated tests covering:

* Text preprocessing
* Dataset loading
* Dataset preparation
* Message prediction
* Input validation

The current test suite contains **12 passing tests**.

---

## 13. Run the Web Application

Start Streamlit using:

```powershell
streamlit run app.py
```

The application provides:

1. Message input
2. Input validation
3. Spam/Ham prediction
4. Confidence score
5. Prediction explanation
6. Prediction history
7. Clear history option

---

## 14. Limitations

The current system has some limitations:

* It is designed for text-message classification.
* It does not automatically access or scan a user's SMS inbox.
* Prediction quality depends on the training dataset.
* The model may not correctly classify messages with patterns that differ significantly from the training data.
* Prediction history currently exists only during the active application session.

---

## 15. Future Enhancements

Possible future improvements include:

* Persistent prediction history using a database
* Support for additional languages
* Comparison of multiple machine learning algorithms
* Improved feature engineering
* Larger and more diverse training datasets
* Model retraining functionality
* Deployment as a cloud application
* Additional visualization and analytics

---

## 16. Testing Status

The project currently contains **12 automated tests**, covering the major implemented modules.

All current tests pass successfully.

```text
12 passed
```

---

## 17. Project Documentation

Additional project documentation is available in:

```text
statement.md
```

The final project documentation will also include architecture diagrams, workflow diagrams, UML diagrams, screenshots, testing results, challenges, learnings, and future enhancements.

---

## 18. License

This project is developed for educational purposes as part of a VITyarthi Build Your Own Project submission.
