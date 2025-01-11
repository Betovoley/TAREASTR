import streamlit as st
from PIL import Image

# Personalizando el nombre de lengueta
img = Image.open('assets/bola.ico')
st.set_page_config(page_title='Betovoley', page_icon=img, layout='wide', initial_sidebar_state='auto')

# Importar después de configurar la página
import common.login as login

# st.header('Página principal')
login.generarLogin()

def main():
    st.title("Bem-vindo a Betovoley-Sada Cruzeiro Stats")

    # Header con color verde HEX #116F4B
    st.markdown(
        """
        <h1 style="color: #116F4B;">Site dedicado ao trabalho estatístico e de análise do clube SADA CRUZEIRO VOLEI</h1>
        """, 
        unsafe_allow_html=True
    )

    # Texto enmarcado
    st.markdown("""
    <div style="border: 1px solid black; padding: 10px; border-radius: 5px;">
        <p style="font-size: 24px;">Neste site você encontrará estatísticas básicas de desempenho para todos os fundamentos da nossa equipe, por jogador e por torneio.
        Você também encontrará estatísticas avançadas com métricas criadas internamente para avaliar o desempenho coletivo e individual.</p>
    </div>
    """, unsafe_allow_html=True)

    # Cuerpo principal
    # Agregar el logo
    st.image("assets/logo_sada.png", width=200)

    # Imagen en la barra lateral
    HORIZONTAL_RED = "assets/medalla.png"
    ICON_BLUE = "assets/logo_sada.png"

    # Mostrar el logo en el sidebar
    st.sidebar.image(HORIZONTAL_RED, use_container_width=False, width=100)

    # Footer
    st.markdown(
        """
        <footer style="background-color: #2C3E3F; color: white; padding: 10px; text-align: center; position: fixed; left: 0; bottom: 0; width: 100%; font-size: 14px; margin-top: 20px;">
            © 2024 Sada Cruzeiro Vôlei. Todos os direitos reservados.
            Site criado por Betovoley
            <br>
            <a href="https://www.sadacruzeiro.com.br" target="_blank" style="color: white;">Visite nosso site</a>
        </footer>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

