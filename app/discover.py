import streamlit as st
import os

def mostrar_discover():
    opciones = {
        "📊 EDA": ("eda_dataset.png", "Análisis Exploratorio de Datos (EDA)"),
        "🎬 Títulos por Tipo": ("titulo_tipo.png", "Cantidad de Títulos por Contenido"),
        "🏷️ Clasificación": ("titulos_clasificacion.png", "Cantidad de Títulos por Clasificación"),
        "📅 Por Año": ("titulos_anio.png", "Contenidos lanzados por Año"),
        "🎥 Directores": ("top_directores.png", "Top 10 directores más frecuentes"),
        "🌍 Países": ("paises_titulos.png", "Países con más Títulos"),
        "📈 Evolución": ("estrenos_anio.png", "Movimiento lineal de Títulos en el Tiempo"),
        "🌐 Tipo por País": ("contenido_pais.png", "Tipo de Contenido por País"),
        "⏳ Duración": ("duracion_contenido.png", "Duración por tipo de Contenido"),
        "🎭 Géneros": ("contenido_genero.png", "Distribución de Géneros por Tipo de Contenido"),
    }

    # Selector horizontal
    seleccion = st.radio("Selecciona gráfico:", list(opciones.keys()), horizontal=True)

    archivo, titulo = opciones[seleccion]
    st.title(titulo)
    mostrar_imagen(archivo)

def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=False, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
