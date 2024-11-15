""" Photon from the perspective of the probability of the existence of a quantum """
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
title_ax0 = "Photon from the perspective of the probability"
title_tk = title_ax0

x_min = -4.
x_max = 4.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.

fig = Figure()
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_box_aspect((8, 4, 4))
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

    def set_direction(self, vector):
        self.vector = vector
        if self.vector[2] != 0.:
            self.u = self.x + self.vector[0] / self.vector[2]
            self.v = self.y + self.vector[1] / self.vector[2]
            self.w = self.z + 1.
        else:
            self.u, self.v, self.w = 1e5, 1e5, 1.
        self.line_projection.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])

    def get_projection_point(self):
        return self.u, self.v, self.w


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
        else:   # "z"
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
        else:   # "z"
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


class CosCurve3d:
    def __init__(self, ax, x_start, x_end, wave_number, amplitude, cycle_length, x_offset, y_offset, z_offset,
                 resolution, line_width, line_style, color):
        self.ax = ax
        self.x_start, self.x_end = x_start, x_end
        self.wave_number = wave_number
        self.amplitude = amplitude
        self.cycle_length = cycle_length
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.z_offset = z_offset
        self.line_width = line_width
        self.line_style = line_style
        self.color = color

        self.x = np.linspace(x_start, x_end, resolution)
        self.y = self.x * 0. + self.y_offset
        self.z = (self.amplitude * np.cos(self.wave_number * self.x * self.cycle_length * (2. * np.pi) / 2. + self.x_offset)
                  + self.z_offset)
        self.cos_curve, = self.ax.plot(self.x, self.y, self.z, linewidth=self.line_width, linestyle=self.line_style,
                                       color=self.color)

    def set_wave_number(self, wave_number):
        self.wave_number = wave_number
        self.z = (self.amplitude * np.cos(self.wave_number * self.x * self.cycle_length * (2. * np.pi) / 2. + self.x_offset)
                  + self.z_offset)
        self.cos_curve.set_xdata(np.array(self.x))
        self.cos_curve.set_ydata(np.array(self.y))
        self.cos_curve.set_3d_properties(np.array(self.z))


class CosLine3d:
    def __init__(self, ax, x, y, z, wave_number, amplitude, cycle_length, line_width, line_style, color):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.wave_number = wave_number
        self.amplitude = amplitude
        self.cycle_length = cycle_length
        self.line_width = line_width
        self.line_style = line_style
        self.color = color

        self.h = self.z + self.amplitude * np.cos(self.wave_number * self.x * self.cycle_length * (2. * np.pi) / 2.)

        self.line, = self.ax.plot([self.x, self.x], [self.y, self.y], [self.z, self.h],
                                  linewidth=self.line_width, color=self.color, linestyle=self.line_style)
        self.start_marker, = self.ax.plot(self.x, self.y, self.z, marker="o", markersize=2,
                                          color=self.color)
        self.end_marker, = self.ax.plot(self.x, self.x, self.h, marker="o", markersize=3, color=self.color)

    def set_data(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.h = self.z + self.amplitude * np.cos(self.wave_number * self.x * self.cycle_length * (2. * np.pi) / 2.)

        self.line.set_xdata(np.array([self.x, self.x]))
        self.line.set_ydata(np.array([self.y, self.y]))
        self.line.set_3d_properties(np.array([self.z, self.h]))

        self.start_marker.set_data_3d([self.x], [self.y], [self.z])
        self.end_marker.set_data_3d([self.x], [self.y], [self.h])

    def set_wave_number(self, wave_number):
        self.wave_number = wave_number

    def get_phase_point(self):
        return [self.x], [self.y], [self.h]


class Scatter3D:
    def __init__(self, ax, size, color):
        self.ax = ax
        self.size = size
        self.color = color
        self.x, self.y, self.z = [], [], []
        self.scat = self.ax.scatter([], [], [], s=self.size, color=self.color)

    def add_data(self, x, y, z):
        self.x = np.concatenate([self.x, x])
        self.y = np.concatenate([self.y, y])
        self.z = np.concatenate([self.z, z])
        self.scat._offsets3d = (self.x, self.y, self.z)

    def clear_data(self):
        self.x, self.y, self.z = [], [], []
        self.scat._offsets3d = (self.x, self.y, self.z)


def create_center_lines():
    line_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_x)
    line_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_y)
    line_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(line_axis_z)


def create_circle(ax, x, y, z, z_dir, edge_col, fill_flag, line_width, line_style, label):
    c_spin_axis_guide = Circle((x, y), 1., ec=edge_col, fill=fill_flag,
                               linewidth=line_width, linestyle=line_style, label=label)
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
    light_phase_curve.set_wave_number(nu_light)
    light_phase_line.set_wave_number(nu_light)


def set_arrow_motion(value):
    global arrow_motion_option
    arrow_motion_option = value
    reset()


def create_parameter_setter():
    frm_am = ttk.Labelframe(root, relief='ridge', text='Arrow motion', labelanchor='n')
    frm_am.pack(side='left', fill=tk.Y)

    var_am = tk.IntVar(root)
    rd1_am = tk.Radiobutton(frm_am, text="Rotation", value=0, var=var_am, command=lambda: set_arrow_motion(var_am.get()))
    rd1_am.pack()
    rd2_am = tk.Radiobutton(frm_am, text="Random", value=1, var=var_am, command=lambda: set_arrow_motion(var_am.get()))
    rd2_am.pack()
    var_am.set(0)

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
    create_circle(ax0, 0., 0., 0., "y", "darkorange", False, 0.5,
                  "--", "Light-sphere")
    create_center_lines()
    line_spacial = art3d.Line3D([x_min, x_max], [0., 0.], [1., 1.], color="green", ls="-", linewidth=1,
                                label="Spatial line")
    ax0.add_line(line_spacial)


def update_diagrams():
    if arrow_motion_option == 0:
        angle = (cnt.get() * np.pi / 180.) % (2. * np.pi)
    else:
        angle = np.deg2rad(np.random.random() * 360)
    light_arrow.rotate(angle, vector_y_axis)
    projection_line.set_direction(light_arrow.get_vector())
    light_vibration_circle.rotate(angle, vector_y_axis)
    light_vibration_line.rotate2(angle, nu_light * angle, vector_y_axis, light_arrow.get_vector())
    point = projection_line.get_projection_point()
    light_phase_line.set_data(point[0], point[1], point[2])
    if arrow_motion_option == 1:
        x_phase, y_phase, z_phase = light_phase_line.get_phase_point()
        light_phase_dots.add_data(x_phase, y_phase, z_phase)


def reset():
    global is_play
    is_play = False
    cnt.reset()
    light_phase_dots.clear_data()
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

    light_arrow = Arrow3d(ax0, 0., 0., 0., 0., 0., "darkorange", "Light-arrow")
    projection_line = ProjectionLine3d(ax0, 0., 0., 0., vector_z_axis,
                                       "darkorange", 1, "--", "Projection line")
    light_vibration_circle = Circle3d(ax0, 0., 0., 0., 0.5, "z",
                                      1, "-", "red", 0.3)
    light_vibration_line = LineRotation3d(ax0, 0., 0., 0., 0.5, "x", 1.5,
                                          "-", "red", "Light vibration phase")
    light_phase_curve = CosCurve3d(ax0, x_min, x_max, 1., 0.5, 1.,
                                   0., 0., 1., 500, 0.5, "-", "gray")
    light_phase_line = CosLine3d(ax0, 0., 0., 1., 1.,0.5, 1., 1.5,
                                 "-", "red")
    light_phase_dots = Scatter3D(ax0, 3, "gray")

    ax0.legend(loc='lower right', fontsize=8)

    create_animation_control()
    create_parameter_setter()

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
