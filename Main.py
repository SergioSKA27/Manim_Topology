import streamlit as st
from streamlit_lottie import st_lottie
# Título de la aplicación
st.title("Topology Manim Videos")

st_lottie("https://lottie.host/4f56c993-fd92-42e4-9945-c5df0387f986/mTRLkrdQVJ.json")
# Subtítulo
st.header("Selecciona un video de Manim:")

# Lista de videos disponibles
videos = ["Homeomorfismo",
"Discos_D0_D2",
"DiscoD3",
"Esferas_S0_S1",
"EsferaS2",
"EsferaS2Ejemplo2",
"Homotopia",
"Torus_knot",
"TorusKnot2Dto3D"]


# Widget de selección de video
selected_video = st.selectbox("Selecciona un video:", videos)

# Visualizador de video
video_widget = st.empty()  # Widget para mostrar el video

# Deslizador para cambiar entre los videos
video_index = videos.index(selected_video)
video_index = st.slider("Cambia el video:", 0, len(videos) - 1, video_index)

# Actualizar el video seleccionado
selected_video = videos[video_index]

# Diccionario de videos y sus enlaces
video_links = {
   'Homeomorfismo':"Videos/CirculoACuadrado.mp4",
"Discos_D0_D2":"Videos/Disco.mp4",
"DiscoD3":"Videos/ThreeDLightSourcePosition.mp4",
"Esferas_S0_S1":"/Videos/Esfera.mp4",
"EsferaS2":"Videos/Esfera2D.mp4",
"EsferaS2Ejemplo2":"Videos/Esfera2Example2.mp4",
"Video":"Videos/Homotopia.mp4",

"Torus_knot":"Videos/Torus_knot.mp4",
"TorusKnot2Dto3D":"Videos/TorusKnot2Dto3D.mp4"}

# Mostrar el video seleccionado
video_widget.video(video_links[selected_video])






r'''
# Título: Explorando Nudos y Enlaces en Topología

## Objetivo:

El objetivo fundamental de esta exposición es desvelar el misterioso mundo de los nudos y enlaces en la topología, demostrando cómo estos conceptos abstractos se extienden mucho más allá de las páginas de los libros de matemáticas. A través de ejemplos visualmente atractivos y aplicaciones sorprendentes en campos como la biología, la tecnología y el arte, invitamos a nuestra audiencia a descubrir cómo los nudos y enlaces son protagonistas en la resolución de problemas complejos y en la creación de belleza en nuestras vidas cotidianas.

**I. Introducción**

**A. Definición de Topología**

La topología es una rama de la matemática que se ocupa del estudio de propiedades geométricas que permanecen inalteradas bajo deformaciones continuas, como la flexión y el estiramiento, pero no la rotación ni la perforación. En otras palabras, la topología se enfoca en entender las propiedades espaciales de objetos y figuras que son independientes de su tamaño, forma o ubicación exacta en el espacio.

En el corazón de la topología se encuentra la noción de continuidad, donde se considera qué partes de una figura pueden ser transformadas de manera continua sin romperlas o deformarlas de manera fundamental. Esto nos permite explorar conceptos abstractos de cercanía, convergencia y conexión que tienen aplicaciones sorprendentes en una amplia gama de campos, desde la física y la biología hasta la informática y la teoría de números.

**B. Importancia de los Nudos y Enlaces en Topología**

Dentro de la topología, los nudos y enlaces son objetos de estudio particularmente fascinantes y relevantes. Los nudos son estructuras simples y cerradas que pueden considerarse como una cuerda atada en una serie de cruces y bucles. Los enlaces, por otro lado, son conjuntos de nudos que se interconectan de manera especial. Aunque estos conceptos pueden parecer abstractos a primera vista, tienen un profundo impacto en la teoría de nudos y en la topología en general.

La importancia de los nudos y enlaces radica en su capacidad para representar problemas y conceptos complejos de manera simplificada. Se utilizan en diversas disciplinas, como la biología molecular para describir la estructura del ADN, en la física para modelar el comportamiento de partículas subatómicas, y en la teoría de números para abordar cuestiones de simetría y clasificación.

**C. Objetivos de la Exposición**

El propósito principal de esta exposición es explorar la fascinante intersección entre los nudos, los enlaces y la topología, revelando cómo estos conceptos abstractos se aplican en la ciencia, la matemática y la vida cotidiana. Los objetivos específicos incluyen:

1. **Comprender la definición y los fundamentos de la topología.** Exploraremos cómo la topología se diferencia de otras disciplinas matemáticas y cómo se enfoca en la continuidad y la conectividad.

2. **Explorar la naturaleza de los nudos y enlaces.** A través de ejemplos visuales y conceptuales, veremos cómo los nudos y enlaces se representan y analizan en topología.

3. **Destacar la importancia de los nudos y enlaces en diversas áreas.** Mostraremos cómo estos conceptos abstractos se aplican en biología, física, matemáticas y más, y cómo ayudan a resolver problemas y comprender el mundo que nos rodea.

4. **Fomentar la apreciación de la topología como una rama de la matemática relevante y accesible.** Queremos demostrar que la topología y sus aplicaciones pueden ser apasionantes y comprensibles para una amplia audiencia.



### **II. Nudos en Topología**

**A. Definición de un Nudo**

Un **nudo**, en el contexto de la topología, es una estructura matemática que consiste en una **curva cerrada simple** en el espacio tridimensional, sin puntos dobles ni intersecciones consigo misma, excepto en los extremos donde se cierra la curva. Matemáticamente, un nudo se representa como una función continua $K : S^1 \rightarrow \mathbb{R}^3$, donde $S^1$ es la esfera unitaria en $\mathbb{R}^2$. Esta representación garantiza que el nudo sea un objeto sin autocortes ni superposiciones.

**B. Ejemplos de Nudos Simples**

Los **nudos simples** son los nudos más básicos y se caracterizan por no tener componentes adicionales ni intersecciones. Algunos ejemplos notables de nudos simples son:

1. **Nudo Trivial ($0_1$):** También conocido como el nudo sin nudos, se representa como una simple curva cerrada que no contiene cruces ni intersecciones.

   ![Nudo Trivial](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Triivialknot.svg/220px-Triivialknot.svg.png)

2. **Nudo de Lazo Simple ($1_1$):** Este nudo se forma al tomar una cuerda y enrollarla en forma de un solo bucle sin cruces.

   ![Nudo de Lazo Simple](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Overhand-knot.gif/150px-Overhand-knot.gif)

**C. Representación Visual de Nudos**

Los nudos se pueden representar visualmente de varias formas. Una de las representaciones más comunes es utilizando diagramas de proyección en el plano, donde los cruces se indican mediante cruces en el dibujo. Esta representación facilita el estudio y la comparación de diferentes tipos de nudos.

**D. Características Clave de los Nudos**

Los nudos tienen características clave que los distinguen:

1. **Número de Cruces:** El número de cruces en un diagrama de proyección de un nudo es una característica importante que ayuda a distinguir diferentes tipos de nudos. Dos nudos con diferente número de cruces son topológicamente distintos.

2. **Orientación:** La orientación de un nudo se refiere a la dirección en que se sigue la curva cerrada. Invertir la orientación de un nudo puede llevar a un nudo topológicamente diferente.

**E. Ejemplos de Nudos Notables**

Algunos ejemplos de nudos notables incluyen:

- **Nudo de Trébol ($3_1$):** Un nudo con tres cruces y una forma característica de trébol.

- **Nudo de Ocho ($4_1$):** Un nudo con cuatro cruces que se asemeja al número ocho.

Estos ejemplos ilustran la diversidad de formas que pueden tomar los nudos y su importancia en la topología y otras disciplinas.




### **III. Enlaces en Topología**

**A. Definición de un Enlace**

Un **enlace** en el contexto de la topología es una colección finita de nudos inmersos en el espacio tridimensional $\mathbb{R}^3$. Cada uno de los nudos que componen un enlace es una curva cerrada simple, y estos nudos pueden interconectarse de diversas maneras sin superposiciones ni cortes en el espacio tridimensional. En esencia, un enlace es una configuración de nudos entrelazados o conectados entre sí.

**B. Diferencia entre Nudos y Enlaces**

Es fundamental comprender la diferencia clave entre nudos y enlaces:

- Un **nudo** es una única curva cerrada simple sin puntos dobles ni intersecciones consigo misma, excepto en los extremos donde se cierra la curva.

- Un **enlace** es una colección de nudos, es decir, múltiples curvas cerradas simples, que pueden interconectarse o entrelazarse de diversas formas, sin intersecciones ni cortes adicionales.

**C. Representación Visual de Enlaces**

La representación visual de enlaces es similar a la de nudos, pero con la adición de múltiples curvas cerradas que se entrelazan o conectan entre sí. Los diagramas de proyección en el plano son una herramienta común para visualizar enlaces, donde cada nudo dentro del enlace se representa con una línea y los cruces se indican con símbolos específicos.

**D. Tipos de Enlaces**

Existen dos tipos principales de enlaces en topología:

1. **Enlaces Simples:** Los enlaces simples son aquellos en los que todos los nudos que lo componen son topológicamente equivalentes a un nudo simple, es decir, no tienen intersecciones internas y pueden desenredarse en una sola curva cerrada simple sin cortes adicionales.

2. **Enlaces Compuestos:** Los enlaces compuestos son aquellos que incluyen al menos un nudo que no es topológicamente equivalente a un nudo simple. Estos enlaces son más complejos y pueden requerir un análisis topológico más profundo para comprender su estructura.

**E. Ejemplos de Enlaces Notables**

Uno de los enlaces más notables en topología es el **Enlace Borromeo**, que consiste en tres anillos entrelazados de tal manera que, si se corta cualquiera de ellos, los otros dos se separan. Es un ejemplo intrigante de cómo los enlaces pueden ser sorprendentemente interconectados y tienen propiedades topológicas únicas.

![Enlace Borromeo](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/BorromeanRings123.png/220px-BorromeanRings123.png)




### **IV. Propiedades y Características de Nudos y Enlaces**

**A. Invariancia Topológica**

**1. Definición**

La **invariancia topológica** se refiere a una propiedad fundamental de los nudos y enlaces que no cambia bajo transformaciones topológicas. En otras palabras, si dos nudos o enlaces son topológicamente equivalentes, compartirán las mismas propiedades topológicas, como el número de cruces y la estructura de interconexión, a pesar de que puedan tener apariencias visuales diferentes.

**2. Ejemplos de Invariancia (Nudo Trivial)**

Un ejemplo claro de invariancia topológica se encuentra en el **nudo trivial**. Este nudo, que es simplemente una curva cerrada sin cruces, es topológicamente equivalente a sí mismo bajo deformaciones continuas, como estirar, retorcer o doblar la cuerda sin cortarla. Esto ilustra cómo las transformaciones topológicas preservan las propiedades esenciales de los nudos y enlaces.

**B. Diagramas de Proyección de Nudos**

**1. Representación Plana de Nudos**

Los **diagramas de proyección de nudos** son representaciones planas de nudos y enlaces en el plano o en superficies bidimensionales. Estos diagramas permiten visualizar y analizar la estructura de los nudos y enlaces de manera más accesible. Los cruces se indican mediante cruces en el dibujo, y las interconexiones se representan gráficamente.

**2. Notación de Dowker-Thistlethwaite**

La **notación de Dowker-Thistlethwaite** es una notación específica utilizada para describir nudos y enlaces en diagramas de proyección. Proporciona una forma sistemática de enumerar los cruces en un diagrama de proyección y permite una clasificación más precisa de los nudos. Esta notación es especialmente útil para comparar y estudiar distintos nudos y enlaces.

**C. Número de Cruces como Invariante**

El **número de cruces** en un diagrama de proyección de un nudo es una propiedad invariante topológica. Dos nudos topológicamente equivalentes siempre tendrán el mismo número de cruces, lo que significa que esta característica es una herramienta importante para distinguir entre diferentes tipos de nudos.

**D. Enlaces no Equivalentes**

La invariancia topológica nos permite establecer que algunos enlaces no son equivalentes. Esto significa que, incluso si dos enlaces se ven diferentes, si uno de ellos no puede ser transformado en el otro mediante deformaciones continuas sin cortes ni pegamentos, entonces son topológicamente distintos.

**E. Teorema del Nudo de Alexander-Briggs**

El **Teorema del Nudo de Alexander-Briggs** establece que dos nudos con el mismo polinomio de Alexander (una invariante algebraica) son topológicamente equivalentes. Esto proporciona una poderosa herramienta para determinar la equivalencia topológica entre nudos.

**F. El Problema de la Trivialidad**

El **problema de la trivialidad** se refiere a la pregunta de si un nudo dado es topológicamente equivalente al nudo trivial. Resolver este problema es un desafío fundamental en la teoría de nudos y enlaces y está relacionado con la comprensión de las propiedades de los nudos en términos de invariancia topológica.



### **V. Aplicaciones de Nudos y Enlaces**

**A. Matemáticas**

**1. Teoría de Nudos y Topología**

La **teoría de nudos** es una rama importante de las matemáticas que utiliza conceptos topológicos para estudiar las propiedades y clasificaciones de los nudos y enlaces. Los matemáticos han desarrollado innumerables invariantes topológicos para distinguir entre diferentes tipos de nudos, lo que ha llevado a avances significativos en la topología geométrica y la teoría de la homología.

**2. Teoría de Grafos y Teoría de Grupos**

Los nudos y enlaces se han relacionado con la **teoría de grafos** y la **teoría de grupos**, lo que ha llevado a la resolución de problemas complejos en estas áreas. Por ejemplo, se pueden representar nudos mediante grafos planos y se pueden aplicar técnicas de teoría de grupos para estudiar sus propiedades algebraicas.

**B. Ciencia y Tecnología**

**1. Biología Molecular (ADN)**

Los nudos y enlaces son cruciales en la **biología molecular** para comprender la estructura del **ADN** (ácido desoxirribonucleico). El ADN a menudo se superenrolla y forma estructuras en forma de nudos para empaquetarse eficientemente en las células. La topología del ADN influye en procesos biológicos como la replicación, la transcripción y la recombinación genética.

**2. Criptografía (Nudos y Seguridad)**

La topología de los nudos se ha utilizado en **criptografía** para mejorar la seguridad de los sistemas de encriptación. Los métodos criptográficos basados en nudos aprovechan la dificultad de desatar nudos complejos para proteger la información y desarrollar sistemas de seguridad robustos.

**C. Arte y Cultura**

**1. Arte Visual y Diseño**

Los nudos y enlaces han inspirado a artistas y diseñadores en la creación de patrones, joyería y obras de arte visuales. La belleza de las estructuras de nudos se refleja en la estética de muchas culturas, y su representación gráfica se utiliza en el diseño de logotipos y símbolos.

**2. Simbolismo Cultural (Ej. Nudos Celtas)**

Los **nudos celtas** son un ejemplo destacado de cómo los nudos y enlaces tienen un profundo simbolismo cultural en algunas sociedades. Los nudos celtas, con sus interconexiones intrincadas, a menudo se asocian con conceptos como la unidad, la eternidad y la interdependencia, y se encuentran en la iconografía celta y en la ornamentación de manuscritos antiguos.



'''
