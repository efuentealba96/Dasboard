import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard de Monitoreo de Covid-19 en Chile")

Defunciones_URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/RegistroCivil/Nacimientos/Nacimientos_2020-01-01_2020-11-11_DO.csv"

st.subheader("Defunciones en Chile")

def CargarDatos():
    datos = pd.read_csv(Defunciones_URL)
    st.write(datos)
    st.subheader("Grafica de Defunciones")
    st.line_chart(datos)

print(CargarDatos())

st.subheader("Mapa")
st.map()