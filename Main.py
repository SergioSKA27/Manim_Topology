import streamlit as st
from streamlit_lottie import st_lottie
# Título de la aplicación
st.title("Topology Manim Videos")

st_lottie("https://lottie.host/4f56c993-fd92-42e4-9945-c5df0387f986/mTRLkrdQVJ.json")
# Subtítulo
st.header("Selecciona un video de Manim:")

# Lista de videos disponibles
videos = ["Homeomorfismo",
"Discos_D0_D2",
"DiscoD3",
"Esferas_S0_S1",
"EsferaS2",
"EsferaS2Ejemplo2",
"Homotopia",
"Torus_knot",
"TorusKnot2Dto3D"]


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
video_links = {
   'Homeomorfismo':"Videos/CirculoACuadrado.mp4",
"Discos_D0_D2":"Videos/Disco.mp4",
"DiscoD3":"Videos/ThreeDLightSourcePosition.mp4",
"Esferas_S0_S1":"/Videos/Esfera.mp4",
"EsferaS2":"Videos/Esfera2D.mp4",
"EsferaS2Ejemplo2":"Videos/Esfera2Example2.mp4",
"Video":"Videos/Homotopia.mp4",

"Torus_knot":"Videos/Torus_knot.mp4",
"TorusKnot2Dto3D":"Videos/TorusKnot2Dto3D.mp4"}

# Mostrar el video seleccionado
video_widget.video(video_links[selected_video])
