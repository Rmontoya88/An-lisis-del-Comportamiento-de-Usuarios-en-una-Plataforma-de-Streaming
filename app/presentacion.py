import streamlit as st
import os

def mostrar_presentacion():
    st.title("""📚Historia""")
    mostrar_imagen("netflix_empresa.jpg")


def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Función para cargar imágenes desde carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
