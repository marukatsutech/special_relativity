""" Rotating vector of fermion """
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
vector_xz_axis = np.array([1., 0., 1.])

""" Create figure and axes """
title_ax0 = "Rotating vector of fermion"
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


class Arrow3d:
    def __init__(self, ax, x, y, z, is_normalize, length, theta, phi, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.is_normalize = is_normalize
        self.r = length
        self.theta_init = theta
        self.phi_init = phi
        self.color = color
        self.line_width = line_width
        self.line_style = line_style
        self.label = label

        self.u, self.v, self.w = spherical_to_cartesian(self.r, self.theta_init, self.phi_init)

        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize, linewidth=self.line_width,
                                      linestyle=self.line_style)

        self.vector_init = np.array([self.u, self.v, self.w])
        self.is_rotate = True

    def rotate(self, angle, rotation_axis):
        if not self.is_rotate:
            return
        rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        vector_rotated = rot_matrix.apply(self.vector_init)
        self.u, self.v, self.w = vector_rotated[0], vector_rotated[1], vector_rotated[2]
        self.qvr.remove()
        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize, linewidth=self.line_width,
                                      linestyle=self.line_style)

    def rotate2(self, angle_1st, angle_2nd, rotation_axis_1st, rotation_axis_2nd):
        if not self.is_rotate:
            return
        rotation_axis_1st = rotation_axis_1st / np.linalg.norm(rotation_axis_1st)
        rotation_axis_2nd = rotation_axis_2nd / np.linalg.norm(rotation_axis_2nd)
        rot_matrix_1st = Rotation.from_rotvec(angle_1st * rotation_axis_1st)
        rot_matrix_2nd = Rotation.from_rotvec(angle_2nd * rotation_axis_2nd)

        vector_rotated_1st = rot_matrix_1st.apply(self.vector_init)
        vector_rotated = rot_matrix_2nd.apply(vector_rotated_1st)

        self.u, self.v, self.w = vector_rotated[0], vector_rotated[1], vector_rotated[2]
        self.qvr.remove()
        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize, linewidth=self.line_width,
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
        self.plain_data = self.angle_space * 0. + self.z

        if direction == "x":
            self.x_circle, self.y_circle, self.z_circle = self.plain_data, self.cos_data, self.sin_data
        elif direction == "y":
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.plain_data, self.sin_data
        else:  # "z"
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.sin_data, self.plain_data

        self.plt_circle, = self.ax.plot(self.x_circle, self.y_circle, self.z_circle,
                                        linewidth=self.line_width, linestyle=self.line_style,
                                        color=self.color, alpha=self.alpha)

        self.is_rotate = True

    def rotate(self, angle, rotation_axis):
        if not self.is_rotate:
            return
        rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
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


class ProjectionLine3d:
    def __init__(self, ax, x, y, z, vector, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.vector = vector
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.label = label

        if self.vector[2] != 0.:
            self.u = self.x + self.vector[0] / self.vector[2]
            self.v = self.y + self.vector[1] / self.vector[2]
            self.w = self.z + 1.
        else:
            self.u, self.v, self.w = 1e5, 1e5, 1.
        self.line_projection = art3d.Line3D([self.x, self.u], [self.y, self.v], [self.z, self.w],
                                            linewidth=self.line_width, color=self.color, linestyle=self.line_style,
                                            label=self.label)
        self.ax.add_line(self.line_projection)
        self.end_marker, = self.ax.plot(self.u, self.v, self.w, marker="o", markersize=3, color=self.color)

    def set_direction(self, vector):
        self.vector = vector
        if self.vector[2] != 0.:
            self.u = self.x + self.vector[0] / self.vector[2]
            self.v = self.y + self.vector[1] / self.vector[2]
            self.w = self.z + 1.
        else:
            self.u, self.v, self.w = 1e5, 1e5, 1.
        self.line_projection.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])
        self.end_marker.set_data_3d([self.u], [self.v], [self.w])

    def get_projection_point(self):
        return self.u, self.v, self.w


def create_center_lines():
    ln_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_x)
    ln_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_y)
    ln_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
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


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")


def create_parameter_setter():
    pass


def draw_static_diagrams():
    create_circle(ax0, 0., 0., 0., "x", "darkorange", False, 0.5,
                  "--", "Light-sphere")
    create_circle(ax0, 0., 0., 0., "y", "darkorange", False, 0.5,
                  "--", "")
    create_circle(ax0, 0., 0., 0., "z", "darkorange", False, 0.5,
                  "--", "")
    create_center_lines()

    light_arrow_path_circle_upper = Circle3d(ax0, 0., 0., np.cos(np.pi / 4.), np.sqrt(2.) / 2., "z",
                                             2, "-", "gold", 1)
    light_arrow_path_circle_upper.set_direction(np.pi / 4., 0.)
    light_arrow_path_circle_lower = Circle3d(ax0, 0., 0., np.cos(np.pi / 4.), np.sqrt(2.) / 2., "z",
                                             2, "-", "gold", 1)
    light_arrow_path_circle_lower.set_direction(np.pi * 3. / 4., 0.)

    y_parabola = np.arange(x_min, x_max, 0.01)
    z_parabola = y_parabola * 0. + 1.
    x_parabola = y_parabola ** 2. * 0.5
    parabola0 = art3d.Line3D(x_parabola, y_parabola, z_parabola, color='magenta', ls='--', linewidth=1, label="Parabola")
    ax0.add_line(parabola0)

    parabola1 = art3d.Line3D(- x_parabola, y_parabola, z_parabola, color='magenta', ls='--', linewidth=1)
    ax0.add_line(parabola1)


def update_diagrams():
    cycle = cnt.get() % 720
    angle = - np.deg2rad(cycle)
    if 0 < cycle <= 180:
        light_arrow.rotate(angle, rot_vector_arrow_upper.get_vector())
    elif 180 < cycle <= 540:
        light_arrow.rotate2(np.pi / 2., - angle + np.pi, vector_y_axis, rot_vector_arrow_lower.get_vector())
    else:
        light_arrow.rotate(angle, rot_vector_arrow_upper.get_vector())

    projection_line.set_direction(light_arrow.get_vector())


def on_off_rot_light(value):
    light_arrow.set_rotate(value)
    cnt.reset()
    update_diagrams()


def on_off_rot_axis(value):
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
    draw_static_diagrams()

    light_arrow = Arrow3d(ax0, 0., 0., 0., True, 1., 0., 0., "darkorange",
                          2, "-", "Light arrow as whole")
    rot_vector_arrow_upper = Arrow3d(ax0, 0., 0., 0., False, 1.4, np.pi / 4., 0., "blue",
                                     2, "-", "Rotating vector as whole")
    rot_vector_arrow_lower = Arrow3d(ax0, 0., 0., 0., False, 1.4, np.pi * 3. / 4., 0., "blue",
                                     2, "-", "")

    projection_line = ProjectionLine3d(ax0, 0., 0., 0., vector_z_axis,
                                       "darkorange", 1, "--", "Projection line")

    ax0.legend(loc='lower right', fontsize=8)

    create_animation_control()
    create_parameter_setter()

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
