""" Spinor 2D """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
import matplotlib.patches as patches

from matplotlib.colors import Normalize

""" Global variables """
cnt = 0
num_of_points = 500
magnitude_phase = 0.

p0 = np.array([0., 0.])
r0 = 1.
theta0 = 0.
p1 = np.array([0., 2.])
r1 = 1.
p0_d = np.array([0., 1.])

""" Animation control """
is_play = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Create figure and axes """
title_tk = "Spinor 2D"
title_ax0 = title_tk

x_min = -3.
x_max = 3.
y_min = -3.
y_max = 3.

fig = Figure()
ax0 = fig.add_subplot(111)
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")


""" Embed in Tkinter """
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

""" Global objects of Tkinter """
var_num_points = tk.StringVar(root)
var_theta_s2_deg = tk.StringVar(root)
var_turn = tk.StringVar(root)

""" Classes and functions """


class Scatter2D:
    def __init__(self, ax, size_scat, cmap_scat, norm_vmin, norm_vmax):
        self.ax = ax
        self.size_scat = size_scat
        self.cmap_scat = cmap_scat
        self.norm = Normalize(vmin=norm_vmin, vmax=norm_vmax)

        self.points = [(0, 0)]   # Dummy
        self.magnitude = [0]

        xs, ys = zip(*self.points)
        self.scat_data = ax0.scatter(xs, ys, c=self.magnitude, cmap=self.cmap_scat, s=self.size_scat, norm=self.norm)

    def append(self, x, y, value):
        self.points.append((x, y))
        self.magnitude.append(value)

        xs, ys = zip(*self.points[1:])
        self.scat_data.remove()
        self.scat_data = ax0.scatter(xs, ys, c=self.magnitude[1:], cmap=self.cmap_scat, s=self.size_scat, norm=self.norm)

    def clear_scatter(self):
        self.points = [(0, 0)]  # Dummy
        self.magnitude = [0]

        xs, ys = zip(*self.points)
        self.scat_data.remove()
        self.scat_data = ax0.scatter(xs, ys, c=self.magnitude, cmap=self.cmap_scat, s=self.size_scat, norm=self.norm)

    def set_cmap(self, value):
        self.cmap_scat = value

    def set_size(self, value):
        self.size_scat = value


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")
    btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: scatter_internal_phase.clear_scatter())
    btn_clear.pack(side="left")


def update_diagram():
    global cnt, line0, arrow1, l0_x, l0_y, l1_x, l1_y, circle_d
    global magnitude_phase
    tx_step.set_text(' Step=' + str(cnt))
    tx_theta0.set_text(' Theta0=' + str(round(cnt % 360)) + "deg")
    tx_theta1.set_text(' Theta1=' + str(round((cnt * 2) % 720)) + "deg")

    th0 = (theta0 + (2. * np.pi) / 360. * cnt) % (2. * np.pi)
    l0_x = r0 * np.cos(- th0 + np.pi / 2.)
    l0_y = r0 * np.sin(- th0 + np.pi / 2.)
    th1 = (theta0 + (2. * np.pi) / 360. * cnt * 2) % (2. * np.pi)
    l1_x = l0_x + r1 * np.cos(- th1 + np.pi / 2.)
    l1_y = l0_y + r1 * np.sin(- th1 + np.pi / 2.)
    line0.set_data([0., l0_x], [0., l0_y])
    arrow1.xy = [l1_x, l1_y]
    arrow1.set_position([l0_x, l0_y])
    circle_d.set_center([l0_x, l0_y])
    magnitude_phase = (np.cos(th0) + 1) / 2.


def reset():
    global is_play
    global cnt, theta0, magnitude_phase
    if is_play:
        is_play = not is_play
    cnt = 0
    theta0 = 0.
    magnitude_phase = 0.
    update_diagram()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt, line0, arrow1, l0_x, l0_y, l1_x, l1_y, circle_d
    if is_play:
        update_diagram()
        scatter_internal_phase.append(l1_x, l1_y, magnitude_phase)
        cnt += 1


""" main loop """
if __name__ == "__main__":
    create_animation_control()

    tx_step = ax0.text(x_min, y_max * 0.9, " Step=" + str(0))
    tx_theta0 = ax0.text(x_min, y_max * 0.8, " Theta0=" + str(0) + "deg")
    tx_theta1 = ax0.text(x_min, y_max * 0.7, " Theta1=" + str(0) + "deg")

    circle = patches.Circle(xy=p0, radius=r0, fill=False, color="gray", linestyle="--")
    ax0.add_patch(circle)
    circle_d = patches.Circle(xy=p0_d, radius=r0, fill=False, color="red", linestyle="--")
    ax0.add_patch(circle_d)

    x = np.linspace(x_min, x_max, num_of_points)

    l0_x = r0 * np.cos(theta0 + np.pi / 2.)
    l0_y = r0 * np.sin(theta0 + np.pi / 2.)
    l1_x = l0_x + r1 * np.cos(theta0 * 2. + np.pi / 2.)
    l1_y = l0_y + r1 * np.sin(theta0 * 2. + np.pi / 2.)
    line0, = ax0.plot([0., l0_x], [0., l0_y], linewidth=2, color="gray")

    arrow1 = ax0.annotate('', xy=[l1_x, l1_y], xytext=[l0_x, l0_y],
                          arrowprops=dict(width=1, headwidth=6, headlength=6,
                                          facecolor="red", edgecolor="red"))
    theta = np.linspace(0, 2 * np.pi, 100)
    radius = 0.3

    a0 = r0 * np.cos(- theta + np.pi / 2.)
    b0 = r0 * np.sin(- theta + np.pi / 2.)
    a1 = a0 + r1 * np.cos(- theta * 2. + np.pi / 2.)
    b1 = b0 + r1 * np.sin(- theta * 2. + np.pi / 2.)
    curve, = ax0.plot(a1, b1, linestyle="-", color="gray", linewidth=1)

    scatter_internal_phase = Scatter2D(ax0, 10, "plasma", 0, 1)

    anim = animation.FuncAnimation(fig, update, interval=50, save_count=100)
    root.mainloop()

