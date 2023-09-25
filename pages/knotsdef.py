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

], format_func='title', open_all=True,index=5)


if men == 'Topología':
    switch_page('topospaces')

if men == 'Historia':
    switch_page('history')

if men == 'Pagina Principal':
    switch_page('Main')


if men == 'Nudos Toroidales':
    switch_page('torusknots')

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
  <h1 class="title">Definiciones basicas
    <div class="aurora">
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
    </div>
  </h1>

</div>
''',unsafe_allow_html=True)

sac.divider(label='', icon='balloon-heart', align='center')



cols = st.columns([.5,.5])

with cols[0]:
    st.header('Disco $D^n$')
    st.divider()
    r'''
**Definición:** El $n$-disco, denotado como $D^n$, se define como el conjunto de puntos en $\mathbb{R}^n$ que satisfacen
la siguiente condición:

$$
D^n = \{ x \in \mathbb{R}^n \mid \|x\| \leq 1 \}
$$
'''

with cols[1]:
    tabs = st.tabs(['Discos $D^0,D^1,D^2$','Discos $D^3$'])
    with tabs[0]:
        st.video('Videos/PAGINA2/Disco.mp4')

    with tabs[1]:
        st.video('Videos/PAGINA2/Disco3.mp4')


sac.divider(label='', icon='balloon-heart', align='center',key='div1')

cols1 = st.columns([.5,.5])

with cols1[0]:
    st.header('Esfera $S^{n-1}$')
    st.divider()
    r'''
**Definición:** La esfera $S^{n-1}$ en el $n$-disco $D^n$ se define como el conjunto de puntos en el $n$-disco $D^n$ que satisfacen la siguiente condición:

$$
S^{n-1} = \{ x \in D^n \mid \|x\| = 1 \}  = \partial D^n
$$

'''

with cols1[1]:
    tabs1 = st.tabs(['Esferas $S^0,S^1$','Esfera $S^2$', 'Esfera $S^2$ (Ejemplo 2)'])
    with tabs1[0]:
        st.video('Videos/PAGINA2/Esfera.mp4')

    with tabs1[1]:
        st.video('Videos/PAGINA2/Esfera2D.mp4')

    with tabs1[2]:
        st.video('Videos/PAGINA2/Esfera2Example2.mp4')


sac.divider(label='', icon='balloon-heart', align='center',key='div2')

cols2 = st.columns([.5,.5])

with cols2[0]:
    st.header('Nudos')
    st.divider()
    r'''
**Definició$n_1$ :** Un **nudo** es una **inmersión continua** de la
circunferencia estándar $S^1$ en el espacio tridimensional $\mathbb{R}^3$. En otras palabras, un nudo es
una función continua $f : S^1 \to \mathbb{R}^3$ que asigna cada punto en la circunferencia $S^1$ a un punto
en el espacio tridimensional $\mathbb{R}^3$, de manera que la función es inyectiva (no se cruza a sí misma) y
su imagen es una curva cerrada y simple en $\mathbb{R}^3$.

**Definició$n_2$ :** Un **nudo** es un subconjunto $K$ del espacio tridimensional
euclidiano $\mathbb{R}^3$ que es **homeomorfo** a la circunferencia estándar $S^1$, es decir, existe un
homeomorfismo $\varphi : S^1 \to K$ entre la circunferencia $S^1$ y el conjunto $K$.



'''

with cols2[1]:
    tabs2 = st.tabs(['Ejemplo 1','Ejemplo 2'])

    with tabs2[0]:
        st.video('Videos/PAGINA3/Knot.mp4')

    with tabs2[1]:
        st.video('Videos/PAGINA3/nudos1_3d.mp4')



sac.divider(label='', icon='balloon-heart', align='center',key='div3')

cols3 = st.columns([.5,.5])

with cols3[0]:
    st.header('Nudos Semejantes')
    st.divider()
    r'''
**Definición:** Dos nudos $K_1$ y $K_2$ son semejantes si existe un homeomorfismo
$$
h : \mathbb{R}^3 \to \mathbb{R}^3
$$
tal que  $h(K_1) = K_2$.


En otras palabras, dos nudos son semejantes si pueden ser deformados continuamente uno en el otro sin romper ni cruzar la estructura de nudo en ningún momento. Esto significa que los nudos semejantes tienen la misma topología y se diferencian solo por su forma tridimensional.

'''

with cols3[1]:
    st.video('Videos/PAGINA3/nudos_semejantes.mp4')





sac.divider(label='', icon='balloon-heart', align='center',key='div4')

cols4 = st.columns([.5,.5])

with cols4[0]:
    st.header('¿Por qué $\mathbb{R}^3$?')
    st.divider()
    r'''
Uno podría preguntarse por qué se define un nudo como un subconjunto del espacio tridimensional $\mathbb{R}^3$.
¿Únicamente debido a que vivimos en un mundo tridimensional? ¿Por qué no definir un nudo $K$ como un subconjunto del
espacio $\mathbb{R}^n$ que sea homeomorfo a $S^1$? Debemos notar que $n$ debe ser mayor o igual a dos, ya que
cualquier aplicación continua de la circunferencia en la recta real manda al menos un par de puntos diametralmente
opuestos al mismo punto y, por lo tanto, no puede haber subconjuntos de $\mathbb{R}$ que sean homeomorfos a $S^1$.
Sin embargo, si $n \neq 3$, existe un homeomorfismo $h : \mathbb{R}^n \rightarrow \mathbb{R}^n$ tal que $h(K)$ es
la circunferencia estándar. Para $n = 2$, esto constituye el famoso Teorema de Schönflies; para $n \geq 4$,
el resultado nos dice que si viviéramos en un mundo de 4 o más dimensiones, podríamos desanudar todos los nudos.
'''

with cols4[1]:
    st.header('Teorema de Schönflies')
    st.divider()
    r'''

**Teorema:** Sea $C$ una curva cerrada simple en el plano euclidiano $\mathbb{R}^2$. Entonces, existe un homeomorfismo
entre el conjunto $C$ y el círculo estándar $S^1$, es decir, existe un homeomorfismo $h : C \to S^1$.

En otras palabras, el Teorema de Schönflies establece que cualquier curva cerrada simple en el plano puede ser
transformada mediante un homeomorfismo en el círculo estándar. Esto implica que las curvas cerradas simples en
el plano son topológicamente equivalentes al círculo y pueden ser "desenrolladas" o "transformadas" en una forma
estándar de círculo mediante una función continua.
'''

sac.divider(label='', icon='balloon-heart', align='center',key='div5')

cols5 = st.columns([.5,.5])

with cols5[0]:
    st.header('Nudos Equivalentes')
    st.divider()
    r'''
**Definición.** Dos nudos $K_1$ y $K_2$ son equivalentes si existe un homeomorfismo

$$
h : \mathbb{R}^3 \rightarrow \mathbb{R}^3
$$
que preserva la orientación, es decir, $h$ es una función continua y
biyectiva con una inversa continua, y además $h(K_1) = K_2$. La equivalencia de nudos se denotará como $K_1 \sim K_2$.

El concepto de nudos equivalentes coincide con el concepto físico de igualdad de nudos.
De hecho, se puede demostrar que dos nudos $K_1$ y $K_2$ son equivalentes si y solo si existe un homeomorfismo
$h : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ y un número real $k > 0$ tal que $h(K_1) = K_2$ y $h(x) = x$ siempre que
$\|x\| \geq k$.

'''

with cols5[1]:
    st.video('Videos/PAGINA3/nudos_eq.mp4')


sac.divider(label='', icon='balloon-heart', align='center',key='div6')

cols6 = st.columns([.5,.5])

with cols6[0]:
    st.header('Nudos Anfiqueirales')
    st.divider()
    r'''

**Definición:** Un nudo $K$ es anfiqueiral si existe un homeomorfismo que invierte la orientación
$h : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ tal que $h(K) = K$.

Una formulación equivalente se presenta en el siguiente lema.

**Definición:** La imagen especular de un nudo $K$ es la imagen de $K$ bajo la reflexión $R$ definida por $(x, y, z) \mapsto (x, y, -z)$.

**Lema:** Un nudo es anfiqueiral si y solo si existe un homeomorfismo que preserva la orientación de $\mathbb{R}^3$
en $\mathbb{R}^3$ que lleva a $K$ a su imagen especular.

La demostración del **Lema** se basa en la definición de un nudo anfiqueiral y la relación entre un nudo y su imagen especular. Aquí está la demostración:

**Demostración del Lema:**

Supongamos que tenemos un nudo $K$ que es anfiqueiral, lo que significa que existe un homeomorfismo $h : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ que invierte la orientación y que lleva a $K$ en sí mismo, es decir, $h(K) = K$.

Definimos la reflexión $R : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ como la transformación que refleja cada punto $(x, y, z)$ en el plano $z = 0$, es decir, $R(x, y, z) = (x, y, -z)$. Claramente, $R$ es un homeomorfismo que preserva la orientación, ya que no altera la orientación de las figuras en el espacio tridimensional.

Ahora, consideramos la imagen especular de $K$, que llamaremos $K'$. $K'$ es simplemente la aplicación de $R$ a todos los puntos de $K$, es decir, $K' = R(K)$.

Como $h$ es un homeomorfismo que lleva a $K$ en sí mismo (ya que $h(K) = K$), podemos aplicar $h$ tanto antes como después de aplicar $R$ a $K$. Esto nos da:

$$
h(R(K)) = R(h(K)) = R(K)
$$

'''

with cols6[1]:
    r'''
    Por lo tanto, hemos demostrado que existe un homeomorfismo $h : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ (que es la composición de $h$ y $R$) que preserva la orientación y que lleva a $K$ en su imagen especular $K'$, lo que demuestra la afirmación "si" del lema.

La demostración en la dirección opuesta (la afirmación "solo si") es análoga y se basa en el hecho de que si un nudo es equivalente a su imagen especular, entonces existe un homeomorfismo que invierte la orientación que lleva al nudo en sí mismo.

Por lo tanto, hemos demostrado que un nudo es anfiqueiral si y solo si existe un homeomorfismo que preserva la orientación que manda al nudo en su imagen especular, lo que completa la demostración del Lema.
    '''
    st.video('Videos/PAGINA3/anfiqueiral.mp4')


sac.divider(label='', icon='balloon-heart', align='center',key='div7')

cols7 = st.columns([.5,.5])

with cols7[0]:
    st.header('Nudos Invertibles')
    st.divider()
    r'''

De la misma manera en que cualquier homeomorfismo de $\mathbb{R}^3$ en sí mismo preserva o invierte la orientación,
lo mismo ocurre con cualquier homeomorfismo de $K$ en sí mismo. Al dar una dirección al nudo $K$, la función $f$
preserva o invierte la orientación según si el orden de los puntos en $K$ se conserva o se invierte.

**Definición:** Un nudo $K$ se considera invertible si existe un homeomorfismo de $\mathbb{R}^3$ en sí mismo que
preserva la orientación, y además, la restricción de este homeomorfismo a $K$, denotada como $h|_K$, es un
homeomorfismo que invierte la orientación de $K$ en sí mismo.

Esta definición establece que un nudo se considera invertible cuando puede ser transformado mediante un homeomorfismo
que preserva la orientación en el espacio tridimensional $\mathbb{R}^3$, y al mismo tiempo, cuando esta transformación
invierte la orientación del propio nudo $K$.
'''

with cols7[1]:
    st.video('Videos/PAGINA3/Nudos_inver.mp4')

sac.divider(label='', icon='balloon-heart', align='center',key='div8')

cols8 = st.columns([.5,.5])

with cols8[0]:
    st.header('Nudos Dóciles vs. Nudos Salvajes')
    st.divider()
    r'''
Vamos a focalizar nuestro estudio en una categoría de nudos que presentan un comportamiento más manejable.

**Definición:** Un nudo poligonal es aquel que está compuesto por una unión finita de segmentos de recta, denominados
aristas, cuyos puntos extremos definen los vértices del nudo. Un nudo se clasifica como "dócil" si es equivalente a un
nudo poligonal. Por otro lado, los nudos que no cumplen esta propiedad se denominan "salvajes."

Todos los ejemplos previamente mencionados son ejemplos de nudos dóciles. A partir de este punto, nos centraremos
exclusivamente en el estudio de nudos dóciles.
'''

with cols8[1]:
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Wild_knot.svg/575px-Wild_knot.svg.png','Nudo Salvaje 1.')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj7gCoAFljQ83iCT1jO1TwNvGJ_694s6qhQL-o97It3rgmMxFHn6Vg1WlZRCTMyO6a0Jc&usqp=CAU','Nudo Salvaje 2.')

sac.divider(label='', icon='balloon-heart', align='center',key='div9')




