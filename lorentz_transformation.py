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
length_rod = 3.

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

ax0 = fig.add_subplot(121)
ax0.set_title("Minkowski diagram")
ax0.set_xlabel("x")
ax0.set_ylabel("ct")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")
ax0.grid()
ax0.set_xticks(np.arange(x_min, x_max, 1))
ax0.set_yticks(np.arange(y_min, y_max, 1))

ax1 = fig.add_subplot(122)
ax1.set_title("Lorentz transformation")
ax1.set_xlabel("x")
ax1.set_ylabel("ct")
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)
ax1.set_aspect("equal")
ax1.grid()
ax1.set_xticks(np.arange(x_min, x_max, 1))
ax1.set_yticks(np.arange(y_min, y_max, 1))

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


class HyperbolaHorizontal:
    def __init__(self, ax, a, b, line_style, line_width, color, alpha):
        self.ax = ax
        self.a, self.b = a, b
        self.line_style = line_style
        self.line_width = line_width
        self.color = color
        self.alpha = alpha

        self.x_r = np.linspace(a, x_max, 200)  # Right branch
        # x_l = np.linspace(x_min, -a, 200)  # Left branch
        self.y_r = np.sqrt((self.x_r ** 2 / self.a ** 2 - 1) * self.b ** 2)
        # y_l = np.sqrt((self.x_l ** 2 / self.a ** 2 - 1) * self.b ** 2)

        self.plt_right_u, = ax.plot(self.x_r, self.y_r, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)
        self.plt_right_l, = ax.plot(self.x_r, -self.y_r, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)

        # self.plt_left_u, = ax.plot(self.x_l, self.y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
        # self.plt_left_l, = ax.plot(self.x_l, -self.y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)

    def set_ab(self, a, b):
        self.a, self.b = a, b

        self.x_r = np.linspace(a, x_max, 200)  # Right branch
        # x_l = np.linspace(x_min, -a, 200)  # Left branch
        self.y_r = np.sqrt((self.x_r ** 2 / self.a ** 2 - 1) * self.b ** 2)
        # y_l = np.sqrt((self.x_l ** 2 / self.a ** 2 - 1) * self.b ** 2)

        self.plt_right_u.set_data(self.x_r, self.y_r)
        self.plt_right_l.set_data(self.x_r, -self.y_r)


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
    global beta
    global txt_beta, txt_beta1
    beta = value

    # print(np.rad2deg(phi_t), np.rad2deg(phi_x))

    txt_beta.set_text("Beta(=v/c): " + str(beta))
    txt_beta1.set_text("Beta(=v/c): " + str(beta))

    update_diagrams()


def set_length(value):
    global length_rod
    length_rod = value

    hyperbola_h1.set_ab(length_rod, length_rod)
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

    frm_length = ttk.Labelframe(root, relief="ridge", text="Length of rod", labelanchor="n")
    frm_length.pack(side='left', fill=tk.Y)

    var_length = tk.StringVar(root)
    var_length.set(str(length_rod))
    spn_length = tk.Spinbox(
        frm_length, textvariable=var_length, format="%.1f", from_=1., to=4., increment=1.,
        command=lambda: set_length(float(var_length.get())), width=4
    )
    spn_length.pack(side='left')


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
    # ax0
    ax0.arrow(x_min, 0., x_max - x_min, 0., head_width=0.2, ec='black', color='black', length_includes_head=True)
    ax0.arrow(0., y_min, 0., y_max - y_min, head_width=0.2, ec='black', color='black', length_includes_head=True)

    ax0.plot([x_min, x_max], [y_min, y_max], linestyle="-", linewidth=1, color="darkorange")
    ax0.plot([x_min, x_max], [y_max, y_min], linestyle="-", linewidth=1, color="darkorange")

    for i in range(1, 5):
        hyperbola_v(ax0, i, i, "--", 0.5, "red", 1)
        hyperbola_h(ax0, i, i, "--", 0.5, "blue", 1)

    # ax1
    ax1.arrow(x_min, 0., x_max - x_min, 0., head_width=0.2, ec='black', color='black', length_includes_head=True)
    ax1.arrow(0., y_min, 0., y_max - y_min, head_width=0.2, ec='black', color='black', length_includes_head=True)

    ax1.plot([x_min, x_max], [y_min, y_max], linestyle="-", linewidth=1, color="darkorange")
    ax1.plot([x_min, x_max], [y_max, y_min], linestyle="-", linewidth=1, color="darkorange")


def update_diagrams():
    global quiver_t_observer, quiver_x_observer
    global dots_t1, dots_t2, dots_x1, dots_x2
    global lines_t1, lines_t2, lines_x1, lines_x2
    global txt_ct_p, txt_x_p

    global quiver_t_observer1, quiver_x_observer1

    # ax0
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

    # ax1
    quiver_t_observer1.set_offsets(np.array([- beta * x_max, y_min]))
    quiver_t_observer1.set_UVC(beta * x_max * 2, y_max - y_min)
    quiver_x_observer1.set_offsets(np.array([x_min, beta * y_min]))
    quiver_x_observer1.set_UVC(x_max - x_min, beta * y_max * 2)

    txt_ct_p1.set_position((beta * x_max, y_max))
    txt_x_p1.set_position((x_max, beta * y_max))

    if abs(beta) != 1:
        x_rod_r = length_rod * np.cosh(np.arctanh(beta))
        y_rod_r = length_rod * np.sinh(np.arctanh(beta))
    else:
        # Escape out of range
        x_rod_r = x_max * 10
        y_rod_r = y_max * 10

    dot_rod_right.set_data([x_rod_r], [y_rod_r])
    line_rod_right.set_data([x_rod_r + beta * (y_min - y_rod_r), x_rod_r + beta * (y_max - y_rod_r)], [y_min, y_max])
    line_rod.set_data([0., x_rod_r], [0., y_rod_r])
    x_rod_right_ct_x = y_rod_r * beta
    line_rod_x.set_data([0., x_rod_r - x_rod_right_ct_x], [0., 0.])
    line_rod0.set_data([- y_rod_r * beta, x_rod_r - x_rod_right_ct_x], [- y_rod_r, 0.])


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

    # ax0
    ax0.arrow(0., y_min, 0., y_max - y_min, head_width=0.2, ec='black', color='black', length_includes_head=True)
    ax0.arrow(x_min, 0., x_max - x_min, 0., head_width=0.2, ec='black', color='black', length_includes_head=True)

    quiver_t_observer = ax0.quiver(0., y_min, 0., y_max - y_min, color="red",
                                   width=0.005, alpha=1.0, scale_units='xy', scale=1)
    quiver_x_observer = ax0.quiver(x_min, 0., x_max - x_min, 0., color="blue",
                                   width=0.005, alpha=1.0, scale_units='xy', scale=1)

    txt_ct_p = ax0.text(0., y_max, "ct'", color="red")
    txt_x_p = ax0.text(x_max, 0., "x'", color="blue")

    txt_beta = ax0.text(x_min + 0.5, y_max - 0.5, "Beta(=v/c): " + str(beta))

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
                       color="red", linewidth=0.5, linestyle="--", label="Proper time")
    dummy2, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="blue", linewidth=0.5, linestyle="--", label="Proper distance")
    ax0.legend(loc='lower right', fontsize=8)

    # ax1
    quiver_t_observer1 = ax1.quiver(0., y_min, 0., y_max - y_min, color="red",
                                    width=0.005, alpha=1.0, scale_units='xy', scale=1)
    quiver_x_observer1 = ax1.quiver(x_min, 0., x_max - x_min, 0., color="blue",
                                    width=0.005, alpha=1.0, scale_units='xy', scale=1)

    txt_ct_p1 = ax1.text(0., y_max, "ct'", color="red")
    txt_x_p1 = ax1.text(x_max, 0., "x'", color="blue")

    txt_beta1 = ax1.text(x_min + 0.5, y_max - 0.5, "Beta(=v/c): " + str(beta))

    hyperbola_h1 = HyperbolaHorizontal(ax1, length_rod, length_rod, "--", 0.5, "blue", 1.)

    dot_rod_right, = ax1.plot(0., 0., "o", color="blue", markersize=3)
    line_rod_right, = ax1.plot([0., 0.], [y_min, y_max], linestyle="-", linewidth=0.5, color="blue")
    line_rod, = ax1.plot([0., length_rod], [0., 0.], linestyle="-", linewidth=4, color="green", alpha=0.5,
                         label="Rod on the coordinate ct'-x', \nwith its left end at the coordinate ct-x when ct = 0")
    line_rod_x, = ax1.plot([0., length_rod], [0., 0.], linestyle="-", linewidth=4, color="gray", alpha=0.5,
                           label="Rod observed at ct = 0 by an observer in the coordinate ct-x")
    line_rod0, = ax1.plot([0., length_rod], [0., 0.], linestyle="--", linewidth=2, color="green", alpha=0.5,
                          label="Rod on the coordinate ct'-x', \nwith its right end at the coordinate ct-x when ct = 0")

    ax1.legend(loc='lower right', fontsize=8)

    # Start animation
    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
