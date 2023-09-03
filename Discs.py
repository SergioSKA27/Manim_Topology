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
        titulo = MathTex("Disco D^n en R^n").scale(0.9).to_edge(DR)

        # Dibujar un disco de dimensión 0 con título y definición
        disco_0 = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(axes.coords_to_point(0, 0))
        texto_disco_0 = VGroup(
            Text("Dimensión 0"),
            Text(r"Un punto en el plano")
        ).arrange(DOWN).to_corner(UL)
        disco_0_def = VGroup(disco_0, texto_disco_0)
        # Dibujar un disco de dimensión 1 con título y definición
        # Crear una línea numérica en 3D
        number_line = NumberLine(
            x_range=[-1, 1],
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            line_to_number_buff=SMALL_BUFF,
        )
        texto_disco_1 = VGroup(
            Text("Dimensión 1"),
            MathTex(r"|x| \leq 1")
        ).arrange(DOWN).to_corner(UL)
        disco_1_def = VGroup(number_line, texto_disco_1)

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
