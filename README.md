# 📧 AI Email Fraud Detection System

## Overview

AI Email Fraud Detection System is a Machine Learning-based web application that analyzes email content and classifies it as either **Spam/Fraud** or **Genuine (Ham)**.

The system uses Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes classifier to identify suspicious patterns in email text. Users can paste email content into the application and receive instant fraud detection results along with a risk assessment.

---

## Features

* Real-time Email Analysis
* Spam and Fraud Detection
* Machine Learning-Based Classification
* NLP Text Processing
* Risk Score Indicator
* Suspicious Keyword Detection
* Interactive Dashboard UI
* Fast Prediction Response

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-Learn
* Multinomial Naive Bayes

### NLP

* CountVectorizer

### Data Processing

* Pandas
* NumPy

---

## Project Architecture

```text
User Input Email
        │
        ▼
Text Preprocessing
        │
        ▼
CountVectorizer
        │
        ▼
Naive Bayes Model
        │
        ▼
Prediction Engine
        │
        ▼
Spam / Genuine Result
```

---

## Dataset

The project uses the SMS Spam Collection Dataset containing thousands of labeled messages.

Classes:

* Ham (Legitimate Message)
* Spam (Fraudulent Message)

Example:

| Label | Message                           |
| ----- | --------------------------------- |
| ham   | Hi, how are you?                  |
| spam  | Congratulations! You won ₹50,000. |

---

## Machine Learning Workflow

### Step 1: Data Collection

Spam and legitimate email/message dataset is collected.

### Step 2: Data Cleaning

* Remove duplicate records
* Handle missing values
* Prepare text data

### Step 3: Feature Extraction

Text is converted into numerical vectors using:

```python
CountVectorizer()
```

### Step 4: Model Training

The dataset is split into:

* Training Data
* Testing Data

Model Used:

```python
MultinomialNB()
```

### Step 5: Prediction

The trained model predicts:

* Spam
* Genuine

---

## Installation

Clone Repository

```bash
git clone https://github.com/yourusername/email-fraud-detection.git
```

Move to Project Folder

```bash
cd email-fraud-detection
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
email-fraud-detection/

│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
└── dataset/
    └── spam.csv
```

---

## Sample Spam Email

```text
Congratulations!

You have won ₹50,000 cash reward.

Click the link below immediately to claim your prize.

Limited time offer.
```

Output:

```text
SPAM EMAIL DETECTED
```

---

## Sample Genuine Email

```text
Hello Team,

The meeting has been scheduled for tomorrow at 10 AM.

Please review the attached report.

Regards,
Manager
```

Output:

```text
GENUINE EMAIL
```

---

## Future Enhancements

* Deep Learning Models (LSTM/BERT)
* Confidence Score Visualization
* Email Attachment Analysis
* Phishing URL Detection
* Multi-language Support
* AI-Powered Explanation System
* Email File Upload Support
* Dashboard Analytics

---

## Applications

* Email Security Systems
* Corporate Mail Filtering
* Banking Fraud Detection
* Phishing Detection
* Cybersecurity Solutions

---

## Learning Outcomes

Through this project:

* Supervised Learning
* Classification Problems
* Natural Language Processing
* Feature Engineering
* Model Training
* Model Evaluation
* Streamlit Deployment

were successfully implemented and demonstrated.

---

## Author

Adarsh

Machine Learning Project

Built using Python, Scikit-Learn, NLP, Streamlit, and Machine Learning.

