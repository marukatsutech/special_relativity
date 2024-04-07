# Spin of fermion
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


def set_spin_n(value):
    global spin_numerator
    spin_numerator = int(value)
    reset()
    update_diagram()


def set_spin_d(value):
    global spin_denominator
    spin_denominator = int(value)
    reset()
    update_diagram()


def draw_pass_spin():
    global x_light_arrow_pass, y_light_arrow_pass, z_light_arrow_pass
    global theta_rad_spin_axis, theta_rad_light_arrow
    x_light_arrow_pass = []
    y_light_arrow_pass = []
    z_light_arrow_pass = []
    theta_rad_spin_axis = 0.
    theta_rad_light_arrow = 0.
    for i in range(360):
        rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis * vector_z_axis)
        vector_rotated_spin_axis_z = rot_matrix_z.apply(vector_spin_axis_initial)
        vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_initial)
        rot_matrix_spin_axis_rotated = Rotation.from_rotvec(theta_rad_light_arrow * vector_rotated_spin_axis_z)
        vector_rotated_light_arrow = rot_matrix_spin_axis_rotated.apply(vector_rotated_light_arrow_z)
        u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
        x_light_arrow_pass.append(u1)
        y_light_arrow_pass.append(v1)
        z_light_arrow_pass.append(w1)
        theta_rad_spin_axis = theta_rad_spin_axis - spin_numerator * ((2. * np.pi) / 360)
        theta_rad_light_arrow = theta_rad_light_arrow - spin_denominator * ((2. * np.pi) / 360)
    plt_light_arrow_pass.set_xdata(np.array(x_light_arrow_pass))
    plt_light_arrow_pass.set_ydata(np.array(y_light_arrow_pass))
    plt_light_arrow_pass.set_3d_properties(np.array(z_light_arrow_pass))


def update_diagram():
    global plt_guide_circle, theta_rad_spin_axis_anim, theta_rad_light_arrow_anim
    global qvr_spin_axis, qvr_light_arrow
    draw_pass_spin()
    # Rotation matrix (z axis)
    rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis_anim * vector_z_axis)
    # Guide circle
    x_guide_circle_rotated_z = []
    y_guide_circle_rotated_z = []
    z_guide_circle_rotated_z = []
    for i in range(len(x_guide_circle)):
        vector_point = np.array([x_guide_circle[i], y_guide_circle[i], z_guide_circle[i]])
        point_rotated_z = rot_matrix_z.apply(vector_point)
        x_guide_circle_rotated_z.append(point_rotated_z[0])
        y_guide_circle_rotated_z.append(point_rotated_z[1])
        z_guide_circle_rotated_z.append(point_rotated_z[2])
    plt_guide_circle.set_xdata(np.array(x_guide_circle_rotated_z))
    plt_guide_circle.set_ydata(np.array(y_guide_circle_rotated_z))
    plt_guide_circle.set_3d_properties(np.array(z_guide_circle_rotated_z))
    # Rotate spin axis arrow
    rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis_anim * vector_z_axis)
    vector_rotated_spin_axis_z = rot_matrix_z.apply(vector_spin_axis_initial)
    x0, y0, z0 = 0., 0., 0.
    u0, v0, w0 = vector_rotated_spin_axis_z[0], vector_rotated_spin_axis_z[1], vector_rotated_spin_axis_z[2]
    qvr_spin_axis.remove()
    qvr_spin_axis = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='blue', normalize=True, label='Axis of spin')
    # Rotate light arrow
    vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_initial)
    rot_matrix_spin_axis_rotated = Rotation.from_rotvec(theta_rad_light_arrow_anim * vector_rotated_spin_axis_z)
    vector_rotated_light_arrow = rot_matrix_spin_axis_rotated.apply(vector_rotated_light_arrow_z)
    qvr_light_arrow.remove()
    x1, y1, z1 = 0., 0., 0.
    u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
    qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True,
                                 label='Phase(light arrow)')
    # Change theta
    theta_rad_spin_axis_anim = theta_rad_spin_axis_anim - spin_numerator * ((2. * np.pi) / 360)
    theta_rad_light_arrow_anim = theta_rad_light_arrow_anim - spin_denominator * ((2. * np.pi) / 360)


def reset():
    global is_play, cnt
    global theta_rad_spin_axis_anim, theta_rad_light_arrow_anim
    is_play = False
    cnt = 0
    theta_rad_light_arrow_anim = 0.
    theta_rad_spin_axis_anim = 0.
    update_diagram()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt
    txt_step.set_text("Step=" + str(cnt))
    txt_spin.set_text("Spin " + str(spin_numerator) + "/" + str(spin_denominator))
    if is_play:
        update_diagram()
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

vector_z_axis = np.array([0., 0., 1.])
vector_spin_axis_initial = np.array([0., 1., 0.])
vector_light_arrow_initial = np.array([0., 0., 1.])
theta_rad_spin_axis = 0.
theta_rad_light_arrow = 0.
theta_rad_spin_axis_anim = 0.
theta_rad_light_arrow_anim = 0.

step_rotation = 0.1

spin_numerator = 1
spin_denominator = 1

# Generate figure and axes
title_ax0 = "Spin of fermion"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max
z_min = range_z_min
z_max = range_z_max

fig = Figure()
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_zlabel('t')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

# Generate items
txt_step = ax0.text2D(x_min, y_max, "Step=" + str(0))
xz, yz, _ = proj3d.proj_transform(x_min, y_max, z_max, ax0.get_proj())
txt_step.set_position((xz, yz))
txt_spin = ax0.text2D(x_min, y_max, "Spin " + str(spin_numerator) + "/" + str(spin_denominator), fontsize=24)
xz, yz, _ = proj3d.proj_transform(x_min, y_min, z_max, ax0.get_proj())
txt_spin.set_position((xz, yz))

ln_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_x)
ln_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_y)
ln_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_z)

# Spin pass
x_light_arrow_pass = []
y_light_arrow_pass = []
z_light_arrow_pass = []
plt_light_arrow_pass, = ax0.plot(np.array(x_light_arrow_pass), np.array(y_light_arrow_pass),
                                 np.array(z_light_arrow_pass), color='darkorange')

# Guide circle
angle_guide_circle = np.arange(0., 360., 1.)
x_guide_circle = np.cos(angle_guide_circle * np.pi / 180.)
y_guide_circle = angle_guide_circle * 0.
z_guide_circle = np.sin(angle_guide_circle * np.pi / 180.)
plt_guide_circle, = ax0.plot(x_guide_circle, y_guide_circle, z_guide_circle, linewidth=1, linestyle=':', c='darkorange')

# Spin axis arrow
x0_, y0_, z0_ = 0., 0., 0.
u0_, v0_, w0_ = vector_spin_axis_initial[0], vector_spin_axis_initial[1], vector_spin_axis_initial[2]
qvr_spin_axis = ax0.quiver(x0_, y0_, z0_, u0_, v0_, w0_, length=1, color='blue', normalize=True,
                           label='Axis of spin')

# Light arrow
x1_, y1_, z1_ = 0., 0., 0.
u1_, v1_, w1_ = vector_light_arrow_initial[0], vector_light_arrow_initial[1], vector_light_arrow_initial[2]
qvr_light_arrow = ax0.quiver(x1_, y1_, z1_, u1_, v1_, w1_, length=1, color='darkorange', normalize=True,
                             label='Phase(light arrow)')

# Draw initial diagram
update_diagram()

# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

btn_play = tk.Button(root, text="Play/Pause", command=switch)
btn_play.pack(side='left')
btn_reset = tk.Button(root, text="Reset", command=reset)
btn_reset.pack(side='left')

# Parameter setting
frm_spin = ttk.Labelframe(root, relief='ridge', text='Spin', labelanchor='n')
frm_spin.pack(side='left', fill=tk.Y)
lbl_spin_n = tk.Label(frm_spin, text='Numerator:')
lbl_spin_n.pack()
var_spin_n = tk.StringVar(root)  # variable for spinbox-value
var_spin_n.set(spin_numerator)  # Initial value
spn_spin_n = tk.Spinbox(
    frm_spin, textvariable=var_spin_n, from_=0, to=8, increment=1,
    command=lambda: set_spin_n(var_spin_n.get()), width=6
    )
spn_spin_n.pack()
lbl_spin_d = tk.Label(frm_spin, text='Denominator:')
lbl_spin_d.pack()
var_spin_d = tk.StringVar(root)  # variable for spinbox-value
var_spin_d.set(spin_numerator)  # Initial value
spn_spin_d = tk.Spinbox(
    frm_spin, textvariable=var_spin_d, from_=0, to=8, increment=1,
    command=lambda: set_spin_d(var_spin_d.get()), width=6
    )
spn_spin_d.pack()

# main loop
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
