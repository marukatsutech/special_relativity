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
    update_diagram()


def set_spin_d(value):
    global spin_denominator
    spin_denominator = int(value)
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
    draw_pass_spin()


def reset():
    global is_play, cnt
    is_play = False
    cnt = 0


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt
    txt_step.set_text("Spin " + str(spin_numerator) + "/" + str(spin_denominator))
    if True:
        update_diagram()
        # cnt += 1


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
txt_step = ax0.text2D(x_min, y_max, "Spin " + str(spin_numerator) + "/" + str(spin_denominator), fontsize=24)
xz, yz, _ = proj3d.proj_transform(x_min, y_max, z_max, ax0.get_proj())
txt_step.set_position((xz, yz))

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

# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

'''
btn_play = tk.Button(root, text="Play/Pause", command=switch)
btn_play.pack(side='left')
btn_reset = tk.Button(root, text="Reset", command=reset)
btn_reset.pack(side='left')
'''

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
anim = animation.FuncAnimation(fig, update, interval=200)
root.mainloop()
