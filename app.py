import streamlit as st 

import defunciones
import icovid
import comunas
import mapa

st.sidebar.title('Navegación')
opt = st.sidebar.radio("",
    ["Defunciones Registro Civil","Datos ICOVID","Datos por Comuna","Mapa 3D interactivo"]
)
# dentro de esta zona se hace el llamado de los diferentes archivos .py con el fin de optimizar el codigo
# y la velocidad de  carga de los archivos que estos poseen indicando la opción y la función main a ejecutar
if opt == "Defunciones Registro Civil":
    defunciones.main()

if opt == "Datos ICOVID":
    icovid.main()

if opt == "Datos por Comuna":
    comunas.main()

if opt == "Mapa 3D interactivo":
    mapa.main()