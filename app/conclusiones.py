import streamlit as st
import os

def mostrar_conclusiones():

    st.title("""🎯Conclusiones""")

    mostrar_imagen("conclusiones.png")


def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Función para cargar imágenes desde carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
