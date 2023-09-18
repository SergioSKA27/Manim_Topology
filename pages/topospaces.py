import streamlit as st
from itertools import combinations, permutations,chain
from os import system
import time
import copy
import pandas as pd
from threading  import Thread

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
st.set_page_config(layout="wide")


#Created by: Lopez Martinez Sergio Demis
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

    kk = 1

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
        print("1) ",str(Set(0,[])),",", s,"¬(E) τ.")
        return False


    print("1) ",str(Set(0,[])),",", s,"E τ.")
    print("---------------------------------------------")



    #Combinations of families Union
    print("2) La union de todas la posibles familias de conjuntos de τ")
    flag2 = True
    for i in range(2,len(T)+1):
        cm = combinations(T,i)
        #print("Colecciones de Tamaño", i)
        #print(list(cm))

        for j in list(cm):
            print("U",j)
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
        print("¬(E) τ.")
        return False
    else:
        print("E τ.")

    print("---------------------------------------------")
    pairs = list(combinations(T,2))
    print("3) La intersección de todos los posibles pares de elementos de τ")
    flag3 =  True
    for i in  range(0,len((pairs))):
        print(pairs[i][0],"n",pairs[i][1])
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
        print("¬(E) τ.")
        return False

    print("E τ.")
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



st.header('UN POCO DE TOPOLOGIA')
st.header('Espacio Topológico')
st.divider()

cols1 = st.columns([.5,.5])


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
    st.info('Ejemplo: {1,2,3,4} o 1,2,3,4')
    stet = readinput(s)
    if st.button('Calcular'):
        with st.spinner('Espera un momento, estamos calculando las topologías ⌛...'):
            topologies, notopologies = topologies_of_Set(stet)
        st.data_editor(pd.DataFrame(topologies).fillna(""))

st.header('Conjuntos Abiertos y Cerrados en un Espacio Topológico')
st.divider()
cols2 = st.columns([.5,.5])
with cols2[0]:
    r'''En un espacio topológico $(X, \tau)$, un conjunto $A \subseteq X$ se llama:

1. Abierto si $A \in \tau$.
2. Cerrado si su complemento $X \setminus A$ es abierto, es decir, $X \setminus A \in \tau$.

'''

with cols2[1]:
    tabs1 = st.tabs(["Abiertos Ejemplo 1", "Abiertos Ejemplo 2"])

    with tabs1[0]:
        st.video('Videos/PAGINA1/Openset.mp4')

    with tabs1[1]:
        st.video('Videos/PAGINA1/Openset2.mp4')
