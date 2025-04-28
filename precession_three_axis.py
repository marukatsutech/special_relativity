""" Precession (three-axis) """
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

""" Animation control """
is_play = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Other parameters """
phase_deg = 0.
phase_deg_step = 4.

""" Create figure and axes """
title_ax0 = "Precession (three-axis)"
title_tk = title_ax0

x_min = -2.
x_max = 2.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.

fig = Figure()
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_box_aspect((1, 1, 1))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("x or t")
ax0.set_ylabel("y or t")
ax0.set_zlabel("z or t")
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


class TwoArrow:
    def __init__(self, ax=None, xyz=None, color1=None, color2=None):
        self.ax = ax
        self.xyz = xyz
        self.color1 = color1
        self.color2 = color2

        self.axis_center = np.array([1., 0., 0.])
        self.axis_vector1 = np.array([1., 0., 1.])
        self.axis_vector1 = self.axis_vector1 / np.linalg.norm(self.axis_vector1)
        self.axis_vector2 = np.array([-1., 0., 1.])
        self.axis_vector2 = self.axis_vector2 / np.linalg.norm(self.axis_vector2)

        self.vector1 = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                      self.axis_vector1[0], self.axis_vector1[1], self.axis_vector1[2],
                                      length=1, color=self.color1, normalize=True, linewidth=3, alpha=0.7)

        self.vector2 = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                      self.axis_vector2[0], self.axis_vector2[1], self.axis_vector2[2],
                                      length=1, color=self.color2, normalize=True, linewidth=1, alpha=1)

    def update_quiver(self):
        self.vector1.remove()
        self.vector1 = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                      self.axis_vector1[0], self.axis_vector1[1], self.axis_vector1[2],
                                      length=1, color=self.color1, normalize=True, linewidth=3, alpha=0.7)

        self.vector2.remove()
        self.vector2 = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                      self.axis_vector2[0], self.axis_vector2[1], self.axis_vector2[2],
                                      length=1, color=self.color2, normalize=True, linewidth=1, alpha=1)

    def rotate_around_center(self):
        rot_matrix = Rotation.from_rotvec(np.deg2rad(phase_deg_step) * self.axis_center)
        self.axis_vector1 = rot_matrix.apply(self.axis_vector1)
        self.axis_vector2 = rot_matrix.apply(self.axis_vector2)

        self.update_quiver()

    def rotate_all(self, angle_deg, vector):
        rot_matrix = Rotation.from_rotvec(np.deg2rad(angle_deg) * vector)
        self.axis_center = rot_matrix.apply(self.axis_center)
        self.axis_vector1 = rot_matrix.apply(self.axis_vector1)
        self.axis_vector2 = rot_matrix.apply(self.axis_vector2)

        self.update_quiver()

    def get_vector(self):
        return self.axis_vector1


class CrossArrow:
    def __init__(self, ax=None, xyz=None, color1=None, vector1=None, vector2=None):
        self.ax = ax
        self.xyz = xyz
        self.color1 = color1
        # self.color2 = color2
        self.axis_cross = np.cross(vector1, vector2)
        self.axis_cross = self.axis_cross / np.linalg.norm(self.axis_cross)

        self.vector_cross = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                           self.axis_cross[0], self.axis_cross[1], self.axis_cross[2],
                                           length=1, color=self.color1, normalize=True, linewidth=3, alpha=0.7)

        self.x_path = []
        self.y_path = []
        self.z_path = []
        self.path, = self.ax.plot(np.array(self.x_path), np.array(self.y_path), np.array(self.z_path),
                                  color=self.color1, linewidth=1)

    def update(self, vector1, vector2):
        self.axis_cross = np.cross(vector1, vector2)
        self.axis_cross = self.axis_cross / np.linalg.norm(self.axis_cross)
        self.vector_cross.remove()
        self.vector_cross = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                           self.axis_cross[0], self.axis_cross[1], self.axis_cross[2],
                                           length=1, color=self.color1, normalize=True, linewidth=3, alpha=0.7)
        self.update_path()

    def update_path(self):
        self.x_path.append(self.axis_cross[0])
        self.y_path.append(self.axis_cross[1])
        self.z_path.append(self.axis_cross[2])
        self.path.set_xdata(np.array(self.x_path))
        self.path.set_ydata(np.array(self.y_path))
        self.path.set_3d_properties(np.array(self.z_path))


def create_parameter_setter():
    pass


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(fill=tk.X)
    # btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    # btn_reset.pack(fill=tk.X)
    # btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: three_axes.clear_path())
    # btn_clear.pack(fill=tk.X)


def create_center_lines():
    line_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_x)
    line_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_y)
    line_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_z)


def create_circle(ax, x, y, z, r, z_dir, edge_col, fill_flag, line_width, line_style, label):
    if label != "":
        c_spin_axis_guide = Circle((x, y), r, ec=edge_col, fill=fill_flag,
                                   linewidth=line_width, linestyle=line_style, label=label)
    else:
        c_spin_axis_guide = Circle((x, y), r, ec=edge_col, fill=fill_flag,
                                   linewidth=line_width, linestyle=line_style)
    ax.add_patch(c_spin_axis_guide)
    art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=z, zdir=z_dir)


def draw_static_diagrams():
    create_center_lines()
    create_circle(ax0, 0., 0., 0., 1., "x", "gray", False, 0.5,
                  "-", "")
    create_circle(ax0, 0., 0., 0., 1., "y", "gray", False, 0.5,
                  "-", "")
    create_circle(ax0, 0., 0., 0., 1., "z", "gray", False, 0.5,
                  "--", "")

    r2 = 1. / np.sqrt(2)
    create_circle(ax0, 0., 0., r2, r2, "x", "red", False, 1,
                  "-", "")
    create_circle(ax0, 0., 0., - r2, r2, "y", "green", False, 1,
                  "-", "")
    create_circle(ax0, 0., 0., r2, r2, "z", "blue", False, 1,
                  "--", "")


def update_diagrams():
    two_arrow_red.rotate_around_center()
    two_arrow_green.rotate_around_center()
    # two_arrow_blue.rotate_around_center()
    cross_arrow.update(two_arrow_green.get_vector(), two_arrow_red.get_vector())


def reset():
    global is_play, phase_deg
    cnt.reset()


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

    two_arrow_red = TwoArrow(ax0, np.array([0., 0., 0.]), "red", "brown")
    two_arrow_red.rotate_all(90, vector_x_axis)
    two_arrow_green = TwoArrow(ax0, np.array([0., 0., 0.]), "green", "olive")
    two_arrow_green.rotate_all(270, vector_z_axis)
    two_arrow_green.rotate_all(270, vector_y_axis)
    # two_arrow_blue = TwoArrow(ax0, np.array([0., 0., 0.]), "blue", "steelblue")
    # two_arrow_blue.rotate_all(270, vector_y_axis)
    # two_arrow_blue.rotate_all(270, vector_z_axis)
    cross_arrow = CrossArrow(ax0, np.array([0., 0., 0.]), "blue",
                             two_arrow_green.get_vector(), two_arrow_red.get_vector())

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
