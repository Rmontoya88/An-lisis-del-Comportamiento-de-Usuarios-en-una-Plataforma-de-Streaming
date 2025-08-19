import streamlit as st
import os

def mostrar_intro():

    st.title("""🧠Análisis del Comportamiento de Usuarios en plataforma      
    """)

    mostrar_imagen("presentacion.png")

    st.title("""Agenda    
            """)

    st.markdown("""
                        - 📚Historia
                        - 📊Exploración de la Data
                        - 🧹Proceso de Limpieza
                        - 🔍Análisis Exploratorio (EDA)
                        - 🚀Análisis con Discover
                        - 📝Conclusiones Finales
                        """)




    st.title("Integrantes:")
    st.markdown("👨‍💻 **Roberto Montoya L.**")
    st.markdown("👩‍💻 **Mariel Rodriguez A.**")
    st.markdown("👨‍💻 **Victor Rojas N.**")


def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Función para cargar imágenes desde carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=True, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
