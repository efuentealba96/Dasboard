# importamos librerias necesarias 
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np 
import pydeck as pdk

# abrimos la imagen
image = Image.open('/home/franco-os/Imágenes/head.jpg')

# la función markdown se utiliza para ocupar funcionalidades de html y css en streamlit
st.markdown('<style> body {background-color: #449A04;}', unsafe_allow_html = True)
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
        st.button('mostrar monitoreo')
   
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
                latitude=-30.0000000,
                longitude=-71.0000000,
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
        columna1, columna2, columna3 = st.beta_columns(3)

        with columna1:
            st.write(pd.DataFrame({
                "1ra_Región": ['Iquique','Alto hospicio','Pozo almonte','Camiña',
                               'Colchane','Huara','Pica']
            }))      
        
        with columna2:
            st.write(pd.DataFrame({
               "2da_Región": ['Antofagasta','Mejillones','Sierra gorda','Taital',
                           'Calama','Ollagüe','San pedro de atacama','Tocopilla','María elena']
            }))

        with columna3:
            st.write(pd.DataFrame({
                "3ra_Región": ['Copiapó','Caldera','Tierra amarilla','Chañaral',
                               'Diego de almagro','Vallenar','Alto del carmen','Freirina','Huasco']
            }))

        with columna1:
            st.write(pd.DataFrame({
                "4ta_Región": ['La serena','Coquimbo','Andacollo','La higuera','Paihuano','Vicuña',
                               'Illapel','Canela','Los vilos','Salamanca','Ovalle','Combartala',
                               'Monte patria','Punitaqui','Río hurtado']
            }))

        with columna2:
            st.write(pd.DataFrame({
                "5ta_Región": ['Valparaiso','Casablanca','Concón','Juan fernández','Puchuncavi',
                               'Quintero','Viña del mar','Isla de pascua','Los andes','Calle larga',
                               'Rinconada','San esteban','La ligua','Cabildo','Papudo','Petorca',
                               'Zapallar','Quillota','La calera','Hijuelas','La cruz','Nogales',
                               'San antonio','Algarrobo','Cartagena','El quisco','El tabo','Santo domingo',
                               'San felipe','Catemu','Llay-Llay','Panquehue','Putaendo','Santa maría',
                               'Quilpue','Limache','Olmue','Villa alemana']
        }))

        with columna3:
            st.write(pd.DataFrame({
                "6ta_Región": ['Rancagua','Cogua','Coinco','Coltauco','Doñihue','Graneros',
                               'Las cabras','Machali','Malloa','Mostazal','Olivar','Peumo','Pichidegua',
                               'Quinta tilcoco','Rengo','Requinoa','San vicente','Pichilemu','La estrella',
                               'Litueche','Marchihue','Navidad','Paredones','San fernando','Chépica',
                               'Chimbarongo','Lolol','Nancagua','Palmilla','Peralillo','Plascilla','pumanque',
                               'Santa cruz']
        }))

        with columna1:
            st.write(pd.DataFrame({
                "7ma_Región": ['Talca','Constitución','Curepto','EMpedrado','Maule','Pelarco','Pencahue',
                               'Rio claro','San clemente','San rafael','Cauquenes','Chanco','Pelluhue',
                               'Curicó','Hualañé','Licanten','Molina','Rauco','Romeral','Sagrada familia',
                               'Teno','Vichuquén','Linares','Colbún','Longavi','Parral','Retiro','San javier',
                               'Villa alegre','Yerbas buenas']
        }))

        with columna2:
            st.write(pd.DataFrame({
                "8va_Región": ['Concepción','Coronel','chiguayante','Florida','Hualqui',
                               'Lota','Penco','San pedro de la paz','Santa juana','Talcahuano','Tomé',
                               'Hualpen','Lebu','Arauco','Cañete','Contulmo','Curanilahue','Los alamos',
                               'Tirúa','Los ángeles','Antuco','Cabrero','Laja','Mulchén','Nacimiento',
                               'Negrete','Quilaco','Quilleco','San rosendo','Santa bárbara','Tucapel',
                               'Yumbel','Alto biobio']
        }))

        with columna3:
            st.write(pd.DataFrame({
                "9na_Región": ['Temuco','Carahue','Chol Chol','Cunco','Curarrehue','Freire',
                               'Galvarino','Gorbea','Lautaro','Loncoche','Melipeuco','Nueva Imperial',
                               'Padre Las Casas','Perquenco','Pitrufquén','Pucón','Saavedra','Teodoro Schmidt',
                               'Toltén','Vilcún', 'Villarrica']
        }))

        with columna1:
            st.write(pd.DataFrame({
                "10ma_Región":  ['Puerto montt','Calbuco','Cochamó','Fresia','Frutillar','Los muermos',
                                 'Llanquihue','Maullin','puerto varas','Castro','Ancud','Curaco de vélez',
                                 'Dalcahue','Puqueldón','Queillen','Quellon','Quemchi','Quinchao','Puerto octay',
                                 'Purranque','Peyehue','Río negro','San juan de la costa','San pablo','Chaitén',
                                 'Futaleufu','Hualaihue','Palena']
        }))

        with columna2:
            st.write(pd.DataFrame({
                "11ma_Región": ['Coyaique','Lago verde','Aysén','Cisnes','Guatitecas','COnchrane',
                                "O'higgins",'Tortel','Chile chico','Río ibáñez']
        }))

        with columna3:
            st.write(pd.DataFrame({
                "12ma_Región": ['Punta arenas','Laguna blanca','Río verde','San gregorio','Cabo de hornos',
                                'Artartica','Porvenir','Primavera','Timaukel','Natales','Torres del paine']
        }))

        with columna1:
            st.write(pd.DataFrame({
                "Región_Metropolitana": ['Colina', 'Lampa','Til-Til', 'Puente Alto', 'Pirque', 'San José de Maipo', 
                                         'San Bernardo', 'Buin', 'Calera de Tango', 'Paine', 'Melipilla', 'Alhué', 
                                         'Curacaví', 'María Pinto', 'San Pedro', 'Santiago', 'Cerrillos', 
                                         'Cerro Navia', 'Conchalí', 'El Bosque', 'Estación Central', 'Huechuraba', 
                                         'Independencia', 'La Cisterna', 'La Florida', 'La Granja', 'La Pintana', 
                                         'La Reina', 'Las Condes', 'Lo Barnechea', 'Lo Espejo', 'Lo Prado', 'Macul', 
                                         'Maipú', 'Ñuñoa', 'Pedro Aguirre Cerda', 'Peñalolen', 'Providencia', 
                                         'Pudahuel', 'Quilicura', 'Quinta Normal', 'Recoleta', 'Renca', 'San Joaquín', 
                                         'San Miguel', 'San Ramón', 'Vitacura', 'Talagante', 'El Monte', 'Isla de Maipo', 
                                         'Padre Hurtado', 'Peñaflor']
        }))

        with columna2:
            st.write(pd.DataFrame({
                "14ta_Región": ['Valdivia','Corral','Lanco','Los lagos','Máfil','Mariquina','Paillaco',
                                'Panguipulli','La union','Futrono','Lago ranco','Río bueno']
        }))

        with columna3:
            st.write(pd.DataFrame({
                "15ta_Región": ['Arica','Camarones','Putre','General lagos']
        }))

        with columna1:
            st.write(pd.DataFrame({
                "16ta_Región": ['Chillán','Buines','Chillán viejo','El carmen','Pemuco','Pinto','Quillon',
                                'San ignacio','Yungay','Quirihue','Cobquecura','Coelemu','Ninhue','Portezuelo',
                                'Ránquil','Treguaco','San carlos','Colihueco','Ñinquén','San fabián',
                                'San nicolás']
        }))
    
except:
    st.warning('Realizó una consulta errónea, pruebe nuevamente')