# Special relativity (Lorentz transformation and rotation)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.patches as patches
import tkinter as tk
from tkinter import ttk


def draw_light_rot(th):
    rot = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])  # Matrix of horizontal rotation
    light_r1 = np.array([x_max, y_max])
    light_l1 = np.array([x_min, y_max])
    light_r1_rot = np.dot(rot, light_r1)
    light_l1_rot = np.dot(rot, light_l1)
    ax1.plot([light_l1_rot[0], 0., light_r1_rot[0]], [light_l1_rot[1], 0., light_r1_rot[1]], linestyle=':', c='orange',
             linewidth=2, label='World line of light (observer A)')
    light_r2 = np.array([x_max, -y_max])
    light_l2 = np.array([x_min, -y_max])
    light_r2_rot = np.dot(rot, light_r2)
    light_l2_rot = np.dot(rot, light_l2)
    ax1.plot([light_l2_rot[0], 0., light_r2_rot[0]], [light_l2_rot[1], 0., light_r2_rot[1]],
             linestyle=':', c='orange', linewidth=1)


def draw_rocket_rot(th):
    length_body = 2.4
    width_body = 0.6
    rot = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])  # Matrix of horizontal rotation
    rocket_center = np.array([0., 3.])
    rocket_ru = np.array([0. + length_body / 2., 3. + width_body / 2.])
    rocket_rd = np.array([0. + length_body / 2., 3. - width_body / 2.])
    rocket_lu = np.array([0. - length_body / 2., 3. + width_body / 2.])
    rocket_ld = np.array([0. - length_body / 2., 3. - width_body / 2.])
    rocket_center_rot = np.dot(rot, rocket_center)
    rocket_ru_rot = np.dot(rot, rocket_ru)
    rocket_rd_rot = np.dot(rot, rocket_rd)
    rocket_lu_rot = np.dot(rot, rocket_lu)
    rocket_ld_rot = np.dot(rot, rocket_ld)
    body = plt.Polygon((rocket_ru_rot, rocket_lu_rot,
                        rocket_ld_rot, rocket_rd_rot), fill=False, ec='red')
    ax1.add_patch(body)

    if th <= 0.:
        rocket_nose = np.array([0. + length_body / 2. + 0.5, 3.])
        rocket_nose_rot = np.dot(rot, rocket_nose)
        nose = plt.Polygon((rocket_ru_rot, rocket_nose_rot,
                            rocket_rd_rot), fill=False, ec='red')
        ax1.add_patch(nose)
        fin1_top = np.array([0. - length_body / 2., 3. + width_body / 2. + 0.3])
        fin1_front = np.array([0. - length_body / 2. + 0.5, 3. + width_body / 2.])
        fin1_top_rot = np.dot(rot, fin1_top)
        fin1_front_rot = np.dot(rot, fin1_front)
        fin1 = plt.Polygon((rocket_lu_rot, fin1_top_rot,
                            fin1_front_rot), fill=False, ec='red')
        ax1.add_patch(fin1)
        fin2_top = np.array([0. - length_body / 2., 3. - width_body / 2. - 0.3])
        fin2_front = np.array([0. - length_body / 2. + 0.5, 3. - width_body / 2.])
        fin2_top_rot = np.dot(rot, fin2_top)
        fin2_front_rot = np.dot(rot, fin2_front)
        fin2 = plt.Polygon((rocket_ld_rot, fin2_top_rot,
                            fin2_front_rot), fill=False, ec='red')
        ax1.add_patch(fin2)
    else:
        rocket_nose = np.array([0. - length_body / 2. - 0.5, 3.])
        rocket_nose_rot = np.dot(rot, rocket_nose)
        nose = plt.Polygon((rocket_lu_rot, rocket_nose_rot,
                            rocket_ld_rot), fill=False, ec='red')
        ax1.add_patch(nose)
        fin1_top = np.array([0. + length_body / 2., 3. + width_body / 2. + 0.3])
        fin1_front = np.array([0. + length_body / 2. - 0.5, 3. + width_body / 2.])
        fin1_top_rot = np.dot(rot, fin1_top)
        fin1_front_rot = np.dot(rot, fin1_front)
        fin1 = plt.Polygon((rocket_ru_rot, fin1_top_rot,
                            fin1_front_rot), fill=False, ec='red')
        ax1.add_patch(fin1)
        fin2_top = np.array([0. + length_body / 2., 3. - width_body / 2. - 0.3])
        fin2_front = np.array([0. + length_body / 2. - 0.5, 3. - width_body / 2.])
        fin2_top_rot = np.dot(rot, fin2_top)
        fin2_front_rot = np.dot(rot, fin2_front)
        fin2 = plt.Polygon((rocket_rd_rot, fin2_top_rot,
                            fin2_front_rot), fill=False, ec='red')
        ax1.add_patch(fin2)
    lamp1 = patches.Circle(xy=(rocket_center_rot[0], rocket_center_rot[1]), radius=0.16, fc='orange')
    ax1.add_patch(lamp1)
    lamp2_center = np.array([0., 3. - 0.01])
    lamp2_center_rot = np.dot(rot, lamp2_center)
    lamp2 = patches.Circle(xy=(lamp2_center_rot[0], lamp2_center_rot[1]), radius=0.1, fc='yellow')
    ax1.add_patch(lamp2)
    lamp3_ru = np.array([0. + 0.08, 3. - 0.13])
    lamp3_rd = np.array([0. + 0.08, 3. - 0.25])
    lamp3_lu = np.array([0. - 0.08, 3. - 0.13])
    lamp3_ld = np.array([0. - 0.08, 3. - 0.25])
    lamp3_ru_rot = np.dot(rot, lamp3_ru)
    lamp3_rd_rot = np.dot(rot, lamp3_rd)
    lamp3_lu_rot = np.dot(rot, lamp3_lu)
    lamp3_ld_rot = np.dot(rot, lamp3_ld)
    lamp3 = plt.Polygon((lamp3_ru_rot, lamp3_lu_rot,
                         lamp3_ld_rot, lamp3_rd_rot), fc='gray', ec='gray')
    ax1.add_patch(lamp3)
    light_r0 = np.array([0. + 0.3, 3.])
    light_r1 = np.array([0. + distance_right_wall, 3.])
    light_r0_rot = np.dot(rot, light_r0)
    light_r1_rot = np.dot(rot, light_r1)
    ax1.annotate('', xy=light_r1_rot,
                 xytext=light_r0_rot,
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    light_l0 = np.array([0. - 0.3, 3.])
    light_l1 = np.array([0. + distance_left_wall, 3.])
    light_l0_rot = np.dot(rot, light_l0)
    light_l1_rot = np.dot(rot, light_l1)
    ax1.annotate('', xy=light_l1_rot,
                 xytext=light_l0_rot,
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    person = np.array([0. + 0.3, 3. - 0.06])
    person_rot = np.dot(rot, person)
    draw_person(person_rot[0], person_rot[1], 0.2, 'red')
    ax1.text(person_rot[0], person_rot[1] - 0.5, "Observer A", c='red')


def draw_light(th):
    rot = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])  # Matrix of horizontal rotation
    light_r1 = np.array([x_max, y_max])
    light_l1 = np.array([x_min, y_max])
    light_r1_rot = np.dot(rot, light_r1)
    light_l1_rot = np.dot(rot, light_l1)
    ax1.plot([light_l1_rot[0], 0., light_r1_rot[0]], [light_l1_rot[1], 0., light_r1_rot[1]], linestyle=':', c='orange',
             linewidth=2, label='World line of light (observer A)')
    light_r2 = np.array([x_max, -y_max])
    light_l2 = np.array([x_min, -y_max])
    light_r2_rot = np.dot(rot, light_r2)
    light_l2_rot = np.dot(rot, light_l2)
    ax1.plot([light_l2_rot[0], 0., light_r2_rot[0]], [light_l2_rot[1], 0., light_r2_rot[1]],
             linestyle=':', c='orange', linewidth=1)


def draw_person(x_p, y_p, scale_p, col):
    size_head = 0.15 * scale_p
    head = patches.Circle(xy=(x_p, y_p), radius=size_head, fc=col)
    ax1.add_patch(head)
    ax1.plot([x_p, x_p], [y_p, y_p - 0.5 * scale_p], linestyle='-', c=col, linewidth=1)
    ax1.plot([x_p - 0.2 * scale_p, x_p, x_p + 0.2 * scale_p], [y_p - 0.4 * scale_p, y_p - 0.2 * scale_p,
                                                               y_p - 0.4 * scale_p], linestyle='-', c=col, linewidth=1)
    ax1.plot([x_p - 0.1 * scale_p, x_p, x_p + 0.1 * scale_p],
             [y_p - 0.8 * scale_p, y_p - 0.5 * scale_p, y_p - 0.8 * scale_p], linestyle='-', c=col, linewidth=1)


def draw_rocket(bt):
    length_body = 2.4
    width_body = 0.6
    y_rocket = 3.
    x_rocket = bt * 3.
    x_body_right = x_rocket + length_body / 2.
    x_body_left = x_rocket - length_body / 2.
    y_body_top = y_rocket + width_body / 2.
    y_body_bottom = y_rocket - width_body / 2.
    # draw body
    bdy = patches.Rectangle(xy=[x_body_left, y_body_bottom], width=length_body,
                            height=width_body, fill=False, ec='red')
    ax1.add_patch(bdy)
    # draw nose corn and fins
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
    ax1.add_patch(nose)
    ax1.add_patch(fin1)
    ax1.add_patch(fin2)
    # draw walls
    ax1.plot([x_rocket + distance_right_wall, x_rocket + distance_right_wall],
             [y_rocket - width_body / 2., y_rocket + width_body / 2.], linestyle='-', c='green', linewidth=2)
    ax1.plot([x_rocket + distance_left_wall, x_rocket + distance_left_wall],
             [y_rocket - width_body / 2., y_rocket + width_body / 2.], linestyle='-', c='green', linewidth=2)
    # draw lights in rocket
    ax1.annotate('', xy=[x_rocket + distance_right_wall, y_rocket], xytext=[x_rocket + 0.2, y_rocket],
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    ax1.annotate('', xy=[x_rocket + distance_left_wall, y_rocket], xytext=[x_rocket - 0.2, y_rocket],
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    # draw lamp in rocket
    lamp1 = patches.Circle(xy=(x_rocket, y_rocket), radius=0.16, fc='orange')
    ax1.add_patch(lamp1)
    lamp2 = patches.Circle(xy=(x_rocket, y_rocket - 0.01), radius=0.1, fc='yellow')
    ax1.add_patch(lamp2)
    lamp3 = patches.Rectangle(xy=[x_rocket - 0.08, y_rocket - 0.25], width=0.16, height=0.12, fc='gray', ec='gray')
    ax1.add_patch(lamp3)
    # draw observer A
    draw_person(x_rocket + 0.3, y_rocket - 0.06, 0.2, 'red')
    ax1.text(x_rocket, y_rocket - 0.5, "Observer A", c='red')


def set_axis():
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_title('Special relativity (Lorentz transformation and rotation)')
    ax1.set_xlabel('Spatial axis of B')
    ax1.set_ylabel('World line of B')
    ax1.grid()
    ax1.set_aspect("equal")


def draw_hyperbolic():
    # Hyperbolic curve; ct**2 - x**2 = 1 (y**2 - x**2 = 1)
    y = np.sqrt(1. + x ** 2.)
    ax1.plot(x, y, linewidth=1, c='magenta', label='ct**2 - x**2 = 1')
    y = - np.sqrt(1. + x ** 2.)
    ax1.plot(x, y, linewidth=1, c='magenta')


def draw_rotation():
    # Additional circle
    additional_c = patches.Circle(xy=(0., 0.), radius=1., fill=False, ec='green', linestyle='-.', linewidth=1)
    ax1.add_patch(additional_c)
    # World line of of A (lamp)
    beta = v_percentage / 100. * c
    theta = np.arctan(beta)
    ax1.annotate('', xy=[y_max * np.tan(theta), y_max], xytext=[y_min * np.tan(theta), y_min],
                 arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax1.text(x_max * beta, y_max - 0.3, "World line of Lamp", c='red')
    # Spatial line of of A (lamp)
    ax1.annotate('', xy=[x_max, x_max * np.tan(- theta)], xytext=[x_min, x_min * np.tan(- theta)],
                 arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax1.text(x_max, x_max * np.tan(- theta), "Spatial axis of A", c='red')
    # World line of A (right wall)
    a = np.tan(theta)
    b = np.cos(- theta) - np.sin(- theta) * np.tan(theta)
    x_head_rw = y_max * a + b
    x_tail_rw = y_min * a + b
    y_head_rw = y_max
    y_tail_rw = y_min
    if x_head_rw > x_max:
        x_head_rw = x_max
        y_head_rw = (x_max - b) / a
    if x_tail_rw > x_max:
        x_tail_rw = x_max
        y_tail_rw = (x_max - b) / a
    ax1.annotate('', xy=[x_head_rw, y_head_rw], xytext=[x_tail_rw, y_tail_rw],
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    ax1.text(x_head_rw, y_max - 0.5, "World line of right wall", c='green')
    # World line of A (left wall)
    x_head_lw = y_max * a - b
    x_tail_lw = y_min * a - b
    y_head_lw = y_max
    y_tail_lw = y_min
    if x_head_lw < x_min:
        x_head_lw = x_min
        y_head_lw = (x_min + b) / a
    if x_tail_lw < x_min:
        x_tail_lw = x_min
        y_tail_lw = (x_min + b) / a
    ax1.annotate('', xy=[x_head_lw, y_head_lw], xytext=[x_tail_lw, y_tail_lw],
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    ax1.text(x_head_lw, y_max - 0.7, "World line of left wall", c='green')
    # Crossing points, simultaneous line and spatial axis
    if - 0.999 <= beta <= 0.999:
        # Crossing points
        y_cp1 = b / (1 - a)
        x_cp1 = y_cp1
        y_cp2 = b / (1 + a)
        x_cp2 = - y_cp2
        cl1 = patches.Circle(xy=(x_cp1, y_cp1), radius=0.1, fc='orange')
        ax1.add_patch(cl1)
        cl2 = patches.Circle(xy=(x_cp2, y_cp2), radius=0.1, fc='orange')
        ax1.add_patch(cl2)
        # Simultaneous line and spatial axis
        a = (y_cp2 - y_cp1) / (x_cp2 - x_cp1)
        b = y_cp1 - a * x_cp1
        ax1.plot([x_min, x_max], [a * x_min + b, a * x_max + b], linestyle='-.', c='grey')
        # ax1.annotate('', xy=[x_max, a * x_max], xytext=[x_min, a * x_min],
        #             arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
        # ax1.text(x_max, a * x_max, "Spatial axis of A", c='red')
        ax1.text(x_max, a * x_max + b, "Simultaneous line of A", c='gray')
    draw_rocket_rot(-theta)
    draw_light_rot(-theta)


def draw_lorentz():
    # World line of A (lamp)
    beta = v_percentage / 100. / c
    ax1.annotate('', xy=[x_max * beta, y_max], xytext=[x_min * beta, y_min],
                 arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax1.text(x_max * beta, y_max - 0.3, "World line of Lamp", c='red')
    # World line of A (right wall)
    x_head_rw = beta * y_max + distance_right_wall
    x_tail_rw = beta * y_min + distance_right_wall
    y_head_rw = y_max
    y_tail_rw = y_min
    if x_head_rw > x_max:
        x_head_rw = x_max
        y_head_rw = (x_max - distance_right_wall) / beta
    if x_tail_rw > x_max:
        x_tail_rw = x_max
        y_tail_rw = (x_max - distance_right_wall) / beta
    ax1.annotate('', xy=[x_head_rw, y_head_rw], xytext=[x_tail_rw, y_tail_rw],
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    ax1.text(x_head_rw, y_max - 0.5, "World line of right wall", c='green')
    # World line of A (left wall)
    x_head_lw = beta * y_max + distance_left_wall
    x_tail_lw = beta * y_min + distance_left_wall
    y_head_lw = y_max
    y_tail_lw = y_min
    if x_head_lw < x_min:
        x_head_lw = x_min
        y_head_lw = (x_min - distance_left_wall) / beta
    if x_tail_lw < x_min:
        x_tail_lw = x_min
        y_tail_lw = (x_min - distance_left_wall) / beta
    ax1.annotate('', xy=[x_head_lw, y_head_lw], xytext=[x_tail_lw, y_tail_lw],
                 arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    ax1.text(x_head_lw, y_max - 0.7, "World line of left wall", c='green')
    # Crossing points, simultaneous line and spatial axis
    if - 0.999 <= beta <= 0.999:
        # Crossing points
        y_cp1 = distance_right_wall / (1 - beta)
        x_cp1 = y_cp1
        y_cp2 = - distance_left_wall / (1 + beta)
        x_cp2 = - y_cp2
        cl1 = patches.Circle(xy=(x_cp1, y_cp1), radius=0.1, fc='orange')
        ax1.add_patch(cl1)
        cl2 = patches.Circle(xy=(x_cp2, y_cp2), radius=0.1, fc='orange')
        ax1.add_patch(cl2)
        # Simultaneous line and spatial axis
        a = (y_cp2 - y_cp1) / (x_cp2 - x_cp1)
        b = y_cp1 - a * x_cp1
        ax1.plot([x_min, x_max], [a * x_min + b, a * x_max + b], linestyle='-.', c='grey')
        ax1.annotate('', xy=[x_max, a * x_max], xytext=[x_min, a * x_min],
                     arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
        ax1.text(x_max, a * x_max, "Spatial axis of A", c='red')
        ax1.text(x_max, a * x_max + b, "Simultaneous line of A", c='gray')
        draw_rocket(beta)


def draw_common():
    # World line of Photon B
    ax1.plot([x_min, 0., x_max], [y_max, 0., y_max], linestyle='--', c='orange',
             label='World line of light (observer B)')
    ax1.plot([x_min, 0., x_max], [y_min, 0., y_min], linestyle='--', c='orange', linewidth=1)
    # World line of B
    ax1.annotate('', xy=[0., y_max], xytext=[0., y_min], arrowprops=dict(width=1, headwidth=4, headlength=4,
                                                                         facecolor='blue', edgecolor='blue'))
    # Spatial axis of B
    ax1.annotate('', xy=[x_max, 0.], xytext=[x_min, 0.], arrowprops=dict(width=1, headwidth=4, headlength=4,
                                                                         facecolor='blue', edgecolor='blue'))
    # Observer B
    draw_person(0.2, y_min + 2.0, 1.0, 'blue')
    ax1.text(0.4, -2.4, "Observer B", c='blue')


def draw_graph():
    ax1.cla()
    set_axis()
    draw_common()
    if transformation_number == 0:
        draw_lorentz()
    elif transformation_number == 1:
        draw_rotation()
    draw_hyperbolic()
    ax1.legend(loc='lower right', fontsize=8)
    canvas.draw()
    ax1.grid()


def change_transformation():
    global transformation_number
    transformation_number = var_transformation.get()
    draw_graph()


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

transformation_number = 0

# Generate tkinter
root = tk.Tk()
root.title("Special relativity (Lorentz transformation and rotation)")

# Generate figure and axes
fig = Figure()
ax1 = fig.add_subplot(1, 1, 1)

# Embed Figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

# Draw circles as initial
draw_graph()

# Add toolbar
toolbar = NavigationToolbar2Tk(canvas, root)

# Widgets
frm_transformation = ttk.Labelframe(root, relief="ridge", text="Transformation", labelanchor="n", width=100)
frm_transformation.pack(side='left')
var_transformation = tk.IntVar(value=transformation_number)
rdb0_transformation = tk.Radiobutton(frm_transformation, text="Lorentz", command=change_transformation,
                                     variable=var_transformation, value=0)
rdb1_transformation = tk.Radiobutton(frm_transformation, text="Rotation", command=change_transformation,
                                     variable=var_transformation, value=1)
rdb0_transformation.pack(anchor=tk.W)
rdb1_transformation.pack(anchor=tk.W)

lbl_position = tk.Label(root, text="Velocity of rocket (percentage of light speed)")
lbl_position.pack(side='left')
scl_var = tk.StringVar(root)
scl_v = tk.Scale(root, variable=scl_var, orient='horizontal', length=200, from_=-100, to=100, command=slider_changed)
scl_v.pack(side='left')
scl_var.set(v_percentage)

# main loop
set_axis()
root.mainloop()
