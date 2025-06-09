""" Hyperbola """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import proj3d


""" Global variables """
a, b = 1., 1.

""" Animation control """
is_play = True

""" Other parameters """

""" Create figure and axes """
title_ax0 = "Hyperbola"
title_tk = title_ax0

x_min = -5.
x_max = 5.
y_min = -5.
y_max = 5.

fig = Figure()

ax0 = fig.add_subplot(111)
ax0.set_title("Hyperbola")
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


class HyperbolaHorizontal:
    def __init__(self, ax, a, b, line_style, line_width, color, alpha):
        self.ax = ax
        self.a, self.b = a, b
        self.line_style = line_style
        self.line_width = line_width
        self.color = color
        self.alpha = alpha

        self.x_r = np.linspace(a, x_max, 200)  # Right branch
        self.x_l = np.linspace(x_min, - a, 200)  # Left branch
        self.y_r = np.sqrt((self.x_r ** 2 / self.a ** 2 - 1) * self.b ** 2)
        self.y_l = np.sqrt((self.x_l ** 2 / self.a ** 2 - 1) * self.b ** 2)

        self.plt_right_u, = ax.plot(self.x_r, self.y_r, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)
        self.plt_right_l, = ax.plot(self.x_r, - self.y_r, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)

        self.plt_left_u, = ax.plot(self.x_l, self.y_l, linestyle=self.line_style, linewidth=self.line_width,
                                   color=self.color, alpha=self.alpha)
        self.plt_left_l, = ax.plot(self.x_l, - self.y_l, linestyle=self.line_style, linewidth=self.line_width,
                                   color=self.color, alpha=self.alpha)

    def set_ab(self, value_a, value_b):
        if value_a != 0. and value_b != 0.:
            self.a, self.b = value_a, value_b

            self.x_r = np.linspace(a, x_max, 200)  # Right branch
            self.x_l = np.linspace(x_min, - a, 200)  # Left branch
            self.y_r = np.sqrt((self.x_r ** 2 / self.a ** 2 - 1) * self.b ** 2)
            self.y_l = np.sqrt((self.x_l ** 2 / self.a ** 2 - 1) * self.b ** 2)

            self.plt_right_u.set_data(self.x_r, self.y_r)
            self.plt_right_l.set_data(self.x_r, -self.y_r)

            self.plt_left_u.set_data(self.x_l, self.y_l)
            self.plt_left_l.set_data(self.x_l, - self.y_l)

    def set_a(self, value_a):
        self.set_ab(value_a, self.b)

    def set_b(self, value_b):
        self.set_ab(self.a, value_b)


class HyperbolaVertical:
    def __init__(self, ax, a, b, line_style, line_width, color, alpha):
        self.ax = ax
        self.a, self.b = a, b
        self.line_style = line_style
        self.line_width = line_width
        self.color = color
        self.alpha = alpha

        self.y_u = np.linspace(b, y_max, 200)  # Upper branch
        self.y_l = np.linspace(y_min, - a, 200)  # Lower branch
        self.x_u = np.sqrt((self.y_u ** 2 / self.b ** 2 - 1) * self.a ** 2)
        self.x_l = np.sqrt((self.y_l ** 2 / self.b ** 2 - 1) * self.a ** 2)

        self.plt_upper_r, = ax.plot(self.x_u, self.y_u, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)
        self.plt_upper_l, = ax.plot(- self.x_u, self.y_u, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)

        self.plt_lower_r, = ax.plot(self.x_l, self.y_l, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)
        self.plt_lower_l, = ax.plot(- self.x_l, self.y_l, linestyle=self.line_style, linewidth=self.line_width,
                                    color=self.color, alpha=self.alpha)

    def set_ab(self, value_a, value_b):
        if value_a != 0. and value_b != 0.:
            self.a, self.b = value_a, value_b

            self.y_u = np.linspace(b, y_max, 200)  # Upper branch
            self.y_l = np.linspace(y_min, - b, 200)  # Lower branch

            self.x_u = np.sqrt((self.y_u ** 2 / self.b ** 2 - 1) * self.a ** 2)
            self.x_l = np.sqrt((self.y_l ** 2 / self.b ** 2 - 1) * self.a ** 2)

            self.plt_upper_r.set_data(self.x_u, self.y_u)
            self.plt_upper_l.set_data(- self.x_u, self.y_u)

            self.plt_lower_r.set_data(self.x_l, self.y_l)
            self.plt_lower_l.set_data(- self.x_l, self.y_l)

    def set_a(self, value_a):
        self.set_ab(value_a, self.b)

    def set_b(self, value_b):
        self.set_ab(self.a, value_b)


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
    y_r = np.sqrt((x_r ** 2 / b ** 2 - 1) * b ** 2)
    y_l = np.sqrt((x_l ** 2 / b ** 2 - 1) * a ** 2)

    plt_right_u, = ax.plot(x_r, y_r, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
    plt_right_l, = ax.plot(x_r, -y_r, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)

    plt_left_u, = ax.plot(x_l, y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)
    plt_left_l, = ax.plot(x_l, -y_l, linestyle=line_style, linewidth=line_width, color=color, alpha=alpha)


def set_a(value):
    global a, txt_ab
    a = value
    txt_ab.set_text("a: " + str(a) + ", " + "b: " + str(b))
    hyperbola_h1.set_a(a)
    hyperbola_v1.set_a(a)
    # update_diagrams()


def set_b(value):
    global b, txt_ab
    b = value
    txt_ab.set_text("a: " + str(a) + ", " + "b: " + str(b))
    hyperbola_h1.set_b(b)
    hyperbola_v1.set_b(b)
    # update_diagrams()


def set_ab(value):
    global a, b, txt_ab
    a = value
    b = value
    txt_ab.set_text("a: " + str(a) + ", " + "b: " + str(b))
    hyperbola_h1.set_a(a)
    hyperbola_h1.set_b(b)
    hyperbola_v1.set_a(a)
    hyperbola_v1.set_b(b)
    # update_diagrams()


def create_parameter_setter():
    frm_a = ttk.Labelframe(root, relief="ridge", text="a", labelanchor="n")
    frm_a.pack(side='left', fill=tk.Y)

    var_a = tk.StringVar(root)
    var_a.set(str(a))
    spn_a = tk.Spinbox(
        frm_a, textvariable=var_a, format="%.1f", from_=0.1, to=5., increment=0.1,
        command=lambda: set_a(float(var_a.get())), width=4
    )
    spn_a.pack(side='left')

    frm_b = ttk.Labelframe(root, relief="ridge", text="b", labelanchor="n")
    frm_b.pack(side='left', fill=tk.Y)

    var_b = tk.StringVar(root)
    var_b.set(str(a))
    spn_b = tk.Spinbox(
        frm_b, textvariable=var_b, format="%.1f", from_=0.1, to=5., increment=0.1,
        command=lambda: set_b(float(var_b.get())), width=4
    )
    spn_b.pack(side='left')

    frm_ab = ttk.Labelframe(root, relief="ridge", text="a and b", labelanchor="n")
    frm_ab.pack(side='left', fill=tk.Y)

    var_ab = tk.StringVar(root)
    var_ab.set(str(a))
    spn_ab = tk.Spinbox(
        frm_ab, textvariable=var_ab, format="%.1f", from_=0.1, to=5., increment=0.1,
        command=lambda: set_ab(float(var_ab.get())), width=4
    )
    spn_ab.pack(side='left')


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


def update_diagrams():
    pass


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

    txt_ab = ax0.text(x_min + 0.5, y_max - 0.5, "a: " + str(a) + ", " + "b: " + str(b))

    hyperbola_h1 = HyperbolaHorizontal(ax0, a, b, "-", 2, "blue", 1.)
    hyperbola_v1 = HyperbolaVertical(ax0, a, b, "-", 2, "red", 1.)

    # Start animation
    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
