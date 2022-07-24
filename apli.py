from flask import Flask, jsonify, make_response
import pandas as pd
import numpy as np
import csv
import json

#from flask_mysqldb import MySQL

app = Flask(__name__) #inicializar, ¿es el archivo princiapl?

@app.route('/')
def index():
    return jsonify({'Nothing':"Nothing"})
    
datos = pd.read_csv("https://raw.githubusercontent.com/empathyco/academy-government-data/main/data-plugin/datos_limpios/convocatorias_demo.csv",header = 0)
cursos = []
@app.route('/GD', methods = ['GET']) # Metodo pero por defecto pero es importante para git y post
def listar_cursos():
    try:

        datos = pd.read_csv("https://raw.githubusercontent.com/empathyco/academy-government-data/main/data-plugin/datos_limpios/convocatorias_demo.csv",header = 0)
        litle_datos = datos[:5]
        listado = []
        for i in litle_datos.index: # el csv se guarda en un dictionary
            
            sub={'codigo_bdns':float(litle_datos['codigo_bdns'][i]),
                    'MRR':bool(litle_datos["MRR"][i]), #Parsear las cosas siempre
                    'administracion':litle_datos['administracion'][i],
                    'departamento':litle_datos['departamento'][i],
                    #'organo':litle_datos['organo'][i],
                    'fecha_registro':litle_datos['fecha_registro'][i],
                    'titulo_convocatoria':litle_datos['titulo_convocatoria'][i],
                    'url_bases_regul':litle_datos['url_bases_regul'][i]
                } 
            '''
            sub=jsonify(codigo_bdns=float(litle_datos['codigo_bdns'][i]),
                    MRR=litle_datos["MRR"][i],
                    administracion=litle_datos['administracion'][i],
                    departamento=litle_datos['departamento'][i],
                    #'organo':litle_datos['organo'][i],
                    fecha_registro=litle_datos['fecha_registro'][i],
                    titulo_convocatoria=litle_datos['titulo_convocatoria'][i],
                    url_bases_regul=litle_datos['url_bases_regul'][i]
                )
            '''
            listado.append(sub)
        
        print("GD right")
            # Esto es transformar los datos que tengo a un diccionario y es de vital importancia a 
            # la hora de devolver los datos como json
        print(listado)
        return jsonify(listado)#aqui se devuelve en forma de respuesta en forma de json
    except Exception as ex:
        response = app.response_class(response = jsonify(mensaje = "error"),status=500,mimetype='application/json')
        return response
    else:
        litle_datos = datos[:200]
        listado = []
        for i in litle_datos.index: # el csv se guarda en un dictionary
            sub={'codigo_bdns':litle_datos['codigo_bdns'][i],
                    'MRR':litle_datos['MRR'][i],
                    'administracion':litle_datos['administracion'][i],
                    'departamento':litle_datos['departamento'][i],
                    'organo':litle_datos['organo'][i],
                    'fecha_registro':litle_datos['fecha_registro'][i],
                    'titulo_convocatoria':litle_datos['titulo_convocatoria'][i],
                    'url_bases_regul':litle_datos['url_bases_regul'][i]
                } 
            listado.append(sub)
        print("GD right")
            # Esto es transformar los datos que tengo a un diccionario y es de vital importancia a 
            # la hora de devolver los datos como json

        return jsonify(listado)

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
    app.run(debug = True,use_reloader = False)#debug = True,use_reloader = False) #debug = True #hace que no haga falta reiniciarlo, lo hace solo
    # codigo para que el servidor funcione
    # python .\src\app.py deberia ejecutarse en la terminal
    # parametros a entender: 
    # depuracion apagada (cambio en codigo fuente hay que reiniciar), 
    # corriendo en local host y direccion (al buscarlo no se encuentra) no es que no funcione es que no ha encontrado respuesta
    # Se reinicia con control C en la terminal 


# Thunder client es como postman pero en Visual Studio

