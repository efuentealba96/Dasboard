# impportamos librerias necesarias para el funcionamiento
from pymongo import MongoClient
import pandas as pd 
import streamlit as st
import numpy as np
import datetime
import plotly.express as px 
import plotly.graph_objects as gr

# creamos una variable que almacenara la conexión a mongodb
cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
# indicamos elnombre de la base de datos donde estan almacenados 
# los datos con los que se trabajaran 
db = cliente['Proyecto']

# creamos nuestra primera función con la cual mostraremos la grafica de las defunciones
def get_data():
# indicamos la tabla de la cual obtendrmos la información necesaria 
# para poder graficar
    colecion = db['Defunciones']
    df = pd.DataFrame(list(colecion.find()))
# indicamos los campos a tener en consideración para graficar
    df["Año"] = [df['Fecha'][i].split("-")[0] for i in range(df.shape[0])]
    df["Mes"] = [df['Fecha'][i].split("-")[1] for i in range(df.shape[0])]
    df["Dia"] = [df['Fecha'][i].split("-")[2] for i in range(df.shape[0])]    
    df = df[[int(df['Año'][i])>=2020 for i in range(df.shape[0])]].reset_index(drop=True)
    n_semana = [datetime.datetime.strptime(df["Fecha"][i], '%Y-%m-%d').date().isocalendar()[1] for i in range(df.shape[0])]
    df['Semana'] = n_semana   
    data = df.groupby(['Año','Semana','Region','Comuna'], as_index=False).sum()
# indicamos el identificador de cada región y comuna    
    del data['Codigo region']
    del data['Codigo comuna']
    return data

def grafica_region(dfs,region):
    dfs = dfs[dfs['Region'] == region]
    fig = gr.Figure()
# indicamos el color de la grafica    
    color = ["red"]
# indicamos el metodo por el cual se agruparan los datos
    grupo =dfs.groupby("Año")
    i = 0
    for year,group in grupo:
        n_semana = []
        n_def = []
        grupo2 = group.groupby("Semana")
        for semana,group2 in grupo2:
            n_semana.append(semana)
            n_def.append(sum(group2['Defunciones']))
        fig.add_trace(gr.Scatter(x=n_semana[1:-1], y=n_def[1:-1],
                        mode='lines',
                        name=year,
                        marker_color=color[i]))

    fig.update_layout(
        title_text = f'Defunciones inscritas en region {region}',
        xaxis_title = "Numero de semana",
        height = 500
    )
    return fig
# comenzamos con el llamado de nuestras funciones
df = get_data()
st.dataframe(df)
st.header('Gráfico por regiones')
regiones = list(set(df['Region']))
reg = st.selectbox('Region', regiones, index=regiones.index('Metropolitana de Santiago'))
fig = grafica_region(df, reg)
st.plotly_chart(fig, use_container_width=True) 
