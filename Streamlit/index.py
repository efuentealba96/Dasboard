import streamlit as st 

import defunciones
import icovid
import comunas
import mapa

st.sidebar.title('Navegación')
opt = st.sidebar.radio("",
    ["Defunciones Registro Civil","Datos ICOVID","Datos por Comuna","Mapa 3D interactivo"]
)

if opt == "Defunciones Registro Civil":
    defunciones.main()

if opt == "Datos ICOVID":
    icovid.main()

if opt == "Datos por Comuna":
    comunas.main()

if opt == "Mapa 3D interactivo":
    mapa.main()