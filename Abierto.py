from manim import *

class ConjuntoAbierto(Scene):
    def construct(self):
        # Dibuja el espacio topológico (una línea de números)
        espacio = NumberLine(
            x_range=[-5,5],
            include_numbers=True,
            include_ticks=True
        )

        # Dibuja un conjunto abierto (por ejemplo, un intervalo abierto)
        conjunto_abierto = NumberLine(
            x_range=[-5,5],
            color=BLUE
        )

        # Añade el conjunto abierto al espacio topológico
        self.add(espacio, conjunto_abierto)

        # Agrega texto descriptivo
        texto = Text("Conjunto Abierto")
        texto.next_to(espacio, DOWN)
        self.add(texto)

        # Anima la revelación del conjunto abierto
        self.play(Create(conjunto_abierto))
        self.wait(2)
        # Anima la desaparición del conjunto abierto
        self.play(FadeOut(conjunto_abierto))
