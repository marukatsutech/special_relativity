""" Precession (rotation)"""
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
title_ax0 = "Precession (rotation)"
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
var_rot_r_ab = tk.BooleanVar(root)
var_rot_all_r = tk.BooleanVar(root)

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


class ThreeAxes:
    def __init__(self, ax=None, xyz=None):
        self.ax = ax
        self.xyz = xyz
        self.is_rotate_xyz = False
        self.phase_step_deg = 1

        self.axis_a = np.array([1., 0., 0.])
        self.axis_b = np.array([0., 1., 0.])
        self.axis_c = np.array([0., 0., 1.])
        self.axis_ab = np.array([0., 1., 0.])
        self.axis_r = np.array([1., 0., 0.])

        self.x_axis_a = [self.axis_a[0], - self.axis_a[0]]
        self.y_axis_a = [self.axis_a[1], - self.axis_a[1]]
        self.z_axis_a = [self.axis_a[2], - self.axis_a[2]]
        self.line_axis_a, = self.ax.plot(self.x_axis_a, self.y_axis_a, self.z_axis_a,
                                         label='Axis A', color="red", ls="-.", linewidth=2)

        self.x_axis_b = [self.axis_b[0], - self.axis_b[0]]
        self.y_axis_b = [self.axis_b[1], - self.axis_b[1]]
        self.z_axis_b = [self.axis_b[2], - self.axis_b[2]]
        self.line_axis_b, = self.ax.plot(self.x_axis_b, self.y_axis_b, self.z_axis_b,
                                         label='Axis B', color="green", ls="-.", linewidth=2)

        self.x_axis_c = [self.axis_c[0], - self.axis_c[0]]
        self.y_axis_c = [self.axis_c[1], - self.axis_c[1]]
        self.z_axis_c = [self.axis_c[2], - self.axis_c[2]]
        self.line_axis_c, = self.ax.plot(self.x_axis_c, self.y_axis_c, self.z_axis_c,
                                         label='Axis C', color="blue", ls="-.", linewidth=2)

        self.x_axis_ab = [self.axis_ab[0], - self.axis_ab[0]]
        self.y_axis_ab = [self.axis_ab[1], - self.axis_ab[1]]
        self.z_axis_ab = [self.axis_ab[2], - self.axis_ab[2]]
        self.line_axis_ab, = self.ax.plot(self.x_axis_ab, self.y_axis_ab, self.z_axis_ab,
                                          label='Axis A-B', color="darkorange", ls="-.", linewidth=2)

        self.vector_a_b = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                         self.axis_r[0], self.axis_r[1], self.axis_r[2],
                                         length=1, color="darkorange", normalize=True, linewidth=2, alpha=1.0)

        self.x_r = []
        self.y_r = []
        self.z_r = []
        self.path_r, = self.ax.plot(np.array(self.x_r), np.array(self.y_r), np.array(self.z_r),
                                    color="darkorange", linewidth=1)

    def set_phase_step_deg(self, value):
        self.phase_step_deg = value

    def rotate_axis_ab(self):
        rot_matrix = Rotation.from_rotvec(np.deg2rad(self.phase_step_deg) * self.axis_c)
        self.axis_ab = rot_matrix.apply(self.axis_ab)
        self.update_axes()

        self.axis_r = rot_matrix.apply(self.axis_r)
        self.update_vector_a_b()

    def rotate_r_axis_ab(self):
        rot_matrix = Rotation.from_rotvec(np.deg2rad(self.phase_step_deg) * self.axis_ab)
        self.axis_r = rot_matrix.apply(self.axis_r)
        self.update_vector_a_b()

    def update_vector_a_b(self):
        self.vector_a_b.remove()
        self.vector_a_b = self.ax.quiver(self.xyz[0], self.xyz[1], self.xyz[2],
                                         self.axis_r[0], self.axis_r[1], self.axis_r[2],
                                         length=1, color="darkorange", normalize=True, linewidth=2, alpha=1.0)

    def update_path(self):
        if True:
            self.x_r.append(self.axis_r[0])
            self.y_r.append(self.axis_r[1])
            self.z_r.append(self.axis_r[2])
        self.path_r.set_xdata(np.array(self.x_r))
        self.path_r.set_ydata(np.array(self.y_r))
        self.path_r.set_3d_properties(np.array(self.z_r))

    def rotate_all_axis_r(self):
        rot_matrix = Rotation.from_rotvec(np.deg2rad(self.phase_step_deg) * self.axis_r)
        self.axis_a = rot_matrix.apply(self.axis_a)
        self.axis_b = rot_matrix.apply(self.axis_b)
        self.axis_c = rot_matrix.apply(self.axis_c)
        self.axis_ab = rot_matrix.apply(self.axis_ab)

    def update_axes(self):
        self.x_axis_a = [self.axis_a[0], - self.axis_a[0]]
        self.y_axis_a = [self.axis_a[1], - self.axis_a[1]]
        self.z_axis_a = [self.axis_a[2], - self.axis_a[2]]
        self.line_axis_a.set_data_3d(self.x_axis_a, self.y_axis_a, self.z_axis_a)

        self.x_axis_b = [self.axis_b[0], - self.axis_b[0]]
        self.y_axis_b = [self.axis_b[1], - self.axis_b[1]]
        self.z_axis_b = [self.axis_b[2], - self.axis_b[2]]
        self.line_axis_b.set_data_3d(self.x_axis_b, self.y_axis_b, self.z_axis_b)

        self.x_axis_c = [self.axis_c[0], - self.axis_c[0]]
        self.y_axis_c = [self.axis_c[1], - self.axis_c[1]]
        self.z_axis_c = [self.axis_c[2], - self.axis_c[2]]
        self.line_axis_c.set_data_3d(self.x_axis_c, self.y_axis_c, self.z_axis_c)

        self.x_axis_ab = [self.axis_ab[0], - self.axis_ab[0]]
        self.y_axis_ab = [self.axis_ab[1], - self.axis_ab[1]]
        self.z_axis_ab = [self.axis_ab[2], - self.axis_ab[2]]
        self.line_axis_ab.set_data_3d(self.x_axis_ab, self.y_axis_ab, self.z_axis_ab)

    def clear_path(self):
        self.x_r = []
        self.y_r = []
        self.z_r = []
        self.update_path()

    def reset(self):
        self.xyz = np.array([0., 0., 0.])
        self.axis_a = np.array([1., 0., 0.])
        self.axis_b = np.array([0., 1., 0.])
        self.axis_c = np.array([0., 0., 1.])
        self.axis_ab = np.array([0., 1., 0.])
        self.axis_r = np.array([1., 0., 0.])

        self.clear_path()
        self.update_axes()
        self.update_vector_a_b()


def set_phase_deg_step(value):
    global phase_deg_step
    phase_deg_step = value


def create_parameter_setter():
    global var_rot_r_ab, var_rot_all_r
    # Rotations
    frm_rot = ttk.Labelframe(root, relief="ridge", text="Rotations", labelanchor='n')
    frm_rot.pack(side="left", fill=tk.Y)

    # var_rot_all_r = tk.BooleanVar(root)
    chk_rot_all_r = tk.Checkbutton(frm_rot, text="Rotate all axes around vector R", variable=var_rot_all_r)
    chk_rot_all_r.pack(anchor=tk.W)
    var_rot_all_r.set(False)
    
    # var_rot_r_ab = tk.BooleanVar(root)
    chk_rot_r_ab = tk.Checkbutton(frm_rot, text="Rotate vector A-B around axis A-B", variable=var_rot_r_ab)
    chk_rot_r_ab.pack(anchor=tk.W)
    var_rot_r_ab.set(False)


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(fill=tk.X)
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(fill=tk.X)
    btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: three_axes.clear_path())
    btn_clear.pack(fill=tk.X)


def create_center_lines():
    line_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_x)
    line_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_y)
    line_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_z)


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
    create_circle(ax0, 0., 0., 0., "x", "gray", False, 0.5,
                  "--", "")
    create_circle(ax0, 0., 0., 0., "y", "gray", False, 0.5,
                  "--", "")
    create_circle(ax0, 0., 0., 0., "z", "gray", False, 0.5,
                  "--", "")


def update_diagrams():
    three_axes.rotate_axis_ab()
    if var_rot_r_ab.get():
        three_axes.rotate_r_axis_ab()
    if var_rot_all_r.get():
        three_axes.rotate_all_axis_r()
    three_axes.update_path()


def reset():
    global is_play, phase_deg
    cnt.reset()
    three_axes.reset()


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

    three_axes = ThreeAxes(ax0, np.array([0., 0., 0.]))

    dummy0, = ax0.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]),
                       color="darkorange", linewidth=2, linestyle="-", label="Rotation vector A-B")

    ax0.legend(loc='lower right', fontsize=8)

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
