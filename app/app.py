import streamlit as st
import sys
import os
from PIL import Image
import base64
import pandas as pd
from Intro import mostrar_intro
from presentacion import mostrar_presentacion
from Limpieza import mostrar_limpieza
from eda import mostrar_eda
from conclusiones import mostrar_conclusiones
from discover import mostrar_discover

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

st.set_page_config(
    page_title="Análisis del Comportamiento de Usuarios en plataforma de Streaming",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ruta para la imagen
logo_path = "C:/Users/rmont/Downloads/Proyecto final Exploracion/web/app/imagenes/netflix_logo.png"

# Mostrar la imagen del logo en el sidebar
def display_logo(logo_path):
    image = Image.open(logo_path)
    return image

# Estilo personalizado
st.markdown("""
    <style>
        /* OCULTAR HEADER Y FOOTER */
        #MainMenu {visibility: hidden;}
        footer {visibility: none;}
        header {visibility: hidden;}

        /* General background and text */
        body, .main, .block-container {
            background-color: #141414;
            color: #ffffff;
            font-family: 'Open Sans', sans-serif;
        }
        .main > div {
            padding-bottom: 0 !important;
            margin-bottom: 0 !important;
        }

        /* Fuente externa de Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

        /* Header personalizado*/
        .header {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1rem;
            border-bottom: 1px solid #333;
        }

        .header h1 {
            font-size: 2rem;
            color: #ffffff;
            margin: 0;
            font-weight: 700;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: black;
            color: white;
        }

        /* Radio buttons */
        .stRadio label {
            font-weight: 600;
            color: #ffffff !important;
        }

        /* Selected option */
        div[role="radiogroup"] > label[data-selected="true"] {
            background-color: #e50914;
            border-radius: 5px;
            color: white !important;
        }

        /* Markdown links */
        a {
            color: #e50914;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Buttons */
        .stButton>button {
            background-color: #e50914;
            color: white;
            font-weight: bold;
            border-radius: 4px;
            padding: 0.5em 1em;
        }

        .stButton>button:hover {
            background-color: #f40612;
        }

        /* Center images */
        .stImage > div {
            text-align: center;
        }

        img {
            max-width: 200px;
            height: auto;
            border-radius: 8px;
        }

        /* Estilos para st.title y h1 */
        h1, .stApp h1 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 700 !important;
            font-size: 3rem !important;
            color: #e50914 !important;
            text-shadow: 1px 1px 2px black;
            margin-bottom: 0.5rem !important;
        }

        /* Estilos para st.header y h2 */
        h2 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
            font-size: 2rem !important;
            color: #f40612 !important;
            margin-top: 1rem !important;
            margin-bottom: 0.5rem !important;
        }

        /* Texto general */
        p, span, div, h3, h4 {
            color: #ffffff;
            font-family: 'Open Sans', sans-serif !important;
            font-size: 1rem !important;
            line-height: 1.5rem !important;
        }

        .block-container img {
            max-width: 600px;
            height: auto;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    logo = display_logo(logo_path)
    if logo:
        st.image(logo, use_container_width=True)

    st.markdown("### **Opciones del Proyecto**", unsafe_allow_html=True)
    selected_option = st.radio(
        "Selecciona una opción:",
        ["Presentación", "Historia", "Dataset y limpieza", "EDA", "Análisis con Discover", "Conclusión", "Repositorio GIT"]
    )

# Contenido según opción seleccionada

col1, col2 = st.columns([3,0.5])

if selected_option == "Presentación":
    with col1:
        mostrar_intro()
    with col2:
        st.write("")

elif selected_option == "Historia":

    with col1:
        mostrar_presentacion()
    with col2:
        pass

elif selected_option == "Dataset y limpieza":
    with col1:
        mostrar_limpieza()
    with col2:
        st.write("")

elif selected_option == "EDA":
    with col1:
        mostrar_eda()
    with col2:
        st.write("")

elif selected_option == "Análisis con Discover":
     mostrar_discover()


elif selected_option == "Conclusión":
    with col1:
        mostrar_conclusiones()
    with col2:
        st.write("")

elif selected_option == "Repositorio GIT":
    with col1:
        st.title("""
            [Ir al Repositorio en GitHub](https://github.com/Rmontoya88/Optimizacion-y-Prediccion-de-Demanda-del-Transporte-Publico/tree/main)
        """)



else:
    st.markdown("Error", unsafe_allow_html=True)


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"


def mostrar_imagen(ruta, ancho=800):
    imagen = Image.open(ruta)
    st.image(imagen, use_column_width=False, width=ancho)

