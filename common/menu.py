import streamlit as st
import pandas as pd
import os

def generarMenu(usuario):
    """Genera el menú dependiendo del usuario

    Args:
        usuario (str): usuario utilizado para generar el menú
    """        
    with st.sidebar:
        # Construir la ruta relativa al archivo usuarios.csv desde el archivo login.py
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'usuarios.csv')

        # Convertir a ruta absoluta
        csv_path = os.path.abspath(csv_path)

        # Cargamos la tabla de usuarios
        dfusuarios = pd.read_csv(csv_path)
        # Filtramos la tabla de usuarios
        dfUsuario =dfusuarios[(dfusuarios['usuario']==usuario)]
        # Cargamos el nombre del usuario
        nombre= dfUsuario['nombre'].values[0]
        #Mostramos el nombre del usuario
        st.write(f"Hola **:blue-background[{nombre}]** ")
        # Mostramos los enlaces de páginas
        st.page_link("home.py", label="Home", icon="🏐")
        st.subheader("Análise")
        st.page_link("pages/pagina1.py", label="Análise básica por equipe", icon="🏆")
        st.page_link("pages/pagina2.py", label="Análise avançada de equipe", icon="🥇")
        st.page_link("pages/pagina3.py", label="Análise de jogadores", icon="🤾")
    
        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()