# Fake News Detection System

## Project Overview

This project detects whether a news article is **Fake** or **Real** using **Machine Learning and Natural Language Processing (NLP)** techniques.

The system analyzes the text of news articles and predicts whether the news is fake or real using a trained machine learning model.

---

## Features

* Detects Fake and Real News
* Machine Learning based text classification
* Simple Web Interface
* Fast prediction using trained model

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Streamlit

---

## Project Structure

Fake-News-Detection
│
├── data
│ ├── Fake.csv
│ └── True.csv
│
├── models
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── src
│ ├── data.py
│ └── model.py
│
├── app.py
├── requirements.txt
└── README.md

---

## Installation

Install required libraries:

pip install -r requirements.txt

---

## Run the Project

Train the model:

python src/model.py

Run the web application:

streamlit run app.py

---

## Usage

1. Enter news text in the input box
2. Click **Predict**
3. The system will classify the news as **Fake News** or **Real News**

---

## Model Used

Logistic Regression with TF-IDF feature extraction.

Accuracy: ~95%+

---

## Future Improvements

* Deep Learning models (LSTM / BERT)
* More datasets for better accuracy
* Improved UI design

---

## 👨‍💻 Author
Rohit Yadav
