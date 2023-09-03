from manim import *

class Homotopia(Scene):
    def construct(self):
        # Definir las dos funciones iniciales
        f = lambda x, y: x**2 + y**2  # Por ejemplo, una circunferencia
        g = lambda x, y: x + y        # Por ejemplo, una línea

        # Crear un plano cartesiano
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )

        # Graficar f inicialmente
        grafica_f = axes.plot(lambda x: f(x, 0), color=RED)

        # Graficar g inicialmente
        grafica_g = axes.plot(lambda x: g(x, 0), color=GREEN)

        # Añadir el título "Homotopía"
        titulo = Text("Homotopía").scale(0.5).to_edge(UP)

        # Anima la transición entre f y g y muestra el título
        self.play(Create(axes), Create(titulo))
        self.play(Transform(grafica_f, grafica_g), run_time=5)
        self.wait(5)
