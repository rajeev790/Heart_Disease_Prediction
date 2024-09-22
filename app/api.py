from flask import Flask, request, jsonify
import pickle
import numpy as np
from sqlalchemy.orm import Session
from .database import SessionLocal

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([data['features']])
    prediction = model.predict(features)[0]

    # Save the prediction and input data to the database
    db: Session = SessionLocal()
    db.execute(
        """
        INSERT INTO heart_disease_predictions (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction)
        VALUES (:age, :sex, :cp, :trestbps, :chol, :fbs, :restecg, :thalach, :exang, :oldpeak, :slope, :ca, :thal, :prediction)
        """,
        {
            'age': data['features'][0],
            'sex': data['features'][1],
            'cp': data['features'][2],
            'trestbps': data['features'][3],
            'chol': data['features'][4],
            'fbs': data['features'][5],
            'restecg': data['features'][6],
            'thalach': data['features'][7],
            'exang': data['features'][8],
            'oldpeak': data['features'][9],
            'slope': data['features'][10],
            'ca': data['features'][11],
            'thal': data['features'][12],
            'prediction': prediction
        }
    )
    db.commit()

    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
