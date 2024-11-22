""" Light speed constancy """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import proj3d
import matplotlib.patches as patches

""" Global variables """

""" Animation control """
is_play = False

""" Other parameters """
point_center_photon = np.array([- 2., 0.])
point_center_fermion = np.array([2., 0.])

angle_deg_fermion = 90.
angle_deg_photon = 45.

""" Create figure and axes """
title_ax0 = "Light speed constancy"
title_tk = title_ax0

x_min = - 10.
x_max = 10.
y_min = - 2.
y_max = 10.

fig = Figure()
ax0 = fig.add_subplot(111)
ax0.set_aspect("equal")
ax0.set_xticks(np.arange(x_min, x_max, 1))
ax0.set_yticks(np.arange(y_min, y_max, 1))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("t")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)

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


class Arrow2d:
    def __init__(self, ax, x, y, theta, width, col, alpha, label):
        self.ax = ax
        self.x, self.y = x, y
        self.theta_init = theta
        self.width = width
        self.col = col
        self.alpha = alpha
        self.label = label

        self.r = 1.
        self.u, self.v = np.cos(self.theta_init), np.sin(self.theta_init)
        self.qvr = self.ax.quiver(self.x, self.y, self.u, self.v,
                                  scale_units='xy', scale=1., width=self.width, color=self.col, alpha=self.alpha,
                                  label=self.label)

        self.vector_init = np.array([self.u, self.v])

    def set_direction(self, theta):
        self.u, self.v = np.cos(theta), np.sin(theta)
        self.qvr.set_UVC(self.u, self.v)

    def set_data(self, x, y, theta):
        self.x, self.y = x, y
        self.u, self.v = np.cos(theta), np.sin(theta)
        self.qvr.set_offsets(np.c_[self.x, self.y])
        self.qvr.set_UVC(self.u, self.v)

    def get_vector(self):
        return np.array([self.u, self.v])

    def set_color(self, color):
        self.qvr.set_color(color)


class LineAngleLength2d:
    def __init__(self, ax, x, y, theta, length, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y = x, y
        self.theta = theta
        self.length = length
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.label = label

        if self.theta != 0.:
            self.u = self.x + self.length * np.cos(self.theta)
            self.v = self.y + self.length * np.sin(self.theta)
        else:
            self.u, self.v = 1e5, 1.
        self.line, = self.ax.plot([self.x, self.u], [self.y, self.v],
                                  linewidth=self.line_width, color=self.color, linestyle=self.line_style,
                                  label=self.label)

    def set_direction(self, theta):
        self.theta = theta
        if self.theta != 0.:
            self.u = self.x + self.length * np.cos(self.theta)
            self.v = self.y + self.length * np.sin(self.theta)
        else:
            self.u, self.v = 1e5, 1.
        self.line.set_data([self.x, self.u], [self.y, self.v])

    def get_end_point(self):
        return self.u, self.v

    def get_vector(self):
        return np.array([self.u - self.x, self.v - self.y])

    def get_direction(self):
        return self.theta


class Fermion:
    def __init__(self, ax, x, y, theta, alpha):
        self.ax = ax
        self.x, self.y = x, y
        self.theta = theta
        self.alpha = alpha

        self.xy = np.array([self.x, self.y])

        self.circle = patches.Circle(xy=self.xy, radius=0.5, fill=True, color="darkorange",
                                     linestyle="-", linewidth=1, alpha=0.3)
        self.ax.add_patch(self.circle)
        self.arrow_upper_right = Arrow2d(self.ax, self.x, self.y, self.theta - np.pi / 4., 0.004, "red", self.alpha, "")
        self.arrow_upper_left = Arrow2d(self.ax, self.x, self.y, self.theta + np.pi / 4., 0.004, "red", self.alpha, "")
        self.arrow_lower_right = Arrow2d(self.ax, self.x, self.y, self.theta - np.pi * 3. / 4., 0.004, "red",
                                         self.alpha, "")
        self.arrow_lower_left = Arrow2d(self.ax, self.x, self.y, self.theta + np.pi * 3. / 4., 0.004, "red", self.alpha,
                                        "")

    def set_data(self, x, y, theta):
        self.x, self.y = x, y
        self.xy = np.array([self.x, self.y])
        self.theta = theta
        self.circle.set_center(self.xy)
        self.arrow_upper_right.set_data(self.x, self.y, self.theta - np.pi / 4.)
        self.arrow_upper_left.set_data(self.x, self.y, self.theta + np.pi / 4.)
        self.arrow_lower_right.set_data(self.x, self.y, self.theta - np.pi * 3. / 4.)
        self.arrow_lower_left.set_data(self.x, self.y, self.theta + np.pi * 3. / 4.)

    def set_color(self, color_circle, color_arrow):
        self.arrow_upper_right.set_color(color_arrow)
        self.arrow_upper_left.set_color(color_arrow)
        self.arrow_lower_right.set_color(color_arrow)
        self.arrow_lower_left.set_color(color_arrow)
        self.circle.set_color(color_circle)

    def get_point(self):
        return self.xy


class ReactionPointPath:
    def __init__(self, ax, point_a, point_b, line_width, line_style, color):
        self.ax = ax
        self.point_a = point_a
        self.point_b = point_b
        self.line_width = line_width
        self.line_style = line_style
        self.color = color

        self.angle_space = np.arange(0, 360)
        self.x_path = []
        self.y_path = []

        self.calc_path(self.point_a, self.point_b)
        self.draw_path()

    def calc_path(self, point_a, point_b):
        self.x_path = []
        self.y_path = []
        for i in range(360):
            vector_a = np.array([np.cos(np.deg2rad(i)), np.sin(np.deg2rad(i))])
            vector_b = np.array([np.cos(np.deg2rad(i + 45)), np.sin(np.deg2rad(i + 45))])
            cross_point = get_cross_point(point_a, point_b, vector_a, vector_b)
            self.x_path.append(cross_point[0])
            self.y_path.append(cross_point[1])

    def draw_path(self):
        self.path = self.ax.plot(self.x_path, self.y_path, linewidth=self.line_width, linestyle=self.line_style,
                                 color=self.color, label="Reaction points path")


class FermionAfterImages:
    def __init__(self, ax, number, point, line_width, line_style, color, alpha):
        self.ax = ax
        self.number = number
        self.point = point
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.alpha = alpha

        self.fermion_arrows = []
        self.fermion_lines = []
        self.fermions = []

        for i in range(self.number):
            angle_deg = np.random.rand() * 360
            self.arrow = Arrow2d(ax0, self.point[0], self.point[1], np.deg2rad(angle_deg),
                                 self.line_width / 300, self.color, self.alpha, "")
            self.fermion_arrows.append(self.arrow)
            self.line = LineAngleLength2d(ax0, point[0], point[1], np.deg2rad(angle_deg),
                                          20, self.color, self.line_width, self.line_style, "")
            self.fermion_lines.append(self.line)
            distance = np.random.rand() * 15.
            point_fermion_x = distance * np.cos(np.deg2rad(angle_deg)) + self.point[0]
            point_fermion_y = distance * np.sin(np.deg2rad(angle_deg)) + self.point[1]
            self.fermion = Fermion(self.ax, point_fermion_x, point_fermion_y, np.deg2rad(angle_deg), self.alpha)
            self.fermion.set_color("gray", "gray")
            self.fermions.append(self.fermion)

    def redraw(self):
        for i in range(self.number):
            angle_deg = np.random.rand() * 360
            distance = np.random.rand() * 15.
            point_fermion_x = distance * np.cos(np.deg2rad(angle_deg)) + self.point[0]
            point_fermion_y = distance * np.sin(np.deg2rad(angle_deg)) + self.point[1]
            self.fermion_lines[i].set_direction(np.deg2rad(angle_deg))
            self.fermions[i].set_data(point_fermion_x, point_fermion_y, np.deg2rad(angle_deg))


class PhotonAfterImages:
    def __init__(self, ax, number, point, line_width, line_style, color, alpha):
        self.ax = ax
        self.number = number
        self.point = point
        self.line_width = line_width
        self.line_style = line_style
        self.alpha = alpha
        self.color = color
        self.photon_arrows = []
        self.photon_lines = []

        for i in range(self.number):
            angle_deg = np.random.rand() * 360
            self.photon_arrow = Arrow2d(ax0, self.point[0], self.point[1], np.deg2rad(angle_deg),
                                        self.line_width / 300, self.color, self.alpha, "")
            self.photon_arrows.append(self.photon_arrow)
            self.line = LineAngleLength2d(ax0, self.point[0], self.point[1], np.deg2rad(angle_deg),
                                          20, self.color, self.line_width, self.line_style, "")
            self.photon_lines.append(self.line)

    def redraw(self):
        for i in range(self.number):
            angle_deg = np.random.rand() * 360
            self.photon_lines[i].set_direction(np.deg2rad(angle_deg))


class ParametricLine:
    def __init__(self, ax, point, angle, range_min, range_max, resolution, line_width, line_style, color, label):
        self.ax = ax
        self.point = point
        self.angle = angle
        self.range_min = range_min
        self.range_max = range_max
        self.resolution = resolution
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.label = label

        self.direction = np.array([np.cos(self.angle), np.sin(self.angle)])
        self.t = np.linspace(self.range_min, self.range_max, self.resolution)

        self.line_x = self.point[0] + self.t * self.direction[0]
        self.line_y = self.point[1] + self.t * self.direction[1]

        self.line, = self.ax.plot(self.line_x, self.line_y, linewidth=self.line_width, linestyle=self.line_style,
                                  color=self.color, label=self.label)

    def set_direction(self, angle):
        self.angle = angle
        self.direction = np.array([np.cos(self.angle), np.sin(self.angle)])
        self.line_x = self.point[0] + self.t * self.direction[0]
        self.line_y = self.point[1] + self.t * self.direction[1]
        self.line.set_data(self.line_x, self.line_y)

    def set_point(self, point):
        self.point = point
        self.line_x = self.point[0] + self.t * self.direction[0]
        self.line_y = self.point[1] + self.t * self.direction[1]
        self.line.set_data(self.line_x, self.line_y)


def get_cross_point(point_a, point_b, vector_a, vector_b):
    a0, a1 = vector_a
    b0, b1 = vector_b
    c = point_b - point_a

    matrix = np.array([[a0, - b0], [a1, - b1]])
    solution = np.linalg.solve(matrix, c)
    t = solution[0]
    cross_point = point_a + t * vector_a

    return cross_point


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")


def update_fermion():
    cross_point = get_cross_point(point_center_photon, point_center_fermion, photon_line.get_vector(),
                                  fermion_line.get_vector())
    x_fermion, y_fermion = cross_point[0], cross_point[1]
    theta_fermion = fermion_line.get_direction()
    fermion.set_data(x_fermion, y_fermion, theta_fermion)
    if np.abs(angle_deg_fermion - angle_deg_photon) == 45:
        fermion.set_color("darkorange", "red")
    else:
        fermion.set_color("gray", "gray")


def set_angle_fermion(value):
    global angle_deg_fermion
    angle_deg_fermion = value
    fermion_arrow.set_direction(np.deg2rad(angle_deg_fermion))
    fermion_line.set_direction(np.deg2rad(angle_deg_fermion))
    update_fermion()
    time_axis_fermion.set_direction(np.deg2rad(angle_deg_fermion))
    spatial_axis_fermion.set_direction(np.deg2rad(angle_deg_fermion + 90.))
    world_line_stationary_observer.set_point(fermion.get_point())


def set_angle_photon(value):
    global angle_deg_photon
    angle_deg_photon = value
    photon_arrow.set_direction(np.deg2rad(angle_deg_photon))
    photon_line.set_direction(np.deg2rad(angle_deg_photon))
    update_fermion()
    world_line_stationary_observer.set_point(fermion.get_point())


def redraw_afterimage():
    photon_after_images.redraw()
    fermion_after_images.redraw()


def create_parameter_setter():
    frm_p = ttk.Labelframe(root, relief="ridge", text="Photon", labelanchor='n')
    frm_p.pack(side='left', fill=tk.Y)

    lbl_angle_p = tk.Label(frm_p, text="Angle")
    lbl_angle_p.pack(side="left")

    var_angle_p = tk.StringVar(root)
    var_angle_p.set(str(angle_deg_photon))
    spn_angle_p = tk.Spinbox(
        frm_p, textvariable=var_angle_p, format="%.1f", from_=-360, to=360, increment=1,
        command=lambda: set_angle_photon(float(var_angle_p.get())), width=5
    )
    spn_angle_p.pack(side="left")

    frm_f = ttk.Labelframe(root, relief="ridge", text="Fermion", labelanchor='n')
    frm_f.pack(side='left', fill=tk.Y)

    lbl_angle_f = tk.Label(frm_f, text="Angle")
    lbl_angle_f.pack(side="left")

    var_angle_f = tk.StringVar(root)
    var_angle_f.set(str(angle_deg_fermion))
    spn_angle_f = tk.Spinbox(
        frm_f, textvariable=var_angle_f, format="%.1f", from_=-360, to=360, increment=1,
        command=lambda: set_angle_fermion(float(var_angle_f.get())), width=5
    )
    spn_angle_f.pack(side="left")

    btn_redraw = tk.Button(root, text="Redraw afterimages", command=redraw_afterimage)
    btn_redraw.pack(side="left")


def draw_static_diagrams():
    center_line_h, = ax0.plot([x_min, x_max], [0., 0.], color="gray", linestyle="-.", linewidth=1.5)
    center_line_v0, = ax0.plot([point_center_photon[0], point_center_photon[0]], [y_min, y_max],
                               color="gray", linestyle="-.", linewidth=1.5)
    center_line_v1, = ax0.plot([point_center_fermion[0], point_center_fermion[0]], [y_min, y_max],
                               color="gray", linestyle="-.", linewidth=1.5)

    circle_photon = patches.Circle(xy=point_center_photon, radius=1, fill=False, color="darkorange",
                                   linestyle=":", linewidth=1.5)
    ax0.add_patch(circle_photon)
    circle_fermion = patches.Circle(xy=point_center_fermion, radius=1, fill=False, color="darkorange",
                                    linestyle=":", linewidth=1.5)
    ax0.add_patch(circle_fermion)


def update_diagrams():
    pass


def reset():
    global is_play
    is_play = False
    # cnt.reset()
    update_diagrams()


def switch():
    global is_play
    is_play = not is_play


def update(f):
    if is_play:
        # cnt.count_up()
        update_diagrams()


""" main loop """
if __name__ == "__main__":
    # cnt = Counter(False, ax0, x_min, y_max, 0., "Step=")
    draw_static_diagrams()

    photon_arrow = Arrow2d(ax0, point_center_photon[0], point_center_photon[1], np.deg2rad(angle_deg_photon),
                           0.004, "darkorange", 1, "")
    photon_line = LineAngleLength2d(ax0, point_center_photon[0], point_center_photon[1],
                                    np.deg2rad(angle_deg_photon), 20, "darkorange", 1.5,
                                    "--", "Photon direction")
    fermion_arrow = Arrow2d(ax0, point_center_fermion[0], point_center_fermion[1], np.deg2rad(angle_deg_fermion),
                            0.004, "blue", 1, "")
    fermion_line = LineAngleLength2d(ax0, point_center_fermion[0], point_center_fermion[1],
                                     np.deg2rad(angle_deg_fermion), 20, "blue", 1.5, "--",
                                     "Fermion direction (Fermion's world line)")

    cross_point = get_cross_point(point_center_photon, point_center_fermion, photon_line.get_vector(),
                                  fermion_line.get_vector())
    x_fermion, y_fermion = cross_point[0], cross_point[1]
    theta_fermion = fermion_line.get_direction()
    fermion = Fermion(ax0, x_fermion, y_fermion, theta_fermion, 1)

    path = ReactionPointPath(ax0, point_center_photon, point_center_fermion, 0.5, "-.", "gold")

    photon_after_images = PhotonAfterImages(ax0, 40, point_center_photon, 0.5, "--",
                                            "silver", 0.5)
    fermion_after_images = FermionAfterImages(ax0, 40, point_center_fermion, 0.5, "--",
                                              "silver", 0.2)

    dummy, = ax0.plot([0, 0], [0, 0], linewidth=0.5, linestyle="--", color="gray", label="Afterimages")

    time_axis_fermion = ParametricLine(ax0, point_center_photon, np.deg2rad(angle_deg_fermion),
                                       -20., 20., 100, 1, "-", "red",
                                       "Time axis of fermion")
    spatial_axis_fermion = ParametricLine(ax0, point_center_photon, np.deg2rad(angle_deg_fermion + 90),
                                          -20., 20., 100, 1, "--", "red",
                                          "Spatial axis of fermion")

    photon_path0 = ParametricLine(ax0, point_center_photon, np.deg2rad(45.),
                                  -20., 20., 100, 1, "-", "darkorange",
                                  "Photon path of stationary observer")
    photon_path1 = ParametricLine(ax0, point_center_photon, np.deg2rad(-45.),
                                  -20., 20., 100, 1, "-", "darkorange",
                                  "")

    world_line_stationary_observer = ParametricLine(ax0, fermion.get_point(), np.deg2rad(90.),
                                                    -20., 20., 100, 1, "-.",
                                                    "pink", "World line of stationary observer")

    ax0.legend(loc='upper left', fontsize=6)

    create_animation_control()
    create_parameter_setter()

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
