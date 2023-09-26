import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
import time
from st_click_detector import click_detector
import streamlit_antd_components as sac
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
st.markdown('''
<style>
.css-79elbk {
  position: unset;
  display: none;
}

.css-j463ke {
  position: fixed;
  top: 0px;
  left: 0px;
  right: 0px;
  height: 2.875rem;
  background: rgba(255, 231, 231, 0);
  outline: none;
  z-index: 999990;
  display: block;
}
</style>
''',unsafe_allow_html=True)


with st.sidebar:
  men = sac.menu([

    sac.MenuItem('Pagina Principal', icon='house',),

    sac.MenuItem('Topología', icon='egg-fried'),

    sac.MenuItem('Nudos y Enlaces', icon='command', tag=sac.Tag('Inicio',color='',bordered=False), children=[
        sac.MenuItem('Historia', icon='bank'),
        sac.MenuItem('Nudos', icon='flower1', children=[

            sac.MenuItem('Definiciones', icon='gear-wide-connected'),

            sac.MenuItem('Nudos Toroidales', icon='life-preserver'),
            ],
            ),
        sac.MenuItem('Enlaces', icon='link'),
        sac.MenuItem('Problemas', icon='puzzle'),
    ]),

    sac.MenuItem('Invariantes', icon='infinity'),

    sac.MenuItem('Trenzas', icon='bezier2'),

    sac.MenuItem(type='divider'),

    sac.MenuItem('Acerca de', type='group',icon='info-circle', children=[
        sac.MenuItem('Referencias', icon='card-heading'),
        sac.MenuItem('Github', icon='github', href='https://github.com/SergioSKA27'),
        sac.MenuItem('Streamlit', icon='cpu', href='https://streamlit.io/'),
        sac.MenuItem('Autor: Lopez Martinez Sergio Demis', icon='person-circle',disabled=True),

    ]),

], format_func='title', open_all=True)


if men == 'Topología':
    switch_page('topospaces')

if men == 'Historia':
    switch_page('history')

if men == 'Definiciones':
    switch_page('knotsdef')

if men == 'Nudos Toroidales':
    switch_page('torusknots')

if men == 'Enlaces':
    switch_page('links')

if men == 'Problemas':
    switch_page('Problems')

if men == 'Invariantes':
    switch_page('Invariants')

if men == 'Trenzas':
    switch_page('braids')

if men == 'Referencias':
    switch_page('References')



page_bg_img = '''
<style>
.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 5;
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
            z-index: 5;
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
  color: #1D1A1A;
  border-right: 4px solid #000;
  animation: cursor 1s infinite step-end, typing 15s infinite steps(16);
  white-space: nowrap;
  overflow: hidden;
  font-family: "Inter";
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
  color: #1D1A1A;
  border-right: 4px solid #000;
  animation: cursor 1s infinite step-end, typing 15s infinite steps(16);
  white-space: nowrap;
  overflow: hidden;
  font-family: "Inter";
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
  color: #1D1A1A;
  border-right: 4px solid #000;
  animation: cursor 1s infinite step-end, typing 15s infinite steps(16);
  white-space: nowrap;
  overflow: hidden;
  font-family: "Inter";
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




st.markdown(r'''
<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;800&display=swap");

:root {
  --bg: #FFFFFF;
  --clr-1: #00c2ff;
  --clr-2: #33ff8c;
  --clr-3: #ffc640;
  --clr-4: #e54cff;

  --blur: 1rem;
  --fs: clamp(3rem, 8vw, 7rem);
  --ls: clamp(-1.75px, -0.25vw, -3.5px);
}

body {
  min-height: 100vh;
  display: grid;
  place-items: center;
  background-color: var(--bg);
  color: #fff;
  font-family: "Inter", "DM Sans", Arial, sans-serif;
}

*,
*::before,
*::after {
  font-family: inherit;
  box-sizing: border-box;
}

.content {
  text-align: center;
}

.title {
  font-size: var(--fs);
  font-weight: 800;
  letter-spacing: var(--ls);
  position: relative;
  overflow: hidden;
  background: var(--bg);
  margin: 0;
}

.subtitle {
}

.aurora {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
  mix-blend-mode: difference;
  pointer-events: none;
}

.aurora__item {
  overflow: hidden;
  position: absolute;
  width: 60vw;
  height: 60vw;
  background-color: var(--clr-1);
  border-radius: 37% 29% 27% 27% / 28% 25% 41% 37%;
  filter: blur(var(--blur));
  mix-blend-mode: overlay;
}

.aurora__item:nth-of-type(1) {
  top: -50%;
  animation: aurora-border 20s ease-in-out infinite,
    aurora-1 12s ease-in-out infinite alternate;
}

.aurora__item:nth-of-type(2) {
  background-color: var(--clr-3);
  right: 0;
  top: 0;
  animation: aurora-border 20s ease-in-out infinite,
    aurora-2 12s ease-in-out infinite alternate;
}

.aurora__item:nth-of-type(3) {
  background-color: var(--clr-2);
  left: 0;
  bottom: 0;
  animation: aurora-border 20s ease-in-out infinite,
    aurora-3 8s ease-in-out infinite alternate;
}

.aurora__item:nth-of-type(4) {
  background-color: var(--clr-4);
  right: 0;
  bottom: -50%;
  animation: aurora-border 19s ease-in-out infinite,
    aurora-4 24s ease-in-out infinite alternate;
}

@keyframes aurora-1 {
  0% {
    top: 0;
    right: 0;
  }

  50% {
    top: 100%;
    right: 75%;
  }

  75% {
    top: 100%;
    right: 25%;
  }

  100% {
    top: 0;
    right: 0;
  }
}

@keyframes aurora-2 {
  0% {
    top: -50%;
    left: 0%;
  }

  60% {
    top: 100%;
    left: 75%;
  }

  85% {
    top: 100%;
    left: 25%;
  }

  100% {
    top: -50%;
    left: 0%;
  }
}

@keyframes aurora-3 {
  0% {
    bottom: 0;
    left: 0;
  }

  40% {
    bottom: 100%;
    left: 75%;
  }

  65% {
    bottom: 40%;
    left: 50%;
  }

  100% {
    bottom: 0;
    left: 0;
  }
}

@keyframes aurora-4 {
  0% {
    bottom: -50%;
    right: 0;
  }

  50% {
    bottom: 0%;
    right: 40%;
  }

  90% {
    bottom: 50%;
    right: 25%;
  }

  100% {
    bottom: -50%;
    right: 0;
  }
}

@keyframes aurora-border {
  0% {
    border-radius: 37% 29% 27% 27% / 28% 25% 41% 37%;
  }

  25% {
    border-radius: 47% 29% 39% 49% / 61% 19% 66% 26%;
  }

  50% {
    border-radius: 57% 23% 47% 72% / 63% 17% 66% 33%;
  }

  75% {
    border-radius: 28% 49% 29% 100% / 93% 20% 64% 25%;
  }

  100% {
    border-radius: 37% 29% 27% 27% / 28% 25% 41% 37%;
  }
}



 h2 {
  font-size: 28px;
  font-weight: 500;
  letter-spacing: 0;
  line-height: 1.5em;
  padding-bottom: 15px;
  position: relative;
}
 h2:before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 5px;
  width: 55px;
  background-color: #111;
}
 h2:after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 2px;
  height: 1px;
  width: 95%;
  max-width: 255px;
  background-color: #333;
}


 .s h1 {
  font-size:50px;text-align:center; line-height:1.5em; padding-bottom:45px; font-family:"Playfair Display", serif; text-transform:uppercase;letter-spacing: 2px; color:#111;
}


 .s h1:before {
  position: absolute;
  left: 0;
  bottom: 35px;
  width: 60%;
  left:50%; margin-left:-30%;
  height: 1px;
  content: "";
  background-color: #777; z-index: 4;
}
 .s h1:after {
  position:absolute;
  width:40px; height:40px; left:50%; margin-left:-20px; bottom:0px;
  content: '\00a7'; font-size:30px; line-height:40px; color:#c50000;
  font-weight:400; z-index: 5;
  display:block;
  background-color:#f8f8f8;
}


.twelve h1 {
  font-size:26px; font-weight:700;  letter-spacing:1px; text-transform:uppercase; width:160px; text-align:center; margin:auto; white-space:nowrap; padding-bottom:13px;
}
.twelve h1:before {
    background-color: #c50000;
    content: '';
    display: block;
    height: 3px;
    width: 75px;
    margin-bottom: 5px;
}
.twelve h1:after {
    background-color: #c50000;
    content: '';
    display: block;
  position:absolute; right:0; bottom:0;
    height: 3px;
    width: 75px;
    margin-bottom: 0.25em;
}



.thirteen h1 {
  position:relative; font-size:20px; font-weight:700;  letter-spacing:0px; text-transform:uppercase; width:150px; text-align:center; margin:auto; white-space:nowrap; border:2px solid #222;padding:5px 11px 3px 11px;
}
.thirteen h1:before, .thirteen h1:after {
    background-color: #c50000;
    position:absolute;
    content: '';
    height: 7px;

    width: 7px; border-radius:50%;
    bottom: 12px;
}
.thirteen h1:before {
   left:-20px;
}
.thirteen h1:after {
   right:-20px;
}
</style>
''',unsafe_allow_html=True)


st.markdown('''
<div class="content">
  <div class="aurora">
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
  </div>
</div>
''',unsafe_allow_html=True)




st_lottie("https://lottie.host/4f56c993-fd92-42e4-9945-c5df0387f986/mTRLkrdQVJ.json",quality="high",key='knot')





