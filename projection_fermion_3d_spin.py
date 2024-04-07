# Projection of double rotation in 3D (Spin)
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from matplotlib.patches import Circle
from scipy.spatial.transform import Rotation
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import proj3d


def update_diagram():
    global theta_rad_spin_axis, theta_rad_light_arrow
    global x0, y0, z0, u0, v0, w0, qvr_spin_axis
    global x1, y1, z1, u1, v1, w1, qvr_light_arrow
    global plt_guide_circle
    global line_projection
    global c_upper0_guide, line_light_arrow_projection, line_spin_axis_projection, line_spin_axis_projection_guide
    # Rotate spin axis
    rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis * vector_z_axis)
    vector_rotated_spin_axis_z = rot_matrix_z.apply(vector_spin_axis_initial)
    x0, y0, z0 = 0., 0., 0.
    u0, v0, w0 = vector_rotated_spin_axis_z[0], vector_rotated_spin_axis_z[1], vector_rotated_spin_axis_z[2]
    qvr_spin_axis.remove()
    qvr_spin_axis = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='blue', normalize=True, label='Axis of spin')
    # Rotate light arrow
    vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_initial)
    rot_matrix_spin_axis_rotated = Rotation.from_rotvec(theta_rad_light_arrow * vector_rotated_spin_axis_z)
    vector_rotated_light_arrow = rot_matrix_spin_axis_rotated.apply(vector_rotated_light_arrow_z)
    qvr_light_arrow.remove()
    x1, y1, z1 = 0., 0., 0.
    u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
    qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True,
                                 label='Phase(light arrow)')
    # Rotate Guide circle
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
    # Projection
    if vector_rotated_light_arrow[2] != 0.:
        slope_x_z = vector_rotated_light_arrow[0] / vector_rotated_light_arrow[2]
        slope_y_z = vector_rotated_light_arrow[1] / vector_rotated_light_arrow[2]
        line_projection.set_data_3d([0., slope_x_z], [0., slope_y_z], [0., 1.])
        c_upper0_guide.remove()
        r = np.sqrt(slope_x_z ** 2. + slope_y_z ** 2.)
        c_upper0_guide = Circle((0., 0.), r, ec='green', fill=False, linewidth=1, linestyle='--')
        ax0.add_patch(c_upper0_guide)
        art3d.pathpatch_2d_to_3d(c_upper0_guide, z=1, zdir='z')
        line_light_arrow_projection.set_data_3d([x_min * 10., x_max * 10.], [r, r], [1., 1.])
        projection_point = r * np.tan(- theta_rad_spin_axis)
        line_spin_axis_projection.set_data_3d([projection_point, 0.], [r, 0.], [1., 1.])
        line_spin_axis_projection_guide.set_data_3d([projection_point, projection_point], [r, 0.], [1., 1.])
    # Change theta
    theta_rad_spin_axis = (theta_rad_spin_axis - step_rotation) % (2. * np.pi)
    theta_rad_light_arrow = (theta_rad_light_arrow - step_rotation)


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
range_z_max = 2.

vector_z_axis = np.array([0., 0., 1.])
vector_spin_axis_initial = np.array([0., 1., 0.])
vector_light_arrow_initial = np.array([0., 0., 1.])
theta_rad_spin_axis = 0.
theta_rad_light_arrow = 0.

step_rotation = 0.1

# Generate figure and axes
title_ax0 = "Projection of double rotation in 3D (Spin)"
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

ln_axis_x = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_x)
ln_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_y)
ln_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color='gray', ls="-.", linewidth=1)
ax0.add_line(ln_axis_z)


x0, y0, z0 = 0., 0., 0.
u0, v0, w0 = vector_spin_axis_initial[0], vector_spin_axis_initial[1], vector_spin_axis_initial[2]
qvr_spin_axis = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='blue', normalize=True,
                           label='Axis of spin')
x1, y1, z1 = 0., 0., 0.
u1, v1, w1 = vector_light_arrow_initial[0], vector_light_arrow_initial[1], vector_light_arrow_initial[2]
qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True,
                             label='Phase(light arrow)')

angle_guide_circle = np.arange(0., 360., 1.)
x_guide_circle = np.cos(angle_guide_circle * np.pi / 180.)
y_guide_circle = angle_guide_circle * 0.
z_guide_circle = np.sin(angle_guide_circle * np.pi / 180.)
plt_guide_circle, = ax0.plot(x_guide_circle, y_guide_circle, z_guide_circle, linewidth=1, linestyle=':', c='darkorange')

line_projection = art3d.Line3D([0., 0.], [0., 0.], [0., 1.], linewidth=0.5, color='darkorange', ls='--')
ax0.add_line(line_projection)

x_light_arrow_pass = []
y_light_arrow_pass = []
z_light_arrow_pass = []
theta_rad_spin_axis_ = 0.
theta_rad_light_arrow_ = 0.
for i_ in range(len(angle_guide_circle)):
    rot_matrix_z_ = Rotation.from_rotvec(theta_rad_spin_axis_ * vector_z_axis)
    vector_rotated_spin_axis_z_ = rot_matrix_z_.apply(vector_spin_axis_initial)
    u0_, v0_, w0_ = vector_rotated_spin_axis_z_[0], vector_rotated_spin_axis_z_[1], vector_rotated_spin_axis_z_[2]
    vector_rotated_light_arrow_z_ = rot_matrix_z_.apply(vector_light_arrow_initial)
    rot_matrix_spin_axis_rotated_ = Rotation.from_rotvec(theta_rad_light_arrow_ * vector_rotated_spin_axis_z_)
    vector_rotated_light_arrow_ = rot_matrix_spin_axis_rotated_.apply(vector_rotated_light_arrow_z_)
    u1_, v1_, w1_ = vector_rotated_light_arrow_[0], vector_rotated_light_arrow_[1], vector_rotated_light_arrow_[2]
    x_light_arrow_pass.append(u1_)
    y_light_arrow_pass.append(v1_)
    z_light_arrow_pass.append(w1_)
    theta_rad_spin_axis_ = theta_rad_spin_axis_ - (2. * np.pi) / len(angle_guide_circle)
    theta_rad_light_arrow_ = theta_rad_light_arrow_ - (2. * np.pi) / len(angle_guide_circle)
plt_light_arrow_pass, = ax0.plot(np.array(x_light_arrow_pass), np.array(y_light_arrow_pass),
                                 np.array(z_light_arrow_pass), color='darkorange')

# Parabola
y_parabola = np.arange(x_min, x_max, 0.01)
z_parabola = y_parabola * 0. + 1.
x_parabola = y_parabola ** 2.
parabola = art3d.Line3D(x_parabola, y_parabola, z_parabola, color='magenta', ls='--', linewidth=1)
ax0.add_line(parabola)

# Projection to axis x
c_upper0_guide = Circle((0., 0.), 0, ec='green', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(c_upper0_guide)
art3d.pathpatch_2d_to_3d(c_upper0_guide, z=1, zdir='z')
line_upper0_radius = art3d.Line3D([0., 0.], [0., 0.], [0., 0.], linewidth=0.5, color='green', ls='-.')
ax0.add_line(line_upper0_radius)
line_light_arrow_projection = art3d.Line3D([x_min * 10., x_max * 10.], [0., 0.], [1., 1.], linewidth=0.5,
                                           color='green', ls='--')
ax0.add_line(line_light_arrow_projection)
line_spin_axis_projection = art3d.Line3D([0., 0.], [0., 0.], [1., 1.], linewidth=0.5, color='blue', ls='--')
ax0.add_line(line_spin_axis_projection)
line_spin_axis_projection_guide = art3d.Line3D([0., 0.], [0., 0.], [1., 1.], linewidth=1, color='magenta', ls='--')
ax0.add_line(line_spin_axis_projection_guide)

# Legend
ax0.legend(loc='lower right')

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
anim = animation.FuncAnimation(fig, update, interval=200)
root.mainloop()
