import streamlit as st


st.sidebar.title("MENU")
paginaseleccionada = st.selectbox('seleccione una pagina', ['pagina 1', 'pagina 2'])

if paginaseleccionada == 'pagina 1':
    st.title('MONITOREO NACIONAL')
    st.selectbox('selecione una opción', ['opción 1', 'opción 2'])
elif paginaseleccionada == 'pagina 2':
    st.title('usted esta en la pagina 2')