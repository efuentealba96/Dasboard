from pymongo import MongoClient
import pandas as pd 
import streamlit as st
import plotly.express as px     
import plotly.graph_objects as gr


cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = cliente['Proyecto']

# creamos nuestra primera función con la cual mostraremos la grafica de las defunciones
def get_defunciones():
# indicamos la tabla de la cual obtendrmos la información necesaria 
# para poder graficar
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
# función para graficar las defunciones
def grafica_defunciones(df,regiones):
# se crea una variable en la cual se almacena una figura
    fig = gr.Figure()
# se indica dentro del for los elementos a tomar para graficar en base a la tabla de region
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

def main():
# se definen los estilos que tendra la pagina en el fondo asi como en la barra lateral
# haciendo uso de propiedades de html en streamlit
    st.title("Defunciones durante el año 2020")
    st.markdown('<style> body {background-color: #449A04;}', unsafe_allow_html = True)
    st.markdown("""
    <style>.sidebar .sidebar-content { 
            background-image: linear-gradient(#4EC1B8, #070C33);
            color: white;
        }
    </style>""",unsafe_allow_html=True,)
    df = get_defunciones()
# se indica que dada la condición se ejecute la acción de mostrar los graficos
    if st.checkbox("Mostrar datos graficados"):
        st.dataframe(df)
    st.header('Gráfico por regiones')
    regiones = list(set(df['Region']))
    reg = st.multiselect('Seleccionar regiones',regiones,['La Araucanía','Tarapacá'])
    fig = grafica_defunciones(df, reg)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
