# Flask
from flask import Flask, render_template, request
# Data manipulation
import pandas as pd
# Matrices manipulation
import numpy as np
# Script logging
import logging
# ML model
import joblib
# JSON manipulation
import json
# Utilities
import sys
import os
import requests

# Current directory
current_dir = os.path.dirname(__file__)

# Flask app
app = Flask(__name__, static_folder='static', template_folder='template')

# Logging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# Function
def ValuePredictor(data=pd.DataFrame):
    # Model name
    model_name = 'modelo_CV_RFC.pkl'
    # Directory where the model is stored
    model_dir = os.path.join(current_dir, model_name)
    # Load the model
    loaded_model = joblib.load(open(model_dir, 'rb'))
    # Predict the data
    result = loaded_model.predict(data)
    return result[0]

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction page
@app.route('/prediction', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the data from form
        municipio = request.form['municipio']
        habitantes = request.form['habitantes']
        accidentes = request.form['accidentes']
        muertos = request.form['muertos']
        heridos = request.form['heridos']

        # Load template of JSON file containing columns name
        schema_name = 'columns_set.json'
        schema_dir = os.path.join(current_dir, schema_name)
        with open(schema_dir, 'r') as f:
            cols = json.loads(f.read())
        schema_cols = cols['data_columns']

        schema_cols['municipio'] = municipio
        schema_cols['habitantes'] = habitantes
        schema_cols['accidentes'] = accidentes
        schema_cols['muertos'] = muertos
        schema_cols['heridos'] = heridos

        df = pd.DataFrame(
            data={k: [v] for k, v in schema_cols.items()},
            dtype=float
        )

        # Create a prediction
        result = ValuePredictor(data=df)

        # Prepare the data to send to the Spring Boot API
        data_to_send = {
            'municipio': municipio,
            'habitantes': habitantes,
            'accidentes': accidentes,
            'muertos': muertos,
            'heridos': heridos,
            'peligroso': bool(int(result))  # Cambia 'prediction' por un booleano
        }

        # Send data to Spring Boot API
        api_url = 'http://localhost:8080/api/municipios/crear'  # Ajusta la URL según tu configuración
        try:
            response = requests.post(api_url, json=data_to_send)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            app.logger.error(f"Error al enviar datos a la API de Spring Boot: {e}")

        # Select image based on prediction
        if int(result) == 1:
            image_url = '/static/images/chocado.jpg'
            prediction_text = 'Sitio Peligroso!'
        else:
            image_url = '/static/images/seguro.jpg'
            prediction_text = 'Lugar seguro, Maneje con cuidado!'

        # Return the prediction
        return render_template('prediction.html', prediction=prediction_text, image_url=image_url)

    else:
        # Return error
        return render_template('error.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
