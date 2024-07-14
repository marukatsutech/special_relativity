# Composition of spins

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


def set_phase_a(value):
    global phase_a, vector_light_arrow_a_initial
    phase_a = np.deg2rad(float(value))
    vector_light_arrow_a_initial = np.array([np.sin(phase_a), 0., np.cos(phase_a)])
    update_diagram()
    update_light_arrow_path()


def set_phase_b(value):
    global phase_b, vector_light_arrow_b_initial
    phase_b = np.deg2rad(float(value))
    vector_light_arrow_b_initial = np.array([np.sin(phase_b), 0., np.cos(phase_b)])
    update_diagram()
    update_light_arrow_path()


def set_rot_light_arrow_a(value):
    global rot_light_arrow_a
    rot_light_arrow_a = float(value)
    update_diagram()
    update_light_arrow_path()


def set_rot_light_arrow_b(value):
    global rot_light_arrow_b
    rot_light_arrow_b = float(value)
    update_diagram()
    update_light_arrow_path()


def set_rot_light_circle_axis_a(value):
    global rot_light_circle_axis_arrow_a
    rot_light_circle_axis_arrow_a = float(value)
    update_diagram()
    update_light_arrow_path()


def set_rot_light_circle_axis_b(value):
    global rot_light_circle_axis_arrow_b
    rot_light_circle_axis_arrow_b = float(value)
    update_diagram()
    update_light_arrow_path()


def set_scale_a(value):
    global scale_a
    scale_a = float(value)
    update_diagram()
    update_light_arrow_path()


def set_scale_b(value):
    global scale_b
    scale_b = float(value)
    update_diagram()
    update_light_arrow_path()


def update_light_arrow_path():
    global x_light_arrow_a_pass, y_light_arrow_a_pass, z_light_arrow_a_pass
    global x_light_arrow_b_pass, y_light_arrow_b_pass, z_light_arrow_b_pass
    # Spin A
    x_light_arrow_a_pass = []
    y_light_arrow_a_pass = []
    z_light_arrow_a_pass = []
    theta_light_circle_axis_a_path = 0.
    theta_light_arrow_a_path = 0.
    for i in range(360):
        rot_matrix_z = Rotation.from_rotvec(theta_light_circle_axis_a_path * vector_z_axis)
        vector_rotated_light_circle_axis_arrow_z = rot_matrix_z.apply(vector_light_circle_axis_arrow_a_initial)
        vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_a_initial)
        rot_matrix_light_circle_axis_arrow_rotated = Rotation.from_rotvec(theta_light_arrow_a_path *
                                                                          vector_rotated_light_circle_axis_arrow_z)
        vector_rotated_light_arrow = rot_matrix_light_circle_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
        u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
        x_light_arrow_a_pass.append(u1)
        y_light_arrow_a_pass.append(v1)
        z_light_arrow_a_pass.append(w1)
        theta_light_circle_axis_a_path = theta_light_circle_axis_a_path + rot_light_circle_axis_arrow_a * delta_theta
        theta_light_arrow_a_path = theta_light_arrow_a_path + rot_light_arrow_a * delta_theta
    plt_light_arrow_a_pass.set_xdata(np.array(x_light_arrow_a_pass) * scale_a)
    plt_light_arrow_a_pass.set_ydata(np.array(y_light_arrow_a_pass) * scale_a)
    plt_light_arrow_a_pass.set_3d_properties(np.array(z_light_arrow_a_pass) * scale_a)
    # Spin B
    x_light_arrow_b_pass = []
    y_light_arrow_b_pass = []
    z_light_arrow_b_pass = []
    theta_light_circle_axis_b_path = 0.
    theta_light_arrow_b_path = 0.
    for j in range(360):
        rot_matrix_z = Rotation.from_rotvec(theta_light_circle_axis_b_path * vector_z_axis)
        vector_rotated_light_circle_axis_arrow_z = rot_matrix_z.apply(vector_light_circle_axis_arrow_b_initial)
        vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_b_initial)
        rot_matrix_light_circle_axis_arrow_rotated = Rotation.from_rotvec(theta_light_arrow_b_path *
                                                                          vector_rotated_light_circle_axis_arrow_z)
        vector_rotated_light_arrow = rot_matrix_light_circle_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
        u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
        x_light_arrow_b_pass.append(u1)
        y_light_arrow_b_pass.append(v1)
        z_light_arrow_b_pass.append(w1)
        theta_light_circle_axis_b_path = theta_light_circle_axis_b_path + rot_light_circle_axis_arrow_b * delta_theta
        theta_light_arrow_b_path = theta_light_arrow_b_path + rot_light_arrow_b * delta_theta
    plt_light_arrow_b_pass.set_xdata(np.array(x_light_arrow_b_pass) * scale_b)
    plt_light_arrow_b_pass.set_ydata(np.array(y_light_arrow_b_pass) * scale_b)
    plt_light_arrow_b_pass.set_3d_properties(np.array(z_light_arrow_b_pass) * scale_b)
    # Spin Composed
    plt_light_arrow_c_pass.set_xdata(np.array(x_light_arrow_a_pass) * scale_a + np.array(x_light_arrow_b_pass) * scale_b)
    plt_light_arrow_c_pass.set_ydata(np.array(y_light_arrow_a_pass) * scale_a + np.array(y_light_arrow_b_pass) * scale_b)
    plt_light_arrow_c_pass.set_3d_properties(np.array(z_light_arrow_a_pass) * scale_a + np.array(z_light_arrow_b_pass) * scale_b)


def update_diagram():
    global qvr_light_circle_axis_arrow_a, plt_light_circle_a, qvr_light_arrow_a
    global qvr_light_circle_axis_arrow_b, plt_light_circle_b, qvr_light_arrow_b
    global qvr_light_arrow_c
    global x1c, y1c, z1c
    global u1c, v1c, w1c
    rot_matrix_z_a = Rotation.from_rotvec(theta_light_circle_axis_arrow_a * vector_z_axis)
    rot_matrix_z_b = Rotation.from_rotvec(theta_light_circle_axis_arrow_b * vector_z_axis)
    # Rotate light circle axis arrow
    vector_lca_a_rotated_z = rot_matrix_z_a.apply(vector_light_circle_axis_arrow_a_initial)
    x0, y0, z0 = 0., 0., 0.
    u0, v0, w0 = vector_lca_a_rotated_z[0], vector_lca_a_rotated_z[1], vector_lca_a_rotated_z[2]
    qvr_light_circle_axis_arrow_a.remove()
    qvr_light_circle_axis_arrow_a = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='cyan', normalize=False,
                                               label='Light circle axis arrow A', linewidth=1, linestyle='--')

    vector_lca_b_rotated_z = rot_matrix_z_b.apply(vector_light_circle_axis_arrow_b_initial)
    x0, y0, z0 = 0., 0., 0.
    u0, v0, w0 = vector_lca_b_rotated_z[0], vector_lca_b_rotated_z[1], vector_lca_b_rotated_z[2]
    qvr_light_circle_axis_arrow_b.remove()
    qvr_light_circle_axis_arrow_b = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='pink', normalize=False,
                                               label='Light circle axis arrow B', linewidth=1, linestyle='--')
    # Rotate light circle
    x_light_circle_rotated_z = []
    y_light_circle_rotated_z = []
    z_light_circle_rotated_z = []
    for i in range(len(x_light_circle)):
        vector_point = np.array([x_light_circle[i], y_light_circle[i], z_light_circle[i]])
        point_rotated_z = rot_matrix_z_a.apply(vector_point)
        x_light_circle_rotated_z.append(point_rotated_z[0])
        y_light_circle_rotated_z.append(point_rotated_z[1])
        z_light_circle_rotated_z.append(point_rotated_z[2])
    plt_light_circle_a.set_xdata(np.array(x_light_circle_rotated_z) * scale_a)
    plt_light_circle_a.set_ydata(np.array(y_light_circle_rotated_z) * scale_a)
    plt_light_circle_a.set_3d_properties(np.array(z_light_circle_rotated_z) * scale_a)

    x_light_circle_rotated_z = []
    y_light_circle_rotated_z = []
    z_light_circle_rotated_z = []
    for j in range(len(x_light_circle)):
        vector_point = np.array([x_light_circle[j], y_light_circle[j], z_light_circle[j]])
        point_rotated_z = rot_matrix_z_b.apply(vector_point)
        x_light_circle_rotated_z.append(point_rotated_z[0])
        y_light_circle_rotated_z.append(point_rotated_z[1])
        z_light_circle_rotated_z.append(point_rotated_z[2])
    plt_light_circle_b.set_xdata(np.array(x_light_circle_rotated_z) * scale_b)
    plt_light_circle_b.set_ydata(np.array(y_light_circle_rotated_z) * scale_b)
    plt_light_circle_b.set_3d_properties(np.array(z_light_circle_rotated_z) * scale_b)
    # Rotate light arrow A
    vector_rotated_light_arrow_z = rot_matrix_z_a.apply(vector_light_arrow_a_initial)
    rot_matrix_light_circle_axis_arrow_rotated = Rotation.from_rotvec(theta_light_arrow_a * vector_lca_a_rotated_z)
    vector_la_rotated = rot_matrix_light_circle_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
    qvr_light_arrow_a.remove()
    x1a, y1a, z1a = 0., 0., 0.
    u1a = scale_a * vector_la_rotated[0]
    v1a = scale_a * vector_la_rotated[1]
    w1a = scale_a * vector_la_rotated[2]
    qvr_light_arrow_a = ax0.quiver(x1a, y1a, z1a, u1a, v1a, w1a, length=1, color='blue', normalize=False,
                                   label='Light arrow A')

    vector_rotated_light_arrow_z = rot_matrix_z_b.apply(vector_light_arrow_b_initial)
    rot_matrix_light_circle_axis_arrow_rotated = Rotation.from_rotvec(theta_light_arrow_b * vector_lca_b_rotated_z)
    vector_la_rotated = rot_matrix_light_circle_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
    qvr_light_arrow_b.remove()
    x1b, y1b, z1b = 0., 0., 0.
    u1b = scale_b * vector_la_rotated[0]
    v1b = scale_b * vector_la_rotated[1]
    w1b = scale_b * vector_la_rotated[2]
    qvr_light_arrow_b = ax0.quiver(x1b, y1b, z1b, u1b, v1b, w1b, length=1, color='red', normalize=False,
                                   label='Light arrow B')
    qvr_light_arrow_c.remove()
    x1c, y1c, z1c = 0., 0., 0.
    u1c = u1a + u1b
    v1c = v1a + v1b
    w1c = w1a + w1b
    qvr_light_arrow_c = ax0.quiver(x1c, y1c, z1c, u1c, v1c, w1c, length=1, color='green', normalize=False,
                                   label='Light arrow Composed')


def reset():
    global is_play, cnt
    global theta_light_circle_axis_arrow_a, theta_light_arrow_a
    global theta_light_circle_axis_arrow_b, theta_light_arrow_b
    is_play = False
    cnt = 0
    theta_light_circle_axis_arrow_a = 0.
    theta_light_arrow_a = 0.
    theta_light_circle_axis_arrow_b = 0.
    theta_light_arrow_b = 0.
    update_diagram()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt
    global theta_light_circle_axis_arrow_a, theta_light_arrow_a
    global theta_light_circle_axis_arrow_b, theta_light_arrow_b
    txt_step.set_text("Step=" + str(cnt))
    if is_play:
        update_diagram()
        # Change theta
        theta_light_circle_axis_arrow_a = theta_light_circle_axis_arrow_a + rot_light_circle_axis_arrow_a * delta_theta
        theta_light_arrow_a = theta_light_arrow_a + rot_light_arrow_a * delta_theta
        theta_light_circle_axis_arrow_b = theta_light_circle_axis_arrow_b + rot_light_circle_axis_arrow_b * delta_theta
        theta_light_arrow_b = theta_light_arrow_b + rot_light_arrow_b * delta_theta
        cnt += 1


# Global variables

# Animation control
cnt = 0
is_play = False

# Parameters
range_x_min = -2.
range_x_max = 2.
range_y_min = -2.
range_y_max = 2.
range_z_min = -2.
range_z_max = 2.

vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

phase_a = np.deg2rad(0.)
phase_b = np.deg2rad(0.)

vector_light_circle_axis_arrow_a_initial = np.array([0., 1., 0.])
vector_light_circle_axis_arrow_b_initial = np.array([0., 1., 0.])
vector_light_arrow_a_initial = np.array([np.sin(phase_a), 0., np.cos(phase_a)])
vector_light_arrow_b_initial = np.array([np.sin(phase_b), 0., np.cos(phase_b)])
vector_light_arrow_c_initial = np.array([0., 0., 2.])

theta_light_circle_axis_arrow_a = 0.
theta_light_arrow_a = 0.
theta_light_circle_axis_arrow_b = 0.
theta_light_arrow_b = 0.

delta_theta = np.deg2rad(1.)
rot_light_circle_axis_arrow_a = 1
rot_light_arrow_a = 1
rot_light_circle_axis_arrow_b = - 1
rot_light_arrow_b = 1

scale_a = 1.
scale_b = 1.

x1c, y1c, z1c = 0., 0., 0.
u1c, v1c, w1c = 0., 0., 0.

# Generate figure and axes
title_ax0 = "Composition of spins"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max
z_min = range_z_min
z_max = range_z_max

fig = Figure()
# ax0 = fig.add_subplot(121, projection='3d')
ax0 = fig.add_subplot(111, projection='3d')

ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_zlabel('z')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

'''
ax1 = fig.add_subplot(122)
ax1.set_title("Parabola and projection")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_xlim(x_min, 16.)
ax1.set_ylim(y_min, 8.)
ax1.set_aspect("equal")
ax1.grid()
'''

# Generate items
# Text
txt_step = ax0.text2D(x_min, y_max, "Step=" + str(0))
xz, yz, _ = proj3d.proj_transform(x_min, y_max, z_max, ax0.get_proj())
txt_step.set_position((xz, yz))

# axis line
ln_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_x)
ln_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_y)
ln_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_z)

# Light circle
angle_light_circle = np.arange(0., 360., 6.)

x_light_circle = np.cos(angle_light_circle * np.pi / 180.)
z_light_circle = np.sin(angle_light_circle * np.pi / 180.)
y_light_circle = angle_light_circle * 0.
plt_light_circle_a, = ax0.plot(x_light_circle, y_light_circle, z_light_circle, linewidth=2, linestyle=':',
                               c='blue')

plt_light_circle_b, = ax0.plot(x_light_circle, y_light_circle, z_light_circle, linewidth=2, linestyle=':',
                               c='red')

# Guide circle of light circle axis arrow
c_spin_axis_guide = Circle((0., 0.), 1., ec='gray', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(c_spin_axis_guide)
art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=0., zdir='z')

# Light circle axis arrow
x0a_, y0a_, z0a_ = 0., 0., 0.
u0a_, v0a_, w0a_ = (vector_light_circle_axis_arrow_a_initial[0], vector_light_circle_axis_arrow_a_initial[1],
                    vector_light_circle_axis_arrow_a_initial[2])
qvr_light_circle_axis_arrow_a = ax0.quiver(x0a_, y0a_, z0a_, u0a_, v0a_, w0a_, length=1, color='cyan', normalize=False,
                                           label='Light circle axis arrow A', linewidth=1, linestyle='--')

x0a_, y0a_, z0a_ = 0., 0., 0.
u0a_, v0a_, w0a_ = (vector_light_circle_axis_arrow_a_initial[0], vector_light_circle_axis_arrow_a_initial[1],
                    vector_light_circle_axis_arrow_a_initial[2])
qvr_light_circle_axis_arrow_b = ax0.quiver(x0a_, y0a_, z0a_, u0a_, v0a_, w0a_, length=1, color='pink',
                                           normalize=False, label='Light circle axis arrow B', linewidth=1, linestyle='--')


# Light arrow
x1a_, y1a_, z1a_ = 0., 0., 0.
u1a_, v1a_, w1a_ = vector_light_arrow_a_initial[0], vector_light_arrow_a_initial[1], vector_light_arrow_a_initial[2]
qvr_light_arrow_a = ax0.quiver(x1a_, y1a_, z1a_, u1a_, v1a_, w1a_, length=1, color='blue', normalize=False,
                               label='Light arrow A')

x1b_, y1b_, z1b_ = 0., 0., 0.
u1b_, v1b_, w1b_ = vector_light_arrow_b_initial[0], vector_light_arrow_b_initial[1], vector_light_arrow_b_initial[2]
qvr_light_arrow_b = ax0.quiver(x1b_, y1b_, z1b_, u1b_, v1b_, w1b_, length=1, color='red', normalize=False,
                               label='Light arrow B')

x1c_, y1c_, z1c_ = 0., 0., 0.
u1c_, v1c_, w1c_ = vector_light_arrow_c_initial[0], vector_light_arrow_c_initial[1], vector_light_arrow_c_initial[2]
qvr_light_arrow_c = ax0.quiver(x1c_, y1c_, z1c_, u1c_, v1c_, w1c_, length=1, color='green', normalize=False,
                               label='Light arrow Composed')

# Light arrow pass
x_light_arrow_a_pass = []
y_light_arrow_a_pass = []
z_light_arrow_a_pass = []
plt_light_arrow_a_pass, = ax0.plot(np.array(x_light_arrow_a_pass), np.array(y_light_arrow_a_pass),
                                   np.array(z_light_arrow_a_pass), color='blue', linewidth=0.5, linestyle='-')
x_light_arrow_b_pass = []
y_light_arrow_b_pass = []
z_light_arrow_b_pass = []
plt_light_arrow_b_pass, = ax0.plot(np.array(x_light_arrow_b_pass), np.array(y_light_arrow_b_pass),
                                   np.array(z_light_arrow_b_pass), color='red', linewidth=0.5, linestyle='-')
x_light_arrow_c_pass = []
y_light_arrow_c_pass = []
z_light_arrow_c_pass = []
plt_light_arrow_c_pass, = ax0.plot(np.array(x_light_arrow_c_pass), np.array(y_light_arrow_c_pass),
                                   np.array(z_light_arrow_c_pass), color='green', linewidth=1, linestyle='-')
update_light_arrow_path()

# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

frm_anim = ttk.Labelframe(root, relief='ridge', text='Animation', labelanchor='n')
frm_anim.pack(side='left', fill=tk.Y)
btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
btn_play.pack(side='left')
btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
btn_reset.pack(side='left')

# Parameter setting
# Spin A
frm_spin_a = ttk.Labelframe(root, relief="ridge", text="Spin A", labelanchor="n")
frm_spin_a.pack(side='left', fill=tk.Y)

lbl_scl_a = tk.Label(frm_spin_a, text="Scale:")
lbl_scl_a.pack(side='left')
var_scl_a = tk.StringVar(root)
var_scl_a.set(str(scale_a))
spn_scl_a = tk.Spinbox(
    frm_spin_a, textvariable=var_scl_a, format="%.2f", from_=-2., to=2., increment=0.1,
    command=lambda: set_scale_a(var_scl_a.get()), width=6
    )
spn_scl_a.pack(side='left')

lbl_scl_rot_lca_a = tk.Label(frm_spin_a, text="Light circle rotation:")
lbl_scl_rot_lca_a.pack(side='left')
var_scl_rot_lca_a = tk.StringVar(root)
var_scl_rot_lca_a.set(str(rot_light_circle_axis_arrow_a))
spn_scl_rot_lca_a = tk.Spinbox(
    frm_spin_a, textvariable=var_scl_rot_lca_a, format="%.2f", from_=-4., to=4., increment=0.1,
    command=lambda: set_rot_light_circle_axis_a(var_scl_rot_lca_a.get()), width=6
    )
spn_scl_rot_lca_a.pack(side='left')

lbl_scl_rot_la_a = tk.Label(frm_spin_a, text="Light arrow rotation:")
lbl_scl_rot_la_a.pack(side='left')
var_scl_rot_la_a = tk.StringVar(root)
var_scl_rot_la_a.set(str(rot_light_arrow_a))
spn_scl_rot_la_a = tk.Spinbox(
    frm_spin_a, textvariable=var_scl_rot_la_a, format="%.2f", from_=-4., to=4., increment=0.1,
    command=lambda: set_rot_light_arrow_a(var_scl_rot_la_a.get()), width=6
    )
spn_scl_rot_la_a.pack(side='left')

lbl_scl_phase_a = tk.Label(frm_spin_a, text="Initial phase:")
lbl_scl_phase_a.pack(side='left')
var_scl_phase_a = tk.StringVar(root)
var_scl_phase_a.set(str(phase_a))
spn_scl_phase_a = tk.Spinbox(
    frm_spin_a, textvariable=var_scl_phase_a, format="%.2f", from_=-360, to=360, increment=1,
    command=lambda: set_phase_a(var_scl_phase_a.get()), width=6
    )
spn_scl_phase_a.pack(side='left')

# Spin B
frm_spin_b = ttk.Labelframe(root, relief="ridge", text="Spin B", labelanchor="n")
frm_spin_b.pack(side='left', fill=tk.Y)

lbl_scl_b = tk.Label(frm_spin_b, text="Scale:")
lbl_scl_b.pack(side='left')
var_scl_b = tk.StringVar(root)
var_scl_b.set(str(scale_a))
spn_scl_b = tk.Spinbox(
    frm_spin_b, textvariable=var_scl_b, format="%.2f", from_=-2., to=2., increment=0.1,
    command=lambda: set_scale_b(var_scl_b.get()), width=6
    )
spn_scl_b.pack(side='left')

lbl_scl_rot_lca_b = tk.Label(frm_spin_b, text="Light circle rotation:")
lbl_scl_rot_lca_b.pack(side='left')
var_scl_rot_lca_b = tk.StringVar(root)
var_scl_rot_lca_b.set(str(rot_light_circle_axis_arrow_b))
spn_scl_rot_lca_b = tk.Spinbox(
    frm_spin_b, textvariable=var_scl_rot_lca_b, format="%.2f", from_=-4., to=4., increment=0.1,
    command=lambda: set_rot_light_circle_axis_b(var_scl_rot_lca_b.get()), width=6
    )
spn_scl_rot_lca_b.pack(side='left')

lbl_scl_rot_la_b = tk.Label(frm_spin_b, text="Light arrow rotation:")
lbl_scl_rot_la_b.pack(side='left')
var_scl_rot_la_b = tk.StringVar(root)
var_scl_rot_la_b.set(str(rot_light_arrow_a))
spn_scl_rot_la_b = tk.Spinbox(
    frm_spin_b, textvariable=var_scl_rot_la_b, format="%.2f", from_=-4., to=4., increment=0.1,
    command=lambda: set_rot_light_arrow_b(var_scl_rot_la_b.get()), width=6
    )
spn_scl_rot_la_b.pack(side='left')

lbl_scl_phase_b = tk.Label(frm_spin_b, text="Initial phase:")
lbl_scl_phase_b.pack(side='left')
var_scl_phase_b = tk.StringVar(root)
var_scl_phase_b.set(str(phase_a))
spn_scl_phase_b = tk.Spinbox(
    frm_spin_b, textvariable=var_scl_phase_b, format="%.2f", from_=-360, to=360, increment=1,
    command=lambda: set_phase_b(var_scl_phase_b.get()), width=6
    )
spn_scl_phase_b.pack(side='left')

# main loop
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
root.mainloop()
