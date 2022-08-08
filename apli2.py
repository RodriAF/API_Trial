from flask import Flask, jsonify, make_response
import pandas as pd
import numpy as np
import csv
import json


app = Flask(__name__) #inicializar, ¿es el archivo princiapl?

@app.route('/')
def index():
    return jsonify({'Nothing':"Nothing"})
    

@app.route('/data', methods = ['GET']) # Method by default
def listar_cursos():
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
    

@app.route('/GD/<departamento>', methods = ['GET'])
def leer_cursos(departamento):
    try:
        #cursor = conexion.connection.cursor()
        #sql = "SELECT codigo, nombre, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        #cursor.execute(sql)
        #datos = cursor.fetchall()
        #datos ---- #Aqui deberia de meter algun parametro de [codigo_bdns == codigo]
        if datos != None:
            curso={'nombre':datos[0],'edad':datos[1],'ciudad':datos[2]}
            return jsonify({'cursos': cursos, 'mensaje': "codigo concreto"})
        else:
            return jsonify({'mensaje': "dato no encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "error"})

def pagina_no_encontrada(error):
    return "<h1> La pagina web no existe </h1>", 404 # esto se ejecuta gracias a lo de abajo (app.register_error_handler(404, pagina_no_encontrada))


if __name__ == "__main__":
    #app.config.from_object(config['development'])
    #app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug = True,use_reloader = False, host = "0.0.0.0", port=4000)#debug = True,use_reloader = False) #debug = True #hace que no haga falta reiniciarlo, lo hace solo
    # codigo para que el servidor funcione
    # python .\src\app.py deberia ejecutarse en la terminal
    # parametros a entender: 
    # depuracion apagada (cambio en codigo fuente hay que reiniciar), 
    # corriendo en local host y direccion (al buscarlo no se encuentra) no es que no funcione es que no ha encontrado respuesta
    # Se reinicia con control C en la terminal 


# Thunder client es como postman pero en Visual Studio

