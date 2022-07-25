# Libraries
from flask import Flask, jsonify, make_response
import pandas as pd
import numpy as np
import csv
import json

# Initialize the API
app = Flask(__name__) 

@app.route('/')
def index():
    return jsonify({'Nothing':"Nothing"})

# Endpoint that make a response with all the data
@app.route('/data', methods = ['GET']) # Method by default
def list_data():
    try:

        datos = pd.read_csv("src/diabetes_data.csv",header = 0)
        patients = []
        for i in datos.index: # csv must be saved in a dict to then parse it to json 
            #Parse to every data if its not string or it wont work
            sub={'Pregnancies':int(datos['Pregnancies'][i]),
            'Glucose':float(datos['Glucose'][i]),
            'Blood Pressure':float(datos['BloodPressure'][i]),
            'Skin Thickness':float(datos['SkinThickness'][i]),
            'Insulin':float(datos['Insulin'][i]),
            'BMI':float(datos['BMI'][i]),
            'Diabetes Pedigree Function':float(datos['DiabetesPedigreeFunction'][i]),
            'Age':int(datos['Age'][i]),
            'Outcome':int(datos['Outcome'][i])
            } 
            patients.append(sub)
        
        print(patients) # This should be shown in the terminal if the code above works
        return jsonify(patients)# jsonify will give the response as a proper json for the API
    except Exception as ex:
        response = app.response_class(response = jsonify(mensaje = "error"),status=500,mimetype='application/json')
        return response

def not_found(error):
    return "<h1> This url does not exists </h1>", 404 # This error handler executes thanks to the below code (app.register_error_handler(404, not found))


if __name__ == "__main__":
    app.register_error_handler(404, not_found) # This catches the 404 error
    app.run(debug = True, use_reloader = False)# This runs the API if # debug = True not need to reload if any changes are made
   
