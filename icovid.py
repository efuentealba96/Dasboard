from pymongo import MongoClient
import pandas as pd 
import streamlit as st
import plotly.express as px     
import plotly.graph_objects as gr



cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = cliente['Proyecto']

def get_icovid_C():
# indicamos de que tabla se obtendran los datos a graficar
    colecion = db['icovid_C']
# mediante la función list se ordenan los datos a mostrar
    df = pd.DataFrame(list(colecion.find()))
    return df

@st.cache
def grafica_icociv_C(df,comunas):
# se crea una variable en la cual se almacena una figura
    fig = gr.Figure()
# se indica dentro del for los elementos a tomar para graficar en base a la tabla de comuna
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
# indicamos de que tabla se obtendran los datos a graficar
    colecion = db['icovid_R']
# mediante la función list se ordenan los datos a mostrar
    df = pd.DataFrame(list(colecion.find()))
    return df

@st.cache
def grafica_icociv_R(df,regiones):
# se crea una variable en la cual se almacena una figura
    fig = gr.Figure()
# se indica dentro del for los elementos a tomar para graficar en base a la tabla de region
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
# se definen los estilos que tendra la pagina en el fondo asi como en la barra lateral
# haciendo uso de propiedades de html en streamlit
    st.markdown('<style> body {background-color: #C14E61;}', unsafe_allow_html = True)
    st.markdown("""
    <style>.sidebar .sidebar-content { 
            background-image: linear-gradient(#4EC1B8, #070C33);
            color: white;
        }
    </style>""",unsafe_allow_html=True,)
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