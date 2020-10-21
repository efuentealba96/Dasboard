from pandas.io import json
from pymongo import MongoClient
import pandas as pd

cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Prueba?retryWrites=true&w=majority")
db = cliente['Prueba']
colleccion = db['Franco']
jdf = open('Nacimientos.json',encoding="utf-8").read()
data = json.loads(jdf)

colleccion.insert_many(data)