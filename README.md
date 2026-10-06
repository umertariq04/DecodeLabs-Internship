# DecodeLabs AI Internship

A 4-week AI internship at DecodeLabs, with one project built each week. This repo collects the work, starting with foundational rule-based logic and building toward supervised machine learning.

---

## Project 1: Rule-Based AI Chatbot

A rule-based chatbot built in Python, with a Flask-powered web interface. Uses control flow, dictionary-based pattern matching, and basic input handling to simulate conversation.

**Folder:** `Project 1 - Rule Based Chatbot/`

**Tech used:** Python, Flask, HTML/CSS/JavaScript

**What it does:**
- Runs a continuous chat loop that responds to greetings, questions, and small talk
- Matches user input against a dictionary of known phrases
- Falls back to a default reply for anything it doesn't recognize
- Serves a web-based chat interface, with Python handling all the logic server-side

**How to run it:**
```
cd "Project 1 - Rule Based Chatbot"
pip install flask
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

---

## Project 2: Data Classification Using AI

A supervised learning model that classifies iris flowers into one of three species based on their measurements.

**Folder:** `Project 2 - Data Classification Using AI/`

**Tech used:** Python, scikit-learn

**What it does:**
- Loads the classic Iris dataset (150 flower samples, 3 species)
- Splits the data into a training set (80%) and a testing set (20%)
- Scales the features and trains a K-Nearest Neighbors (KNN) classifier
- Evaluates the model using accuracy, a confusion matrix, and a precision/recall/F1 report

**How to run it:**
```
cd "Project 2 - Data Classification Using AI"
pip install scikit-learn
python classifier.py
```

---

## About this internship

Each week introduces a new AI concept, moving from deterministic rule-based logic (Project 1) toward pattern-based, data-driven models (Project 2 and beyond).
