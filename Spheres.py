from manim import *

class Disco(Scene):
    def construct(self):
        # Crear un plano cartesiano
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )

        # Añadir el título
        titulo = MathTex("Esfera S^n en D^{n-1}").scale(0.9).to_edge(DR)

        # Dibujar un disco de dimensión 0 con título y definición
        esfera_0 = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(axes.coords_to_point(1, 0))
        esfera_01 = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(axes.coords_to_point(-1, 0))
        number_line = NumberLine(
            x_range=[-1, 1],
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            line_to_number_buff=SMALL_BUFF,
        )
        texto_esfera_0 = VGroup(
            Text("Dimensión 0"),
            MathTex(r"S^0 = \partial D^1")
        ).arrange(DOWN).to_corner(UL)
        disco_0_def = VGroup(esfera_0, esfera_01,texto_esfera_0)




        # Dibujar una esfera de dimensión 1 con título y definición
        esfera_1 = Circle(radius=1, color=GREEN, fill_opacity=0).move_to(axes.coords_to_point(0, 0))
        texto_esfera_1 = VGroup(
            Text("Dimensión 1"),
            MathTex(r"S^1 = \partial D^2")
        ).arrange(DOWN).to_corner(UL)
        disco_1_def = VGroup(number_line, texto_esfera_1)

        # Dibujar un disco de dimensión 1 con título y definición
        disco_2 = Circle(radius=1, color=BLUE, fill_opacity=0.5).move_to(axes.coords_to_point(0, 0))
        texto_disco_2 = VGroup(
            Text("Dimensión 2"),
            MathTex(r"||(x,y)|| \leq 1")
        ).arrange(DOWN).to_corner(UL)
        disco_2_def = VGroup(disco_2, texto_disco_2)

        # Anima la transición entre los discos y muestra los títulos y definiciones
        self.play(Create(axes), Create(titulo))
        self.play(Create(disco_0_def))
        self.wait(5)
        self.play(Create(disco_1_def),Transform(disco_0_def, disco_1_def))
        self.wait(5)
        self.play(Create(disco_2_def),Transform(disco_1_def, disco_2_def))
        self.wait(3)
