from pymongo import MongoClient
import pandas as pd 
import streamlit as st
import plotly.express as px     
import plotly.graph_objects as gr



cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = cliente['Proyecto']

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

def main():
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

if __name__ == "__main__":
    main()