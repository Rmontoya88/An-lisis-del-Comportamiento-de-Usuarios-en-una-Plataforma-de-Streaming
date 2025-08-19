import streamlit as st
import os

def mostrar_limpieza():
    pasos_limpieza = {
        "1️⃣ Conocer el Dataset": ("dataset.png", ""),
        "2️⃣ Explorar Tipos de Datos (Summary)": ("conocer_data.png", ""),
        "3️⃣ Explorar Tipos de Datos (Str)": ("conocer_data1.png", ""),
        "4️⃣ Valores Nulos y Duplicados": ("nulos.png", ""),
        "5️⃣ Revisar Rango de Fechas": ("fechas.png", "Se filtra el dataset a rangos de fecha del 2020 al 2021"),
        "6️⃣ Revisión de Valores en Blanco": ("valores_blanco.png", ""),
        "7️⃣ Reemplazar Valores Vacíos": ("valores_blanco1.png", ""),
        "8️⃣ Eliminar Columnas Innecesarias": ("valores_blanco_data.png",
                                               "- Se eliminan las columnas: Show ID y Description."),
        "9️⃣ Renombrar Columnas": ("renombrar.png", ""),
        "🔟 Separar y Limpiar Datos (Reparto, Director, País, Listado)": ("separados.png", ""),
        "1️⃣1️⃣ Transformar Columna de Fecha": ("fecha_transform.png", ""),
        "1️⃣2️⃣ Guardar Dataset Limpio": ("data_export.png", "")
    }

    # Estilo visual
    st.markdown("### 📌 Selecciona el paso que quieres visualizar:")
    st.markdown("""
    <style>
    div[data-baseweb="radio"] {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }
    label[data-testid="stMarkdownContainer"] {
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

    # Selector vertical
    seleccion = st.radio("", list(pasos_limpieza.keys()))

    # Mostrar contenido
    archivo, subtitulo = pasos_limpieza[seleccion]
    st.header(seleccion)
    mostrar_imagen(archivo, subtitulo=subtitulo)


def mostrar_imagen(nombre_archivo, subtitulo=""):
    """Carga una imagen desde la carpeta 'imagenes'"""
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", nombre_archivo)
    if os.path.exists(ruta):
        st.image(ruta, use_container_width=False, caption=subtitulo)
    else:
        st.warning(f"No se encontró la imagen: {nombre_archivo}")
