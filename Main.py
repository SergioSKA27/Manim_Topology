import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
import time
# Título de la aplicación
st.set_page_config(
    page_title='Nudos y Enlaces',
    page_icon=':robot_face:',
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={

        'About': """Autor: Lopez Martinez Sergio Demis

©Todos los derechos reservados 2023."""
    }
)

page_bg_img = '''
<style>
.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  font-size: 100px;
}
.centered-text {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(255, 255, 255, 0);
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            z-index: 2;
        }
header {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}

header h1 {
  font-size: 100px;
  min-width: 50%;
  max-width: 100%;
  font-weight: 500;
  color: #553c9a;
  border-right: 4px solid #000;
  animation: cursor 1s infinite step-end, typing 15s infinite steps(16);
  white-space: nowrap;
  overflow: hidden;
  font-family: Courier New;
  overflow: hidden;
  text-shadow:
    1px 1px 1px blue,
    2px 2px 1px blue;
}
@keyframes cursor{
  0%, 100%{border-color: transparent;}
  50%{border-color: #000;}
}

@keyframes typing{
  0%{ width: 0ch} /*Text is hidden*/
  30%{ width: 16ch;} /*The enitre header will be typed out*/
  80%{ width: 16ch;} /*Text stays visible*/
  90%{ width: 0ch;} /*Text is deleted*/
  100%{ width: 0ch;} /*Text stays hidden*/
}

/* For Mobile Portrait View */
@media screen and (max-device-width: 480px)
    and (orientation: portrait) {
    header h1 {
  font-size: 40px;
  min-width: 50%;
  max-width: 100%;
  font-weight: 500;
  color: #553c9a;
  border-right: 4px solid #000;
  animation: cursor 1s infinite step-end, typing 15s infinite steps(16);
  white-space: nowrap;
  overflow: hidden;
  font-family: Courier New;
  overflow: hidden;
  text-shadow:
    1px 1px 1px blue,
    2px 2px 1px blue;
   }
}
/* For Mobile Landscape View */
@media screen and (max-device-width: 640px)
    and (orientation: landscape) {
    header h1 {
   font-size: 40px;
  min-width: 50%;
  max-width: 100%;
  font-weight: 500;
  color: #553c9a;
  border-right: 4px solid #000;
  animation: cursor 1s infinite step-end, typing 15s infinite steps(16);
  white-space: nowrap;
  overflow: hidden;
  font-family: Courier New.;
  overflow: hidden;
  text-shadow:
    1px 1px 1px blue,
    2px 2px 1px blue;
   }
}

</style>


<div class="centered-text">
   <header>
        <h1>Nudos y Enlaces</h1>
    </header>
</div>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st_lottie("https://lottie.host/4f56c993-fd92-42e4-9945-c5df0387f986/mTRLkrdQVJ.json",quality="high",key='knot')





