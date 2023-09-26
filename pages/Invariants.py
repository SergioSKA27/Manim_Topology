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

], format_func='title', open_all=True,index=9)


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
  <h1 class="title">Invariantes
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
En la Sección anterior, se definió un invariante de nudos como una cantidad u objeto matemático que no cambia cuando
transformamos un nudo en otro equivalente. Estos invariantes son esenciales para distinguir entre nudos que no son
equivalentes, ya que basta con mostrar que hay un invariante cuyo valor es diferente para dichos nudos.

Un ejemplo simple de invariante para enlaces, derivado directamente de la definición de equivalencia de enlaces,
es el número de componentes. Dos enlaces con un número diferente de componentes no pueden ser equivalentes.
Sin embargo, este invariante no es muy poderoso, ya que existen muchos enlaces con el mismo número de componentes
que no son equivalentes; por ejemplo, todos los nudos son enlaces de una sola componente.

En el presente capítulo, describiremos algunos de los invariantes de nudos (y enlaces) más importantes y poderosos.
Estos invariantes desempeñan un papel fundamental en la teoría de nudos al proporcionar herramientas para distinguir
entre distintos tipos de nudos y enlaces.'''

sac.divider(label='', icon='link-45deg', align='center',key='div')

cols = st.columns([.5,.5])

with cols[0]:
    st.header('Movimientos de Reidemeister')
    st.divider()
    r'''
Anteriormente , observamos que a menudo es útil proyectar los nudos en el plano y luego estudiarlos a través de sus
diagramas regulares. Para llevar a cabo este proceso, nos preguntamos cómo se transforma el diagrama regular de un nudo
cuando aplicamos una isotopía para convertirlo en otro nudo equivalente en una posición regular. ¿Existen reglas que nos
permitan realizar esta transformación directamente, sin necesidad de considerar la transformación del nudo original?
Esta pregunta fue investigada por K. Reidemeister en la década de 1920, y él describió estas reglas, que ahora se
conocen como los "movimientos de Reidemeister". Gracias a estos movimientos, se pudieron definir muchos invariantes
de nudos. Para demostrar que una cantidad es un invariante de nudos, solo necesitamos verificar que no cambie
al aplicar los movimientos de Reidemeister.
'''

with cols[1]:
    st.header('Invariantes de nudos')
    st.divider()
    r'''
    Los movimientos de Reidemeister se dividen en tres tipos: tipo I (agregar o quitar un rizo), tipo II
    (agregar o quitar dos cruces consecutivos, ya sea por encima o por debajo) y tipo III (movimiento triangular).
    Todos estos movimientos se ilustran en la Figura 4.1.

Reidemeister demostró que estos tres movimientos, junto con equivalencias topológicas planas de los diagramas,
son suficientes para generar la isotopía espacial. En otras palabras, Reidemeister estableció que dos nudos (o enlaces)
en el espacio pueden deformarse uno en el otro (isotopía espacial) si y solo si sus diagramas regulares pueden
transformarse uno en el otro mediante isotopías planas y la aplicación de los tres movimientos (y sus inversos).

 '''
    st.image('https://i0.wp.com/mathemalchemy.org/wp-content/uploads/2021/02/reidemeisters.gif?resize=900%2C292&ssl=1',use_column_width=True)



sac.divider(label='', icon='link-45deg', align='center',key='div1')

cols1 = st.columns([.5,.5])

with cols1[0]:
    st.header('Número Mínimo de Cruces')
    st.divider()
    r'''
En la teoría de nudos, uno de los conceptos clave es el número mínimo de cruces, denotado como $c(K)$. Para comprenderlo
mejor, consideremos un diagrama regular $D$ de un nudo (o enlace) $K$, que contiene un número finito de puntos de cruce.
Sin embargo, es importante destacar que este número, $c(D)$, no es un invariante de nudos. Un ejemplo ilustrativo es la
Figura, que muestra dos diagramas regulares, $D$ y $D'$, del nudo trivial, con diferentes números de puntos de
cruce: $c(D) = 0$ y $c(D') = 1$.

En lugar de considerar un solo diagrama, analizamos todos los diagramas regulares posibles del nudo $K$ y denotamos por
$c(K)$ al número mínimo de puntos de cruce entre todos estos diagramas regulares. Formalmente, se define como:

$$
c(K) = \min_D c(D)
$$

donde $D$ es el conjunto de todos los diagramas regulares de $K$. La importancia de $c(K)$ radica en que es un invariante de
nudos, lo que significa que no cambia cuando transformamos un nudo en otro equivalente. Este invariante tiene propiedades interesantes:

1. El nudo trivial es el único nudo que tiene diagramas regulares con $c(D) = 0, 1\ o\ 2$.

2. El nudo trébol, ya sea dextrógiro o levógiro, tiene $c(K) = 3$. Además, entre todos los nudos y enlaces, es el único con $c(K) = 3$.

3. Para el enlace toroidal $K(q, r)$, el número mínimo de puntos de cruce es dado por:

$$
c(K(q, r)) = \min\{|q|(|r| - 1), |r|(|q| - 1)\}
$$


'''

with cols1[1]:
    r'''
    Además, existe una conjetura que sugiere que este invariante es aditivo bajo la suma conexa:

**Conjetura:** Sean $K1$ y $K2$ dos nudos (o enlaces) arbitrarios. Entonces, $c(K1\# K2) = c(K1) + c(K2)$.

Se ha demostrado que esta conjetura es cierta cuando $K1$ y $K2$ son nudos (o enlaces) alternantes.


 '''


