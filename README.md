# Heart Disease Prediction

## Overview

This project predicts whether a person is likely to have heart disease based on medical attributes using machine learning. The prediction is made using a trained model, which is exposed through a REST API.

## Features

- Train a machine learning model using the heart disease dataset.
- Serve predictions via an API built with Flask.
- Database integration for storing logs, user interactions, or results (optional).
- Uses a Random Forest Classifier for predictions.
- Easy-to-use API for making predictions.

## Project Structure

```bash
heart-disease-prediction/
│
├── app/
│   ├── __init__.py          # Initialization file for the app
│   ├── main.py              # Main file to run the application
│   ├── model.py             # Script to train and save the model
│   ├── api.py               # API file to handle prediction requests
│   ├── database.py          # (Optional) for handling database connections
│
├── data/
│   └── heart_disease.csv    # Dataset used for training the model
│
├── migrations/              # Directory for Alembic migrations (if using a database)
│   ├── alembic.ini
│   └── versions/            # Migration scripts for the database
│
├── model.pkl                # Trained model saved as a pickle file
│
├── requirements.txt         # List of dependencies
│
├── README.md                # Project documentation (this file)
│
└── .gitignore               # Files and directories to ignore in version control
