# Spin of boson and fermion
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from scipy.spatial.transform import Rotation
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import proj3d


def change_spin_state():
    global rot_xy, rot_txy
    if var_chk_axis_ts.get():
        rot_txy = 1
    else:
        rot_txy = 0
    if var_chk_axis_ss.get():
        rot_xy = 1
    else:
        rot_xy = 0
    reset()
    update_diagram()
    draw_pass_spin()


def draw_pass_spin():
    global x_light_arrow_pass, y_light_arrow_pass, z_light_arrow_pass
    global theta_rad_spin_axis, theta_rad_light_arrow
    global spin_pass_additional
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
        theta_rad_spin_axis = theta_rad_spin_axis - rot_xy * ((2. * np.pi) / 360)
        theta_rad_light_arrow = theta_rad_light_arrow + rot_txy * ((2. * np.pi) / 360)
    plt_light_arrow_pass.set_xdata(np.array(x_light_arrow_pass))
    plt_light_arrow_pass.set_ydata(np.array(y_light_arrow_pass))
    plt_light_arrow_pass.set_3d_properties(np.array(z_light_arrow_pass))
    # Spin pass additional
    for j in range(7):
        rot_matrix_z_ad = Rotation.from_rotvec(((j + 1) * np.pi / 180. * 360. / 8.) * vector_z_axis)
        x_light_arrow_pass_ad = []
        y_light_arrow_pass_ad = []
        z_light_arrow_pass_ad = []
        for k in range(360):
            vector_original = np.array([x_light_arrow_pass[k], y_light_arrow_pass[k], z_light_arrow_pass[k]])
            vector_ad = rot_matrix_z_ad.apply(vector_original)
            u_ad, v_ad, w_ad = vector_ad[0], vector_ad[1], vector_ad[2]
            x_light_arrow_pass_ad.append(u_ad)
            y_light_arrow_pass_ad.append(v_ad)
            z_light_arrow_pass_ad.append(w_ad)
        spin_pass_additional[j].set_xdata(np.array(x_light_arrow_pass_ad))
        spin_pass_additional[j].set_ydata(np.array(y_light_arrow_pass_ad))
        spin_pass_additional[j].set_3d_properties(np.array(z_light_arrow_pass_ad))


def update_diagram():
    global plt_guide_circle, theta_rad_spin_axis_anim, theta_rad_light_arrow_anim
    global qvr_spin_axis, qvr_light_arrow
    # draw_pass_spin()
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
    global theta_rad_spin_axis_anim, theta_rad_light_arrow_anim
    txt_step.set_text("Step=" + str(cnt))
    if rot_txy != 0:
        txt_spin.set_text("Spin " + str(1) + "/" + str(rot_txy + rot_xy))
    else:
        txt_spin.set_text("Not available")
    if is_play:
        update_diagram()
        # Change theta
        theta_rad_spin_axis_anim = theta_rad_spin_axis_anim - rot_xy * ((2. * np.pi) / 360)
        theta_rad_light_arrow_anim = theta_rad_light_arrow_anim + rot_txy * ((2. * np.pi) / 360)
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

rot_xy = 1
rot_txy = 1

# Generate figure and axes
title_ax0 = "Spin of boson and fermion"
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
txt_spin = ax0.text2D(x_min, y_max, "Spin " + str(1) + "/" + str(1), fontsize=24)
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
                                 np.array(z_light_arrow_pass), color='darkorange', linewidth=2)

# Guide circle
angle_guide_circle = np.arange(0., 360., 1.)
x_guide_circle = np.cos(angle_guide_circle * np.pi / 180.)
y_guide_circle = angle_guide_circle * 0.
z_guide_circle = np.sin(angle_guide_circle * np.pi / 180.)
plt_guide_circle, = ax0.plot(x_guide_circle, y_guide_circle, z_guide_circle, linewidth=2, linestyle=':', c='darkorange')

# Spin axis arrow
x0_, y0_, z0_ = 0., 0., 0.
u0_, v0_, w0_ = vector_spin_axis_initial[0], vector_spin_axis_initial[1], vector_spin_axis_initial[2]
qvr_spin_axis = ax0.quiver(x0_, y0_, z0_, u0_, v0_, w0_, length=1, color='blue', normalize=True,
                           label='Rotation of light circle')

# Light arrow
x1_, y1_, z1_ = 0., 0., 0.
u1_, v1_, w1_ = vector_light_arrow_initial[0], vector_light_arrow_initial[1], vector_light_arrow_initial[2]
qvr_light_arrow = ax0.quiver(x1_, y1_, z1_, u1_, v1_, w1_, length=1, color='darkorange', normalize=True,
                             label='Phase(light arrow)')

# Spin pass additional
x_light_arrow_pass = []
y_light_arrow_pass = []
z_light_arrow_pass = []
spin_pass_additional = []
for i_ in range(7):
    plt_light_arrow_pass_ad, = ax0.plot(np.array(x_light_arrow_pass), np.array(y_light_arrow_pass),
                                        np.array(z_light_arrow_pass), linewidth=0.5, linestyle='-')
    spin_pass_additional.append(plt_light_arrow_pass_ad)


# Draw initial diagram
update_diagram()
draw_pass_spin()

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
frm_spin = ttk.Labelframe(root, relief='ridge', text='Rotation', labelanchor='n')
frm_spin.pack(side='left', fill=tk.Y)
var_chk_axis_ts = tk.BooleanVar(root)    # Variable for checkbutton
var_chk_axis_ts.set(True)
chk_axis_ts = tk.Checkbutton(frm_spin, text="Time(t)-spatial(xy) (orange arrow)", 
                             variable=var_chk_axis_ts, command=change_spin_state)
chk_axis_ts.pack()
var_chk_axis_ss = tk.BooleanVar(root)    # Variable for checkbutton
var_chk_axis_ss.set(True)
chk_axis_ss = tk.Checkbutton(frm_spin, text="Spatial(x)-spatial(y) (blue arrow)", 
                             variable=var_chk_axis_ss, command=change_spin_state)
chk_axis_ss.pack()

# main loop
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
root.mainloop()
