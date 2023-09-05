from manim import *

class Esfera2D(ThreeDScene):
    def construct(self):
        texto_disco_3 = VGroup(
            Text("Dimensión 3"),
            MathTex(r"\Vert (x,y,z) \Vert \leq 1")
        ).arrange(DOWN).to_corner(UL)
        titulo = MathTex("Disco D^n en R^n").scale(0.9).to_edge(DR)
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[BLUE_D, BLUE_E], resolution=(15, 32),fill_opacity=2,
        )
        esphere2 = Circle(radius=1.5)
        texto_esfera_2 = VGroup(
            Text("Dimensión 1"),
            MathTex(r"S^2 = \partial D^3")
        ).arrange(DOWN).to_corner(UL)
        esfera_2_def = VGroup(texto_esfera_2)


        disco_3_def = VGroup(sphere, texto_disco_3)
        self.renderer.camera.light_source.move_to(2*IN) # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes))
        self.add_fixed_in_frame_mobjects(titulo)
        self.add_fixed_in_frame_mobjects(disco_3_def)
        self.play(Create(disco_3_def))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.play(Transform(disco_3_def, esphere2))
        self.add_fixed_in_frame_mobjects(esfera_2_def)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(2)
