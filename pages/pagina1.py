import streamlit as st
from PIL import Image

# Personalizando el nombre de lengueta
img = Image.open('assets/bola.ico')
st.set_page_config(page_title='Betovoley', page_icon=img, layout='wide', initial_sidebar_state='auto')

# Cuerpo principal
    # Agregar el logo
st.image("assets/logo_sada.png", width=200)

import common.login as login

login.generarLogin()
if 'usuario' in st.session_state:
    st.header('Análise básica por equipe')

