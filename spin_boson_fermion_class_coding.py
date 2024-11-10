""" Spin of boson and fermion (refined with class coding) """
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

""" Create figure and axes """
title_ax0 = "Spin of boson and fermion"
title_tk = title_ax0

x_min = -2.
x_max = 2.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.

fig = Figure()
ax0 = fig.add_subplot(111, projection="3d")
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("y")
ax0.set_zlabel("t")
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

""" Classes and functions """


class Counter:
    def __init__(self, is3d, ax, x, y, z, label):
        self.is3d = is3d
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.label = label

        self.count = 0

        if not is3d:
            self.txt_step = self.ax.text(x_min, y_max, self.label + str(self.count))
        else:
            self.txt_step = self.ax.text2D(self.x, self.y, self.label + str(self.count))
            self.xz, self.yz, self._ = proj3d.proj_transform(self.x, self.y, self.z, self.ax.get_proj())
            self.txt_step.set_position((self.xz, self.yz))

    def count_up(self):
        self.count += 1
        self.txt_step.set_text(self.label + str(self.count))

    def reset(self):
        self.count = 0
        self.txt_step.set_text(self.label + str(self.count))

    def get(self):
        return self.count


def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z


class Arrow:
    def __init__(self, ax, x, y, z, theta, phi, col, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.theta_init = theta
        self.phi_init = phi
        self.r = 1.
        self.u, self.v, self.w = spherical_to_cartesian(self.r, self.theta_init, self.phi_init)
        self.col = col
        self.label = label
        self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                  length=1, color=self.col, normalize=True, label=self.label)

        self.vector_init = np.array([self.u, self.v, self.w])
        self.is_rotate = True

    def rotate(self, angle, rotation_axis):
        if not self.is_rotate:
            return
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        vector_rotated = rot_matrix.apply(self.vector_init)
        self.u, self.v, self.w = vector_rotated[0], vector_rotated[1], vector_rotated[2]
        self.qvr.remove()
        self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                  length=1, color=self.col, normalize=True, label=self.label)

    def set_rotate(self, flag):
        self.is_rotate = flag

    def get_vector(self):
        return np.array([self.u, self.v, self.w])


class Circle3d:
    def __init__(self, ax, x, y, z, r, line_width, line_style, col, alpha):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.r = r
        self.line_width = line_width
        self.line_style = line_style
        self.col = col
        self.alpha = alpha

        self.angle_space = np.arange(0, 360)
        self.x_circle = np.cos(self.angle_space * np.pi / 180.)
        self.z_circle = np.sin(self.angle_space * np.pi / 180.)
        self.y_circle = self.angle_space * 0.
        self.plt_circle, = self.ax.plot(self.x_circle, self.y_circle, self.z_circle,
                                        linewidth=self.line_width, linestyle=self.line_style,
                                        c=self.col, alpha=self.alpha)

        self.is_rotate = True

    def rotate(self, angle, rotation_axis):
        if not self.is_rotate:
            return
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        x_circle_rotated = []
        y_circle_rotated = []
        z_circle_rotated = []
        for i in range(len(self.angle_space)):
            vector_point = np.array(
                [self.x_circle[i], self.y_circle[i], self.z_circle[i]])
            point_rotated_z = rot_matrix.apply(vector_point)
            x_circle_rotated.append(point_rotated_z[0])
            y_circle_rotated.append(point_rotated_z[1])
            z_circle_rotated.append(point_rotated_z[2])
        self.plt_circle.set_xdata(np.array(x_circle_rotated))
        self.plt_circle.set_ydata(np.array(y_circle_rotated))
        self.plt_circle.set_3d_properties(np.array(z_circle_rotated))

    def set_rotate(self, flag):
        self.is_rotate = flag


class LightArrowPath:
    def __init__(self, ax, theta_axis, phi_axis, theta_light, phi_light):
        self.plt_light_arrow_path = None
        self.ax = ax
        self.theta_axis_init = theta_axis
        self.phi_axis_init = phi_axis
        self.theta_light_init = theta_light
        self.phi_light_init = phi_light
        self.r = 1.
        self.vector_axis_arrow_init = np.array(
            spherical_to_cartesian(self.r, self.theta_axis_init, self.phi_axis_init))
        self.vector_light_arrow_init = np.array(
            spherical_to_cartesian(self.r, self.theta_light_init, self.phi_light_init))
        self.x_light_arrow_path = []
        self.y_light_arrow_path = []
        self.z_light_arrow_path = []
        self.phi = 0.
        self.theta = 0.

        self.is_rotate_light = True
        self.is_rotate_axis = True
        self.calc_path()
        self.draw_path()

    def calc_path(self):
        for i in range(360):
            if self.is_rotate_axis:
                self.phi = self.phi_axis_init + i * np.pi / 180.
            else:
                self.phi = self.phi_axis_init
            if self.is_rotate_light:
                self.theta = self.theta_light_init + i * np.pi / 180.
            else:
                self.theta = self.theta_light_init
            rot_matrix_z = Rotation.from_rotvec(self.phi * vector_z_axis)
            vector_axis_arrow_rotated = rot_matrix_z.apply(self.vector_axis_arrow_init)
            rot_matrix_axis_arrow = Rotation.from_rotvec(self.theta * vector_axis_arrow_rotated)
            vector_light_arrow_rotated = rot_matrix_axis_arrow.apply(self.vector_light_arrow_init)
            self.x_light_arrow_path.append(vector_light_arrow_rotated[0])
            self.y_light_arrow_path.append(vector_light_arrow_rotated[1])
            self.z_light_arrow_path.append(vector_light_arrow_rotated[2])

    def draw_path(self):
        self.plt_light_arrow_path, = self.ax.plot(
            np.array(self.x_light_arrow_path), np.array(self.y_light_arrow_path), np.array(self.z_light_arrow_path),
            color='gold', linewidth=2, linestyle='-')

    def re_draw_path(self):
        self.x_light_arrow_path = []
        self.y_light_arrow_path = []
        self.z_light_arrow_path = []
        self.calc_path()
        self.plt_light_arrow_path.set_xdata(np.array(self.x_light_arrow_path))
        self.plt_light_arrow_path.set_ydata(np.array(self.y_light_arrow_path))
        self.plt_light_arrow_path.set_3d_properties(np.array(self.z_light_arrow_path))

    def set_rotate_axis(self, flag):
        self.is_rotate_axis = flag

    def set_rotate_light(self, flag):
        self.is_rotate_light = flag


def create_center_lines():
    ln_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_x)
    ln_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_y)
    ln_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_z)


def create_circle(ax, x, y, z, z_dir, edge_col, fill_flag, line_width, line_style):
    c_spin_axis_guide = Circle((x, y), 1., ec=edge_col, fill=fill_flag,
                               linewidth=line_width, linestyle=line_style)
    ax.add_patch(c_spin_axis_guide)
    art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=z, zdir=z_dir)


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")


def create_parameter_setter():
    frm_spin = ttk.Labelframe(root, relief='ridge', text='Rotation', labelanchor='n')
    frm_spin.pack(side='left', fill=tk.Y)
    var_chk_axis_ts = tk.BooleanVar(root)
    var_chk_axis_ts.set(True)
    chk_axis_ts = tk.Checkbutton(frm_spin, text="Time(t)-spatial(xy) (orange arrow)", variable=var_chk_axis_ts,
                                 command=lambda: on_off_rot_light(var_chk_axis_ts.get()))
    chk_axis_ts.pack()
    var_chk_axis_ss = tk.BooleanVar(root)  # Variable for checkbutton
    var_chk_axis_ss.set(True)
    chk_axis_ss = tk.Checkbutton(frm_spin, text="Spatial(x)-spatial(y) (blue arrow)", variable=var_chk_axis_ss,
                                 command=lambda: on_off_rot_axis(var_chk_axis_ss.get()))
    chk_axis_ss.pack()


def update_diagrams():
    angle = cnt.get() * np.pi / 180.
    rot_axis_arrow.rotate(angle, vector_z_axis)
    light_arrow.rotate(angle, rot_axis_arrow.get_vector())
    light_circle.rotate(np.pi / 2. + angle, vector_z_axis)
    light_arrow_path.re_draw_path()


def on_off_rot_light(value):
    light_arrow.set_rotate(value)
    light_arrow_path.set_rotate_light(value)
    cnt.reset()
    update_diagrams()


def on_off_rot_axis(value):
    rot_axis_arrow.set_rotate(value)
    light_circle.set_rotate(value)
    light_arrow_path.set_rotate_axis(value)
    cnt.reset()
    update_diagrams()


def reset():
    global is_play
    is_play = False
    cnt.reset()
    update_diagrams()


def switch():
    global is_play
    is_play = not is_play


def update(f):
    if is_play:
        cnt.count_up()
        update_diagrams()


""" main loop """
if __name__ == "__main__":
    cnt = Counter(True, ax0, x_min, y_max, z_max, "Step=")
    create_center_lines()
    create_circle(ax0, 0., 0., 0., "z", "blue", False, 0.5, "--")
    light_arrow = Arrow(ax0, 0., 0., 0., 0., 0., "darkorange", "Light arrow")
    rot_axis_arrow = Arrow(ax0, 0., 0., 0., np.pi / 2., 0., "blue", "Rotation axis")
    light_circle = Circle3d(ax0, 0., 0., 0., 2, 2, ":", "darkorange", 0.8)
    light_circle.rotate(np.pi / 2., vector_z_axis)
    light_arrow_path = LightArrowPath(ax0, np.pi / 2., 0., 0., 0.)
    create_animation_control()
    create_parameter_setter()
    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
