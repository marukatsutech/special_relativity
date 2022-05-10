# Special relativity 2
import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.patches as patches


def draw_rocket_a(th):
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
    ax.add_patch(body)

    if th <= 0.:
        rocket_nose = np.array([0. + length_body / 2. + 0.5, 3.])
        rocket_nose_rot = np.dot(rot, rocket_nose)
        nose = plt.Polygon((rocket_ru_rot, rocket_nose_rot,
                            rocket_rd_rot), fill=False, ec='red')
        ax.add_patch(nose)
        fin1_top = np.array([0. - length_body / 2., 3. + width_body / 2. + 0.3])
        fin1_front = np.array([0. - length_body / 2. + 0.5, 3. + width_body / 2.])
        fin1_top_rot = np.dot(rot, fin1_top)
        fin1_front_rot = np.dot(rot, fin1_front)
        fin1 = plt.Polygon((rocket_lu_rot, fin1_top_rot,
                            fin1_front_rot), fill=False, ec='red')
        ax.add_patch(fin1)
        fin2_top = np.array([0. - length_body / 2., 3. - width_body / 2. - 0.3])
        fin2_front = np.array([0. - length_body / 2. + 0.5, 3. - width_body / 2.])
        fin2_top_rot = np.dot(rot, fin2_top)
        fin2_front_rot = np.dot(rot, fin2_front)
        fin2 = plt.Polygon((rocket_ld_rot, fin2_top_rot,
                            fin2_front_rot), fill=False, ec='red')
        ax.add_patch(fin2)
    else:
        rocket_nose = np.array([0. - length_body / 2. - 0.5, 3.])
        rocket_nose_rot = np.dot(rot, rocket_nose)
        nose = plt.Polygon((rocket_lu_rot, rocket_nose_rot,
                            rocket_ld_rot), fill=False, ec='red')
        ax.add_patch(nose)
        fin1_top = np.array([0. + length_body / 2., 3. + width_body / 2. + 0.3])
        fin1_front = np.array([0. + length_body / 2. - 0.5, 3. + width_body / 2.])
        fin1_top_rot = np.dot(rot, fin1_top)
        fin1_front_rot = np.dot(rot, fin1_front)
        fin1 = plt.Polygon((rocket_ru_rot, fin1_top_rot,
                            fin1_front_rot), fill=False, ec='red')
        ax.add_patch(fin1)
        fin2_top = np.array([0. + length_body / 2., 3. - width_body / 2. - 0.3])
        fin2_front = np.array([0. + length_body / 2. - 0.5, 3. - width_body / 2.])
        fin2_top_rot = np.dot(rot, fin2_top)
        fin2_front_rot = np.dot(rot, fin2_front)
        fin2 = plt.Polygon((rocket_rd_rot, fin2_top_rot,
                            fin2_front_rot), fill=False, ec='red')
        ax.add_patch(fin2)
    lamp1 = patches.Circle(xy=(rocket_center_rot[0], rocket_center_rot[1]), radius=0.16, fc='orange')
    ax.add_patch(lamp1)
    lamp2_center = np.array([0., 3. - 0.01])
    lamp2_center_rot = np.dot(rot, lamp2_center)
    lamp2 = patches.Circle(xy=(lamp2_center_rot[0], lamp2_center_rot[1]), radius=0.1, fc='yellow')
    ax.add_patch(lamp2)
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
    ax.add_patch(lamp3)
    light_r0 = np.array([0. + 0.3, 3.])
    light_r1 = np.array([0. + distance_right_wall, 3.])
    light_r0_rot = np.dot(rot, light_r0)
    light_r1_rot = np.dot(rot, light_r1)
    ax.annotate('', xy=light_r1_rot,
                xytext=light_r0_rot,
                arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    light_l0 = np.array([0. - 0.3, 3.])
    light_l1 = np.array([0. + distance_left_wall, 3.])
    light_l0_rot = np.dot(rot, light_l0)
    light_l1_rot = np.dot(rot, light_l1)
    ax.annotate('', xy=light_l1_rot,
                xytext=light_l0_rot,
                arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    person = np.array([0. + 0.3, 3. - 0.06])
    person_rot = np.dot(rot, person)
    draw_person(person_rot[0], person_rot[1], 0.2, 'red')
    ax.text(person_rot[0], person_rot[1] - 0.5, "Observer A", c='red')


def draw_light(th):
    rot = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])  # Matrix of horizontal rotation
    light_r1 = np.array([x_max, y_max])
    light_l1 = np.array([x_min, y_max])
    light_r1_rot = np.dot(rot, light_r1)
    light_l1_rot = np.dot(rot, light_l1)
    ax.plot([light_l1_rot[0], 0., light_r1_rot[0]], [light_l1_rot[1], 0., light_r1_rot[1]], linestyle=':', c='orange',
            linewidth=2, label='World line of light (observer A)')
    light_r2 = np.array([x_max, -y_max])
    light_l2 = np.array([x_min, -y_max])
    light_r2_rot = np.dot(rot, light_r2)
    light_l2_rot = np.dot(rot, light_l2)
    ax.plot([light_l2_rot[0], 0., light_r2_rot[0]], [light_l2_rot[1], 0., light_r2_rot[1]],
            linestyle=':', c='orange', linewidth=1)


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
                            height=width_body, fill=False, ec='red', linestyle='--')
    ax.add_patch(bdy)
    x_body_right = x_rocket + length_body / 2.
    x_body_left = x_rocket - length_body / 2.
    y_body_top = y_rocket + width_body / 2.
    y_body_bottom = y_rocket - width_body / 2.
    if bt >= 0.:
        nose = plt.Polygon(((x_body_right, y_body_top), (x_body_right + 0.5, y_rocket),
                           (x_body_right, y_body_bottom)), fill=False, ec='red', linestyle='--')

        fin1 = plt.Polygon(((x_body_left, y_body_top), (x_body_left, y_body_top + 0.3),
                           (x_body_left + 0.5, y_body_top)), fill=False, ec='red', linestyle='--')

        fin2 = plt.Polygon(((x_body_left, y_body_bottom), (x_body_left, y_body_bottom - 0.3),
                            (x_body_left + 0.5, y_body_bottom)), fill=False, ec='red', linestyle='--')

    else:
        nose = plt.Polygon(((x_body_left, y_body_top), (x_body_left - 0.5, y_rocket),
                            (x_body_left, y_body_bottom)), fill=False, ec='red', linestyle='--')

        fin1 = plt.Polygon(((x_body_right, y_body_top), (x_body_right, y_body_top + 0.3),
                            (x_body_right - 0.5, y_body_top)), fill=False, ec='red', linestyle='--')

        fin2 = plt.Polygon(((x_body_right, y_body_bottom), (x_body_right, y_body_bottom - 0.3),
                            (x_body_right - 0.5, y_body_bottom)), fill=False, ec='red', linestyle='--')
    ax.add_patch(nose)
    ax.add_patch(fin1)
    ax.add_patch(fin2)
    ax.plot([x_rocket + distance_right_wall, x_rocket + distance_right_wall],
            [y_rocket - width_body / 2., y_rocket + width_body / 2.], linestyle='--', c='green', linewidth=2)
    ax.plot([x_rocket + distance_left_wall, x_rocket + distance_left_wall],
            [y_rocket - width_body / 2., y_rocket + width_body / 2.], linestyle='--', c='green', linewidth=2)
    ax.annotate('', xy=[x_rocket + distance_right_wall, y_rocket],
                xytext=[x_rocket + 0.2, y_rocket],
                arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    ax.annotate('', xy=[x_rocket + distance_left_wall, y_rocket],
                xytext=[x_rocket - 0.2, y_rocket],
                arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='orange', edgecolor='orange'))
    lamp1 = patches.Circle(xy=(x_rocket, y_rocket), radius=0.16, fill=False, ec='orange', linestyle='--')
    ax.add_patch(lamp1)
    # lamp2 = patches.Circle(xy=(x_rocket, y_rocket - 0.01), radius=0.1, fc='yellow')
    # ax.add_patch(lamp2)
    lamp3 = patches.Rectangle(xy=[x_rocket - 0.08, y_rocket - 0.25], width=0.16,
                              height=0.12, fill=False, ec='gray', linestyle='--')
    ax.add_patch(lamp3)
    # draw_person(x_rocket + 0.3, y_rocket - 0.06, 0.2, 'red')
    # ax.text(x_rocket, y_rocket - 0.5, "Observer A", c='red')


def set_axis():
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title('Special relativity 2')
    ax.set_xlabel('Spatial axis of B')
    ax.set_ylabel('World line of B')
    ax.grid()
    ax.set_aspect("equal")


def draw_graph():
    ax.cla()
    set_axis()
    # World line of Photon B
    ax.plot([x_min, 0., x_max], [y_max, 0., y_max], linestyle='--', c='orange',
            label='World line of light (observer B)')
    ax.plot([x_min, 0., x_max], [y_min, 0., y_min], linestyle='--', c='orange', linewidth=1)
    # World line of B
    ax.annotate('', xy=[0., y_max], xytext=[0., y_min], arrowprops=dict(width=1, headwidth=4, headlength=4,
                                                                        facecolor='blue', edgecolor='blue'))
    # Spatial axis of B
    ax.annotate('', xy=[x_max, 0.], xytext=[x_min, 0.], arrowprops=dict(width=1, headwidth=4, headlength=4,
                                                                        facecolor='blue', edgecolor='blue'))
    # Additional circle
    additional_c = patches.Circle(xy=(0., 0.), radius=1., fill=False, ec='green', linestyle='-.', linewidth=1)
    ax.add_patch(additional_c)
    # World line of of A (lamp)
    beta = v_percentage / 100. * c
    theta = np.arctan(beta)
    ax.annotate('', xy=[y_max * np.tan(theta), y_max], xytext=[y_min * np.tan(theta), y_min],
                arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax.text(x_max * beta, y_max - 0.3, "World line of Lamp", c='red')
    # Spatial line of of A (lamp)
    ax.annotate('', xy=[x_max, x_max * np.tan(- theta)],
                xytext=[x_min, x_min * np.tan(- theta)],
                arrowprops=dict(width=1, headwidth=4, headlength=4, facecolor='red', edgecolor='red'))
    ax.text(x_max, x_max * np.tan(- theta), "Spatial axis of A", c='red')
    # World line of A (right wall)
    ax.plot([x_max * beta + distance_right_wall, x_min * beta + distance_right_wall], [y_max, y_min],
            c='green', linestyle='--', linewidth=1)
    a = np.tan(theta)
    b = np.cos(- theta) - np.sin(- theta) * np.tan(theta)
    xu_wl_rw = y_max * a + b
    xd_wl_rw = y_min * a + b
    if xu_wl_rw <= x_max and xd_wl_rw <= x_max:
        ax.annotate('', xy=[xu_wl_rw, y_max], xytext=[xd_wl_rw, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    elif xu_wl_rw > x_max and not xd_wl_rw > x_max:
        yu_wl_rw = (x_max - b) / a
        ax.annotate('', xy=[x_max, yu_wl_rw], xytext=[xd_wl_rw, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    else:
        yd_wl_rw = (x_max - b) / a
        ax.annotate('', xy=[xu_wl_rw, y_max], xytext=[x_max, yd_wl_rw],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    # World line of A (left wall)
    ax.plot([x_max * beta + distance_left_wall, x_min * beta + distance_left_wall], [y_max, y_min],
            c='green', linestyle='--', linewidth=1)
    xu_wl_lw = y_max * a - b
    xd_wl_lw = y_min * a - b
    if xu_wl_lw >= x_min and xd_wl_lw >= x_min:
        ax.annotate('', xy=[xu_wl_lw, y_max], xytext=[xd_wl_lw, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    elif xu_wl_lw < x_min:
        yu_wl_lw = (x_min + b) / a
        ax.annotate('', xy=[x_min, yu_wl_lw], xytext=[xd_wl_lw, y_min],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    else:
        yd_wl_lw = (x_min + b) / a
        ax.annotate('', xy=[xu_wl_lw, y_max], xytext=[x_min, yd_wl_lw],
                    arrowprops=dict(width=0.5, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
    # Crossing points
    if beta != 0.:
        if beta != 1. and beta != -1.:
            x_cp1 = - distance_right_wall * (1. / beta) / (1 - (1. / beta))
            y_cp1 = x_cp1
            cl1 = patches.Circle(xy=(x_cp1, y_cp1), radius=0.1, fc='orange', ec='brown')
            ax.add_patch(cl1)
            x_cp2 = distance_left_wall * (1. / beta) / (1 + (1. / beta))
            y_cp2 = - x_cp2
            cl2 = patches.Circle(xy=(x_cp2, y_cp2), radius=0.1, fc='orange', ec='brown')
            ax.add_patch(cl2)

            x_cp1a = b / (1 - a)
            y_cp1a = x_cp1a
            cl1a = patches.Circle(xy=(x_cp1a, y_cp1a), radius=0.1, fc='orange', ec='brown')
            ax.add_patch(cl1a)
            x_cp2a = - b / (1 + a)
            y_cp2a = - x_cp2a
            cl2a = patches.Circle(xy=(x_cp2a, y_cp2a), radius=0.1, fc='orange', ec='brown')
            ax.add_patch(cl2a)
    else:
        x_cp1 = distance_right_wall
        y_cp1 = x_cp1
        cl1 = patches.Circle(xy=(x_cp1, y_cp1), radius=0.1, fc='orange', ec='brown')
        ax.add_patch(cl1)
        x_cp2 = distance_left_wall
        y_cp2 = - x_cp2
        cl2 = patches.Circle(xy=(x_cp2, y_cp2), radius=0.1, fc='orange', ec='brown')
        ax.add_patch(cl2)
    # Simultaneous line and spatial axis
    try:
        if (x_cp2 - x_cp1) != 0.:
            a = (y_cp2 - y_cp1) / (x_cp2 - x_cp1)
            b = y_cp1 - a * x_cp1
            ax.plot([x_min, x_max], [a * x_min + b, a * x_max + b], linestyle='-.', c='grey')
            ax.text(x_max, a * x_max + b, "Simultaneous line of A", c='gray')
            ya_max = a * x_max
            ya_min = a * x_min
            ax.plot([x_min, x_max], [ya_min, ya_max], linestyle='-', c='red', linewidth=1)
            ax.text(x_max, ya_max, "Spatial axis of A for B", c='red')
        if (x_cp2a - x_cp1a) != 0.:
            aa = (y_cp2a - y_cp1a) / (x_cp2a - x_cp1a)
            ba = y_cp1a - aa * x_cp1a
            ax.plot([x_min, x_max], [aa * x_min + ba, aa * x_max + ba], linestyle='-.', c='grey', linewidth=2)
            # ax.text(x_max, aa * x_max + ba, "Simultaneous line of A", c='gray')
    except:
        pass
    draw_light(-theta)
    # Hyperbolic curve; ct**2 - x**2 = 1 (y**2 - x**2 = 1)
    y = np.sqrt(1. + x ** 2.)
    ax.plot(x, y, linewidth=1, c='magenta', label='ct**2 - x**2 = 1')
    y = - np.sqrt(1. + x ** 2.)
    ax.plot(x, y, linewidth=1, c='magenta')
    ax.legend(loc='lower right')
    draw_rocket_a(-theta)
    draw_rocket(beta)
    draw_person(0.2, y_min + 2.0, 1.0, 'blue')
    ax.text(0.4, -2.4, "Observer B", c='blue')
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
root.title("Special relativity 2")

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
