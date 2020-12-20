from pymongo import MongoClient
import pandas as pd 
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as gr

cliente = MongoClient("mongodb+srv://Eliacer:elia968@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = cliente['Proyecto']

# Creamos una funcion para obtener las comunas del país por 1000 habitantes
def get_CComunas():
    colecion = db['C_Comunas']
    df = pd.DataFrame(list(colecion.find()))
    df['Casos x 1000'] = 1000*df['Casos confirmados']/df['Poblacion']
    del df['_id']
    del df['Codigo region']
    del df['Codigo comuna']
    return df


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

def main():
    op = st.sidebar.checkbox('Numero de casos por cada 1000 habitantes',value=False)
    st.title("Datos por comuna")
    df = get_CComunas()
    if st.checkbox("Mostrar datos graficados"):
        st.dataframe(df)
    st.header('Gráfico por comunas')
    comunas = list(set(df["Comuna"]))
    com = st.multiselect("Selecionar comunas",comunas,['Talcahuano','La Serena'])
    fig = grafica_CComunas(df,com,op)
    st.plotly_chart(fig,use_container_width=True)


if __name__ == "__main__":
    main()