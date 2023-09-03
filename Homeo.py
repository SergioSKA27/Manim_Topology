from manim import *

class CirculoACuadrado(Scene):
    def construct(self):
        # Crea un círculo
        circulo = Circle()
        circulo.set_fill(BLUE, opacity=0.5)

        # Crea un cuadrado
        cuadrado = Square()
        cuadrado.set_fill(RED, opacity=0.5)

        # Añade el título "Homeomorfismo"
        titulo = Tex("Homeomorfismo").scale(1.5)

        # Anima la transformación del círculo al cuadrado
        self.play(Create(circulo))
        self.wait(2)
        self.play(Transform(circulo, cuadrado), FadeIn(titulo))
        self.wait(5)
