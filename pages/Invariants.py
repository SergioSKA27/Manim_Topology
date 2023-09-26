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

sac.divider(label='', icon='infinity', align='center',key='div')

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



sac.divider(label='', icon='infinity', align='center',key='div1')

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
    st.image('pages/resources/minimum-number-of-crossings.png')
    st.image('pages/resources/minimum-number-of-crossings2.png',use_column_width=True)
    st.image('pages/resources/Crossing_numbers_trefoil.svg.png',use_column_width=True)

sac.divider(label='', icon='infinity', align='center',key='div2')

cols2 = st.columns([.5,.5])

with cols2[0]:
    st.header('Grupo del Nudo: Un Invariante Fundamental')
    st.divider()
    r'''
En la Sección anterior, mencionamos el Teorema , que establece que dos nudos equivalentes tienen complementos homeomorfos.
Aprovechando este hecho, podemos utilizar un invariante de espacios topológicos para obtener un invariante de los nudos
al aplicarlo a los complementos de los mismos.

Uno de los primeros y más fundamentales invariantes para espacios topológicos es el **grupo fundamental**.
Es importante notar que, en este caso, el invariante no es un número, como en los ejemplos anteriores de invariantes,
sino un grupo, un concepto matemático más complejo.

El grupo fundamental se basa en las propiedades topológicas de los espacios y se convierte en un invariante esencial
en la teoría de nudos. Este grupo capta las propiedades fundamentales de la conectividad y la estructura topológica
de los espacios, lo que lo convierte en una herramienta valiosa para distinguir y clasificar nudos en términos
de su topología subyacente.

'''

with cols2[1]:
    st.header('Grupo Fundamental')
    st.divider()
    r'''
El grupo fundamental es un invariante topológico fundamental en matemáticas. Su construcción se basa en un espacio topológico $X$. Aquí está la idea detrás de su construcción:

1. Consideramos el conjunto $\Omega$ de todas las trayectorias cerradas (o lazos) que parten de un punto fijo $p$ en $X$. Este punto se llama "punto base".

2. Dividimos el conjunto $\Omega$ en clases de equivalencia, donde dos lazos son equivalentes si uno puede ser deformado continuamente en el otro. Estos lazos equivalentes se llaman "homotópicos".

3. Damos a estas clases de lazos homotópicos una representación mediante corchetes, por ejemplo, $[\alpha]$. Si $\alpha$ es homotópico a $\beta$, entonces las clases $[\alpha]$ y $[\beta]$ son idénticas.

4. Definimos una operación de multiplicación entre estas clases de lazos: tomamos dos representantes de las clases, $\alpha$ y $\beta$, y definimos $[\alpha][\beta]$ como la clase del lazo que parte de $p$, sigue $\alpha$, regresa a $p$, sigue $\beta$ y luego regresa nuevamente a $p$.

5. Esta operación de multiplicación está bien definida, es decir, no depende de los representantes específicos que elijamos. Además, estas clases de equivalencia forman un grupo, lo que significa que la multiplicación es asociativa, existe un elemento neutro (la clase del lazo constante $e$) y cada elemento tiene un inverso. Sin embargo, la multiplicación no necesariamente es conmutativa ($[\alpha][\beta] \neq [\beta][\alpha]$).

El grupo formado por estas clases de lazos homotópicos se denota como $\pi_1(X, p)$ y se llama el "grupo fundamental de $X$ con punto base $p$". Este grupo fundamental captura propiedades topológicas esenciales del espacio $X$ y se convierte en un invariante topológico poderoso utilizado en la teoría de nudos y otros campos de las matemáticas y la topología.

**Definición:** El grupo del nudo, denotado como $\pi_1(R^3 \backslash K, p)$, se define como el grupo fundamental asociado a un nudo $K$ en $\mathbb{R}^3$. Aquí, $p$ es cualquier punto en el espacio tridimensional que no pertenezca al nudo $K$.
 '''



sac.divider(label='', icon='infinity', align='center',key='div3')

cols3 = st.columns([.5,.5])

with cols3[0]:
    st.header('Grupo del Nudo Trivial')
    st.divider()
    r'''
Vamos a calcular el grupo fundamental del nudo trivial utilizando los conceptos que hemos presentado hasta ahora. En la Figura 4.7, podemos identificar dos tipos de lazos en $R^3 \backslash K$: aquellos que rodean el nudo $K$ como $\alpha$ y $\gamma$, y aquellos que no lo hacen como $\beta$ y $\beta'$. Además, observamos que $[\alpha] = [\alpha']$ y $[\beta] = [\beta']$.

Es evidente que los lazos que son homotópicos entre sí son aquellos que rodean el nudo $K$ el mismo número de veces. Por lo tanto, tenemos la clase del lazo constante $[e]$, la clase de los lazos que dan una vuelta alrededor de $K$ como $[ \alpha]$, la clase de los lazos que dan dos vueltas como $[\gamma]$, y en general, $[ \alpha^n]$ representa la clase de los lazos que dan $n$ vueltas alrededor de $K$, y tenemos que $[ \alpha^n] [ \alpha] = [ \alpha^{n+1}]$.

Además, los inversos de estas clases están representados por los lazos que rodean el nudo $K$ en la dirección opuesta. Por lo tanto, es evidente que $\pi_1(R^3 \backslash K, p) \cong \mathbb{Z}$. En otras palabras, el grupo del nudo trivial es un grupo cíclico infinito, o, dicho de otra manera, isomorfo a los números enteros.
 '''

with cols3[1]:
    st.image('pages/resources/gruponudotrivial.png')



sac.divider(label='', icon='infinity', align='center',key='div4')

cols4 = st.columns([.5,.5])

with cols4[0]:
    st.header('Presentaciones de Grupos')
    st.divider()
    r'''
En ocasiones, es más sencillo definir un grupo mediante algunos de sus elementos, llamados generadores, y ciertas
relaciones entre ellos. Para ilustrar este concepto, consideremos un ejemplo.

Sea $G$ el grupo formado por el conjunto $\{1, a, b\}$ y la operación de multiplicación definida por la siguiente tabla:

$$
\begin{array}{c|c|c|c}
    & 1 & a & b \\
    \hline
  1 & 1 & a & b \\
  a & a & b & 1 \\
  b & b & 1 & a \\
\end{array}
$$

'''

with cols4[1]:
    r'''

En ocasiones, podemos simplificar la descripción de un grupo al reducir la información necesaria para definirlo.
Por ejemplo, en una tabla de multiplicación anterior, con 9 entradas, podemos observar que $b = a^2$.
Esto nos permite describir el grupo de manera más eficiente, indicando que los elementos del grupo son $1$, $a$, y $a^2$,
y que $a^3 = 1$. Esta forma de describir el grupo se llama una "presentación del grupo" y se denota como $\langle a \,|\, a^3 = 1 \rangle$.

En general, una presentación de grupo consta de un conjunto de generadores $\hat{x} = \{x_1, x_2, \ldots\}$ y un conjunto
de relaciones $\hat{r} = \{r_1, r_2, \ldots\}$, denotados como $\langle \hat{x} \,|\, \hat{r} \rangle$.

Las relaciones en una presentación pueden implicar otras relaciones, conocidas como "consecuencias". Por ejemplo,
si tenemos las relaciones $\hat{r} = \{a^3 = 1, b = a^2\}$, entonces $ba = 1$ es una consecuencia de $\hat{r}$.

Algunos ejemplos de presentaciones de grupos son los siguientes:

1. $\langle x, y \,|\, xyx = yxy \rangle$
2. $\langle x, y \,|\, xy^2 = y^3x, yx^2 = x^3y \rangle$.

Es importante destacar que un grupo puede tener múltiples presentaciones diferentes, y una pregunta relevante es
determinar cuándo dos presentaciones distintas corresponden al mismo grupo.
    '''




sac.divider(label='', icon='infinity', align='center',key='div5')

cols5 = st.columns([.5,.5])

with cols5[0]:
    st.header('Operaciones de Tietze y Equivalencia de Presentaciones de Grupos')
    st.divider()
    r'''

**Definición:**   Decimos que dos presentaciones de grupos son equivalentes si corresponden a grupos isomorfos.

Para resolver el problema de determinar cuándo dos presentaciones son equivalentes, introducimos las operaciones de Tietze:

**Operación Tipo I**: Dada una presentación $\langle \hat{x} \,|\, \hat{r} \rangle$ y una consecuencia $s$ de $\hat{r}$, podemos considerar la presentación $\langle \hat{x} \,|\, \hat{s} \rangle$ con $\hat{s} = \hat{r} \cup \{s\}$. Entonces, $\langle \hat{x} \,|\, \hat{r} \rangle$ y $\langle \hat{x} \,|\, \hat{s} \rangle$ son equivalentes.

**Operación Tipo I'**: Si una relación $r$ en $\hat{r}$ es una consecuencia de las otras relaciones en $\hat{r}$, entonces la presentación $\langle \hat{x} \,|\, \hat{r}' \rangle$ con $\hat{r}' = \hat{r} \setminus \{r\}$ es equivalente a $\langle \hat{x} \,|\, \hat{r} \rangle$.

**Operación Tipo II**: Dada una presentación $\langle \hat{x} \,|\, \hat{r} \rangle$, un generador $y$ que no pertenece a $\hat{x}$, y un producto $\xi$ de elementos en $\hat{x}$, podemos considerar la presentación $\langle \hat{y} \,|\, \hat{s} \rangle$ con $\hat{y} = \hat{x} \cup \{y\}$ y $\hat{s} = \hat{r} \cup \{y = \xi\}$. Entonces, $\langle \hat{x} \,|\, \hat{r} \rangle$ y $\langle \hat{y} \,|\, \hat{s} \rangle$ son equivalentes.

**Operación Tipo II'**: La inversa de la operación Tipo II.


'''

with cols5[1]:
    r'''
    A continuación, mostramos un ejemplo que demuestra la equivalencia entre las presentaciones $\langle x, y \,|\, xyx = yxy \rangle$ y $\langle a, b \,|\, a^3 = b^2 \rangle$:


$\langle x, y \,|\, xyx = yxy \rangle$

⇓ Tipo II: $a, a = xy$

$\langle x, y, a \,|\, xyx = yxy, a = xy \rangle$

⇓ Tipo II: $b, b = xyx$

$\langle x, y, a, b \,|\, xyx = yxy, a = xy, b = xyx \rangle$

⇓ Tipo I: $a^3 = b^2 \, (xyx)(xyx)(xyx) = (xy)(xy)(xy)$

$\langle x, y, a, b \,|\, xyx = yxy, a = xy, b = xyx, a^3 = b^2 \rangle$

⇓ Tipo I: $x = a^{-1}b, \, xyx = yxy ⇒ x = y^{-1}x^{-1}yxy ⇒ x = a^1b$

$\langle x, y, a, b \,|\, xyx = yxy, a = xy, b = xyx, a^3 = b^2, x = a^{-1}b \rangle$

⇓ Tipo I' (tres veces)

$\langle x, y, a, b \,|\, a^3 = b^2, x = a^{-1}b, y = b^{-1}a^2 \rangle$

⇓ Tipo II' (dos veces)

$\langle a, b \,|\, a^3 = b^2 \rangle$.

De esta manera, hemos demostrado que las presentaciones $\langle x, y \,|\, xyx = yxy \rangle$ y $\langle a, b \,|\, a^3 = b^2 \rangle$ son equivalentes.


    '''



sac.divider(label='', icon='infinity', align='center',key='div6')

cols6 = st.columns([.5,.5])

with cols6[0]:
    st.header('Presentación del Grupo del Trébol')
    st.divider()
    r'''
Para calcular la presentación del grupo de cualquier nudo poligonal, como el nudo trébol, se sigue un algoritmo específico. Aquí se describe cómo se calcula la presentación del nudo trébol como ejemplo:

1. Comenzamos con un diagrama regular del nudo.

2. Dividimos el nudo en 2n segmentos, eligiendo dos puntos cerca de cada cruce por debajo. Los segmentos que contienen un cruce por arriba se llaman "pasos por arriba," y los que tienen un cruce por debajo se llaman "pasos por abajo."

3. Orientamos el nudo y dibujamos una flecha perpendicular en cada paso por arriba, siguiendo de izquierda a derecha con respecto a la orientación. Asignamos una letra a cada flecha, que servirá como generador en la presentación.

4. Dibujamos rectángulos alrededor de cada paso por abajo y los orientamos en sentido contrario a las manecillas del reloj.

5. Obtenemos una relación de cada rectángulo escribiendo una letra por cada paso por arriba que cruce un lado del
rectángulo, siguiendo el orden y la orientación del mismo. Asignamos un exponente +1 o -1 según si la orientación del
lado del rectángulo coincide o es opuesta a la flecha del paso correspondiente. Por ejemplo, para el rectángulo B1,
obtenemos la relación: $x^{-1}yzy^{-1} = 1$, y para el rectángulo B2, obtenemos $y^{-1}zxz^{-1} = 1$.Finalmente, para
el rectángulo B3, obtenemos la relación  $z^{-1}xyx^{-1} = 1.$

Esta relación completa el proceso de obtener las relaciones de cada rectángulo alrededor de los pasos por abajo en el cálculo de la presentación del grupo del nudo trébol..
'''

with cols6[1]:
    st.image('pages/resources/grupotrebol.png',use_column_width=True)



sac.divider(label='', icon='infinity', align='center',key='div7')

cols7 = st.columns([.5,.5])

with cols7[0]:
    st.header('Presentación del Grupo del Trébol')
    st.divider()
    r'''
    Se demuestra que cualquiera de las relaciones obtenidas es consecuencia de las otras, lo que nos permite descartar una de ellas (por ejemplo, la tercera). Así, obtenemos una presentación del grupo del nudo trébol como:

$$
⟨ x, y, z | x = yzy^{-1}, y = zxz^{-1} ⟩.
$$

Si sustituimos $z = xyx^{-1}$ en las otras relaciones y realizamos una operación de Tietze de Tipo II', obtenemos:

$$
⟨ x, y | x = yxyx^{-1}y^{-1}, y = xyxy^{-1}x^{-1} ⟩.
$$

Multiplicando por la derecha la segunda relación por $xyx^{-1}y^{-1}$, obtenemos la primera relación. Esto demuestra que cualquiera de las relaciones obtenidas es una consecuencia de las otras. Finalmente, llegamos a la siguiente presentación del grupo del nudo trébol:

$$
⟨ x, y | xyx = yxy ⟩.
$$

Esta presentación es equivalente a la presentación anterior:

$$
⟨ a, b | a^3 = b^2 ⟩.
$$


'''

with cols7[1]:
    st.image('pages/resources/grupotrebol2.png',use_column_width=True)




sac.divider(label='', icon='infinity', align='center',key='div8')
st.header('Polinomios')
'''
En esta sección, exploraremos un nuevo tipo de invariante para nudos que involucra la asignación de polinomios en lugar de números o grupos. A lo largo de la historia de la teoría de nudos, dos descubrimientos fundamentales han impulsado y enriquecido la comprensión de este campo: el polinomio de Alexander en 1928 y el polinomio de Jones en 1984. Estos polinomios desempeñan un papel crucial en el estudio y la clasificación de los nudos.
'''
sac.divider(label='', icon='infinity', align='center',key='d')

cols8 = st.columns([.5,.5])

with cols8[0]:
    st.header('Polinomio de Alexander')
    st.divider()
    r'''
   El polinomio de Alexander es un invariante de nudos que desempeñó un papel fundamental en el desarrollo de la teoría de nudos. Fue introducido por el matemático James W. Alexander en 1928. Este polinomio se utiliza para distinguir nudos, es decir, para determinar si dos nudos dados son equivalentes o no. Además, proporciona información valiosa sobre la estructura de un nudo.

La idea principal detrás del polinomio de Alexander es representar un nudo mediante una cierta cantidad de variables y ecuaciones, lo que resulta en un polinomio único asociado al nudo. Este polinomio se denota comúnmente como $\Delta(t)$, donde $t$ es la variable del polinomio. La forma exacta del polinomio depende de cómo el nudo esté proyectado en el espacio tridimensional.

Para entender mejor este concepto, consideremos un ejemplo simple: el nudo trébol (también conocido como nudo de tres hojas). Este nudo se representa mediante una proyección plana, y el polinomio de Alexander asociado se denota como $\Delta(t)$. La representación del polinomio de Alexander para el nudo trébol es:

$\Delta(t) = t^{-1} - 1 + t$

En este caso, la variable $t$ es una variable formal utilizada en álgebra, y el polinomio tiene coeficientes enteros. La forma específica del polinomio se deriva de las ecuaciones que describen cómo las partes del nudo interactúan en la proyección.

El polinomio de Alexander puede ser utilizado para determinar si dos proyecciones diferentes de un nudo representan el mismo nudo. Si los polinomios asociados a estas proyecciones son idénticos, entonces los nudos son equivalentes.

En resumen, el polinomio de Alexander es una herramienta matemática fundamental en la teoría de nudos que nos permite caracterizar y distinguir diferentes nudos. Su utilización proporciona una forma formal de estudiar y clasificar los nudos en el vasto mundo de la topología y la geometría.
'''

with cols8[1]:
    st.image('pages/resources/alexanderpoly.png',use_column_width=True)




