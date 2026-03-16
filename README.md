# Fake News Detection System

A lightweight fake news classifier built with TF-IDF and Logistic Regression, plus a simple Streamlit UI for predictions.

## Highlights

- Text classification with TF-IDF features
- Logistic Regression baseline model
- Fast local inference via Streamlit
- Simple data preparation script

## Project Structure


Fake-News-Detection
├── app.py
├── data
│   ├── Fake.csv
│   ├── True.csv
│   └── news.csv
├── models
│   ├── model.pkl
│   └── vectorizer.pkl
├── requirements.txt
├── README.md
└── src
    ├── data.py
    └── model.py


## Requirements

- Python 3.8+
- The packages in requirements.txt

Install dependencies:

bash
pip install -r requirements.txt


## Data

This project expects two raw CSV files:

- data/Fake.csv
- data/True.csv

The preparation script src/data.py:

- Adds labels (0 for fake, 1 for real)
- Concatenates and shuffles the data
- Optionally saves a combined dataset to data/news.csv

To generate data/news.csv, open src/data.py and ensure the following lines are uncommented:

- data = data[["text", "label"]]
- data.to_csv("data/news.csv", index=False)

Then run:

bash
python src/data.py


## Training

Train the model with:

bash
python src/model.py


This script will:

- Load data/news.csv
- Fit a TfidfVectorizer
- Train a LogisticRegression model
- Print accuracy on a held-out test set
- Save artifacts to:
  - models/model.pkl
  - models/vectorizer.pkl

If the models/ folder does not exist, create it before training:

bash
mkdir -p models


## Run the App

Start the Streamlit UI:

bash
streamlit run app.py


Enter a news article and click *Predict* to classify it as Fake or Real.

## Notes on Accuracy

Reported accuracy depends on the dataset and split. The README does not guarantee a specific accuracy value. Re-run training to validate on your environment and data.

## Troubleshooting

- FileNotFoundError: data/news.csv
  - Run python src/data.py after confirming Fake.csv and True.csv exist.
- FileNotFoundError: models/model.pkl
  - Run python src/model.py to train and save the model.
- ModuleNotFoundError
  - Reinstall dependencies with pip install -r requirements.txt.

## Future Ideas

- Add preprocessing like lowercasing, lemmatization, and URL removal
- Evaluate with precision, recall, and F1
- Add model persistence versioning
- Try transformer-based models (e.g., BERT)

## Author

Rohit Yadav