import streamlit as st
from itertools import combinations, permutations,chain
from os import system
import time
import copy
import pandas as pd
from threading  import Thread
from stmol import *
import streamlit_antd_components as sac
from streamlit_extras.switch_page_button import switch_page

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

], format_func='title', open_all=True,index=3)


if men == 'Topología':
    switch_page('topospaces')

if men == 'Pagina Principal':
    switch_page('Main')

if men == 'Definiciones':
    switch_page('knotsdef')


if men == 'Nudos Toroidales':
    switch_page('torusknots')


if men == 'Enlaces':
    switch_page('links')

if men == 'Referencias':
    switch_page('References')

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
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
  mix-blend-mode: darken;
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
  animation: aurora-border 6s ease-in-out infinite,
    aurora-1 12s ease-in-out infinite alternate;
}

.aurora__item:nth-of-type(2) {
  background-color: var(--clr-3);
  right: 0;
  top: 0;
  animation: aurora-border 6s ease-in-out infinite,
    aurora-2 12s ease-in-out infinite alternate;
}

.aurora__item:nth-of-type(3) {
  background-color: var(--clr-2);
  left: 0;
  bottom: 0;
  animation: aurora-border 6s ease-in-out infinite,
    aurora-3 8s ease-in-out infinite alternate;
}

.aurora__item:nth-of-type(4) {
  background-color: var(--clr-4);
  right: 0;
  bottom: -50%;
  animation: aurora-border 6s ease-in-out infinite,
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
# Session


#st.title('Antecedentes Historicos')
st.markdown('''
<div class="content">
  <h1 class="title">Antecedentes Historicos
    <div class="aurora">
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
    </div>
  </h1>

</div>
''',unsafe_allow_html=True)
sac.divider(label='', icon='bank', align='center',key='div2')
'''
Desde tiempos antiguos hasta hoy, los seres humanos han utilizado nudos, trenzas y enlaces en diversas aplicaciones.
Por ejemplo, nuestros ancestros usaron nudos para unir piedras a palos y crear herramientas como hachas.
También trenzaron lianas y pelo de animales para hacer cuerdas que luego usaron en redes de pesca.
Los nudos han sido representados en arte, como manuscritos, esculturas y pinturas, en todo el mundo.
La civilización Inca utilizó un sistema de nudos llamado "quipu" para comunicación escrita y contabilidad.

'''



cols = st.columns(5)
with cols[1]:
    st.image('data:image/jpeg;base64,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')

with cols[3]:
    st.image(caption='sistema de nudos "quipu"',image='data:image/jpeg;base64,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')



'''
A pesar de su uso histórico, el estudio matemático de los nudos es relativamente reciente.
En el siglo XIX, los físicos, incluido Lord Kelvin, consideraron la idea de que los átomos podrían ser vórtices
tubulares de éter anudados. Argumentaron que la estabilidad de la materia, la diversidad de elementos químicos y
las líneas espectrales de los átomos podrían explicarse mediante nudos. En retrospectiva, también podríamos considerar
la capacidad de los átomos para transformarse a altas energías como relacionada con los nudos.

'''

cols1 = st.columns(5)

with cols1[1]:
    st.image(caption='Lord Kelvin',image='data:image/jpeg;base64,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')



with cols1[3]:
    st.image(caption='Atomos de Hidrogeno, Oxigeno y Carbono',image='data:image/png;base64,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')



'''
Durante un período de aproximadamente 20 años, la teoría de Kelvin fue tomada en serio, pero eventualmente fue
descartada. La clasificación de nudos y las "Conjeturas de Tait" surgieron de este estudio. Después de ser
desechada como teoría atómica, el estudio de los nudos se convirtió en una rama esotérica de las matemáticas puras.

'''


cols2 = st.columns(5)

with cols2[1]:
    st.image(caption='Peter Guthrie Tait',image='data:image/jpeg;base64,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')



with cols2[3]:
    st.image(caption='Clasificación de Nudos',image='data:image/png;base64,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')




'''
A pesar de los esfuerzos de los topólogos en el siglo XX, las Conjeturas de Tait resistieron todas las tentativas de
demostración hasta finales de los años 80, cuando se descubrió un nuevo invariante de nudos, conocido como el polinomio
de Jones, que resultó ser lo suficientemente poderoso como para demostrar la mayoría de las conjeturas de manera sencilla.

Un hito importante en la topología moderna fue el descubrimiento en 1928 del polinomio de Alexander para nudos y enlaces.
Aunque no contribuyó a la demostración de las Conjeturas de Tait, fue un invariante de nudos muy útil que simplificó
significativamente la clasificación de los nudos. Durante más de 50 años, el polinomio de Alexander fue el único
invariante de su tipo, por lo que causó sorpresa cuando en 1984, Vaughan Jones descubrió otro invariante polinomial para nudos y enlaces.
'''



cols3 = st.columns(5)

with cols3[1]:
    st.image(caption='James Waddell Alexander II',image='https://mathshistory.st-andrews.ac.uk/Biographies/Alexander/thumbnail.jpg')

with cols3[3]:
    st.image('https://www.researchgate.net/publication/226908765/figure/fig5/AS:669016536408082@1536517380875/6-The-simplest-knots-A-links-B-and-their-Alexander-polynomials-For-unknotted.ppm')





'''
Con el tiempo, la teoría de nudos ha encontrado nuevas aplicaciones en diversas disciplinas, como el estudio de la molécula
de ADN, la química, la biología molecular y la mecánica cuántica, entre otras.
'''



cols4 = st.columns(5)

with cols4[1]:
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/DNA_orbit_animated.gif/200px-DNA_orbit_animated.gif')




with cols4[3]:
    st.image('https://qph.cf2.quoracdn.net/main-qimg-704c8f6aef588f18512134433a7cbb6b')



pdb_ids =[
    "1A3N",  # Hemoglobin
    "1BNA",  # DNA Double Helix
    "1GFL",  # Green Fluorescent Protein
    "1ZEH",  # Insulin
    "4V5D",  # Ribosome
    "4AKE",  # Adenylate Kinase
    "2VIS",  # Vitamin B12 Transporter
    "3HFM",  # HIV-1 Protease
    "6DDE",  # CRISPR-Cas9 DNA Complex
    "2DRE"   # DNA Recombinase
]
mole = st.selectbox('Seleccione la estructura biológica: ',pdb_ids)

showmol(render_pdb(id = mole),700,700)


pdb_dict = {
    "1A3N": "Hemoglobina - Proteína que transporta el oxígeno en los glóbulos rojos.",
    "1BNA": "Doble hélice de ADN - La estructura icónica del ADN.",
    "1GFL": "Proteína de Fluorescencia Verde (GFP) - Usada como marcador en biología molecular debido a su fluorescencia natural.",
    "1ZEH": "Insulina - Hormona que regula los niveles de azúcar en la sangre.",
    "4V5D": "Ribosoma - La estructura celular responsable de la síntesis de proteínas en todos los organismos.",
    "4AKE": "Adenylate Kinase - Una enzima que participa en la transferencia de energía en las células.",
    "2VIS": "Transportador de Vitamina B12 - Proteína involucrada en el transporte de vitamina B12.",
    "3HFM": "Proteasa del VIH-1 - Enzima crucial para la replicación del VIH.",
    "6DDE": "Complejo CRISPR-Cas9 DNA - Componente esencial del sistema de edición genética CRISPR-Cas9.",
    "2DRE": "Recombinasa de ADN - Enzima que facilita la recombinación del ADN en procesos genéticos."
}

dataa = pdb_dict[mole]

st.info(dataa)



