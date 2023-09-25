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

], format_func='title', open_all=True,index=1)


if men == 'Pagina Principal':
    switch_page('Main')

if men == 'Historia':
    switch_page('history')

if men == 'Definiciones':
    switch_page('knotsdef')


if men == 'Nudos Toroidales':
    switch_page('torusknots')





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
# Session

if 'topologies' not in st.session_state:
    st.session_state['topologies'] = None

if 'notopologies' not in st.session_state:
    st.session_state['notopologies'] = None



#Created by: Lopez Martinez Sergio
#this help us to identify all the topologies in a given set

#the conditions we consider to say  a pair  of the form (T,s)
#whit T a set of subsets of s. Is given as follow

#1.the empty set belongs to T, as well as  the set s

#2.the union  of an arbitrary number of elements on T , belongs to T as well

#3.the intersection of  any two members of T belongs to T



# If the elements are a string, then the elements are set to None. Otherwise, the elements are set to a dictionary with
# the elements as keys and the elements as values
class Set:
    def __init__(self,size, elements):
        """
        If the elements are a string, then the elements are set to None. Otherwise, the elements are set to a dictionary with
        the elements as keys and the elements as values.

        :param size: the size of the set
        :param elements: a list of elements that are in the set
        """
        self.size = size

        if type(elements) !=  type(""):
            self.elements = {}
            if self.size > 0:
                for i in list(elements):
                    if self.elements.get(i,None) == None:
                        self.elements[i] = i
        else:
            self.elements = None

        self.elemtslist = list(self.elements)



    def belong(self,element):
        """
        It returns True if the element is in the set, and False otherwise

        :param element: The element to check for
        :return: The value of the key element.
        """
        return self.elements.get(element, None) != None

    def addelement(self,element):
        """
        It adds an element to the set.

        :param element: The element to add to the set
        """
        attr = self.elementsscpy()
        attr[element] = element
        self.elements = attr
        self.elemtslist = list(attr)

    def elementsscpy(self):
        """
        It returns a copy of the elements in the set.
        :return: A copy of the elements list.
        """
        return copy.copy(self.elements)

    def is_emptyset(self):
        """
        It checks if the set is empty.
        :return: True if the set is empty,false in other case
        """
        return len(self.elements) == 0

    def uNION(self, other):
        """
        It takes the elements of the first set and adds them to a new set, then it takes the elements of the second set and
        adds them to the new set

        :param other: Set
        :return: The union of the two sets.
        """
        uni = Set(0,[])

        for i in self.elemtslist:
                uni.addelement(i)
        for j in list(other.elementsscpy()):
                uni.addelement(j)

        return uni

    def Intersection(self, other):
        """
        It returns the intersection of two sets.

        :param other: Set
        :return: The intersection of two sets.
        """
        inter = Set(0,[])

        if self.is_emptyset() or other.is_emptyset():
            return inter

        for i in self.elemtslist:
            if other.belong(i):
                inter.addelement(i)

        return inter

    def __repr__(self) -> str:
        """
        The function returns a string representation of the set
        :return: The elements of the set.
        """
        if self.is_emptyset():
            return "∅"
        return str(self.elements)

    def __str__(self) -> str:
        """
        The function takes a set and returns a string representation of the set
        """
        if self.is_emptyset():
            return "∅"
        ss = "{"
        for i in  self.elemtslist:
            ss = ss + str(i) + ','
        return ss + '}'

    def __eq__(self, __o: object) -> bool:
        """
        It checks if the two sets are equal by checking if the elements of one set are in the other set and vice versa

        :param __o: object
        :type __o: object
        :return: a boolean value.
        """
        flag = True
        if len(self.elements) != len(__o.elementsscpy()):
            return False
        else:
            if len(self.elements) == 0:
                return True
            for i in self.elemtslist:
                if __o.belong(i) == False:
                    flag = False
                    break
                else:
                    continue
            if flag:
                for j in list(__o.elementsscpy()):
                    if self.belong(j) == False:
                        flag = False
                        break
                    else:
                        continue
        return flag

    def Powerset(self):
        """
        It returns the powerset of a set.
        :return: A list of sets.
        """
        Ps = []
        ts = chain.from_iterable(combinations(self.elemtslist, r) for r in range(len(self.elements)+1))
        for e in ts:
            if len(e) == 0:
                Ps.append(Set(0,[]))
            else:
                Ps.append(Set(len(e),e))
        return Ps

    def lenn(self):
        """
        The function returns the length of a list or string.
        :return: The length of the "elements" attribute of the object.
        """
        return len(self.elements)


def FamilySetUnion(F) -> Set:
    U = copy.copy(F[0])
    for i in range(1,len(F)):
        U = U.uNION(F[i])
    return U



def is_topologie(T, s):
    """
    The function checks if the given set of sets is a topology on the given set.

    :param T: a list of sets
    :param s: the set of all elements
    :return: A boolean value.
    """
    whhy = []
    flag1 = 0
    for i in  T:
        if i.is_emptyset():
            #print("000")
            flag1 += 1
            break

    for i in  T:
        if i == s:
            flag1 += 1
            break

    if flag1 < 2 :
        return False


    pairs = []

    #Combinations of families Union
    flag2 = True
    for i in range(2,len(T)+1):
        cm = combinations(T,i)
        if i == 2:
            pairs = list(cm)

        for j in list(cm):
            #print("TS",j)
            FU = FamilySetUnion(j)
            #print("FU ",FU)
            blongTt = False
            for k in  T:
                if k == FU:
                    blongTt = True
            if blongTt == False:
                flag2 = False
                break

        #print("-------------")

    if(flag2 == False):
        return False

    #print(pairs)
    flag3 =  True
    for i in  range(0,len(pairs)):
        intr = pairs[i][0].Intersection(pairs[i][1])
        gg = False
        for j in T:
            if j == intr:
                gg = True
                break
        if gg == False:
            flag3 = False
            break

    if(flag3 == False):
        return False


    return True


def topologies_of_Set(S):
    """
    The function "topologies_of_Set" generates all possible topologies of a given set.

    :param S: The parameter S represents a set
    :return: The function `topologies_of_Set(S)` returns two lists: `t` and `nt`.
    """
    print('Im running :)')

    kk = 1
    if S.lenn() > 4:
        print('To bigger :(')
        return [],[]

    if S.is_emptyset():
        return [(S,S)],[]
    t = []
    nt = []
    P = S.Powerset()
    for i in range(1,len(P)+1):
        perms = combinations(P,i)
        for cs in list(perms):
            if len(cs) == 1:
                nt.append(cs)
                continue
            if len(cs) == len(P):
                #print(kk,"TOPOLOGY :)",cs)
                kk += 1
                t.append(cs)
                continue

            if len(cs) != len(P) and is_topologie(cs,S) :
                #print(kk,"TOPOLOGY :)",cs)
                kk += 1
                t.append(cs)
            else:
                #print(cs)
                nt.append(cs)
    return t,nt



def readinput(s):
    """
    It takes a string and returns a set

    :param s: the string to be read
    :return: A set of strings.
    """
    if len(s) == 0 :
        return Set(0,[])
    else:
        cset = Set(0,[])
        ss = ""
        for i in s:
            if i != ',' and i != '|' and i != ';' and i !=  ' ' and i != '{' and i != '}' :
                ss = ss + i
            elif i == '{' or i == '}':
                continue
            else :
                cset.addelement(ss)
                ss = ""


        if len(ss) != 0:
            cset.addelement(ss)
        return cset


def whyis_topologie(T, s):
    """
    The function checks if the given set of sets is a topology on the given set.

    :param T: a list of sets
    :param s: the set of all elements
    :return: A boolean value.
    """
    whhy = []
    flag1 = 0
    for i in  T:
        if i.is_emptyset():
            #print("000")
            flag1 += 1
            break

    for i in  T:
        if i == s:
            flag1 += 1
            break

    if flag1 < 2 :
        st.write("1) ",str(Set(0,[])),",", s,r"$\not \in \tau$")
        return False


    st.write("1) ",str(Set(0,[])),",", s,r"$\in \tau$.")
    st.divider()



    #Combinations of families Union
    st.write("2) La union de todas la posibles familias de conjuntos de τ")
    flag2 = True
    for i in range(2,len(T)+1):
        cm = combinations(T,i)
        #print("Colecciones de Tamaño", i)
        #print(list(cm))

        for j in list(cm):
            st.write("U",j)
            FU = FamilySetUnion(j)
            blongTt = False
            for k in  T:
                if k == FU:
                    #print(FU,"∈ τ.")
                    blongTt = True
            if blongTt == False:
                #print(FU,"¬(∈) τ.")
                flag2 = False
                break

        #print("-------------")

    if(flag2 == False):
        st.write(r"$\not \in \tau$.")
        return False
    else:
        st.write(r"$\in \tau$.")

    st.divider()
    pairs = list(combinations(T,2))
    st.write("3) La intersección de todos los posibles pares de elementos de τ")
    flag3 =  True
    for i in  range(0,len((pairs))):
        st.write(pairs[i][0],"n",pairs[i][1])
        intr = pairs[i][0].Intersection(pairs[i][1])
        gg = False
        for j in T:
            if j == intr:
                gg = True
                break
        if gg == False:
            flag3 = False
            break

    if(flag3 == False):
        st.write(r"$\not \in \tau$.")
        return False

    st.write(r"$\in \tau$.")
    return True

##S1 = Set(2, [1,2])
##Sp = Set(3, [1,2,3])
##S2 = Set(4, ["A","B","C","D"])
##P = []
#P2 = []
#start = time.time()
#topologies_of_Set(Sp)
#end = time.time()
#
#print(end-start)
#
#
#print(S1 == Sp)

comentario="""
    Los pasos que seguimos para obtener las topologías de un conjunto finito de elementos son los siguientes :

    1)Obtenemos el conjunto potencia del conjunto dado.

    2)Una vez tenemos el conjunto potencia, procederemos a calcular todas las posibles combinaciones de elementos tomados
    en conjuntos de tamaño 2,... hasta n, de elementos del conjunto potencia.

    3) Con cada conjunto de combinaciones comprobamos cuales de ellas, cumplen las caracteristicas de una Topología

        3.1)Verificamos que el conjunto original y el conjunto vacío pertenescan a la Topología

        3.2)Calculamos todas las posibles combinaciones de elementos(tomados en conjuntos de 2 hasta n) de la topología y verificamos que la unión arbitraria de cualquier numero de elementos pertenezca a la topología

        3.3)Calculamos todas las posibles combinaciones de elementos tomados en conjuntos de 2 y verificamos que la intersección pertenezca a la topología

    4)Retornamos una lista con las topologias validas y otra con aquellas que no lo son.
"""

if 'sett' not in st.session_state:
    st.session_state['sett'] = Set(3,[1,2,3])

#st.title('UN POCO DE TOPOLOGIA')

st.markdown('''
<div class="content">
  <h1 class="title">UN POCO DE TOPOLOGIA
    <div class="aurora">
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
      <div class="aurora__item"></div>
    </div>
  </h1>

</div>
''',unsafe_allow_html=True)

st.header('Espacio Topológico')
st.divider()

cols1 = st.columns([.5,.5])
cont1 = st.container()

with cols1[0]:
    st.write(r'''Un espacio topológico es un par ordenado $(X, \tau)$, donde $X$ es un conjunto no vacío y $\tau$ es una colección de subconjuntos de $X$ que satisface las siguientes propiedades:

1. $\emptyset$ y $X$ están en $\tau$, es decir, el conjunto vacío y $X$ son conjuntos abiertos.
2. La intersección finita de conjuntos en $\tau$ está en $\tau$, es decir, si $U_i \in \tau$ para todo $i$ en un conjunto finito, entonces $\bigcap_{i} U_i \in \tau$.
3. La unión arbitraria de conjuntos en $\tau$ está en $\tau$, es decir, si $\{U_\alpha\}$ es una colección de conjuntos en $\tau$, entonces $\bigcup_{\alpha} U_\alpha \in \tau$.

Los conjuntos en $\tau$ se llaman conjuntos abiertos, y la colección $\tau$ se llama una topología en $X$.
''')

with cols1[1]:
    st.subheader('Topologías en un conjunto finito de elementos')
    s = st.text_input('Ingrese un conjunto','{1,2,3}')
    st.info('Ejemplo: {1,2,3,4} o 1,2,3,4}')
    stet = readinput(s)

    if (st.button('Calcular') or st.session_state['topologies'] != None) and len(s.strip().split(',')) < 5 :
        if (st.session_state['topologies']== None and st.session_state['topologies'] == None) or st.session_state['sett'] != stet:
            st.session_state['sett'] = stet
            with st.spinner('Espera un momento, estamos calculando las topologías ⌛...'):
                topologies, notopologies = topologies_of_Set(stet)
                st.session_state['topologies'] = topologies
                st.session_state['notopologies'] = notopologies

        op = st.selectbox('Seleccione una Opción', ['Topologías','No Topologías'])
        if op == 'Topologías':
            st.data_editor(pd.DataFrame(st.session_state['topologies']).fillna(""))
            indx = st.selectbox('Seleccione un Indice', list(range(len(st.session_state['topologies']))))
            with st.expander('¿Por que es una topología?'):
                whyis_topologie(st.session_state['topologies'][indx],stet)
        else:
            st.data_editor(pd.DataFrame(st.session_state['notopologies']).fillna(""))
            indx = st.selectbox('Seleccione un Indice', list(range(len(st.session_state['notopologies']))))
            with st.expander('¿Por que no es una topología?'):
                whyis_topologie(st.session_state['notopologies'][indx],stet)
    else:
        if len(s.strip().split(',')) >= 5:
            st.warning('El conjunto con 5 o mas elementos implica un tiempo de computo de 20 minutos o más 😨 ', icon="⚠️")
            cont1.markdown('''
            | Número de Elementos (n) | Número de Topologías Válidas | Número de "No Topologías" |
|-------------------------|-----------------------------|---------------------------|
|           0             |             1               |            1              |
|           1             |             2               |            2              |
|           2             |             4               |            12             |
|           3             |             29              |            35             |
|           4             |             355             |           101             |
|           5             |            6,786            |          1,674            |
|           6             |           204,226           |          1,547            |
|           7             |         8,777,608          |          32,208           |
|           8             |       552,278,850         |         17,977            |
|           9             |     50,651,204,504       |         8,532            |
|          10             |    6,581,333,312,554     |        58,865           |
|          11             | 1,200,805,559,164,394    |        110,126         |
|          12             |322,476,036,831,006,487   |        15,228         |
|          13             |124,368,486,718,720,872,000|   367,999,929,784,780  |
|          14             |68,315,377,525,720,948,623,028|6,676,291,983,745,026  |
|          15             |53,610,904,822,611,073,395,279,739,360|1,292,594,553,275,842,242,241,925|
|          16             |63,274,971,070,023,555,506,948,029,979,547|418,582,642,539,586,773,993,950,679,615,032,892|
|          17             |113,683,163,605,516,682,141,574,363,700,706,140|117,972,748,832,732,118,283,130,036,098,854,536,262,160|
|          18             |318,608,750,886,299,797,611,073,464,075,027,568,151|15,892,967,091,985,884,231,048,614,178,203,829,878,290,581,284|

            ''')


sac.divider(label='', icon='arrow-down-square', align='center')
st.header('Conjuntos Abiertos y Cerrados')
st.divider()
cols2 = st.columns([.5,.5])
with cols2[0]:
    r'''En un espacio topológico $(X, \tau)$, un conjunto $A \subseteq X$ se llama:

1. Abierto si $A \in \tau$.
2. Cerrado si su complemento $X \setminus A$ es abierto, es decir, $X \setminus A \in \tau$.

'''

with cols2[1]:
    tabs1 = st.tabs(["Abiertos Ejemplo 1", "Abiertos Ejemplo 2",'Cerrados Ejemplo 1'])

    with tabs1[0]:
        st.video('Videos/PAGINA1/Openset.mp4')

    with tabs1[1]:
        st.video('Videos/PAGINA1/Openset2.mp4')

    with tabs1[2]:
        st.video('Videos/PAGINA1/Closedset.mp4')



sac.divider(label='', icon='arrow-down-square', align='center',key='div2')
cols3 = st.columns([.5,.5])

with cols3[0]:
    st.header('Conjuntos Bases y Subbases')
    st.divider()
    r'''
Una colección $\mathcal{B}$ de conjuntos en un espacio topológico $(X, \tau)$ se llama una base para la topología $\tau$ si, para cada conjunto abierto $U \in \tau$ y para cada punto $x \in U$, existe al menos un conjunto $B \in \mathcal{B}$ tal que $x \in B \subseteq U$.
Una colección $\mathcal{S}$ de conjuntos en un espacio topológico $(X, \tau)$ se llama una subbase para la topología $\tau$ si la colección de todas las intersecciones finitas de conjuntos en $\mathcal{S}$ genera la topología $\tau$.
 '''

with cols3[1]:
    st.header('Topología Generada por una Métrica:')
    st.divider()
    r'''
Dado un espacio métrico $(X, d)$, la topología generada por la métrica $d$ en $X$ consiste en todos los conjuntos abiertos $U$ de acuerdo con la siguiente definición:
$$
U \in \tau_d \iff \forall x \in U, \exists \epsilon > 0 \text{ tal que } B_\epsilon(x) \subseteq U,
$$
donde $B_\epsilon(x)$ representa la bola abierta centrada en $x$ con radio $\epsilon$.

    '''


sac.divider(label='', icon='arrow-down-square', align='center',key='div3')
st.header('Punto Frontera')
st.divider()
cols4 = st.columns([.5,.5])

with cols4[0]:
    r'''
Dado un conjunto $A$ en un espacio topológico $(X, \tau)$, un punto $x$ se llama punto frontera de $A$ si para cualquier entorno abierto $U$ de $x$, la intersección de $U$ con $A$ y la intersección de $U$ con el complemento de $A$ no son vacías, es decir,

$$
x \text{ es un punto frontera de } A \iff
$$

$$
\forall U \in \tau, \left( U \cap A \neq \emptyset \text{ y } U \cap (X \setminus A) \neq \emptyset \right).
$$
    '''

with cols4[1]:
    st.video('Videos/PAGINA1/PuntoF.mp4')


sac.divider(label='', icon='arrow-down-square', align='center',key='div4')
cols5 = st.columns([.5,.5])

with cols5[1]:
    st.header('Frontera de un Conjunto')
    st.divider()
    r'''
La frontera de un conjunto $A$ en un espacio topológico $(X,\tau)$ denotada como $\partial A$, es el conjunto de todos los puntos frontera de $A$, es decir,

$$
\partial A = \{ x \in X \mid x \text{ es un punto frontera de } A \}.
$$
    '''




with cols5[0]:

    st.video('Videos/PAGINA1/Frontera.mp4')


sac.divider(label='', icon='arrow-down-square', align='center',key='div5')
cols6 = st.columns([.5,.5])




with cols6[0]:

    st.header('Punto de Acumulación')
    st.divider()
    r'''
Dado un conjunto $A$ en un espacio topológico $(X, \tau)$, un punto $x$ se llama punto de acumulación de $A$ si para cualquier entorno abierto $U$ de $x$, la intersección de $U$ con $A$ contiene al menos un punto distinto de $x$, es decir,

$$
x \text{ es un punto de acumulación de } A \iff \forall U \in \tau, \left( U \cap A \setminus \{x\} \neq \emptyset \right).
$$
    '''




with cols6[1]:

    st.header('Funciones Continuas')
    st.divider()
    r'''
    Sea $X$ un espacio topológico y $Y$ otro espacio topológico. Una función $f: X \rightarrow Y$ se dice continua si,
    para cada conjunto abierto $V$ en $Y$, el conjunto preimagen $f^{-1}(V)$ es un conjunto abierto en $X$. Formalmente,

Una función $f: X \rightarrow Y$ es continua si, para todo conjunto abierto $V \subseteq Y$, su preimagen $f^{-1}(V)$
es un conjunto abierto en $X$.'''

sac.divider(label='', icon='arrow-down-square', align='center',key='div6')
cols7 = st.columns([.5,.5])


with cols7[0]:
    st.header('Conjuntos Conexos')
    st.divider()
    r'''
Un conjunto $X$ en un espacio topológico $T$ se dice que es conexo si no se puede expresar como la unión de dos
conjuntos abiertos disjuntos no vacíos, es decir, si no existen conjuntos abiertos $U$ y $V$ en $T$ tales que:

$$
X = U \cup V
$$

$$
U \cap V = \emptyset
$$

$$
U \neq \emptyset, V \neq \emptyset
$$
'''

sac.divider(label='', icon='arrow-down-square', align='center',key='div7')
cols8 = st.columns([.5,.5])

with cols8[0]:
    st.header('Homeomorfismos')
    st.divider()
    r'''
    Dos espacios topológicos $X$ y $Y$ se dicen homeomorfos si existe una función biyectiva
    $f: X \rightarrow Y$ y su inversa $f^{-1}: Y \rightarrow X$, ambas continuas. En otras palabras,
    $X$ y $Y$ son homeomorfos si hay una correspondencia uno a uno entre sus conjuntos que preserva la estructura topológica.

    '''

with cols8[1]:
    st.video('Videos/PAGINA1/Homeomorfismo.mp4')


sac.divider(label='', icon='arrow-down-square', align='center',key='div8')
cols9 = st.columns([.5,.5])

with cols9[0]:
    st.header('Conjuntos Compactos')
    st.divider()
    r'''
Un conjunto $K$ en un espacio topológico $T$ se llama compacto si, para cualquier colección abierta $A_i$ de conjuntos
en $T$ que cubre $K$ (es decir, $K \subseteq \bigcup_i A_i$), existe una subcolección finita de $A_i$ que aún cubre $K$.

**Propiedades de los Conjuntos Compactos:**

- Los conjuntos compactos son cerrados en espacios de Hausdorff.
- Los conjuntos compactos son limitados en espacios métricos.
- El producto de conjuntos compactos en espacios topológicos también es compacto.
- En espacios métricos, un conjunto es compacto si y solo si es secuencialmente compacto
(cualquier secuencia tiene una subsucesión convergente).
'''





sac.divider(label='', icon='arrow-down-square', align='center',key='div9')
cols10 = st.columns([.5,.5])



with cols10[0]:
    st.header('Espacio Métrico')
    st.divider()
    r'''
Un espacio métrico es un par ordenado $(X, d)$ donde $X$ es un conjunto no vacío y $d: X \times X \rightarrow \mathbb{R}$ es una función llamada métrica que satisface las siguientes propiedades para todos los puntos $x, y, z$ en $X$:

1. **Positividad:** $d(x, y) \geq 0$ (la distancia entre dos puntos es siempre no negativa).
2. **Identidad de los Indiscernibles:** $d(x, y) = 0$ si y solo si $x = y$ (la distancia entre dos puntos es cero si y solo si son el mismo punto).
3. **Simetría:** $d(x, y) = d(y, x)$ (la distancia entre dos puntos es simétrica).
4. **Desigualdad Triangular:** $d(x, z) \leq d(x, y) + d(y, z)$ (la distancia entre dos puntos es siempre menor o igual a la suma de las distancias a un tercer punto).

**Bolas Abiertas en Espacios Métricos:**

La bola abierta de radio $\epsilon > 0$ centrada en un punto $x$ en un espacio métrico $(X, d)$ se denota como $B_\epsilon(x)$ y se define como:

$$
B_\epsilon(x) = \{y \in X \mid d(x, y) < \epsilon\}
$$
'''


with cols10[1]:
    st.header('Espacios Métricos Completos y Compactos')
    st.divider()
    r'''
    - Un espacio métrico $(X, d)$ se dice que es completo si cada sucesión de Cauchy en $X$ converge a un punto en $X$.
- Un espacio métrico $(X, d)$ se dice que es compacto si cada cubierta abierta de $X$ tiene una subcubierta finita, es decir, si cada colección de conjuntos abiertos que cubre $X$ puede reducirse a una colección finita que aún cubre $X$.

    '''



sac.divider(label='', icon='arrow-down-square', align='center',key='div10')
cols11 = st.columns([.5,.5])



with cols11[0]:
    st.header('Espacio de Hausdorff')
    st.divider()
    r'''
Un espacio topológico $X$ se dice que es un espacio de Hausdorff (o $T_2$) si, para cada par de puntos distintos $x$
y $y$ en $X$, existen conjuntos abiertos $U$ y $V$ en $X$ tales que $x$ pertenece a $U$, $y$ pertenece a $V$, y $U$ y
$V$ son disjuntos. En otras palabras, en un espacio de Hausdorff, es posible separar puntos distintos con conjuntos abiertos disjuntos.

**Propiedades de los Espacios de Hausdorff:**

- Los espacios de Hausdorff son $T_1$ (separados por puntos).
- Cualquier subconjunto finito de un espacio de Hausdorff es cerrado.
'''



with cols11[1]:
    st.header('Propiedades de $T_0, T_1, T_2$ y $T_3$')
    st.divider()
    r'''
**Propiedades de T0 y T1:**

- Un espacio topológico $X$ se dice que es $T_0$ si, para cada par de puntos distintos $x$ e $y$ en $X$, existe un
conjunto abierto $U$ que contiene a uno de los puntos pero no al otro.
- Un espacio topológico $X$ se dice que es $T_1$ si, para cada par de puntos distintos $x$ e $y$ en $X$,
existen conjuntos abiertos $U$ y $V$ tales que $x$ pertenece a $U$, $y$ pertenece a $V$, y $U$ no contiene a $y$ ni $V$ contiene a $x$.

**Espacios de T2 (Hausdorff) y T3:**

- Un espacio topológico $X$ es $T_2$ o de Hausdorff si es un espacio de Hausdorff.
- Un espacio topológico $X$ es $T_3$ si es $T_1$ y, para cada par de conjuntos cerrados disjuntos $A$ y $B$ en $X$,
existen conjuntos abiertos disjuntos $U$ y $V$ tales que $A$ está contenido en $U$ y $B$ está contenido en $V$.


'''



sac.divider(label='', icon='arrow-down-square', align='center',key='div11')
cols12 = st.columns([.5,.5])



with cols12[0]:
    st.header('Variedades Topológicas')
    st.divider()
    r'''
Una variedad topológica es un espacio topológico $(M, \mathcal{T})$ que satisface las siguientes condiciones:

1. $M$ es un conjunto no vacío.
2. $\mathcal{T}$ es una topología en $M$ que es Hausdorff y localmente euclidiana, es decir, para cada punto $p$ en $M$,
existe un entorno $U$ de $p$ en $\mathcal{T}$ que es homeomorfo a un subconjunto abierto de $\mathbb{R}^n$ para algún $n$.

'''





with cols12[1]:
    st.header('Variedades de Dimensión n')
    st.divider()
    r'''
Una variedad topológica $M$ se llama una variedad de dimensión $n$ si cada punto $p$ en $M$ tiene un entorno homeomorfo
a un subconjunto abierto de $\mathbb{R}^n$. En otras palabras, localmente, una variedad de dimensión $n$ se parece a $\mathbb{R}^n$.

**Ejemplos de Variedades Topológicas:**

- La esfera $S^n$ es una variedad topológica de dimensión $n$.
- El plano euclidiano $\mathbb{R}^n$ es una variedad topológica de dimensión $n$.
- El toro $T^2$ es una variedad topológica de dimensión $2$.

'''


sac.divider(label='', icon='arrow-down-square', align='center',key='div12')
cols13 = st.columns([.5,.5])



with cols13[0]:

    st.header('Homotopía')
    st.divider()
    r'''
En topología, dos aplicaciones continuas $f$ y $g$ de un espacio topológico $X$ en un espacio topológico $Y$ se
consideran homotópicas si existe una función continua $H: X \times [0,1] \rightarrow Y$ tal que, para todo $x$ en $X$,
$H(x,0) = f(x)$ y $H(x,1) = g(x)$. La función $H$ se llama homotopía entre $f$ y $g$, y esta noción establece una
relación de equivalencia entre aplicaciones continuas.
'''

with cols13[1]:
    st.video('Videos/PAGINA1/Homotopia.mp4')


sac.divider(label='', icon='arrow-down-square', align='center',key='div13')
cols14 = st.columns([.5,.5])

with cols14[0]:

    st.header('Caminos y Lazos')
    st.divider()
    r'''
- Un camino en un espacio topológico $X$ es una función continua $\gamma: [0, 1] \rightarrow X$. El punto $\gamma(0)$
se llama el punto inicial y $\gamma(1)$ el punto final del camino.

- Un lazo en un espacio topológico $X$ es un camino $\gamma: [0, 1] \rightarrow X$ tal que $\gamma(0) = \gamma(1)$,
es decir, el punto inicial y el punto final del camino son el mismo.
'''

with cols14[1]:

    st.header('Grupo Fundamental')
    st.divider()
    r'''
El grupo fundamental $\pi_1(X, x_0)$ de un espacio topológico $X$ con un punto base $x_0$ es un grupo que consiste en
clases de equivalencia de lazos basados en $x_0$, donde la operación del grupo es la concatenación de lazos y la inversa
de un lazo es su inverso homotópico.
'''


temario = '''

1. **Espacios Topológicos Básicos:**
   - Conjuntos abiertos y cerrados en un espacio topológico.
   - Conjuntos bases y subbases.
   - Topología generada por una métrica.

2. **Conexión y Separación:**
   - Espacios conexos y componentes conexas.
   - Espacios de Hausdorff y separación de puntos.
   - Espacios compactos y su importancia.

3. **Funciones Continuas:**
   - Definición de continuidad en el contexto topológico.
   - Homeomorfismos y funciones de inclusión.
   - Espacios topológicos producto.

4. **Compacidad y Propiedades de Conjuntos:**
   - Conjuntos compactos y su relación con subconjuntos cerrados y acotados.
   - Conjuntos de Lindelöf.
   - Propiedad de Borel-Lebesgue.

'''

