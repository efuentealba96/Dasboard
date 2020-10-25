# importamos librerias necesarias 
import streamlit as st
from PIL import Image

# abrimos la imagen
image = Image.open('head.jpg')

# la función markdown se utiliza para ocupar funcionalidades de html y css en streamlit
st.markdown('<style> body {background-color: #33FF8B ;} </style>', unsafe_allow_html = True)
# colores para elejir de fondo de la pagina
#33FF8B
#FFCA33

# agragamos una barra latarel que se puede ocultar para alternar entre dos paginas dentro de streamlit
st.sidebar.header('para alternar en nuestras pesañas seleccione aqui')
st.sidebar.title("MENU")
paginaseleccionada = st.sidebar.selectbox('seleccione una pagina', ['pagina 1', 'pagina 2'])


# indicamos mediante condicionales lo que ocurrira cuando se selecciones las paginas y los cambios que se generaran al hacerlo
if paginaseleccionada == 'pagina 1':
    st.header('Bienvenidos a nuestro sitio')
    st.image(image, use_column_width=True)
    st.title('MONITOREO NACIONAL')
    st.multiselect('selecione una opción', ['I región', 'II región', 'III región',
         'IV región', 'V región', 'VI región', 'VII región', 'VIII región',
         'IX región','X región', 'XI región', 'XII región', 'XIII región',
         'XIV región','XV región'])
    
elif paginaseleccionada == 'pagina 2':
    st.markdown('<style> body {background-color: #FFCA33 ;} </style>', unsafe_allow_html = True)
    st.title('MONITOREO COMUNAL')