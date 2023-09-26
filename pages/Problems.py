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

], format_func='title', open_all=True,index=8)


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
  <h1 class="title">Problemas Fundamentales
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
Los problemas que surgen al estudiar la teoría de nudos pueden clasificarse principalmente en dos tipos: Problemas
Globales y Problemas Locales. Los Problemas Globales se refieren a cómo se comporta el conjunto de todos los nudos,
mientras que los Problemas Locales están relacionados con el comportamiento de un nudo específico. A continuación,
proporcionaremos ejemplos de ambos tipos de problemas y mencionaremos algunos resultados obtenidos hasta ahora.
'''

sac.divider(label='', icon='link-45deg', align='center',key='div')

st.title('Problemas Globales')
cols = st.columns([.5,.5])

with cols[0]:
    st.header('Problema de clasificación')
    st.divider()
    r'''
El problema de clasificación implica la creación de una tabla completa de nudos (o enlaces), lo que significa una tabla
en la que no existan dos nudos equivalentes y en la que cualquier nudo (o enlace) arbitrario sea equivalente a alguno de
los nudos en la tabla. Este problema es altamente complicado y está lejos de resolverse por completo. Un subproblema que
podría resultar más manejable es la clasificación de un tipo específico de nudos, como en el caso de los nudos tóricos.
'''
    st.image('https://d3i71xaburhd42.cloudfront.net/5bd18e843e5df84c12e926702b1e2c8f8bf90d36/4-Figure2-1.png')

with cols[1]:
    st.header('Invariantes de nudos')
    st.divider()
    r'''
    Una forma de determinar si dos nudos son equivalentes o no es encontrar alguna propiedad de los nudos que no cambie
cuando se deforman y que sirva para distinguir nudos que no son equivalentes. A estas propiedades se les llama invariantes de nudos.

Supongamos que a cada nudo $ K $ se le asigna una cantidad (o un objeto matemático, como un número, un grupo, etc.) $ \rho(K) $.
Si para dos nudos equivalentes, las cantidades asignadas son siempre las mismas, entonces $ \rho $ es un invariante de nudos.

En general, un invariante de nudos es unidireccional, es decir,

$$
\text{Si dos nudos son equivalentes} \implies \text{Sus invariantes son iguales}.
$$

En muchos casos, el recíproco no es cierto. Equivalentemente, si el invariante de dos nudos es diferente, entonces los
nudos no pueden ser equivalentes. Por lo tanto, los invariantes de nudos nos proporcionan un método efectivo para
distinguir nudos que no son equivalentes.

En el próximo capítulo, se definirán algunos de los invariantes clásicos de nudos.
    '''




sac.divider(label='', icon='link-45deg', align='center',key='div1')

cols1 = st.columns([.5,.5])

with cols1[0]:
    st.header('Una conjetura fundamental')
    st.divider()
    r'''
Existe un teorema fundamental en el cual se basa la definición de algunos invariantes de nudos, como por ejemplo, el grupo de un nudo,
que definiremos en la siguiente sección.

**Teorema 3.1:** Si dos nudos $ K_1 $ y $ K_2 $ en $ S^3 $ son equivalentes, entonces sus complementos $ S^3 \setminus K_1 $ y $ S^3 \setminus K_2 $ son homeomorfos.

La conjetura fundamental es el recíproco del Teorema 3.1.

**Conjetura 3.2:** Sean $ K_1 $ y $ K_2 $ dos nudos. Si sus complementos $ S^3 \setminus K_1 $ y $ S^3 \setminus K_2 $ son homeomorfos, entonces los nudos son equivalentes.

A finales de los años 80, esta conjetura fue demostrada por C. McA Gordon y J. Luecke [2]. Como consecuencia de este resultado, el problema de los nudos en $ S^3 $, que es un problema relativo porque tiene que ver con la forma del nudo en $ S^3 $, se transforma en un problema absoluto, ya que tiene que ver únicamente con el estudio de los espacios complementarios.

Sin embargo, no siempre es posible transformar un problema relativo en uno absoluto. Un ejemplo de ello es que la conjetura anterior es falsa para el caso de enlaces.
'''


with cols1[1]:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQePw_aJGaiSRy1UPt5xNKg2I9bDHytpFPrrp_lH4zE1oX-K40s-MBUGqBAP7regm5jLBk&usqp=CAU')
    st.image('https://upload.wikimedia.org/wikipedia/commons/3/38/Knot_Unfolding.gif')

st.title('Problemas locales')


sac.divider(label='', icon='link-45deg', align='center',key='div2')

cols2 = st.columns([.5,.5])

with cols2[0]:
    st.header('¿Cuándo un nudo es anfiqueiral?')
    st.divider()
    r'''
Recordemos que un nudo es anfiqueiral si es equivalente a su imagen especular. Como ejemplo, hemos observado que el
nudo 8 es anfiqueiral. Por otro lado, mencionamos que el nudo trébol no lo es. Una forma de demostrarlo es utilizando
el polinomio de Jones, que es un invariante que describiremos en la sección siguiente.

Recordemos que el nudo trébol es un caso particular de nudos tóricos. En general, para los nudos tóricos $K(q, r)$,
se sabe que no son anfiqueirales [4, Teorema 7.4.2].

Además, se ha establecido que los nudos alternantes cuyo número mínimo de puntos de cruce  es impar no pueden ser anfiqueirales.'''


with cols2[1]:
    st.header('¿Cuándo un nudo es primo?')
    st.divider()
    r'''
En muchas ocasiones, no es evidente determinar si un nudo es primo a partir de un diagrama dado. En la Figura 3.2
se presentan dos diagramas del mismo nudo.
Este problema se ha resuelto por completo para el caso de nudos alternantes, es decir, se puede determinar cuándo un nudo
alternante es primo o no. También se ha demostrado que los nudos con un número de puentes igual a 2
son primos. Ejemplos de este tipo de nudos son el nudo trébol y el nudo 8.

    '''


sac.divider(label='', icon='link-45deg', align='center',key='div3')

cols3 = st.columns([.5,.5])

with cols3[0]:
    st.header('¿Cuándo un nudo es invertible?')
    st.divider()
    r'''
Los nudos que tienen un número reducido de puntos de cruce suelen ser invertibles.
Como vimos en la Figuras anteriores, el nudo trébol es un ejemplo de nudo invertible. La existencia de nudos no invertibles
fue demostrada por H. F. Trotter en 1963. En la Figura (a), se presenta un ejemplo de un nudo no invertible
descubierto por Trotter, y después de este hallazgo, se encontraron muchos otros nudos no invertibles.
De hecho, se podría decir que la mayoría de los nudos son no invertibles en la actualidad.
En la Figura  (b), se muestra el nudo no invertible más simple.
'''
    st.image('https://media.nature.com/lw767/magazine-assets/d41586-021-03639-4/d41586-021-03639-4_19914646.gif')


with cols3[1]:
    st.header('¿Cuál es el período de un nudo?')
    st.divider()
    r'''
El período de un nudo se refiere a la cantidad de rotaciones necesarias alrededor de un eje para que el nudo vuelva a
su forma original. En general, si podemos rotar un nudo en un ángulo de $\frac{2\pi}{n}$
radianes alrededor de algún eje de manera que vuelva a su forma original, entonces decimos que el nudo tiene un período de $n$.

El problema local en este contexto es determinar todos los posibles períodos de un nudo dado.
Este problema ha sido completamente resuelto para el caso de los nudos tóricos;
en particular, el nudo $K(q, r)$ tiene períodos $|q|$ y $|r|$.

    '''

    st.image('https://i.gifer.com/881J.gif')
