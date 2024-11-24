# Fermion spin prototype (Spin test5)
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import Circle


def update_diagram():
    global line_phase, theta_rotation
    theta_rotation = (theta_rotation + step_rotation) % (4. * np.pi)
    if 0 <= theta_rotation < np.pi:
        line_phase.set_data_3d([np.cos(theta_rotation), 0.], [np.sin(theta_rotation), 0.], [1., 0.])
    elif np.pi <= theta_rotation < 2. * np.pi:
        line_phase.set_data_3d([-1., 0.], [np.sin(theta_rotation), 0.], [-np.cos(theta_rotation), 0.])
    elif 2. * np.pi <= theta_rotation < 3. * np.pi:
        line_phase.set_data_3d([-np.cos(theta_rotation), 0.], [np.sin(theta_rotation), 0.], [-1., 0.])
    else:
        line_phase.set_data_3d([1., 0.], [np.sin(theta_rotation), 0.], [np.cos(theta_rotation), 0.])


def reset():
    global is_play, cnt, txt_step
    is_play = False
    cnt = 0
    txt_step.set_text("Step=" + str(cnt))


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt, txt_step
    txt_step.set_text("Step=" + str(cnt))
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
range_z_max = 4.

theta_rotation = 0.
step_rotation = 0.1

# Generate figure and axes
title_ax0 = "Spin 1/2"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max
z_min = range_z_min
z_max = range_z_max

fig = Figure()
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_box_aspect((4, 4, 6))
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

c_center = Circle((0., 0.), 1, ec='gray', fill=False)
ax0.add_patch(c_center)
art3d.pathpatch_2d_to_3d(c_center, z=0, zdir="y")

c_upper = Circle((0., 0.), 1, ec='gray', fill=False)
ax0.add_patch(c_upper)
art3d.pathpatch_2d_to_3d(c_upper, z=1, zdir="z")

c_lower = Circle((0., 0.), 1, ec='gray', fill=False)
ax0.add_patch(c_lower)
art3d.pathpatch_2d_to_3d(c_lower, z=-1, zdir="z")

c_right = Circle((0., 0.), 1, ec='gray', fill=False)
ax0.add_patch(c_right)
art3d.pathpatch_2d_to_3d(c_right, z=1, zdir="x")

c_left = Circle((0., 0.), 1, ec='gray', fill=False)
ax0.add_patch(c_left)
art3d.pathpatch_2d_to_3d(c_left, z=-1, zdir="x")

l_center_v = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(l_center_v)

l_center_h = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color='gray', ls="-.", linewidth=1)
ax0.add_line(l_center_h)

for i_ in range(0, 360, 15):
    x_ = np.cos(i_ * np.pi / 180.)
    y_ = np.sin(i_ * np.pi / 180.)
    l_guide_upper = art3d.Line3D([x_, 0.], [y_, 0.], [1., 0.], color='gray', ls="--", linewidth=0.5)
    ax0.add_line(l_guide_upper)
    l_guide_lower = art3d.Line3D([x_, 0.], [y_, 0.], [-1., 0.], color='gray', ls="--", linewidth=0.5)
    ax0.add_line(l_guide_lower)
    l_guide_right = art3d.Line3D([1., 0.], [x_, 0.], [y_, 0.], color='gray', ls="--", linewidth=0.5)
    ax0.add_line(l_guide_right)
    l_guide_left = art3d.Line3D([-1., 0.], [x_, 0.], [y_, 0.], color='gray', ls="--", linewidth=0.5)
    ax0.add_line(l_guide_left)

x_parabola = np.arange(x_min, x_max, 0.01)
y_parabola = x_parabola * 0.
z_parabola = x_parabola ** 2. + 1.
parabola = art3d.Line3D(x_parabola, y_parabola, z_parabola, color='gray', ls="--", linewidth=0.5)
ax0.add_line(parabola)

line_phase = art3d.Line3D([1., 0.], [0., 0.], [1., 0.], linewidth=1, color='blue')
ax0.add_line(line_phase)

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

# main loop
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
