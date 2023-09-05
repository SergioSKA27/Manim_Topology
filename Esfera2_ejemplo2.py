from manim import *

class Esfera2Example2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.wait()
