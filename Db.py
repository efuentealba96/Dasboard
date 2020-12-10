# importamos librerias para trabajar
from pandas.io import json
from pymongo import MongoClient
import pandas as pd

# inicializamos la conexion con el servidor de mongodb
cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Prueba?retryWrites=true&w=majority")
# indicamos el nombre de la base de datos
db = cliente['Prueba']
# indicamos el nombre de la tabla en la que se insertaran los datos
colleccion = db['Franco']
# indicamos la codificacion de los archivos subidos
jdf = open('Nacimientos.json',encoding="utf-8").read()
# se cargan los archivos
data = json.loads(jdf)
# indicamos que los archivos se van a insertar en la db
colleccion.insert_many(data)
