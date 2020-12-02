from pymongo import MongoClient
import pandas as pd 
import streamlit as st
import datetime
import plotly.express as px     
import plotly.graph_objects as gr


cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")

db = cliente['Proyecto']


def get_defunciones():
    colecion = db['Defunciones']
    df = pd.DataFrame(list(colecion.find()))
    df["Año"] = [df['Fecha'][i].split("-")[0] for i in range(df.shape[0])]
    df["Mes"] = [df['Fecha'][i].split("-")[1] for i in range(df.shape[0])]
    df["Dia"] = [df['Fecha'][i].split("-")[2] for i in range(df.shape[0])] 
    df = df[[int(df['Año'][i])>=2020 for i in range(df.shape[0])]].reset_index(drop=True)   
    data = df.groupby(['Año','Mes','Region','Comuna'], as_index=False).sum()
    del data['Codigo region']
    del data['Codigo comuna']
    return data

@st.cache
def grafica_defunciones(df,regiones):
    fig = gr.Figure()
    for i,region in enumerate(regiones):
        aux  = df[df['Region']==region]
        fig.add_trace(gr.Bar(x=aux['Mes'],y=aux['Defunciones'],name=region,marker_color=px.colors.qualitative.G10[i]))
    fig.update_layout(
        barmode = 'group',
        title = 'Defunciones por región',
        xaxis_title = "Meses",
        height = 500,
        width = 2000
    )
    return fig

def get_CComunas():
    colecion = db['C_Comunas']
    df = pd.DataFrame(list(colecion.find()))
    df['Casos x 1000'] = 1000*df['Casos confirmados']/df['Poblacion']
    del df['_id']
    del df['Codigo region']
    del df['Codigo comuna']
    return df

def get_icovid_C():
    colecion = db['icovid_C']
    df = pd.DataFrame(list(colecion.find()))
    return df

@st.cache
def grafica_icociv_C(df,comunas):
    fig = gr.Figure()
    for i,comuna in enumerate(comunas):
        aux = df[df['Comuna']==comuna]
        aux = aux.sort_values(by=['fecha']).reset_index(drop = True)
        y = aux['positividad']
        fig.add_trace(gr.Scatter(
            x = aux['fecha'],
            y = 100*y,
            name = str(comuna),
            mode = 'lines',
            marker_color =(px.colors.qualitative.D3+px.colors.qualitative.Safe)[i]
        ))
    fig.update_layout(
        title = "Positividad de examenes PCR por comuna",
        xaxis_title = "Fecha",
        yaxis_title = "Porcentaje de positividad",
        template = "ggplot2",
        height = 550
    )
    return fig

def get_icovid_R():
    colecion = db['icovid_R']
    df = pd.DataFrame(list(colecion.find()))
    return df

@st.cache
def grafica_icociv_R(df,regiones):
    fig = gr.Figure()
    for i,region in enumerate(regiones):
        aux = df[df['Region']==region]
        aux = aux.sort_values(by=['fecha']).reset_index(drop = True)
        y = aux['positividad']
        fig.add_trace(gr.Scatter(
            x = aux['fecha'],
            y = 100*y,
            name = str(region),
            mode = 'lines',
            marker_color =(px.colors.qualitative.D3+px.colors.qualitative.Safe)[i]
        ))
    fig.update_layout(
        title = "Positividad de examenes PCR por región",
        xaxis_title = "Fecha",
        yaxis_title = "Porcentaje de positividad",
        template = "ggplot2",
        height = 550
    )
    return fig 


@st.cache
def grafica_CComunas(df,comunas,marca):
    fig = gr.Figure()
    for i, comuna in enumerate(comunas):
        aux = df[df['Comuna']==comuna]
        if marca:
            y = aux['Casos x 1000']
        else:
            y = aux["Casos confirmados"]
        fig.add_trace(gr.Bar(x = aux["Semana Epidemiologica"],y = y,name = comuna,marker_color=px.colors.qualitative.G10[i]))
    fig.update_layout(
        title = "Casos por semana de epidemia",
        xaxis_title="Semana epidemiológica",
        yaxis_title="Número de casos",
        template='ggplot2',
        height=550
    )
    return fig

Options = st.sidebar.radio("Barra de Navegacion",['Defuciones segun el registro civil','Casos Por Comuna','Datos de icovid'])
if Options == 'Defuciones segun el registro civil':
    df = get_defunciones()
    st.dataframe(df)
    st.header('Gráfico por regiones')
    regiones = list(set(df['Region']))
    reg = st.multiselect('Seleccionar regiones',regiones,['La Araucanía','Tarapacá'])
    fig = grafica_defunciones(df, reg)
    st.plotly_chart(fig, use_container_width=True) 

if Options == 'Casos Por Comuna':
    op = st.sidebar.checkbox('Numero de casos por cada 1000 habitantes',value=False)
    df = get_CComunas()
    if st.checkbox("Listado de datos"):
        st.dataframe(df)
    st.header("Grafico de casos por region")
    comunas = list(set(df["Comuna"]))
    com = st.multiselect("Selecionar comunas",comunas,['Talcahuano','La Serena'])
    fig = grafica_CComunas(df,com,op)
    st.plotly_chart(fig,use_container_width=True)

if Options == 'Datos de icovid':
    opcion = st.selectbox("Elija que datos desea visualizar",("Datos por comuna","Datos por región"))
    if opcion == "Datos por comuna":
        df = get_icovid_C()
        comunas = list(set(df["Comuna"]))
        selected = st.multiselect("Selecionar comunas",comunas,["Temuco","Curacautín"])
        fig = grafica_icociv_C(df,selected)
        st.plotly_chart(fig,use_container_width=True)
    
    if opcion == "Datos por región":
        df = get_icovid_R()
        region = list(set(df["Region"]))
        selected = st.multiselect("Seleccionar region",region,['Tarapacá'])
        fig = grafica_icociv_R(df,selected)
        st.plotly_chart(fig,use_container_width=True)