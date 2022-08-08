# Libraries
from flask import Flask, jsonify, make_response, request
import pandas as pd
import numpy as np
import csv
import json
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Initialize the API
app = Flask(__name__) 

@app.route('/')
def index():
    return jsonify({'Nothing':"Nothing"})

datos = pd.read_csv("src/diabetes_data.csv",header = 0)

# replacing imposible values with mean
datos['Glucose'] = datos['Glucose'].replace(0, datos.Glucose.mean())
datos['BloodPressure'] = datos['BloodPressure'].replace(0, datos.BloodPressure.mean())
datos['SkinThickness'] = datos['SkinThickness'].replace(0, datos.SkinThickness.mean())
datos['Insulin'] = datos['Insulin'].replace(0, datos.Insulin.mean())
datos['BMI'] = datos['BMI'].replace(0, datos.BMI.mean())

# Endpoint that make a response with all the data
@app.route('/data', methods = ['GET']) # Method by default
def list_data():
    try:
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

@app.route('/data/info', methods = ['GET']) 
def get_info():
    try:
        return jsonify(datos.describe().to_dict())
    except Exception as ex:
        response = app.response_class(response = jsonify(mensaje = "error"),status=500,mimetype='application/json')
        return response

@app.route('/<model>/<n>', methods = ['GET'])
def aplying_ML(model,n):
    try:
        X = datos.iloc[:, :-1].values # the variables
        y = datos.iloc[:, 8].values # the labels
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
        if model == "knn":
            print(model)
            KNN = KNeighborsClassifier(n_neighbors = n)
            scores = []
            KNN.fit(X_train, y_train) # consider KNN scores
            scores.append(KNN.score(X_test, y_test))
            return jsonify(Model = model)
        else:
            return jsonify(Model = "Not found")
        #X = df.iloc[:, :-1].values # the variables
        #y = df.iloc[:, 8].values # the labels
        # choose the n from the request
        #KNN = KNeighborsClassifier(n_neighbors = math.ceil(math.sqrt(768)))
    except Exception as ex:
        response = app.response_class(response = jsonify(mensaje = "error"),status=500,mimetype='application/json')
        return response

# Trial endpoint for a POST (pass a json like this : {'el': 1} and it returns {'el': 2})
@app.route('/data/suma', methods = ['POST']) # POST method
def suma():
    json_request = request.get_json() # This method NEEDS to have request for geting the JSON from the POST
    print(json_request)
    json_request["el"] = int(json_request["el"] + 1)
    print(json_request)
    return jsonify(json_request)

def not_found(error):
    return "<h1> This url does not exists </h1>", 404 # This error handler executes thanks to the below code (app.register_error_handler(404, not found))


if __name__ == "__main__":
    app.register_error_handler(404, not_found) # This catches the 404 error
    app.run(debug = True)#, use_reloader = False)# This runs the API if # debug = True not need to reload if any changes are made