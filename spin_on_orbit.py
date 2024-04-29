# Spin on orbit
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


def set_spin(value):
    global is_play
    global rot_matrix_center
    is_play = False
    if value == 1:
        rot_matrix_center = rot_matrix_x_center
        print(value)
    elif value == 2:
        rot_matrix_center = rot_matrix_y_center
        print(value)
    else:
        rot_matrix_center = rot_matrix_z_center
        print(value)
    reset()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_orbital(value):
    global is_play
    global rot_matrix_orbit
    is_play = False
    if value == 1:
        rot_matrix_orbit = rot_matrix_x_orbit
        print(value)
    elif value == 2:
        rot_matrix_orbit = rot_matrix_y_orbit
        print(value)
    else:
        rot_matrix_orbit = rot_matrix_z_orbit
        print(value)
    reset()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_dir_x(value):
    global is_play
    global dir_center_axis_init
    is_play = False
    dir_center_axis_init[0] = float(value)
    reset()
    set_light_arrow()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_dir_y(value):
    global is_play
    global dir_center_axis_init
    is_play = False
    dir_center_axis_init[1] = float(value)
    reset()
    set_light_arrow()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_dir_z(value):
    global is_play
    global dir_center_axis_init
    is_play = False
    dir_center_axis_init[2] = float(value)
    reset()
    set_light_arrow()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_center_x(value):
    global is_play
    global position_center_init
    is_play = False
    position_center_init[0] = float(value)
    reset()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_center_y(value):
    global is_play
    global position_center_init
    is_play = False
    position_center_init[1] = float(value)
    reset()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def set_center_z(value):
    global is_play
    global position_center_init
    is_play = False
    position_center_init[2] = float(value)
    reset()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_circle()
    update_light_arrow_pass()


def update_light_arrow_pass():
    global x_light_arrow_pass, y_light_arrow_pass, z_light_arrow_pass, plt_light_arrow_pass
    position_center_pass = position_center_init
    dir_center_axis_pass = dir_center_axis_init
    dir_light_arrow_pass = dir_light_arrow_init
    pass
    x = []
    y = []
    z = []
    for i in range(720):
        position_center_pass = rot_matrix_orbit.apply(position_center_pass)
        dir_center_axis_pass = rot_matrix_center.apply(dir_center_axis_pass)
        dir_light_arrow_pass = rot_matrix_center.apply(dir_light_arrow_pass)
        rot_matrix_center_axis_light_pass = Rotation.from_rotvec(theta_light_stp * dir_center_axis_pass)
        dir_light_arrow_pass = rot_matrix_center_axis_light_pass.apply(dir_light_arrow_pass)
        point = position_center_pass + dir_light_arrow_pass
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    plt_light_arrow_pass.set_xdata(np.array(x))
    plt_light_arrow_pass.set_ydata(np.array(y))
    plt_light_arrow_pass.set_3d_properties(np.array(z))


def set_light_arrow():
    global qvr_light_arrow, x1, y1, z1, u1, v1, w1
    global dir_light_arrow
    # r = np.linalg.norm(dir_center_axis)
    r_xy = np.sqrt(dir_center_axis[0] ** 2 + dir_center_axis[1] ** 2)
    phi = np.arctan2(dir_center_axis[1], dir_center_axis[0])
    theta = np.arctan2(r_xy, dir_center_axis[2])
    dir_light_arrow[0] = 1. * np.sin(theta + np.pi / 2.) * np.cos(phi)
    dir_light_arrow[1] = 1. * np.sin(theta + np.pi / 2.) * np.sin(phi)
    dir_light_arrow[2] = 1. * np.cos(theta + np.pi / 2.)
    qvr_light_arrow.remove()
    x1, y1, z1 = position_center[0], position_center[1], position_center[2]
    u1, v1, w1 = dir_light_arrow[0], dir_light_arrow[1], dir_light_arrow[2]
    qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True,
                                 label='Light arrow')


def update_light_arrow():
    global qvr_light_arrow, x1, y1, z1, u1, v1, w1
    qvr_light_arrow.remove()
    x1, y1, z1 = position_center[0], position_center[1], position_center[2]
    u1, v1, w1 = dir_light_arrow[0], dir_light_arrow[1], dir_light_arrow[2]
    qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True,
                                 label='Light arrow')


def update_center_axis_arrow():
    global qvr_center_axis_arrow, x0, y0, z0, u0, v0, w0
    qvr_center_axis_arrow.remove()
    x0, y0, z0 = position_center[0], position_center[1], position_center[2]
    u0, v0, w0 = dir_center_axis[0], dir_center_axis[1], dir_center_axis[2]
    qvr_center_axis_arrow = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='blue', normalize=True,
                                       label='Center axis arrow')


def update_light_circle():
    global plt_light_circle, x_light_circle, y_light_circle, z_light_circle
    point = dir_light_arrow
    rot_matrix_center_axis_light_circle = Rotation.from_rotvec(theta_light_circle_stp * dir_center_axis)
    x = []
    y = []
    z = []
    for i in range(360):
        point = rot_matrix_center_axis_light_circle.apply(point)
        x.append(point[0] + position_center[0])
        y.append(point[1] + position_center[1])
        z.append(point[2] + position_center[2])
    plt_light_circle.set_xdata(np.array(x))
    plt_light_circle.set_ydata(np.array(y))
    plt_light_circle.set_3d_properties(np.array(z))


def reset():
    global is_play, cnt
    global position_center, dir_center_axis, dir_light_arrow
    is_play = False
    cnt = 0
    position_center = position_center_init
    dir_center_axis = dir_center_axis_init
    dir_light_arrow = dir_light_arrow_init
    update_light_circle()
    update_center_axis_arrow()
    update_light_arrow()
    update_light_arrow_pass()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt
    global txt_step, txt_rot
    global position_center, dir_center_axis, dir_light_arrow
    txt_step.set_text("Step=" + str(cnt))
    txt_rot.set_text("Light-arrow" + str(0) + ", Center axis" + str(0))
    if is_play:
        update_center_axis_arrow()
        update_light_arrow()
        update_light_circle()
        cnt += 1
        position_center = rot_matrix_orbit.apply(position_center)
        dir_center_axis = rot_matrix_center.apply(dir_center_axis)
        dir_light_arrow = rot_matrix_center.apply(dir_light_arrow)
        rot_matrix_center_axis_light = Rotation.from_rotvec(theta_light_stp * dir_center_axis)
        dir_light_arrow = rot_matrix_center_axis_light.apply(dir_light_arrow)


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

position_center_init = np.array([0., 0., 0.])
dir_center_axis_init = np.array([0., 1., 0.])
dir_light_arrow_init = np.array([0., 0., 1.])

position_center = position_center_init
dir_center_axis = dir_center_axis_init
dir_light_arrow = dir_light_arrow_init

theta_orbit_stp = np.pi / 180.
rot_matrix_x_orbit = Rotation.from_rotvec(theta_orbit_stp * vector_x_axis)
rot_matrix_y_orbit = Rotation.from_rotvec(theta_orbit_stp * vector_y_axis)
rot_matrix_z_orbit = Rotation.from_rotvec(theta_orbit_stp * vector_z_axis)
rot_matrix_orbit = rot_matrix_x_orbit

theta_center_stp = np.pi / 180.
rot_matrix_x_center = Rotation.from_rotvec(theta_center_stp * vector_x_axis)
rot_matrix_y_center = Rotation.from_rotvec(theta_center_stp * vector_y_axis)
rot_matrix_z_center = Rotation.from_rotvec(theta_center_stp * vector_z_axis)
rot_matrix_center = rot_matrix_x_center

theta_light_stp = np.pi / 180.
theta_light_circle_stp = np.pi / 180.

# Generate figure and axes
title_ax0 = "Spin on orbit"
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
ax0.set_zlabel('z')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

# Generate items
# Text
txt_step = ax0.text2D(x_min, y_max, "Step=" + str(0))
xz, yz, _ = proj3d.proj_transform(x_min, y_max, z_max, ax0.get_proj())
txt_step.set_position((xz, yz))
txt_rot = ax0.text2D(x_min, y_max, "Light-arrow" + str(0) + ", Center axis" + str(0), fontsize=12)
xz, yz, _ = proj3d.proj_transform(x_min, y_min, z_max, ax0.get_proj())
txt_rot.set_position((xz, yz))

# Diagram
# Center line
ln_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_x)
ln_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_y)
ln_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_z)

# Guide circle orbit
crc_orbit_xy = Circle((0., 0.), 1., ec='gray', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(crc_orbit_xy)
art3d.pathpatch_2d_to_3d(crc_orbit_xy, z=0., zdir='z')
crc_orbit_yz = Circle((0., 0.), 1., ec='gray', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(crc_orbit_yz)
art3d.pathpatch_2d_to_3d(crc_orbit_yz, z=0., zdir='y')
crc_orbit_zx = Circle((0., 0.), 1., ec='gray', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(crc_orbit_zx)
art3d.pathpatch_2d_to_3d(crc_orbit_zx, z=0., zdir='x')

# Light circle
theta_light_circle_deg = np.arange(0., 360., 6.)
x_light_circle = theta_light_circle_deg * 0.
y_light_circle = theta_light_circle_deg * 0.
z_light_circle = theta_light_circle_deg * 0.
plt_light_circle, = ax0.plot(x_light_circle, y_light_circle, z_light_circle, linewidth=2, linestyle=':', c='darkorange')

# light circle center axis arrow
x0, y0, z0 = 0., 0., 0.
u0, v0, w0 = 0., 0., 0.
qvr_center_axis_arrow = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='blue', normalize=True,
                                   label='Center axis arrow')
# light arrow
x1, y1, z1 = 0., 0., 0.
u1, v1, w1 = 0., 0., 0.
qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True, label='light arrow')

# light arrow pass
x_light_arrow_pass = []
y_light_arrow_pass = []
z_light_arrow_pass = []
plt_light_arrow_pass, = ax0.plot(np.array(x_light_arrow_pass), np.array(y_light_arrow_pass),
                                 np.array(z_light_arrow_pass), color='gold', linewidth=2, linestyle='-')

# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Animation
frm_anim = ttk.Labelframe(root, relief='ridge', text='Animation', labelanchor='n')
frm_anim.pack(side='left', fill=tk.Y)
btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
btn_play.pack(side='left')
btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
btn_reset.pack(side='left')
# Parameters
# position_center_init = np.array([1., 0., 0.])
frm_center = ttk.Labelframe(root, relief='ridge', text='Center axis position', labelanchor='n')
frm_center.pack(side='left', fill=tk.Y)
lbl_center = tk.Label(frm_center, text='x,y,z:')
lbl_center.pack(side='left')

var_center_x = tk.StringVar(root)
var_center_x.set(position_center_init[0])
spn_center_x = tk.Spinbox(
    frm_center, textvariable=var_center_x, from_=-1, to=1, increment=1,
    command=lambda: set_center_x(var_center_x.get()), width=3
)
spn_center_x.pack(side='left')

var_center_y = tk.StringVar(root)
var_center_y.set(position_center_init[1])
spn_center_y = tk.Spinbox(
    frm_center, textvariable=var_center_y, from_=-1, to=1, increment=1,
    command=lambda: set_center_y(var_center_y.get()), width=3
)
spn_center_y.pack(side='left')

var_center_z = tk.StringVar(root)
var_center_z.set(position_center_init[2])
spn_center_z = tk.Spinbox(
    frm_center, textvariable=var_center_z, from_=-1, to=1, increment=1,
    command=lambda: set_center_z(var_center_z.get()), width=3
)
spn_center_z.pack(side='left')

# dir_center_axis_init = np.array([0., 1., 0.])
frm_dir = ttk.Labelframe(root, relief='ridge', text='Center axis direction', labelanchor='n')
frm_dir.pack(side='left', fill=tk.Y)
lbl_center = tk.Label(frm_dir, text='x,y,z:')
lbl_center.pack(side='left')

var_dir_x = tk.StringVar(root)
var_dir_x.set(dir_center_axis_init[0])
spn_dir_x = tk.Spinbox(
    frm_dir, textvariable=var_dir_x, from_=-1, to=1, increment=1,
    command=lambda: set_dir_x(var_dir_x.get()), width=3
)
spn_dir_x.pack(side='left')

var_dir_y = tk.StringVar(root)
var_dir_y.set(dir_center_axis_init[1])
spn_dir_y = tk.Spinbox(
    frm_dir, textvariable=var_dir_y, from_=-1, to=1, increment=1,
    command=lambda: set_dir_y(var_dir_y.get()), width=3
)
spn_dir_y.pack(side='left')

var_dir_z = tk.StringVar(root)
var_dir_z.set(dir_center_axis_init[2])
spn_dir_z = tk.Spinbox(
    frm_dir, textvariable=var_dir_z, from_=-1, to=1, increment=1,
    command=lambda: set_dir_z(var_dir_z.get()), width=3
)
spn_dir_z.pack(side='left')

# rot_matrix_orbit = rot_matrix_y_orbit
frm_orb = ttk.Labelframe(root, relief='ridge', text='Orbital direction', labelanchor='n')
frm_orb.pack(side='left', fill=tk.Y)
var_orb = tk.IntVar(root)
rd1_orb = tk.Radiobutton(frm_orb, text="x axis", value=1, var=var_orb, command=lambda: set_orbital(var_orb.get()))
rd1_orb.pack()
rd2_orb = tk.Radiobutton(frm_orb, text="y axis", value=2, var=var_orb, command=lambda: set_orbital(var_orb.get()))
rd2_orb.pack()
rd3_orb = tk.Radiobutton(frm_orb, text="z axis", value=3, var=var_orb, command=lambda: set_orbital(var_orb.get()))
rd3_orb.pack()
var_orb.set(1)

# rot_matrix_center = rot_matrix_z_center
frm_spin = ttk.Labelframe(root, relief='ridge', text='Spin direction', labelanchor='n')
frm_spin.pack(side='left', fill=tk.Y)
var_spin = tk.IntVar(root)
rd1_spin = tk.Radiobutton(frm_spin, text="x axis", value=1, var=var_spin, command=lambda: set_spin(var_spin.get()))
rd1_spin.pack()
rd2_spin = tk.Radiobutton(frm_spin, text="y axis", value=2, var=var_spin, command=lambda: set_spin(var_spin.get()))
rd2_spin.pack()
rd3_spin = tk.Radiobutton(frm_spin, text="z axis", value=3, var=var_spin, command=lambda: set_spin(var_spin.get()))
rd3_spin.pack()
var_spin.set(1)

# Draw initial diagram
update_center_axis_arrow()
update_light_arrow()
update_light_circle()
update_light_arrow_pass()

# main loop
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
