import streamlit as st
from itertools import combinations, permutations,chain
from os import system
import time
import copy
import pandas as pd
from threading  import Thread
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

], format_func='title', open_all=True,index=10)


if men == 'Topología':
    switch_page('topospaces')

if men == 'Historia':
    switch_page('history')

if men == 'Definiciones':
    switch_page('knotsdef')

if men == 'Pagina Principal':
    switch_page('Main')

if men == 'Nudos Toroidales':
    switch_page('torusknots')

if men == 'Referencias':
    switch_page('References')

if men == 'Enlaces':
    switch_page('links')

if men == 'Problemas':
    switch_page('Problems')

if men == 'Invariantes':
    switch_page('Invariants')


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
.stVideo {
    border-radius: 20px;
}
</style>
''',unsafe_allow_html=True)



st.markdown('''
<div class="content">
  <h1 class="title">Trenzas
    <div class="aurora">
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
    </div>
  </h1>

</div>
''',unsafe_allow_html=True)

st.divider()
'''
Al principio de la década de 1930, Emil Artin introdujo el concepto matemático de trenza con la intención de aplicarlo al estudio de los nudos. Sin embargo, en ese momento, este enfoque no tuvo mucho éxito y la investigación en este campo comenzó a disminuir. Fue en la década de 1950 cuando se descubrió que la teoría de trenzas tenía aplicaciones en otras áreas de las matemáticas, lo que impulsó nuevas investigaciones en este campo.

Con la aparición del polinomio de Jones en 1984, se revivió la idea original de Artin, ya que las trenzas desempeñaron un papel fundamental en la definición de este polinomio.

En este capítulo, proporcionaremos una breve introducción a los conceptos fundamentales de la teoría de trenzas.'''

sac.divider(label='', icon='bezier', align='center',key='div')

cols = st.columns([.5,.5])

with cols[0]:
    st.header('El grupo de trenzas')
    st.divider()
    r'''
Una n-trenza se define como una colección de cuerdas no anudadas que descienden desde $n$ puntos en la tapa superior de un cubo unitario $B$ y llegan a $n$ puntos diferentes en la tapa inferior del cubo, sin necesidad de que lleguen a los puntos correspondientes. Estas cuerdas se enlazan entre sí mientras descienden. Dos trenzas se consideran equivalentes si pueden deformarse una en la otra mediante isotopías ambientales que mantienen fijos los puntos extremos de las cuerdas.

Similar a los nudos, podemos obtener diagramas regulares de las trenzas proyectándolas sobre el plano $yz$. Estos diagramas consisten en conectar directamente los puntos $A_i$ con los puntos $A_i'$ $(i = 1, \ldots, n)$ mediante segmentos de línea recta. Esto nos da una trenza especial conocida como la n-trenza trivial, que se representa en la siguiente figura:

En la figura, los puntos $A_i$ en la tapa superior se conectan con los puntos correspondientes $A_i'$ en la tapa inferior mediante líneas rectas, formando así la n-trenza trivial.
'''


with cols[1]:
    st.image('pages/resources/trenza1.png')
    st.image('pages/resources/trenzatrivial.png')



sac.divider(label='', icon='bezier', align='center',key='div1')

cols1 = st.columns([.5,.5])

with cols1[0]:
    st.header('El grupo de trenzas')
    st.divider()
    r'''
Dado una n-trenza $\alpha$ en la que sus cuerdas están conectadas de la siguiente manera: $A_1$ con $A_{i_1}$, $A_2$ con $A_{i_2}$, ..., $A_n$ con $A_{i_n}$, podemos asociarle la siguiente permutación:

$$
\left( \begin{array}{cccc}
1 & 2 & \ldots & n \\
i_1 & i_2 & \ldots & i_n \\
\end{array} \right)
$$

Esta permutación se llama la "permutación de la trenza $\alpha$". Es importante destacar que la permutación de
la n-trenza trivial es simplemente la permutación identidad. Las trenzas cuya permutación es la identidad se llaman "trenzas puras".

Denotaremos el conjunto de todas las n-trenzas (considerando clases de equivalencia) como Bn. Si tenemos dos elementos
$\alpha$ y $\beta$ en Bn, podemos definir un producto para estas dos n-trezas. Este producto consiste en pegar la base
del cubo que contiene $\alpha$ con la tapa superior del cubo que contiene $\beta$, lo que resulta en un paralelepípedo
que contiene una nueva trenza creada al superponer $\alpha$ y $\beta$. Esta nueva trenza se llama el "producto de
$\alpha$ y $\beta$" y se denota como $\alpha\beta$. Es importante tener en cuenta que en general, $\alpha\beta$
no es igual a $\beta\alpha$, lo que significa que el producto no es conmutativo.'''


with cols1[1]:
    st.image('pages/resources/productotrenza.png')





sac.divider(label='', icon='bezier', align='center',key='div2')

cols2 = st.columns([.5,.5])

with cols2[0]:
    st.header('El grupo de trenzas')
    st.divider()
    r'''
Bajo esta operación de producto, el conjunto $B_n$ adquiere una estructura de grupo. Es sencillo demostrar, utilizando diagramas de trenzas, que esta operación es asociativa y que el elemento neutro está representado por la n-trenza trivial, que denotaremos como $e$.

Además, todo elemento $\alpha$ en $B_n$ tiene un elemento inverso $\alpha^{-1}$. Si consideramos la base del cubo que contiene a $\alpha$ como un espejo y reflejamos $\alpha$ en ese espejo, obtendremos su inverso $\alpha^{-1}$. Esto se ilustra en la Figura 5.4. Por lo tanto, tenemos que $\alpha\alpha^{-1} = e$ y $\alpha^{-1}\alpha = e$.

El grupo $B_n$ se denomina el "grupo de n-trenzas".'''


with cols2[1]:
    st.image('pages/resources/trenzainversa.png')
