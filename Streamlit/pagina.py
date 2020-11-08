import streamlit as st
import pandas as pd

st.title("Dashboard de Monitoreo de Covid-19 en Chile")

Nacimientos_URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/RegistroCivil/Nacimientos/Nacimientos_2020-01-01_2020-11-04_DO.csv"

st.subheader("Nacimientos en Chile")

def CargarDatos():
    datos = pd.read_csv(Nacimientos_URL)
    st.write(datos)
    st.subheader("Grafica de Nacimientos")
    st.line_chart(datos)

datos = CargarDatos()

st.subheader("Mapa")
st.map(datos)