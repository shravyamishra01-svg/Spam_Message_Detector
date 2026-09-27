# Spam Message Detector System Using Machine Learning

## 1. Problem Statement

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, misleading information, or potentially harmful links. Identifying spam manually can be time-consuming and unreliable, especially when a large number of messages need to be checked.

The objective of this project is to develop a machine learning based Spam Message Detector System that automatically analyzes a text message and classifies it as either **Spam** or **Not Spam (Ham)**.

The system uses text preprocessing, TF-IDF feature extraction, and a Multinomial Naive Bayes classification algorithm to identify patterns in messages and make predictions.

---

## 2. Objectives

The main objectives of the project are:

1. To develop an automated system for detecting spam messages.
2. To preprocess and clean text messages before classification.
3. To convert text messages into numerical features using TF-IDF.
4. To train a machine learning classification model.
5. To classify messages as Spam or Not Spam.
6. To display the prediction confidence to the user.
7. To maintain prediction history during application use.
8. To evaluate the machine learning model using standard performance metrics.
9. To provide a simple and user-friendly web interface.
10. To implement automated tests for important system components.

---

## 3. Functional Requirements

### FR1: Message Input

The system shall allow the user to enter or paste a text message.

### FR2: Input Validation

The system shall validate the entered message and reject empty, invalid, excessively short, or excessively long input.

### FR3: Text Preprocessing

The system shall clean the input text by converting it to lowercase, removing URLs and email addresses, removing unnecessary characters, and handling extra spaces.

### FR4: Spam Classification

The system shall classify the processed message as either Spam or Not Spam (Ham).

### FR5: Confidence Display

The system shall display the confidence associated with the prediction.

### FR6: Prediction History

The system shall maintain a history of messages checked during the current application session.

### FR7: History Management

The system shall allow the user to clear the prediction history.

### FR8: Model Evaluation

The system shall evaluate the trained model using accuracy, precision, recall, F1 score, and a confusion matrix.

### FR9: Automated Testing

The system shall provide automated tests for preprocessing, dataset handling, prediction, and input validation.

---

## 4. Non-Functional Requirements

### NFR1: Usability

The system should provide a simple interface that can be used without technical knowledge.

### NFR2: Performance

The system should provide predictions within a short period after the user submits a message.

### NFR3: Reliability

The system should handle invalid input without crashing the application.

### NFR4: Maintainability

The system should use separate modules for preprocessing, dataset handling, training, evaluation, prediction, validation, and history management.

### NFR5: Testability

Important system components should be independently testable using automated tests.

### NFR6: Scalability

The system structure should allow additional machine learning models or features to be added in the future.

### NFR7: Portability

The application should be executable on systems with Python and the required project dependencies installed.

### NFR8: Security

The system should process user-entered messages only for classification and should not require sensitive personal information.

---

## 5. Project Scope

The current system focuses on classification of text messages into two categories:

* Spam
* Not Spam (Ham)

The project includes dataset processing, machine learning model training, evaluation, prediction, input validation, prediction history, automated testing, and a Streamlit-based user interface.

The current system does not connect to a user's SMS application or automatically delete or block messages.

---

## 6. Technology Stack

| Technology              | Purpose                             |
| ----------------------- | ----------------------------------- |
| Python                  | Core programming language           |
| Pandas                  | Dataset handling                    |
| Scikit-learn            | Machine learning and evaluation     |
| TF-IDF                  | Text feature extraction             |
| Multinomial Naive Bayes | Classification                      |
| Joblib                  | Saving and loading trained model    |
| Matplotlib              | Confusion matrix visualization      |
| Streamlit               | Web interface                       |
| Pytest                  | Automated testing                   |
| Git/GitHub              | Version control and project hosting |

---

## 7. Machine Learning Approach

The system follows these major steps:

1. Load the SMS dataset.
2. Clean and prepare the dataset.
3. Preprocess the message text.
4. Split the dataset into training and testing data.
5. Convert text into numerical TF-IDF features.
6. Train a Multinomial Naive Bayes classifier.
7. Evaluate the model using the test dataset.
8. Save the trained model and TF-IDF vectorizer.
9. Use the saved model to classify new messages.

---

## 8. Model Evaluation

The implemented model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

The current evaluation produced:

| Metric    |  Result |
| --------- | ------: |
| Accuracy  |  96.86% |
| Precision | 100.00% |
| Recall    |  76.51% |
| F1 Score  |  86.69% |

These results are based on the project's current train/test split and should be interpreted in the context of the selected dataset and evaluation methodology.
