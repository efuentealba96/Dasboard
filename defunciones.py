from pymongo import MongoClient
import pandas as pd 
import streamlit as st
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

def main():
    st.title("Defunciones durante el año 2020")
    df = get_defunciones()
    if st.checkbox("Mostrar datos graficados"):
        st.dataframe(df)
    st.header('Gráfico por regiones')
    regiones = list(set(df['Region']))
    reg = st.multiselect('Seleccionar regiones',regiones,['La Araucanía','Tarapacá'])
    fig = grafica_defunciones(df, reg)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
