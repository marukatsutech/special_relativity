""" Minkowski diagram and Light-sphere diagram """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import proj3d
import matplotlib.patches as patches

""" Global variables """
beta = 0.
beta_sphere = 0.
length_rod = 3.
time = 0.

""" Animation control """
is_play = True

""" Other parameters """

""" Create figure and axes """
title_ax0 = "Minkowski diagram and Light-sphere diagram"
title_tk = title_ax0

x_min = -10.
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
ax1.set_title("Light-sphere diagram")
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
var_sync = tk.BooleanVar(root)
var_show = tk.BooleanVar(root)

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


class ConcentricCircles:
    def __init__(self, ax, xy, radius, radius_step, number, line_style, line_width, color):
        self.ax = ax
        self.xy = xy
        self.radius = radius
        self.radius_step = radius_step
        self.number = number
        self.line_style = line_style
        self.line_width = line_width
        self.color = color

        self.circles = []
        for i in range(self.number):
            r = self.radius + i * self.radius_step
            circle = patches.Circle(xy=self.xy, radius=r, fill=False,
                                    linewidth=self.line_width, linestyle=self.line_style, color=self.color)
            self.ax.add_patch(circle)

            self.circles.append(circle)

    def hide(self):
        for i in range(self.number):
            self.circles[i].set_color("white")

    def show(self):
        for i in range(self.number):
            self.circles[i].set_color(self.color)


class LightArrows:
    def __init__(self):
        self.time = 0.

        self.light_r = ax0.quiver(0., 0., self.time, self.time, color="darkorange",
                                  width=0.007, alpha=1.0, scale_units='xy', scale=1)
        self.light_l = ax0.quiver(0., 0., - self.time, self.time, color="darkorange",
                                  width=0.007, alpha=1.0, scale_units='xy', scale=1)

        self.light_sphere = []
        for i in range(16):
            angle = np.deg2rad(i * 360. / 16.)
            self.light_s = ax1.quiver(0., 0., self.time * np.cos(angle), self.time * np.sin(angle),
                                      color="darkorange", width=0.007, alpha=1.0, scale_units='xy', scale=1)
            self.light_sphere.append(self.light_s)

    def set_time(self, value):
        self.time = value
        self.update_arrows()

    def update_arrows(self):
        self.light_r.set_UVC(self.time, self.time)
        self.light_l.set_UVC(- self.time, self.time)

        for i in range(16):
            angle = np.deg2rad(i * 360. / 16.)
            self.light_sphere[i].set_UVC(self.time * np.cos(angle), self.time * np.sin(angle))


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

    txt_beta.set_text("Beta(=v/c): " + str(beta))
    if var_sync.get():
        bt = beta
    else:
        bt = beta_sphere
    txt_beta1.set_text("Beta(=v/c): " + str(bt))

    update_diagrams()


def set_beta_sphere(value):
    global beta_sphere
    global txt_beta, txt_beta1
    beta_sphere = value

    txt_beta.set_text("Beta(=v/c): " + str(beta))
    if var_sync.get():
        bt = beta
    else:
        bt = beta_sphere
    txt_beta1.set_text("Beta(=v/c): " + str(bt))

    update_diagrams()


def show_hide(value):
    if value:
        concentric_circles_time.show()
        concentric_circles_distance.show()
    else:
        concentric_circles_time.hide()
        concentric_circles_distance.hide()


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

    frm_beta_sphere = ttk.Labelframe(root, relief="ridge", text="Beta=v/c in Light-sphere diagram", labelanchor='n')
    frm_beta_sphere.pack(side="left", fill=tk.Y)

    # var_sync = tk.BooleanVar(root)
    chk_sync = tk.Checkbutton(frm_beta_sphere, text="Synchronize", variable=var_sync)
    chk_sync.pack(side='left')
    var_sync.set(True)

    var_beta_sphere = tk.StringVar(root)
    var_beta_sphere.set(str(beta_sphere))
    spn_length = tk.Spinbox(
        frm_beta_sphere, textvariable=var_beta_sphere, format="%.1f", from_=-20., to=20., increment=0.1,
        command=lambda: set_beta_sphere(float(var_beta_sphere.get())), width=4
    )
    spn_length.pack(side='left')

    frm_time = ttk.Labelframe(root, relief="ridge", text="Time", labelanchor="n")
    frm_time.pack(side='left', fill=tk.Y)

    var_time = tk.StringVar(root)
    var_time.set(str(time))
    spn_time = tk.Spinbox(
        frm_time, textvariable=var_time, format="%.1f", from_=0., to=5., increment=1.,
        command=lambda: light_arrows.set_time(float(var_time.get())), width=4
    )
    spn_time.pack(side='left')

    frm_show = ttk.Labelframe(root, relief="ridge", text="Proper time and proper distance \nin Light-sphere diagram",
                              labelanchor='n')
    frm_show.pack(side="left", fill=tk.Y)

    # var_show = tk.BooleanVar(root)
    chk_show = tk.Checkbutton(frm_show, text="Show", variable=var_show,
                              command=lambda: show_hide(float(var_show.get())))
    chk_show.pack(side='left')
    var_show.set(False)


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

    ax0.plot([- x_max, x_max], [y_min, y_max], linestyle="-", linewidth=1, color="gray")
    ax0.plot([- x_max, x_max], [y_max, y_min], linestyle="-", linewidth=1, color="gray")

    for i in range(1, 8):
        r = i / np.sqrt(2)
        hyperbola_v(ax0, r, r, "--", 0.5, "red", 1)
        hyperbola_h(ax0, r, r, "--", 0.5, "blue", 1)

    for m in range(1, 8):
        distance = 4 / np.sqrt(2)
        circle = patches.Circle(xy=(- distance, 0.), radius=m, fill=False, linestyle="-", linewidth=0.5, color="red")
        ax0.add_patch(circle)

    # ax1
    ax1.arrow(x_min, 0., x_max - x_min, 0., head_width=0.2, ec='black', color='black', length_includes_head=True)
    ax1.arrow(0., y_min, 0., y_max - y_min, head_width=0.2, ec='black', color='black', length_includes_head=True)

    for j in range(1, 8):
        r = j / np.sqrt(2)
        circle = patches.Circle(xy=(0., 0.), radius=r, fill=False, linestyle="--", linewidth=0.5, color="blue")
        ax1.add_patch(circle)

    for k in range(1, 8):
        distance = 4 / np.sqrt(2)
        circle = patches.Circle(xy=(- distance, 0.), radius=k, fill=False, linestyle="-", linewidth=0.5, color="red")
        ax1.add_patch(circle)


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
    if var_sync.get():
        bt = beta
    else:
        bt = beta_sphere

    vector_beta_t = np.array([bt, 1])
    vector_beta_t = vector_beta_t / np.linalg.norm(vector_beta_t)
    vector_beta_x = np.array([1., - bt])
    vector_beta_x = vector_beta_x / np.linalg.norm(vector_beta_x)
    if bt < 1:
        quiver_t_observer1.set_offsets(np.array([- bt * x_max, y_min]))
        quiver_t_observer1.set_UVC(bt * x_max * 2, y_max - y_min)
        quiver_x_observer1.set_offsets(np.array([x_min, - bt * y_min]))
        quiver_x_observer1.set_UVC(x_max - x_min, - bt * y_max * 2)

        txt_ct_p1.set_position((bt * x_max, y_max))
        txt_x_p1.set_position((x_max, - bt * y_max))
    else:
        quiver_t_observer1.set_offsets(np.array([x_min, vector_beta_t[1] * x_min / vector_beta_t[0]]))
        quiver_t_observer1.set_UVC(x_max * 2., vector_beta_t[1] * x_max / vector_beta_t[0] * 2.)
        quiver_x_observer1.set_offsets(np.array([vector_beta_x[0] * y_max / vector_beta_x[1], y_max]))
        quiver_x_observer1.set_UVC(vector_beta_x[0] * y_min / vector_beta_x[1] * 2., y_min * 2.)

        txt_ct_p1.set_position((x_max, float(vector_beta_t[1] * x_max / vector_beta_t[0])))
        txt_x_p1.set_position((float(vector_beta_x[0] * y_min / vector_beta_x[1]), y_min))

    for j in range(len(dots_t1s)):
        x_t = (j + 1) * np.cos(np.arctan2(1., bt))
        y_t = (j + 1) * np.sin(np.arctan2(1., bt))

        x_x = (j + 1) * np.cos(- np.arctan2(bt, 1.))
        y_x = (j + 1) * np.sin(- np.arctan2(bt, 1.))

        dots_t1s[j].set_data([x_t], [y_t])
        dots_x1s[j].set_data([x_x], [y_x])

        dots_t2s[j].set_data([- x_t], [- y_t])
        dots_x2s[j].set_data([- x_x], [- y_x])


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
    # create_parameter_setter()

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
    """
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

    """

    dummy0, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="darkorange", linewidth=0.5, linestyle="-", label="Lightray")
    dummy1, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="red", linewidth=0.5, linestyle="--", label="Proper time")
    dummy2, = ax0.plot(np.array([0, 0]), np.array([0, 0]),
                       color="blue", linewidth=0.5, linestyle="--", label="Proper distance")
    # ax0.legend(loc='lower right', fontsize=8)

    # ax1
    quiver_t_observer1 = ax1.quiver(0., y_min, 0., y_max - y_min, color="red",
                                    width=0.005, alpha=1.0, scale_units='xy', scale=1)
    quiver_x_observer1 = ax1.quiver(x_min, 0., x_max - x_min, 0., color="blue",
                                    width=0.005, alpha=1.0, scale_units='xy', scale=1)

    txt_ct_p1 = ax1.text(0., y_max, "ct'", color="red")
    txt_x_p1 = ax1.text(x_max, 0., "x'", color="blue")

    txt_beta1 = ax1.text(x_min + 0.5, y_max - 0.5, "Beta(=v/c): " + str(beta))

    dots_t1s = []
    dots_x1s = []
    dots_t2s = []
    dots_x2s = []

    """
    for j_ in range(1, 5):
        dot_t1s, = ax1.plot(0., j_, "o", color="red", markersize=3)
        dots_t1s.append(dot_t1s)

        dot_x1s, = ax1.plot(j_, 0., "o", color="blue", markersize=3)
        dots_x1s.append(dot_x1s)

        dot_t2s, = ax1.plot(0., - j_, "o", color="red", markersize=3)
        dots_t2s.append(dot_t2s)

        dot_x2s, = ax1.plot(- j_, 0., "o", color="blue", markersize=3)
        dots_x2s.append(dot_x2s)
    """

    concentric_circles_time = ConcentricCircles(ax1, (0., 0.), 1.1, 1, 6, ":",
                                                1, "red")
    concentric_circles_distance = ConcentricCircles(ax1, (0., 0.), 0.9, 1, 6, ":",
                                                    1, "blue")
    concentric_circles_time.hide()
    concentric_circles_distance.hide()

    light_arrows = LightArrows()

    # ax1.legend(loc='lower right', fontsize=8)

    # Start animation
    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
