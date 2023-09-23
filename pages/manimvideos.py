import streamlit as st
from itertools import combinations, permutations,chain
import os
import time
import copy
import pandas as pd
from threading  import Thread

st.set_page_config(
    page_title='Nudos y Enlaces',
    page_icon=':robot_face:',
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={

        'About': """Autor: Lopez Martinez Sergio Demis

©Todos los derechos reservados 2023."""
    }
)

st.title("Topology Manim Videos")

# Subtítulo
st.header("Selecciona un video de Manim:")

# Lista de videos disponibles
videos = [
"Videos/PAGINA1/Openset.mp4",
"Videos/PAGINA1/Openset2.mp4",
"Videos/PAGINA1/PuntoF.mp4",
"Videos/CirculoACuadrado.mp4",
"Videos/Disco.mp4",
"Videos/Esfera.mp4",
"Videos/Esfera2D.mp4",
"Videos/Esfera2Example2.mp4",
"Videos/Homotopia.mp4" ,
"Videos/ThreeDLightSourcePosition.mp4",
"Videos/TorotoKnot.mp4",
"Videos/Torus_knot.mp4",
"Videos/TorusKnot2Dto3D.mp4"]


st.write(os.listdir('Videos'), os.listdir('Videos/PAGINA1'))

# Widget de selección de video
selected_video = st.selectbox("Selecciona un video:", videos)

# Visualizador de video
video_widget = st.empty()  # Widget para mostrar el video

# Deslizador para cambiar entre los videos
video_index = videos.index(selected_video)
video_index = st.slider("Cambia el video:", 0, len(videos) - 1, video_index)

# Actualizar el video seleccionado
selected_video = videos[video_index]

# Diccionario de videos y sus enlaces


# Mostrar el video seleccionado
video_widget.video(selected_video)
