""" Rotation vector """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from matplotlib.patches import Circle
from scipy.spatial.transform import Rotation
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import proj3d

""" Global variables """
phase_step_deg = 1.
radius_world = 4.

""" Animation control """
is_play = False
is_tilt = False
is_precession = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Create figure and axes """
title_ax0 = "Rotation vector"
title_tk = title_ax0

x_min = -4.
x_max = 4.
y_min = -4.
y_max = 4.
z_min = -4.
z_max = 4.

fig = Figure()
ax0 = fig.add_subplot(111, projection="3d")
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("y")
ax0.set_zlabel("z")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

""" Embed in Tkinter """
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill="both")

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

""" Global objects of Tkinter """
var_phase_stp = tk.StringVar(root)
var_radius = tk.StringVar(root)

""" Classes and functions """


class Counter:
    def __init__(self, is3d=None, ax=None, xy=None, z=None, label=""):
        self.is3d = is3d if is3d is not None else False
        self.ax = ax
        self.x, self.y = xy[0], xy[1]
        self.z = z if z is not None else 0
        self.label = label

        self.count = 0

        if not is3d:
            self.txt_step = self.ax.text(self.x, self.y, self.label + str(self.count))
        else:
            self.txt_step = self.ax.text2D(self.x, self.y, self.label + str(self.count))
            self.xz, self.yz, _ = proj3d.proj_transform(self.x, self.y, self.z, self.ax.get_proj())
            self.txt_step.set_position((self.xz, self.yz))

    def count_up(self):
        self.count += 1
        self.txt_step.set_text(self.label + str(self.count))

    def reset(self):
        self.count = 0
        self.txt_step.set_text(self.label + str(self.count))

    def get(self):
        return self.count


class WorldCircle:
    def __init__(self, ax, phase_step, radius):
        self.ax = ax
        self.phase_step = phase_step
        self.radius = radius

        self.angle_space = np.arange(0, 360)

        self.x_circle = self.radius * np.cos(self.angle_space * np.pi / 180.)
        self.z_circle = self.radius * np.sin(self.angle_space * np.pi / 180.)
        self.y_circle = self.angle_space * 0.

        self.plt_circle, = self.ax.plot(self.x_circle, self.y_circle, self.z_circle,
                                        linewidth=1, linestyle="-", color="gray")

        self.phase = np.array([self.radius, 0., 0.])
        self.phase_center = np.array([0., -1., 0.])

        self.x,  self.y, self.z = 0., 0., 0.
        self.u, self.v, self.w = self.phase[0], self.phase[1], self.phase[2]
        self.line_width = 1
        self.color = "gray"
        self.line_style = "--"

        self.line_phase, = self.ax.plot([self.x, self.u], [self.y, self.v], [self.z, self.w],
                                        linewidth=self.line_width, color=self.color, linestyle=self.line_style)

    def rotate(self):
        rot_matrix = Rotation.from_rotvec(self.phase_step * self.phase_center)
        self.phase = rot_matrix.apply(self.phase)
        self.u, self.v, self.w = self.phase[0], self.phase[1], self.phase[2]
        self.line_phase.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])

    def get_phase(self):
        if self.radius != 0:
            return self.phase
        else:
            return np.array([0., 0., 0.])

    def set_phase_step(self, angle):
        self.phase_step = angle

    def reset(self):
        self.phase = np.array([self.radius, 0., 0.])
        self.u, self.v, self.w = self.phase[0], self.phase[1], self.phase[2]
        self.line_phase.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])

    def set_radius(self, r):
        self.radius = r
        self.x_circle = self.radius * np.cos(self.angle_space * np.pi / 180.)
        self.y_circle = self.angle_space * 0.
        self.z_circle = self.radius * np.sin(self.angle_space * np.pi / 180.)

        self.plt_circle.set_data_3d(np.array(self.x_circle), np.array(self.y_circle), np.array(self.z_circle))

        if self.radius != 0:
            self.phase = self.radius * self.phase / np.linalg.norm(self.phase)
            self.u, self.v, self.w = self.phase[0], self.phase[1], self.phase[2]
            self.line_phase.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])


class LightPhaseCircle:
    def __init__(self, ax, phase_step, radius):
        self.ax = ax
        self.phase_step = phase_step
        self.radius = radius

        self.angle_space = np.arange(0, 360)

        self.x_circle = self.radius * np.cos(self.angle_space * np.pi / 180.)
        self.y_circle = self.radius * np.sin(self.angle_space * np.pi / 180.)
        self.z_circle = self.angle_space * 0.

        self.plt_circle, = self.ax.plot(self.x_circle, self.y_circle, self.z_circle,
                                        linewidth=1, linestyle="-", color="red")

        self.rotate_center = np.array([0., -1., 0.])

    def rotate_offset(self, x, y, z):
        rot_matrix = Rotation.from_rotvec(self.phase_step * self.rotate_center)
        x_circle_rotated = []
        y_circle_rotated = []
        z_circle_rotated = []
        for i in range(len(self.angle_space)):
            vector_point = np.array(
                [self.x_circle[i], self.y_circle[i], self.z_circle[i]])
            point_rotated = rot_matrix.apply(vector_point)
            x_circle_rotated.append(point_rotated[0])
            y_circle_rotated.append(point_rotated[1])
            z_circle_rotated.append(point_rotated[2])
            self.x_circle[i] = point_rotated[0]
            self.y_circle[i] = point_rotated[1]
            self.z_circle[i] = point_rotated[2]

        self.plt_circle.set_data_3d(np.array(self.x_circle) + x,
                                    np.array(self.y_circle) + y,
                                    np.array(self.z_circle) + z)

    def reset(self):
        self.x_circle = self.radius * np.cos(self.angle_space * np.pi / 180.)
        self.y_circle = self.radius * np.sin(self.angle_space * np.pi / 180.)
        self.z_circle = self.angle_space * 0.

    def set_phase_step(self, angle):
        self.phase_step = angle


class LightArrow:
    def __init__(self, ax, phase_step):
        self.ax = ax
        self.phase_step = phase_step

        self.color = "red"

        self.vector = np.array([0., 0., 1])
        self.vector_arrow = self.vector * np.rad2deg(self.phase_step)

        self.x, self.y, self.z = 0., 0., 0.
        self.u, self.v, self.w = self.vector_arrow[0], self.vector_arrow[1], self.vector_arrow[2]
        self.quiver = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                     length=1, linewidth=2, color=self.color, normalize=False)

        self.phase = np.array([1., 0., 0.])

        self.x, self.y, self.z = 0., 0., 0.
        self.u, self.v, self.w = self.phase[0], self.phase[1], self.phase[2]
        self.line_phase, = self.ax.plot([self.x, self.u], [self.y, self.v], [self.z, self.w],
                                        linewidth=1, color=self.color, linestyle="--")

        self.end_marker, = self.ax.plot(self.u, self.v, self.z, marker="o", markersize=3, color=self.color)

        self.rotate_center = np.array([0., -1., 0.])

    def set_phase_step(self, angle):
        self.phase_step = angle

    def _rotate_phase(self):
        rot_matrix = Rotation.from_rotvec(self.phase_step * self.vector)
        self.phase = rot_matrix.apply(self.phase)

    def rotate_offset(self, x, y, z):
        self._rotate_phase()

        rot_matrix = Rotation.from_rotvec(self.phase_step * self.rotate_center)
        self.vector = rot_matrix.apply(self.vector)
        self.vector_arrow = self.vector * np.rad2deg(self.phase_step)

        self.quiver.remove()
        self.x, self.y, self.z = x, y, z
        self.u, self.v, self.w = self.vector_arrow[0], self.vector_arrow[1], self.vector_arrow[2]
        self.quiver = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                     length=1, linewidth=2, color=self.color, normalize=False)

        self.phase = rot_matrix.apply(self.phase)
        self.u, self.v, self.w = self.x + self.phase[0], self.y + self.phase[1], self.z + self.phase[2]
        self.line_phase.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])
        self.end_marker.set_data_3d([self.u], [self.v], [self.w])


def set_phase_step_deg(value):
    global phase_step_deg
    phase_step_deg = value
    world_circle.set_phase_step(np.deg2rad(phase_step_deg))
    light_phase_circle.set_phase_step(np.deg2rad(phase_step_deg))
    light_arrow.set_phase_step(np.deg2rad(phase_step_deg))


def create_parameter_setter():
    # Phase per step
    frm_phase_step = ttk.Labelframe(root, relief="ridge", text="Phase(deg) per step", labelanchor='n')
    frm_phase_step.pack(side="left", fill=tk.Y)

    # var_phase_stp = tk.StringVar(root)
    var_phase_stp.set(str(phase_step_deg))
    spn_phase_stp = tk.Spinbox(
        frm_phase_step, textvariable=var_phase_stp, format="%.0f", from_=-360, to=360, increment=1,
        command=lambda: set_phase_step_deg(float(var_phase_stp.get())), width=5
    )
    spn_phase_stp.pack(side="left")

    # Radius of world circle
    frm_radius = ttk.Labelframe(root, relief="ridge", text="Radius of world circle", labelanchor='n')
    frm_radius.pack(side="left", fill=tk.Y)

    # var_radius = tk.StringVar(root)
    var_radius.set(str(radius_world))
    spn_radius = tk.Spinbox(
        frm_radius, textvariable=var_radius, format="%.1f", from_=0, to=10, increment=0.1,
        command=lambda: world_circle.set_radius(float(var_radius.get())), width=5
    )
    spn_radius.pack(side="left")


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")
    # btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: aaa())
    # btn_clear.pack(side="left")


def create_center_lines():
    ln_axis_x = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_x)
    ln_axis_y = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_y)
    ln_axis_z = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_z)


def create_circle(ax, x, y, z, z_dir, edge_col, fill_flag, line_width, line_style, label):
    if label != "":
        c_spin_axis_guide = Circle((x, y), 1., ec=edge_col, fill=fill_flag,
                                   linewidth=line_width, linestyle=line_style, label=label)
    else:
        c_spin_axis_guide = Circle((x, y), 1., ec=edge_col, fill=fill_flag,
                                   linewidth=line_width, linestyle=line_style)
    ax.add_patch(c_spin_axis_guide)
    art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=z, zdir=z_dir)


def draw_static_diagrams():
    create_center_lines()


def update_diagrams():
    world_circle.rotate()
    phase = world_circle.get_phase()
    light_phase_circle.rotate_offset(phase[0], phase[1], phase[2])
    light_arrow.rotate_offset(phase[0], phase[1], phase[2])


def reset():
    global is_play
    cnt.reset()
    if is_play:
        is_play = not is_play
    world_circle.reset()


def switch():
    global is_play
    is_play = not is_play


def update(f):
    if is_play:
        cnt.count_up()
        update_diagrams()


""" main loop """
if __name__ == "__main__":
    cnt = Counter(ax=ax0, is3d=True, xy=np.array([x_min, y_max]), z=z_max, label="Step=")
    draw_static_diagrams()
    create_animation_control()
    create_parameter_setter()

    world_circle = WorldCircle(ax0, np.deg2rad(phase_step_deg), radius_world)
    light_phase_circle = LightPhaseCircle(ax0, np.deg2rad(phase_step_deg), 1.)
    light_arrow = LightArrow(ax0, np.deg2rad(phase_step_deg))

    phase = world_circle.get_phase()
    light_phase_circle.rotate_offset(phase[0], phase[1], phase[2])
    light_arrow.rotate_offset(phase[0], phase[1], phase[2])

    dummy1, = ax0.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]),
                       color="red", linewidth=2, linestyle="-", label="Light-arrow (rotation vector)")
    dummy2, = ax0.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]),
                       color="red", linewidth=1, linestyle="--", label="Phase of light")
    dummy3, = ax0.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]),
                       color="gray", linewidth=1, linestyle="-", label="World circle")
    dummy4, = ax0.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]),
                       color="gray", linewidth=1, linestyle="--", label="Light-arrow-phase")

    ax0.legend(loc='lower right', fontsize=8)

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()