""" Minkowski diagram and Lorentz transformation """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import proj3d


""" Global variables """
beta = 0.
phi_t = 0.
phi_x = 0.
axis_t_observer = np.array([0., 1.])
axis_x_observer = np.array([1., 0.])

""" Animation control """
is_play = True

""" Other parameters """

""" Create figure and axes """
title_ax0 = "Minkowski diagram and Lorentz transformation"
title_tk = title_ax0

x_min = -5.
x_max = 5.
y_min = -5.
y_max = 5.

fig = Figure()

ax0 = fig.add_subplot(111)
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("ct")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")
ax0.grid()
ax0.set_xticks(np.arange(x_min, x_max, 1))
ax0.set_yticks(np.arange(y_min, y_max, 1))

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


def hyperbola_v(ax, a, b, line_style, line_width, color, alpha):
    """ Vertical Hyperbola: y^2 / a^ 2 - x^2 / b^2 = 1 """
    y_u = np.linspace(a, y_max, 200)  # Upper branch
    y_l = np.linspace(y_min, - a, 200)  # Lower branch
    x_u = np.sqrt((y_u ** 2 / a ** 2 - 1) * b ** 2)
    x_l = np.sqrt((y_l ** 2 / a ** 2 - 1) * b ** 2)

    plt_upper_r, = ax.plot(x_u, y_u, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
    plt_upper_l, = ax.plot(- x_u, y_u, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)

    plt_lower_r, = ax.plot(x_l, y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
    plt_lower_l, = ax.plot(- x_l, y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)


def hyperbola_h(ax, a, b, line_style, line_width, color, alpha):
    """ Horizontal Hyperbola: x^2 / a^2 - y^2 / b^2 = 1 """
    x_r = np.linspace(a, x_max, 200)  # Right branch
    x_l = np.linspace(x_min, -a, 200)  # Left branch
    y_r = np.sqrt((x_r ** 2 / a ** 2 - 1) * b ** 2)
    y_l = np.sqrt((x_l ** 2 / a ** 2 - 1) * b ** 2)

    plt_right_u, = ax.plot(x_r, y_r, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
    plt_right_l, = ax.plot(x_r, -y_r, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)

    plt_left_u, = ax.plot(x_l, y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
    plt_left_l, = ax.plot(x_l, -y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)


def set_beta(value):
    global beta, axis_t_observer, axis_x_observer
    global phi_t, phi_x
    beta = value
    axis_t_observer = np.array([beta, 1.])
    axis_x_observer = np.array([1., beta])

    phi_t = np.arctan2(beta, 1.)
    phi_x = np.arctan2(1., beta)

    # print(np.rad2deg(phi_t), np.rad2deg(phi_x))

    update_diagrams()


def create_parameter_setter():
    frm_beta = ttk.Labelframe(root, relief="ridge", text="Beta=v/c", labelanchor="n")
    frm_beta.pack(side='left', fill=tk.Y)

    var_beta = tk.StringVar(root)
    var_beta.set(str(beta))
    spn_beta = tk.Spinbox(
        frm_beta, textvariable=var_beta, format="%.1f", from_=-1., to=1., increment=0.1,
        command=lambda: set_beta(float(var_beta.get())), width=4
    )
    spn_beta.pack(side='left')


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(fill=tk.X)
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(fill=tk.X)
    # btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: aaa.clear())
    # btn_clear.pack(fill=tk.X)


def draw_static_diagrams():
    ax0.arrow(x_min, 0., x_max - x_min, 0., head_width=0.2, ec='black', color='black', length_includes_head=True)
    ax0.arrow(0., y_min, 0., y_max - y_min, head_width=0.2, ec='black', color='black', length_includes_head=True)

    ax0.plot([x_min, x_max], [y_min, y_max], linestyle="-", linewidth=1, color="darkorange")
    ax0.plot([x_min, x_max], [y_max, y_min], linestyle="-", linewidth=1, color="darkorange")

    for i in range(1, 5):
        hyperbola_v(ax0, i, i, "-", 0.5, "red", 1)
        hyperbola_h(ax0, i, i, "-", 0.5, "blue", 1)
        # circle = patches.Circle(xy=(0., 0.), radius=i, fill=False, linestyle="-", linewidth=1, color="magenta")
        # ax0.add_patch(circle)


def update_diagrams():
    global quiver_t_observer, quiver_x_observer
    global dots_t1, dots_t2, dots_x1, dots_x2
    global lines_t1, lines_t2, lines_x1, lines_x2
    global txt_ct_p, txt_x_p
    quiver_t_observer.set_offsets(np.array([- beta * x_max, y_min]))
    quiver_t_observer.set_UVC(beta * x_max * 2, y_max - y_min)
    quiver_x_observer.set_offsets(np.array([x_min, beta * y_min]))
    quiver_x_observer.set_UVC(x_max - x_min, beta * y_max * 2)

    for i in range(len(dots_t1)):
        if abs(beta) != 1:
            x_t = (i + 1) * np.sinh(np.arctanh(beta))
            y_t = (i + 1) * np.cosh(np.arctanh(beta))

            x_x = (i + 1) * np.cosh(np.arctanh(beta))
            y_x = (i + 1) * np.sinh(np.arctanh(beta))
        else:
            # Escape out of range
            x_t = x_max * 10
            y_t = y_max * 10

            x_x = x_max * 10
            y_x = y_max * 10

        dots_t1[i].set_data([x_t], [y_t])
        dots_x1[i].set_data([x_x], [y_x])

        dots_t2[i].set_data([- x_t], [- y_t])
        dots_x2[i].set_data([- x_x], [- y_x])

        lines_t1[i].set_data([x_min, x_max], [y_t + beta * (x_min - x_t), y_t + beta * (x_max - x_t)])
        lines_t2[i].set_data([x_min, x_max], [- y_t + beta * (x_min + x_t), - y_t + beta * (x_max + x_t)])

        lines_x1[i].set_data([x_x + beta * (y_min - y_x), x_x + beta * (y_max - y_x)], [y_min, y_max])
        lines_x2[i].set_data([- x_x + beta * (y_min + y_x), - x_x + beta * (y_max + y_x)], [y_min, y_max])

        txt_ct_p.set_position((beta * x_max, y_max))
        txt_x_p.set_position((x_max, beta * y_max))


def reset():
    global is_play
    # cnt.reset()


def switch():
    global is_play
    is_play = not is_play


def update(f):
    if is_play:
        # cnt.count_up()
        update_diagrams()


""" main loop """
if __name__ == "__main__":
    # cnt = Counter(ax=ax0, is3d=True, xy=np.array([x_min, y_max]), z=z_max, label="Step=")
    draw_static_diagrams()
    # create_animation_control()
    create_parameter_setter()

    ax0.arrow(0., y_min, 0., y_max - y_min, head_width=0.2, ec='black', color='black', length_includes_head=True)
    ax0.arrow(x_min, 0., x_max - x_min, 0., head_width=0.2, ec='black', color='black', length_includes_head=True)

    quiver_t_observer = ax0.quiver(0., y_min, 0., y_max - y_min, color="red",
                                   linewidth=3, alpha=1.0, scale_units='xy', scale=1)
    quiver_x_observer = ax0.quiver(x_min, 0., x_max - x_min, 0., color="blue",
                                   linewidth=3, alpha=1.0, scale_units='xy', scale=1)

    txt_ct_p = ax0.text(0., y_max, "ct'", color="red")
    txt_x_p = ax0.text(x_max, 0., "x'", color="blue")

    dots_t1 = []
    dots_x1 = []
    dots_t2 = []
    dots_x2 = []
    lines_t1 = []
    lines_x1 = []
    lines_t2 = []
    lines_x2 = []
    for i_ in range(1, 5):
        dot_t1, = ax0.plot(0., i_, "o", color="red", markersize=3)
        dots_t1.append(dot_t1)

        dot_x1, = ax0.plot(i_, 0., "o", color="blue", markersize=3)
        dots_x1.append(dot_x1)

        dot_t2, = ax0.plot(0., - i_, "o", color="red", markersize=3)
        dots_t2.append(dot_t2)

        dot_x2, = ax0.plot(- i_, 0., "o", color="blue", markersize=3)
        dots_x2.append(dot_x2)

        line_t1, = ax0.plot([x_min, x_max], [i_, i_], linestyle="-", linewidth=0.2, color="red")
        lines_t1.append(line_t1)

        line_x1, = ax0.plot([i_, i_], [y_min, y_max], linestyle="-", linewidth=0.2, color="blue")
        lines_x1.append(line_x1)

        line_t2, = ax0.plot([x_min, x_max], [- i_,- i_], linestyle="-", linewidth=0.2, color="red")
        lines_t2.append(line_t2)

        line_x2, = ax0.plot([- i_, - i_], [y_min, y_max], linestyle="-", linewidth=0.2, color="blue")
        lines_x2.append(line_x2)

    dummy0, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="darkorange", linewidth=0.5, linestyle="-", label="Lightray")
    dummy1, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="red", linewidth=0.5, linestyle="-", label="Proper time")
    dummy2, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="blue", linewidth=0.5, linestyle="-", label="Proper distance")
    ax0.legend(loc='lower right', fontsize=8)

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
