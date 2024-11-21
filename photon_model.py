""" Photon model """
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
import matplotlib.patches as patches

""" Global variables """

""" Animation control """
is_play = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Other parameters """
nu_light = 1.
arrow_motion_option = 0

""" Create figure and axes """
title_ax0 = "Photon model"
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


class Arrow3d:
    def __init__(self, ax, x, y, z, theta, phi, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.theta_init = theta
        self.phi_init = phi
        self.r = 1.
        self.u, self.v, self.w = spherical_to_cartesian(self.r, self.theta_init, self.phi_init)
        self.color = color
        self.line_width = line_width
        self.line_style = line_style
        self.label = label
        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=True,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=True, linewidth=self.line_width,
                                      linestyle=self.line_style)

        self.vector_init = np.array([self.u, self.v, self.w])
        self.is_rotate = True

    def rotate(self, angle, rotation_axis):
        if not self.is_rotate:
            return
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        vector_rotated = rot_matrix.apply(self.vector_init)
        self.u, self.v, self.w = vector_rotated[0], vector_rotated[1], vector_rotated[2]
        self.qvr.remove()
        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=True,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=True, linewidth=self.line_width,
                                      linestyle=self.line_style)

    def set_rotate(self, flag):
        self.is_rotate = flag

    def set_direction(self, theta, phi):
        self.u, self.v, self.w = spherical_to_cartesian(self.r, theta, phi)
        self.qvr.remove()
        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=True,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=True, linewidth=self.line_width,
                                      linestyle=self.line_style)

    def get_vector(self):
        return np.array([self.u, self.v, self.w])


class Circle3d:
    def __init__(self, ax, x, y, z, r, direction, line_width, line_style, color, alpha):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.r = r
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.alpha = alpha

        self.angle_space = np.arange(0, 360)
        self.cos_data = self.r * np.cos(self.angle_space * np.pi / 180.)
        self.sin_data = self.r * np.sin(self.angle_space * np.pi / 180.)
        self.zero_data = self.angle_space * 0.

        if direction == "x":
            self.x_circle, self.y_circle, self.z_circle = self.zero_data, self.cos_data, self.sin_data
        elif direction == "y":
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.zero_data, self.sin_data
        else:  # "z"
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.sin_data, self.zero_data

        self.plt_circle, = self.ax.plot(self.x_circle, self.y_circle, self.z_circle,
                                        linewidth=self.line_width, linestyle=self.line_style,
                                        color=self.color, alpha=self.alpha)

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
            point_rotated = rot_matrix.apply(vector_point)
            x_circle_rotated.append(point_rotated[0])
            y_circle_rotated.append(point_rotated[1])
            z_circle_rotated.append(point_rotated[2])
        self.plt_circle.set_xdata(np.array(x_circle_rotated))
        self.plt_circle.set_ydata(np.array(y_circle_rotated))
        self.plt_circle.set_3d_properties(np.array(z_circle_rotated))

    def set_rotate(self, flag):
        self.is_rotate = flag

    def set_direction(self, theta, phi):
        rot_matrix_theta = Rotation.from_rotvec(theta * vector_y_axis)
        rot_matrix_phi = Rotation.from_rotvec(phi * vector_z_axis)
        x_circle_rotated = []
        y_circle_rotated = []
        z_circle_rotated = []
        for i in range(len(self.angle_space)):
            vector_point = np.array(
                [self.x_circle[i], self.y_circle[i], self.z_circle[i]])
            point_rotated_theta = rot_matrix_theta.apply(vector_point)
            point_rotated = rot_matrix_phi.apply(point_rotated_theta)
            x_circle_rotated.append(point_rotated[0])
            y_circle_rotated.append(point_rotated[1])
            z_circle_rotated.append(point_rotated[2])
        self.plt_circle.set_xdata(np.array(x_circle_rotated))
        self.plt_circle.set_ydata(np.array(y_circle_rotated))
        self.plt_circle.set_3d_properties(np.array(z_circle_rotated))


class LineRotation3d:
    def __init__(self, ax, x, y, z, length, direction, line_width, line_style, color, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.length = length
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.label = label

        if direction == "x":
            self.u, self.v, self.w = self.length, 0., 0.
        elif direction == "y":
            self.u, self.v, self.w = 0., self.length, 0.
        else:  # "z"
            self.u, self.v, self.w = 0., 0., self.length

        self.line, = self.ax.plot([self.x, self.u], [self.y, self.v], [self.z, self.w],
                                  linewidth=self.line_width, color=self.color, linestyle=self.line_style)
        self.start_marker, = self.ax.plot(self.x, self.y, self.z, marker="o", markersize=2,
                                          color=self.color)
        self.end_marker, = self.ax.plot(self.u, self.v, self.z, marker="o", markersize=3, color=self.color,
                                        label=self.label)

        self.is_rotate = True

    def rotate(self, angle, rotation_axis):
        if not self.is_rotate:
            return
        vector_point = np.array([self.u, self.v, self.w])
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        vector_rotated = rot_matrix.apply(vector_point)
        self.line.set_data_3d([self.x, vector_rotated[0]], [self.y, vector_rotated[1]], [self.z, vector_rotated[2]])
        self.end_marker.set_data_3d([vector_rotated[0]], [vector_rotated[1]], [vector_rotated[2]])

    def rotate2(self, angle_1st, angle_2nd, rotation_axis_1st, rotation_axis_2nd):
        if not self.is_rotate:
            return
        vector_point = np.array([self.u, self.v, self.w])
        rot_matrix_1st = Rotation.from_rotvec(angle_1st * rotation_axis_1st)
        vector_rotated_1st = rot_matrix_1st.apply(vector_point)
        rot_matrix_2nd = Rotation.from_rotvec(angle_2nd * rotation_axis_2nd)
        vector_rotated = rot_matrix_2nd.apply(vector_rotated_1st)
        self.line.set_data_3d([self.x, vector_rotated[0]], [self.y, vector_rotated[1]], [self.z, vector_rotated[2]])
        self.end_marker.set_data_3d([vector_rotated[0]], [vector_rotated[1]], [vector_rotated[2]])

    def set_direction(self, angle_1st, theta, phi):
        vector_point = np.array([self.u, self.v, self.w])
        rot_matrix_1st = Rotation.from_rotvec(angle_1st * vector_z_axis)
        vector_rotated_1st = rot_matrix_1st.apply(vector_point)
        rot_matrix_theta = Rotation.from_rotvec(theta * vector_y_axis)
        rot_matrix_phi = Rotation.from_rotvec(phi * vector_z_axis)
        vector_rotated_theta = rot_matrix_theta.apply(vector_rotated_1st)
        vector_rotated = rot_matrix_phi.apply(vector_rotated_theta)
        self.line.set_data_3d([self.x, vector_rotated[0]], [self.y, vector_rotated[1]], [self.z, vector_rotated[2]])
        self.end_marker.set_data_3d([vector_rotated[0]], [vector_rotated[1]], [vector_rotated[2]])


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


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")


def set_nu(value):
    global nu_light
    reset()
    nu_light = value


def create_parameter_setter():
    frm_lv = ttk.Labelframe(root, relief="ridge", text="Light vibration", labelanchor='n')
    frm_lv.pack(side='left', fill=tk.Y)

    lbl_nu = tk.Label(frm_lv, text="Nu")
    lbl_nu.pack(side="left")

    var_nu = tk.StringVar(root)
    var_nu.set(str(nu_light))
    spn_nu = tk.Spinbox(
        frm_lv, textvariable=var_nu, format="%.1f", from_=1, to=4, increment=1,
        command=lambda: set_nu(float(var_nu.get())), width=5
    )
    spn_nu.pack(side="left")


def draw_static_diagrams():
    create_circle(ax0, 0., 0., 0., "x", "darkorange", False, 0.5,
                  "--", "Light-sphere")
    create_circle(ax0, 0., 0., 0., "y", "darkorange", False, 0.5,
                  "--", "")
    create_circle(ax0, 0., 0., 0., "z", "darkorange", False, 0.5,
                  "--", "")
    create_center_lines()


def update_diagrams():
    theta = np.deg2rad(np.random.rand() * 180.)
    phi = np.deg2rad(np.random.rand() * 360.)

    light_arrow.set_direction(theta, phi)
    light_vibration_circle.set_direction(theta, phi)
    light_vibration_line.set_direction(nu_light * theta, theta, phi)

    for i in range(30):
        theta = np.deg2rad(np.random.rand() * 180.)
        phi = np.deg2rad(np.random.rand() * 360.)
        light_arrow_afterimages[i].set_direction(theta, phi)


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

    draw_static_diagrams()

    light_arrow = Arrow3d(ax0, 0., 0., 0., 0., 0., "darkorange",
                          2, "-", "Light-arrow")
    light_vibration_circle = Circle3d(ax0, 0., 0., 0., 0.5, "z",
                                      1, "-", "red", 0.3)
    light_vibration_line = LineRotation3d(ax0, 0., 0., 0., 0.5, "x", 1.5,
                                          "-", "red", "Light vibration phase")

    light_arrow_afterimages = []
    for i in range(30):
        theta = np.deg2rad(np.random.rand() * 180.)
        phi = np.deg2rad(np.random.rand() * 360.)
        light_arrow_afterimage = Arrow3d(ax0, 0., 0., 0., theta, phi, "gray",
                                         0.5, "--", "")
        light_arrow_afterimages.append(light_arrow_afterimage)

    dummy, = ax0.plot([0, 0], [0, 0], [0, 0], linewidth=0.5, linestyle="--", color="gray", label="Afterimages of Light_arrow")

    ax0.legend(loc='lower right', fontsize=8)

    create_animation_control()
    create_parameter_setter()

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
