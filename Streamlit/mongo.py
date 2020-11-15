import streamlit as st
from pymongo import MongoClient
import pandas as pd

cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")

#Seleccion de base de datos y coleccion a utilizar
db = cliente['Proyecto']
colection = db['Regiones']
#Creación de dataframe y consulta a la base de datos para el llenado del dato frame 
data = pd.DataFrame(list(colection.find()))

st.title("Monitoreo covid")
#@st.cache
def Cagar_datos(data):
    del data['_id']
    st.dataframe(data)


def Consulta(colection):
    cursor = colection.find({"Codigo region":9},{"Codigo comuna":0,"Fecha":0,"Codigo region":0})
    df = pd.DataFrame(list(cursor))
    del df['_id']
    st.dataframe(df)

Cagar_datos(data)
Consulta(colection)