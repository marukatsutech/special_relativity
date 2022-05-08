# Special relativity
import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.patches as patches


def draw_person(x_p, y_p, scale_p, col):
    size_head = 0.15 * scale_p
    head = patches.Circle(xy=(x_p, y_p), radius=size_head, fc=col)
    ax.add_patch(head)
    ax.plot([x_p, x_p], [y_p, y_p - 0.5 * scale_p], linestyle='-', c=col, linewidth=1)
    ax.plot([x_p - 0.2 * scale_p, x_p, x_p + 0.2 * scale_p], [y_p - 0.4 * scale_p, y_p - 0.2 * scale_p,
                                                              y_p - 0.4 * scale_p], linestyle='-', c=col, linewidth=1)
    ax.plot([x_p - 0.1 * scale_p, x_p, x_p + 0.1 * scale_p],
            [y_p - 0.8 * scale_p, y_p - 0.5 * scale_p, y_p - 0.8 * scale_p], linestyle='-', c=col, linewidth=1)


def draw_rocket(bt):
    length_body = 2.4
    width_body = 0.6
    y_rocket = 3.
    x_rocket = bt * 3.
    bdy = patches.Rectangle(xy=[x_rocket - length_body / 2., y_rocket - width_body / 2.], width=length_body,
                            height=width_body, fill=False, ec='red')
    ax.add_patch(bdy)
    x_body_right = x_rocket + length_body / 2.
    x_body_left = x_rocket - length_body / 2.
    y_body_top = y_rocket + width_body / 2.
    y_body_bottom = y_rocket - width_body / 2.
    if bt >= 0.:
        nose = plt.Polygon(((x_body_right, y_body_top), (x_body_right + 0.5, y_rocket),
                           (x_body_right, y_body_bottom)), fill=False, ec='red')

        fin1 = plt.Polygon(((x_body_left, y_body_top), (x_body_left, y_body_top + 0.3),
                           (x_body_left + 0.5, y_body_top)), fill=False, ec='red')

        fin2 = plt.Polygon(((x_body_left, y_body_bottom), (x_body_left, y_body_bottom - 0.3),
                            (x_body_left + 0.5, y_body_bottom)), fill=False, ec='red')

    else:
        nose = plt.Polygon(((x_body_left, y_body_top), (x_body_left - 0.5, y_rocket),
                            (x_body_left, y_body_bottom)), fill=False, ec='red')

        fin1 = plt.Polygon(((x_body_right, y_body_top), (x_body_right, y_body_top + 0.3),
                            (x_body_right - 0.5, y_body_top)), fill=False, ec='red')

        fin2 = plt.Polygon(((x_body_right, y_body_bottom), (x_body_right, y_body_bottom - 0.3),
                            (x_body_right - 0.5, y_body_bottom)), fill=False, ec='red')
    ax.add_patch(nose)
    ax.add_patch(fin1)
    ax.add_patch(fin2)
    ax.plot([x_rocket + distance_right_wall, x_rocket + distance_right_wall],
            [y_rocket - width_body / 2., y_rocket + width_body / 2.], linestyle='-', c='green', linewidth=2)
    ax.plot([x_rocket + distance_left_wall, x_rocket + distance_left_wall],
            [y_rocket - width_body / 2., y_rocket + width_body / 2.], linestyle='-', c='green', linewidth=2)
    ax.annotate('', xy=[x_rocket + distance_right_wall, y_rocket],
                xytext=[x_rocket + 0.2, y_rocket],
                arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    ax.annotate('', xy=[x_rocket + distance_left_wall, y_rocket],
                xytext=[x_rocket - 0.2, y_rocket],
                arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    lamp1 = patches.Circle(xy=(x_rocket, y_rocket), radius=0.16, fc='orange')
    ax.add_patch(lamp1)
    lamp2 = patches.Circle(xy=(x_rocket, y_rocket - 0.01), radius=0.1, fc='yellow')
    ax.add_patch(lamp2)
    lamp3 = patches.Rectangle(xy=[x_rocket - 0.08, y_rocket - 0.25], width=0.16,
                              height=0.12, fc='gray', ec='gray')
    ax.add_patch(lamp3)
    draw_person(x_rocket + 0.3, y_rocket - 0.06, 0.2, 'red')
    ax.text(x_rocket, y_rocket - 0.5, "Observer A", c='red')


def set_axis():
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title('Special relativity')
    ax.set_xlabel('x of B')
    ax.set_ylabel('ct of B')
    ax.grid()
    ax.set_aspect("equal")


def draw_graph():
    ax.cla()
    set_axis()
    # World line of Photon
    ax.plot([x_min, 0., x_max], [y_max, 0., y_max], linestyle='--', c='orange')
    ax.plot([x_min, 0., x_max], [y_min, 0., y_min], linestyle='--', c='orange', linewidth=1)
    # World line of B
    ax.annotate('', xy=[0., y_max], xytext=[0., y_min], arrowprops=dict(width=1, headwidth=4, headlength=4,
                                                                        facecolor='blue', edgecolor='blue'))
    # Spatial axis of B
    ax.annotate('', xy=[x_max, 0.], xytext=[x_min, 0.], arrowprops=dict(width=1, headwidth=4, headlength=4,
                                                                        facecolor='blue', edgecolor='blue'))
    # World line of A (lamp)
    beta = v_percentage / 100. * c
    ax.annotate('', xy=[x_max * beta, y_max], xytext=[x_min * beta, y_min],
                arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax.text(x_max * beta, y_max - 0.3, "World line of Lamp", c='red')
    # World line of A (right wall)
    if x_min + distance_right_wall * 2. <= x_max * beta + distance_right_wall <= x_max:
        ax.annotate('', xy=[x_max * beta + distance_right_wall, y_max],
                    xytext=[x_min * beta + distance_right_wall, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    elif x_max * beta + distance_right_wall > x_max:
        ax.annotate('', xy=[x_max, 1. / beta * (x_max - distance_right_wall)],
                    xytext=[x_min * beta + distance_right_wall, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    elif x_max * beta + distance_right_wall < x_min + distance_right_wall * 2.:
        ax.annotate('', xy=[x_max * beta + distance_right_wall, y_max],
                    xytext=[x_max, 1. / beta * (x_max - distance_right_wall)],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    ax.text(x_max * beta + distance_right_wall, y_max - 0.5, "World line of right wall", c='green')
    # World line of A (left wall)
    if x_min <= x_max * beta + distance_left_wall <= x_max + distance_left_wall * 2.:
        ax.annotate('', xy=[x_max * beta + distance_left_wall, y_max],
                    xytext=[x_min * beta + distance_left_wall, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    elif x_max * beta + distance_left_wall > x_max + distance_left_wall * 2.:
        ax.annotate('', xy=[x_max * beta + distance_left_wall, y_max],
                    xytext=[x_min, 1. / beta * (x_min - distance_left_wall)],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    elif x_max * beta + distance_left_wall < x_min:
        ax.annotate('', xy=[x_min, 1. / beta * (x_min - distance_left_wall)],
                    xytext=[x_min * beta + distance_left_wall, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    ax.text(x_max * beta + distance_left_wall, y_max - 0.7, "World line of left wall", c='green')
    # Crossing points
    if beta != 0.:
        if beta != 1. and beta != -1.:
            x_cp1 = - distance_right_wall * (1. / beta) / (1 - (1. / beta))
            y_cp1 = x_cp1
            cl1 = patches.Circle(xy=(x_cp1, y_cp1), radius=0.1, fc='orange')
            ax.add_patch(cl1)
            x_cp2 = distance_left_wall * (1. / beta) / (1 + (1. / beta))
            y_cp2 = - x_cp2
            cl2 = patches.Circle(xy=(x_cp2, y_cp2), radius=0.1, fc='orange')
            ax.add_patch(cl2)
    else:
        x_cp1 = distance_right_wall
        y_cp1 = x_cp1
        cl1 = patches.Circle(xy=(x_cp1, y_cp1), radius=0.1, fc='orange')
        ax.add_patch(cl1)
        x_cp2 = distance_left_wall
        y_cp2 = - x_cp2
        cl2 = patches.Circle(xy=(x_cp2, y_cp2), radius=0.1, fc='orange')
        ax.add_patch(cl2)
    # Simultaneous line and spatial axis
    try:
        if (x_cp2 - x_cp1) != 0.:
            a = (y_cp2 - y_cp1) / (x_cp2 - x_cp1)
            b = y_cp1 - a * x_cp1
            ax.plot([x_min, x_max], [a * x_min + b, a * x_max + b], linestyle='-.', c='grey')
            ax.annotate('', xy=[x_max, a * x_max], xytext=[x_min, a * x_min],
                        arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
            ax.text(x_max, a * x_max, "Spatial axis of A", c='red')
            ax.text(x_max, a * x_max + b, "Simultaneous line of A", c='gray')
    except:
        pass
    # Hyperbolic curve; ct**2 - x**2 = 1 (y**2 - x**2 = 1)
    y = np.sqrt(1. + x ** 2.)
    ax.plot(x, y, linewidth=1, c='magenta', label='ct**2 - x**2 = 1')
    y = - np.sqrt(1. + x ** 2.)
    ax.plot(x, y, linewidth=1, c='magenta')
    ax.legend(loc='lower right')

    draw_rocket(beta)
    draw_person(0.2, y_min + 1., 1.0, 'blue')
    ax.text(0.2, -2.8, "Observer B", c='blue')
    canvas.draw()
    ax.grid()


def slider_changed(event):
    global v_percentage
    v_percentage = float(scl_v.get())
    draw_graph()


# Global variables
x_min = -4.
x_max = 4.
y_min = -4.
y_max = 4.

c = 1.
v_percentage = 0.

distance_right_wall = 1.
distance_left_wall = -1.

num_of_points = 500
x = np.linspace(x_min, x_max, num_of_points)

cv_x = []
cv_y = []

# Generate tkinter
root = tkinter.Tk()
root.title("Special relativity")

# Generate figure and axes
fig = Figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

# Embed Figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

# Draw circles as initial
draw_graph()

# Add toolbar
toolbar = NavigationToolbar2Tk(canvas, root)

# Widgets
lbl_position = tkinter.Label(root, text="Velocity of rocket (percentage of light speed)")
lbl_position.pack(side='left')
scl_var = tkinter.StringVar(root)
scl_v = tkinter.Scale(root, variable=scl_var, orient='horizontal', length=200, from_=-100, to=100,
                      command=slider_changed)
scl_v.pack(side='left')
scl_var.set(v_percentage)

# main loop
set_axis()
root.mainloop()
