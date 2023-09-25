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

    ]),

], format_func='title', open_all=True,index=6)


if men == 'Topología':
    switch_page('topospaces')

if men == 'Historia':
    switch_page('history')

if men == 'Definiciones':
    switch_page('knotsdef')


if men == 'Pagina Principal':
    switch_page('Main')


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
.stVideo {
    border-radius: 20px;
}
</style>
''',unsafe_allow_html=True)



st.markdown('''
<div class="content">
  <h1 class="title">Nudos Toroidales
    <div class="aurora">
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
    </div>
  </h1>

</div>
''',unsafe_allow_html=True)


sac.divider(label='', icon='life-preserver', align='center',key='div')

'''
A continuación, definiremos un conjunto de nudos que comparten ciertas propiedades destacadas.
Estos nudos se conocen como nudos toroidales porque se construyen en una superficie conocida como toro.
Los nudos toroidales no solo son interesantes por sí mismos, sino que también son importantes porque,
en muchas ocasiones, ayudan a comprender propiedades generales de los nudos.

El toro, denotado como $T$, de manera intuitiva, es el espacio definido por la superficie de una dona.

A continuación, presentaremos tres descripciones diferentes del toro, cada una de las cuales nos proporciona diferentes formas de construir nudos toroidales.

'''
sac.divider(label='', icon='life-preserver', align='center',key='div1')
cols = st.columns([.5,.5])

with cols[0]:
    st.header('Definiciones del Toro')
    st.divider()
    r'''
**(a) Como Espacio Producto:** Consideremos el círculo unitario en el plano complejo $\mathbb{C}$, es decir, el conjunto de puntos dado por:
$$
S^1 = \{ e^{i\theta} \mid 0 \leq \theta < 2\pi \}.
$$
Entonces, el toro es el espacio $S^1 \times S^1$.
'''

with cols[1]:
    r'''
    **(b) Como Espacio Cociente:** Tomemos $X$ como el cuadrado unitario en $\mathbb{R}^2$, es decir:
$$
X = \{ (x, y) \mid 0 \leq x, y \leq 1 \}.
$$
Luego, el toro $T$ es el espacio cociente $X/\sim$, donde la relación de equivalencia se define de la siguiente manera:
$$
(0, y) \sim (1, y) \quad \text{y} \quad (x, 0) \sim (x, 1).
$$
'''
    st.video('Videos/PAGINA3/Torus_cociente.mp4')

sac.divider(label='', icon='life-preserver', align='center',key='div2')

cols1 = st.columns([.5,.5])

with cols1[0]:
    st.header('Definición Geométrica del Toro')
    st.divider()
    r'''
El toro, considerado como un subespacio de $\mathbb{R}^3$, se define mediante la siguiente expresión:
$$
\{ (x, y, z) \in \mathbb{R}^3 \mid (\sqrt{x^2 + y^2} - 2)^2 + z^2 = 1 \}.
$$
Esta definición representa la superficie obtenida al rotar la circunferencia $(x - 2)^2 + z^2 = 1$ en el plano $xz$,
con centro en el punto $(2, 0, 0)$, alrededor del eje $z$. Esta rotación nos proporciona la representación geométrica de una dona.
'''

with cols1[1]:
    st.video('Videos/PAGINA3/Torus3d.mp4')


sac.divider(label='', icon='life-preserver', align='center',key='div3')

cols2 = st.columns([.5,.5])

with cols2[0]:
    st.header('Nudo Tórico')
    st.divider()
    r'''
**Definición:** Un nudo que reside en la superficie de un toro se denomina nudo tórico y puede ser expresado de diversas maneras. La forma más sencilla de construir los nudos tóricos es mediante la función $f$, que proporciona el homeomorfismo entre $S^1 \times S^1$ y la superficie de la dona. Sean $m$ y $n$ un par de enteros primos entre sí. Definimos $K_{m,n}$ como el siguiente subconjunto del toro en $\mathbb{R}^3$:

$$
K_{m,n} = \{ f(\exp(2\pi i m t), \exp(2\pi i n t)) \, | \, t \in I \}.
$$

No es difícil comprobar que la aplicación $g: S^1 \rightarrow K_{m,n}$ definida por

$$
g(\exp(2\pi i t)) = f(\exp(2\pi i m t), \exp(2\pi i n t))
$$

es un homeomorfismo y, por lo tanto, $K_{m,n}$ es un nudo. A $K_{m,n}$ se le llama nudo tórico de tipo $(m, n)$.


'''

with cols2[1]:
    tabs = st.tabs([r'Nudos Toroidales $\mathbb{R}^2$',r'Nudos Toroidales $\mathbb{R}^3$'])
    with tabs[0]:
        st.video('Videos/PAGINA3/NudosToro2d.mp4')
    with tabs[1]:
        st.video('Videos/PAGINA3/NudosToro3d.mp4')





sac.divider(label='', icon='life-preserver', align='center',key='div4')

cols3 = st.columns([.5,.5])

with cols3[0]:
    st.header('¿Como Construir Nudos Tóricos?')
    st.divider()
    r'''
En el toro, existen dos circunferencias estándar: la primera está dada por $f(\exp(2\pi i t), 1)$, llamada meridiano, y la segunda por $f(1, \exp(2\pi i t))$, llamada longitud. Un nudo tórico de tipo $(m, n)$ da $n$ vueltas alrededor del meridiano y $m$ vueltas alrededor de la longitud.

Además, si consideramos el toro $T$ como el espacio cociente $X/\sim$ descrito en (b), entonces $K_{m,n}$ es la imagen en $T$ del segmento rectilíneo en $\mathbb{R}^2$ que pasa por el origen y tiene una pendiente $n/m$.

Esta definición describe los nudos tóricos y cómo se construyen utilizando el toro y las funciones $f$ y $g$, así como su relación con las circunferencias estándar del toro.'''

with cols3[1]:
    tabs1 = st.tabs([r'Nudos Sobre el Toro',r'Toro $\to$ Nudo'])
    with tabs1[0]:
        st.video('Videos/PAGINA3/NudoToro1.mp4')
    with tabs1[1]:
        st.video('Videos/PAGINA3/TorotoKnot.mp4')



sac.divider(label='', icon='life-preserver', align='center',key='div5')

cols4 = st.columns([.5,.5])

with cols4[0]:
    st.header('Tercera Forma de Construir Nudos Tóricos')
    st.divider()
    r'''
Una tercera manera de construir los nudos tóricos es la siguiente. Consideremos un cilindro de altura 1 con la base siendo el círculo unitario en el plano $xy$. Marcamos $r$ puntos $A_0, A_1, \ldots, A_{r-1}$ en la base $C_1$ y $r$ puntos $B_0, B_1, \ldots, B_{r-1}$ en la tapa superior $C_2$ con las siguientes coordenadas (ver Figura 2.10):

$$
A_0 = (1, 0, 0), A_1 = \left(\cos\left(\frac{2\pi}{r}\right), \sin\left(\frac{2\pi}{r}\right), 0\right), \ldots, A_{r-1} = \left(\cos\left(\frac{2(r-1)\pi}{r}\right), \sin\left(\frac{2(r-1)\pi}{r}\right), 0\right)
$$

$$
B_0 = (1, 0, 1), B_1 = \left(\cos\left(\frac{2\pi}{r}\right), \sin\left(\frac{2\pi}{r}\right), 1\right), \ldots, B_{r-1} = \left(\cos\left(\frac{2(r-1)\pi}{r}\right), \sin\left(\frac{2(r-1)\pi}{r}\right), 1\right)
$$

A continuación, conectamos los puntos $A_k$ y $B_k$ (para $k = 0, 1, \ldots, r-1$) en el cilindro mediante segmentos $\alpha_k$. Manteniendo la base $C_1$ fija, torcemos el cilindro rotando la tapa $C_2$ alrededor del eje $z$ por un ángulo de $\frac{2\pi q}{r}$, donde $q$ es un entero que puede ser positivo o negativo, y $r$ y $q$ son primos relativos.

Finalmente, identificamos los puntos $(x, y, 0)$ en $C_1$ con los puntos $(x, y, 1)$ en $C_2$, lo que nos permite obtener un toro con $r$ segmentos $\alpha_0, \alpha_1, \ldots, \alpha_{r-1}$ que se han unido formando el nudo $K_{q,r}$.
'''

with cols4[1]:
    ''''''



sac.divider(label='', icon='life-preserver', align='center',key='div6')

cols5 = st.columns([.5,.5])

with cols5[0]:
    st.divider()
    r'''

**Proposición:** Sean $q$ y $r$ dos enteros primos relativos, donde $r \neq 0$. Entonces:

1. Si $q = 0$, $q = \pm 1$, o $r = \pm 1$, entonces $K(q, r)$ es el nudo trivial.
2. Si $q$ y $r$ son enteros distintos de $0$ y $q$ no es igual a $\pm 1$, entonces $K(-q, r)$ es la imagen especular de $K(q, r)$.

La esfera de dimensión 3, denotada por $S^3$, se puede concebir como $\mathbb{R}^3$ con un punto $\infty$ agregado al infinito. A veces, es beneficioso considerar los nudos inmersos en $S^3$ en lugar de en $\mathbb{R}^3$. Los ajustes necesarios en las definiciones de nudo y equivalencia de nudos consisten únicamente en reemplazar $\mathbb{R}^3$ por $S^3$.
'''

with cols5[1]:
    st.divider()
    '''
    **Proposición:** La esfera tridimensional $S^3$ puede ser construida identificando las superficies de dos toros sólidos $T_1$ y $T_2$ de tal manera que el meridiano y la longitud de $T_1$ se identifican con la longitud y el meridiano de $T_2$, respectivamente.
    '''



sac.divider(label='', icon='life-preserver', align='center',key='div7')

cols6 = st.columns([.5,.5])

with cols6[0]:
    st.header('Clasificación de Nudos Tóricos')
    st.divider()
    r'''
Usando la proposición anterior, podemos demostrar de inmediato el siguiente teorema:

**Teorema:** $K(q, r) \cong K(r, q)$.

Los nudos tóricos están completamente clasificados.La esfera de dimensión 3, denotada por $S^3$, se puede concebir como $\mathbb{R}^3$ con un punto $\infty$ agregado al infinito. A veces, es beneficioso considerar los nudos inmersos en $S^3$ en lugar de en $\mathbb{R}^3$. Los ajustes necesarios en las definiciones de nudo y equivalencia de nudos consisten únicamente en reemplazar $\mathbb{R}^3$ por $S^3$.
'''
    with st.expander('Demostración'):
        r'''
        La demostración del Teorema, que establece $K(q, r) \cong K(r, q)$, se basa en la propiedad de simetría de los nudos tóricos. Para demostrarlo, primero consideremos la construcción de los nudos tóricos.

Recordemos que un nudo tórico $K(q, r)$ se construye identificando puntos en un toro sólido $T_1$ de manera que el meridiano y la longitud de $T_1$ se identifican con la longitud y el meridiano de otro toro sólido $T_2$, respectivamente. Esta construcción es esencialmente simétrica y no depende del orden en que identifiquemos los meridianos y las longitudes de los dos toros.

Ahora, para demostrar $K(q, r) \sim K(r, q)$, podemos considerar la construcción de $K(r, q)$. Siguiendo el mismo razonamiento, identificamos puntos en un toro sólido $T_2$ de manera que el meridiano y la longitud de $T_2$ se identifican con la longitud y el meridiano de otro toro sólido $T_1$, respectivamente. Como mencionamos antes, esta construcción es simétrica y no depende del orden en que identifiquemos los meridianos y las longitudes de los dos toros.

Dado que las construcciones de $K(q, r)$ y $K(r, q)$ son esencialmente las mismas y no dependen del orden, podemos concluir que $K(q, r)$ y $K(r, q)$ son equivalentes, es decir, $K(q, r) \sim K(r, q)$. Esto completa la demostración del teorema.

La clave de esta demostración radica en la simetría inherente de la construcción de nudos tóricos, lo que garantiza que los nudos $K(q, r)$ y $K(r, q)$ sean equivalentes.
        '''

with cols6[1]:
    '''
    '''




sac.divider(label='', icon='life-preserver', align='center',key='div8')

cols7 = st.columns([.5,.5])

with cols7[0]:
    st.header('Clasificación de Nudos Tóricos')
    st.divider()
    r'''
**Teorema:**

1. Si $q$ o $r$ es igual a $0$ o $\pm 1$, entonces $K(q, r)$ es el nudo trivial.

2. Supongamos que $q$, $r$, $p$, $s$ no son iguales a $0$ o $\pm 1$. Entonces:

$$
K(q, r) \cong K(p, s) \iff \{q, r\} = \{p, s\} \text{ o } \{q, r\} = \{-p, -s\}.
$$

Esto implica que existe una infinidad de nudos distintos.'''


with cols7[1]:
    '''
    '''




sac.divider(label='', icon='life-preserver', align='center',key='div9')

cols8 = st.columns([.5,.5])

with cols8[0]:
    st.header('Suma Conexa de Nudos')
    st.divider()
    r'''
A continuación, describiremos una operación relacionada con los nudos. Dados dos nudos orientados, $K_1$ y $K_2$, definimos su **suma conexa**, denotada como $K_1 \# K_2$, como el nudo que se obtiene al eliminar un intervalo en cada uno de los nudos y luego pegar los extremos de estos intervalos de manera que las orientaciones coincidan, como se muestra en la Figura 2.12. Un nudo se considera **primo** si no se puede expresar como la suma conexa de dos nudos no triviales, es decir, si no puede escribirse como $K_1 \# K_2$ con $K_1$ y $K_2$ ambos siendo nudos no triviales.

La suma conexa cumple las siguientes propiedades:

(a) Está bien definida hasta la equivalencia. Esto significa que si $K_1 \cong K'_1$ y $K_2 \cong K'_2$, entonces $K_1 \# K_2 \cong K'_1 \# K'_2$.

(b) Es una operación asociativa, lo que significa que $K_1 \# (K_2 \# K_3) \cong (K_1 \# K_2) \# K_3$.

(c) Es conmutativa, lo que implica que $K_1 \# K_2 \cong K_2 \# K_1$.

'''


with cols8[1]:
    st.video('Videos/PAGINA3/sumaconexa.mp4')
