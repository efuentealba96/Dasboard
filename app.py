# importamos librerias necesarias 
from pymongo import MongoClient
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np 
import pydeck as pdk
import datetime
import plotly.express as px 
import plotly.graph_objects as gr

cliente = MongoClient("mongodb+srv://simsimi2143:josuexd@cluster0.r0w6h.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = cliente['Proyecto']

# abrimos la imagen
image = Image.open('head.jpg')

# la función markdown se utiliza para ocupar funcionalidades de html y css en streamlit
st.markdown('<style> body {background-color: #449A04;}', unsafe_allow_html = True)
st.markdown("""
<style>.sidebar .sidebar-content { 
        background-image: linear-gradient(#070C33, #070C33);
        color: white;
    }
</style>""",unsafe_allow_html=True,)
# colores para elegir de fondo de la pagina
#33FF8B
#FFCA33

# agregamos una barra latarel que se puede ocultar para alternar entre dos paginas dentro de streamlit
st.sidebar.header('para alternar en nuestras pestañas seleccione aqui')
st.sidebar.title("MENU")
paginaseleccionada = st.sidebar.selectbox('seleccione una pagina', ['pagina 1', 'pagina 2'])
try:
    # indicamos mediante condicionales lo que ocurrira cuando se selecciones las paginas y los cambios que se generaran al hacerlo
    if paginaseleccionada == 'pagina 1':
        st.header('Bienvenidos a nuestro sitio')
        # se inserta una imagne antes del titulo con los pixeles origanel que posee esta
        st.image(image, use_column_width=True)
        st.title('MONITOREO NACIONAL')
        # agregamos un multi-selecionador con el fin de que al momento de hacer consultas del servidor de mongo se puedan seleccionar varias
        # opciones al mismo tiempo
        Regiones = st.multiselect('selecione una opción', options=['I región', 'II región', 'III región',
                                  'IV región', 'V región', 'VI región', 'VII región', 'VIII región',
                                  'IX región','X región', 'XI región', 'XII región', 'XIII región',
                                  'XIV región','XV región'])
        I_lati = -20.2167
        I_longi = -70.15

        II_lati = -23.5000000
        II_longi = -69.0000000

        III_lati = -22.9167
        III_longi = -68.2

        IV_lati = -29.95332
        IV_longi = -71.33947

        V_lati = -33.05
        V_longi = -71.6167

        VI_lati = -48.4862300
        VI_longi = -72.9105900

        VII_lati = -35.5000000
        VII_longi = -71.5000000

        VIII_lati = -37.0000000
        VIII_longi = -72.5000000

        IX_lati = -36.8907600
        IX_longi = -72.0219600

        X_lati = -41.7500000
        X_longi = -73.0000000

        XI_lati = -46.5000000
        XI_longi = -73.5000000

        XII_lati = -53.1620100
        XII_longi = -70.9010800

        Metropolitana_lati = -33.4726900
        Metropolitana_longi = -70.6472400

        XIV_lati = -40.7702500
        XIV_longi = -73.4174700

        XV_lati = -18.4746000
        XV_longi = -70.2979200

        XVI_lati = -36.8185500
        XVI_longi = -72.5017100
        
        st.button('mostrar monitoreo')
        
        def mapa(lat,lon):
        # creamos un dataframe para dibujar un mapa
            df = pd.DataFrame(
                np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            # especificamos es que tipo de forma vamos a trabajar con las direcciones 
                columns=['lat', 'lon'])
            # usando pydeck dibujamos un mapa segun su estilo y version de esta libreria
        
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
            # inicializamos la la zona del mapa que queremos ver 
            # todo esto en base a latitud y longitud
                initial_view_state=pdk.ViewState(
                    latitude=lat,
                    longitude=lon,
                    zoom=5,
                # indicamos la altura desde la que visualizara el usuario
                    pitch=80,),

                # por debajo del mapa se trabaja con una matriz por ende mediante layer
                # especificamos la seccion de la matriz que se visualizara en el mapa
                    layers=[
                        pdk.Layer(
                    # formato de datos obtenidos de la matriz
                        'HexagonLayer',
                        data=df,get_position='[lon, lat]',
                        radius=200,elevation_scale=8,elevation_range=[0, 10000],
                        pickable=True,extruded=True,
                        ),
                        pdk.Layer('ScatterplotLayer', data=df, get_position='[lon, lat]', 
                        get_color='[180, 0, 200, 140]',
                        get_radius=200,),
                        ],
                ))        
            
            
    elif paginaseleccionada == 'pagina 2':
        # le asignamos un nuevo color a esta siguiente pestaña para añadirle mas estilo a esta
        st.markdown('<style> body {background-color: #DE7D09;} </style>', unsafe_allow_html = True)
        st.title('MONITOREO COMUNAL')
        ocultar = st.sidebar.checkbox('Alternar información')
        mostrar = st.sidebar.checkbox('Mostar grafico de barras')
        def get_data():
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
        df = get_data()
        st.dataframe(df)
        
        
        
           
except:
    st.warning('Realizó una consulta errónea, pruebe nuevamente')