#Importamos las librerias con las cuales trabajamos
from pandas.io import json
from pymongo import MongoClient

#Creamos la conexión del cliente a nuestra base de datos
cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = cliente['Proyecto']

#Creamos una función para insertar las tablas(colecciones) de nuestra BD
#Trabajamos los archivos json con el formato utf-8 de codificacion
def insertar(json_file):
    coleccion = str(input("Ingresar Nombre de la colecion: "))
    dColeccion = db[coleccion]
    jdf = open(json_file,encoding="utf-8").read()
    data = json.loads(jdf)
    dColeccion.insert_many(data)

#Solicitamos por consola el archivo a cargar de la BD
file_json = str(input("Ingresar nombre del archivo a cargar en base de datos: "))
file = file_json+".json"

insertar(file)
