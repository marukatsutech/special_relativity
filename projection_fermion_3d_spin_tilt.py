# Projection of double rotation in 3D (Spin) with tilt and rotation-speed control
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


def update_guide():
    global c_spin_axis_guide
    # Draw pass of spin axis
    c_spin_axis_guide.remove()
    c_spin_axis_guide = Circle((0., 0.), r_spin_axis_guide, ec='blue', fill=False, linewidth=0.5, linestyle='--')
    ax0.add_patch(c_spin_axis_guide)
    art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=h_spin_axis_guide, zdir='z')


def set_tilt(value):
    global tilt_angle_deg, vector_spin_axis_arrow_initial, vector_light_arrow_initial
    global c_spin_axis_guide
    global r_spin_axis_guide, h_spin_axis_guide
    tilt_angle_deg = float(value)
    r_spin_axis_guide = np.cos(tilt_angle_deg * np.pi / 180.)
    h_spin_axis_guide = np.sin(tilt_angle_deg * np.pi / 180.)
    vector_spin_axis_arrow_initial = np.array([0., r_spin_axis_guide, h_spin_axis_guide])
    vector_light_arrow_initial = np.array([0., np.cos((tilt_angle_deg + 90.) * np.pi / 180.),
                                          np.sin((tilt_angle_deg + 90.) * np.pi / 180.)])
    # update
    reset()
    update_diagram()
    draw_pass_spin()
    update_guide()


def set_spin_s(value):
    global rot_spin_axis_arrow
    rot_spin_axis_arrow = int(value)
    reset()
    update_diagram()
    draw_pass_spin()


def set_spin_l(value):
    global rot_light_arrow
    rot_light_arrow = int(value)
    reset()
    update_diagram()
    draw_pass_spin()


def draw_pass_spin():
    global x_light_arrow_pass, y_light_arrow_pass, z_light_arrow_pass
    global theta_rad_spin_axis_arrow, theta_rad_light_arrow
    x_light_arrow_pass = []
    y_light_arrow_pass = []
    z_light_arrow_pass = []
    theta_rad_spin_axis_arrow = 0.
    theta_rad_light_arrow = 0.
    for i in range(360):
        rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis_arrow * vector_z_axis)
        vector_rotated_spin_axis_arrow_z = rot_matrix_z.apply(vector_spin_axis_arrow_initial)
        vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_initial)
        rot_matrix_spin_axis_arrow_rotated = Rotation.from_rotvec(theta_rad_light_arrow *
                                                                  vector_rotated_spin_axis_arrow_z)
        vector_rotated_light_arrow = rot_matrix_spin_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
        u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
        x_light_arrow_pass.append(u1)
        y_light_arrow_pass.append(v1)
        z_light_arrow_pass.append(w1)
        theta_rad_spin_axis_arrow = theta_rad_spin_axis_arrow - rot_spin_axis_arrow * ((2. * np.pi) / 360)
        theta_rad_light_arrow = theta_rad_light_arrow + rot_light_arrow * ((2. * np.pi) / 360)
    plt_light_arrow_pass.set_xdata(np.array(x_light_arrow_pass))
    plt_light_arrow_pass.set_ydata(np.array(y_light_arrow_pass))
    plt_light_arrow_pass.set_3d_properties(np.array(z_light_arrow_pass))


def update_diagram():
    global plt_light_circle, theta_rad_spin_axis_arrow_anim, theta_rad_light_arrow_anim
    global qvr_spin_axis_arrow, qvr_light_arrow
    global line_projection, c_upper_guide, line_light_arrow_projection, line_spin_axis_projection
    global c_projection_dot, c_projection_dot_center, line_projection_p, c_projection_dot_parabola
    global c_projection_dot_ax1, c_projection_dot_center_ax1, c_projection_dot_parabola_ax1
    global diff_ratios_x, diff_ratios_y, plt_diff_ratio
    global pass_projection_x, pass_projection_y, plt_pass_projection, plt_projection_line_ax1
    # Rotation matrix (z axis)
    rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis_arrow_anim * vector_z_axis)
    # Rotate light circle
    # Rotate x axis (tilt)
    rot_matrix_x = Rotation.from_rotvec((tilt_angle_deg * np.pi / 180.) * vector_x_axis)
    x_light_circle_rotated_x = []
    y_light_circle_rotated_x = []
    z_light_circle_rotated_x = []
    for i in range(len(y_light_circle)):
        vector_point = np.array([x_light_circle[i], y_light_circle[i], z_light_circle[i]])
        point_rotated_x = rot_matrix_x.apply(vector_point)
        x_light_circle_rotated_x.append(point_rotated_x[0])
        y_light_circle_rotated_x.append(point_rotated_x[1])
        z_light_circle_rotated_x.append(point_rotated_x[2])
    # Rotate z axis
    x_light_circle_rotated_z = []
    y_light_circle_rotated_z = []
    z_light_circle_rotated_z = []
    for j in range(len(x_light_circle)):
        vector_point = np.array([x_light_circle_rotated_x[j], y_light_circle_rotated_x[j], z_light_circle_rotated_x[j]])
        point_rotated_z = rot_matrix_z.apply(vector_point)
        x_light_circle_rotated_z.append(point_rotated_z[0])
        y_light_circle_rotated_z.append(point_rotated_z[1])
        z_light_circle_rotated_z.append(point_rotated_z[2])
    plt_light_circle.set_xdata(np.array(x_light_circle_rotated_z))
    plt_light_circle.set_ydata(np.array(y_light_circle_rotated_z))
    plt_light_circle.set_3d_properties(np.array(z_light_circle_rotated_z))
    # Rotation spin axis arrow and light arrow
    # Rotate spin axis arrow (z axis)
    rot_matrix_z = Rotation.from_rotvec(theta_rad_spin_axis_arrow_anim * vector_z_axis)
    vector_rotated_spin_axis_arrow_z = rot_matrix_z.apply(vector_spin_axis_arrow_initial)
    x0, y0, z0 = 0., 0., 0.
    u0, v0, w0 = vector_rotated_spin_axis_arrow_z[0], vector_rotated_spin_axis_arrow_z[1], \
                 vector_rotated_spin_axis_arrow_z[2]
    qvr_spin_axis_arrow.remove()
    qvr_spin_axis_arrow = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='blue', normalize=True, label='Spin axis')
    # Rotate light arrow
    vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_initial)
    rot_matrix_spin_axis_arrow_rotated = Rotation.from_rotvec(theta_rad_light_arrow_anim *
                                                              vector_rotated_spin_axis_arrow_z)
    vector_rotated_light_arrow = rot_matrix_spin_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
    qvr_light_arrow.remove()
    x1, y1, z1 = 0., 0., 0.
    u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
    qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='darkorange', normalize=True,
                                 label='Light arrow)')
    # Projection
    if vector_rotated_light_arrow[2] != 0.:
        slope_x_z = vector_rotated_light_arrow[0] / vector_rotated_light_arrow[2]
        slope_y_z = vector_rotated_light_arrow[1] / vector_rotated_light_arrow[2]
        line_projection.set_data_3d([0., slope_x_z], [0., slope_y_z], [0., 1.])
        c_upper_guide.remove()
        r = np.sqrt(slope_x_z ** 2. + slope_y_z ** 2.)
        c_upper_guide = Circle((0., 0.), r, ec='green', fill=False, linewidth=1, linestyle='--')
        ax0.add_patch(c_upper_guide)
        art3d.pathpatch_2d_to_3d(c_upper_guide, z=1, zdir='z')
        line_light_arrow_projection.set_data_3d([x_min * 10., x_max * 10.], [r, r], [1., 1.])
        theta_xy_rad_spin_axis = np.arctan2(u0, v0)
        projection_point = r * np.tan(theta_xy_rad_spin_axis)
        line_spin_axis_projection.set_data_3d([projection_point, 0.], [r, 0.], [1., 1.])
    c_projection_dot.remove()
    c_projection_dot = Circle((projection_point, r), 0.05, color='blue', ec='blue', linestyle='-')
    ax0.add_patch(c_projection_dot)
    art3d.pathpatch_2d_to_3d(c_projection_dot, z=1, zdir='z')
    c_projection_dot_center.remove()
    c_projection_dot_center = Circle((projection_point, 0.), 0.05, color='red', ec='red', linestyle='-')
    ax0.add_patch(c_projection_dot_center)
    art3d.pathpatch_2d_to_3d(c_projection_dot_center, z=1, zdir='z')
    if projection_point > 0:
        projection_point_sqrt = np.sqrt(projection_point)
    else:
        projection_point_sqrt = 0.
    c_projection_dot_parabola.remove()
    c_projection_dot_parabola = Circle((projection_point, projection_point_sqrt), 0.05, color='magenta',
                                       ec='magenta', linestyle='-')
    ax0.add_patch(c_projection_dot_parabola)
    art3d.pathpatch_2d_to_3d(c_projection_dot_parabola, z=1, zdir='z')
    line_projection_p.set_data_3d([projection_point, projection_point], [r, 0.], [1., 1.])
    # ax1
    c_projection_dot_ax1.set_center((projection_point, r))
    c_projection_dot_center_ax1.set_center((projection_point, 0.))
    c_projection_dot_parabola_ax1.set_center((projection_point, projection_point_sqrt))
    if projection_point < 0.000001:
        diff_ratios_x = []
        diff_ratios_y = []
        pass_projection_x = []
        pass_projection_y = []
    else:
        diff_ratios_x.append(projection_point)
        diff_ratios_y.append(r / np.sqrt(projection_point))
        pass_projection_x.append(projection_point)
        pass_projection_y.append(r)
    plt_diff_ratio.set_data(diff_ratios_x, diff_ratios_y)
    plt_pass_projection.set_data(pass_projection_x, pass_projection_y)
    plt_projection_line_ax1.set_data([projection_point, projection_point], [projection_point_sqrt, 0.])


def reset():
    global is_play, cnt
    global theta_rad_spin_axis_arrow_anim, theta_rad_light_arrow_anim
    is_play = False
    cnt = 0
    theta_rad_light_arrow_anim = 0.
    theta_rad_spin_axis_arrow_anim = 0.
    update_diagram()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True


def update(f):
    global cnt
    global theta_rad_spin_axis_arrow_anim, theta_rad_light_arrow_anim
    txt_step.set_text("Step=" + str(cnt))
    txt_spin.set_text("Light arrow" + str(rot_light_arrow) + ", Spin axis arrow" + str(rot_spin_axis_arrow))
    if is_play:
        update_diagram()
        # Change theta
        theta_rad_spin_axis_arrow_anim = theta_rad_spin_axis_arrow_anim - rot_spin_axis_arrow * ((2. * np.pi) / 360)
        theta_rad_light_arrow_anim = theta_rad_light_arrow_anim + rot_light_arrow * ((2. * np.pi) / 360)
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
vector_spin_axis_arrow_initial = np.array([0., 1., 0.])
vector_light_arrow_initial = np.array([0., 0., 1.])

theta_rad_spin_axis_arrow = 0.
theta_rad_light_arrow = 0.
theta_rad_spin_axis_arrow_anim = 0.
theta_rad_light_arrow_anim = 0.

rot_spin_axis_arrow = 1
rot_light_arrow = 1

tilt_angle_deg = 0.

r_spin_axis_guide = 0.
h_spin_axis_guide = 0.

# Generate figure and axes
title_ax0 = "Projection of double rotation in 3D (Spin) with tilt and rotation-speed control"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max
z_min = range_z_min
z_max = range_z_max

fig = Figure()
ax0 = fig.add_subplot(121, projection='3d')
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_zlabel('z')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

ax1 = fig.add_subplot(122)
ax1.set_title("Parabola and projection")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_xlim(x_min, 16.)
ax1.set_ylim(y_min, 8.)
ax1.set_aspect("equal")
ax1.grid()

# Generate items
txt_step = ax0.text2D(x_min, y_max, "Step=" + str(0))
xz, yz, _ = proj3d.proj_transform(x_min, y_max, z_max, ax0.get_proj())
txt_step.set_position((xz, yz))
txt_spin = ax0.text2D(x_min, y_max, "Light arrow" + str(rot_light_arrow) + ", Spin axis arrow" +
                      str(rot_spin_axis_arrow), fontsize=12)
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
                                 np.array(z_light_arrow_pass), color='gold', linewidth=2, linestyle='-')

# Guide circle
angle_light_circle = np.arange(0., 365., 6.)
x_light_circle = np.cos(angle_light_circle * np.pi / 180.)
z_light_circle = np.sin(angle_light_circle * np.pi / 180.)
y_light_circle = angle_light_circle * 0.
plt_light_circle, = ax0.plot(x_light_circle, y_light_circle, z_light_circle, linewidth=2, linestyle=':',
                             c='darkorange')

# Guide circle spin arrow
c_spin_axis_guide = Circle((0., 0.), 1., ec='blue', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(c_spin_axis_guide)
art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=0., zdir='z')

# Spin axis arrow
x0_, y0_, z0_ = 0., 0., 0.
u0_, v0_, w0_ = vector_spin_axis_arrow_initial[0], vector_spin_axis_arrow_initial[1], vector_spin_axis_arrow_initial[2]
qvr_spin_axis_arrow = ax0.quiver(x0_, y0_, z0_, u0_, v0_, w0_, length=1, color='blue', normalize=True,
                                 label='Spin axis arrow')

# Light arrow
x1_, y1_, z1_ = 0., 0., 0.
u1_, v1_, w1_ = vector_light_arrow_initial[0], vector_light_arrow_initial[1], vector_light_arrow_initial[2]
qvr_light_arrow = ax0.quiver(x1_, y1_, z1_, u1_, v1_, w1_, length=1, color='red', normalize=True,
                             label='Light arrow)')

# Projection guide line and circle
line_projection = art3d.Line3D([0., 0.], [0., 0.], [0., 1.], linewidth=0.5, color='darkorange', ls='--')
ax0.add_line(line_projection)

c_upper_guide = Circle((0., 0.), 0, ec='green', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(c_upper_guide)
art3d.pathpatch_2d_to_3d(c_upper_guide, z=1, zdir='z')

line_upper0_radius = art3d.Line3D([0., 0.], [0., 0.], [0., 0.], linewidth=0.5, color='green', ls='-.')
ax0.add_line(line_upper0_radius)

line_light_arrow_projection = art3d.Line3D([x_min * 10., x_max * 10.], [0., 0.], [1., 1.], linewidth=0.5,
                                           color='green', ls='--')
ax0.add_line(line_light_arrow_projection)

line_spin_axis_projection = art3d.Line3D([0., 0.], [0., 0.], [1., 1.], linewidth=0.5, color='blue', ls='--')
ax0.add_line(line_spin_axis_projection)

c_projection_dot = Circle((0., 0.), 0.05, color='blue', ec='blue', linestyle='-')
ax0.add_patch(c_projection_dot)
art3d.pathpatch_2d_to_3d(c_projection_dot, z=1, zdir='z')

c_projection_dot_center = Circle((0., 0.), 0.05, color='red', ec='red', linestyle='-')
ax0.add_patch(c_projection_dot_center)
art3d.pathpatch_2d_to_3d(c_projection_dot_center, z=1, zdir='z')

line_projection_p = art3d.Line3D([0., 0.], [0., 0.], [1., 1.], linewidth=0.5, color='magenta', ls='--')
ax0.add_line(line_projection_p)

c_projection_dot_parabola = Circle((0., 0.), 0.05, color='magenta', ec='magenta', linestyle='-')
ax0.add_patch(c_projection_dot_parabola)
art3d.pathpatch_2d_to_3d(c_projection_dot_parabola, z=1, zdir='z')

# Parabola
y_parabola = np.arange(x_min, x_max, 0.01)
z_parabola = y_parabola * 0. + 1.
x_parabola = y_parabola ** 2.
parabola = art3d.Line3D(x_parabola, y_parabola, z_parabola, color='magenta', ls='--', linewidth=1)
ax0.add_line(parabola)

line_parabola_center = art3d.Line3D([x_min * 10., x_max * 10.], [0., 0.], [1., 1.], linewidth=0.5, color='red', ls='-.')
ax0.add_line(line_parabola_center)

# Comparison of parabola and projection  (ax1 items)
# Parabola
y_parabola_ax1 = np.arange(- 4., 8., 0.1)
x_parabola_ax1 = y_parabola_ax1 ** 2.
plt_parabola_ax1, = ax1.plot(x_parabola_ax1, y_parabola_ax1, linestyle='--', c='magenta', linewidth=0.5)

# Projection dot
c_projection_dot_ax1 = Circle((0., 0.), 0.05, color='blue', ec='blue', linestyle='-')
ax1.add_patch(c_projection_dot_ax1)
c_projection_dot_parabola_ax1 = Circle((0., 0.), 0.05, color='magenta', ec='magenta', linestyle='-')
ax1.add_patch(c_projection_dot_parabola_ax1)
c_projection_dot_center_ax1 = Circle((0., 0.), 0.05, color='red', ec='red', linestyle='-')
ax1.add_patch(c_projection_dot_center_ax1)

# Projection line
plt_projection_line_ax1, = ax1.plot([0., 0.], [0., 0], linestyle='--', c='magenta', linewidth=0.5)

# Diff ratio projection and parabola
diff_ratios_x = []
diff_ratios_y = []
plt_diff_ratio, = ax1.plot(diff_ratios_x, diff_ratios_y, linestyle='-', label='Ratio(projection point / parabola')

# Pass of projection
pass_projection_x = []
pass_projection_y = []
plt_pass_projection, = ax1.plot(pass_projection_x, pass_projection_x, linestyle='-', label='Projection point', c='blue')

ax1.legend(prop={"size": 8}, loc="lower right")

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
# Rotation speed
frm_spin = ttk.Labelframe(root, relief='ridge', text='Rotation speed', labelanchor='n')
frm_spin.pack(side='left', fill=tk.Y)
lbl_spin_s = tk.Label(frm_spin, text='Spin axis (blue arrow):')
lbl_spin_s.pack(side='left')
var_spin_s = tk.StringVar(root)  # variable for spinbox-value
var_spin_s.set(rot_spin_axis_arrow)  # Initial value
spn_spin_s = tk.Spinbox(
    frm_spin, textvariable=var_spin_s, from_=-8, to=8, increment=1,
    command=lambda: set_spin_s(var_spin_s.get()), width=6
)
spn_spin_s.pack(side='left')
lbl_spin_l = tk.Label(frm_spin, text='Light arrow (Orange arrow):')
lbl_spin_l.pack(side='left')
var_spin_l = tk.StringVar(root)  # variable for spinbox-value
var_spin_l.set(rot_light_arrow)  # Initial value
spn_spin_l = tk.Spinbox(
    frm_spin, textvariable=var_spin_l, from_=-8, to=8, increment=1,
    command=lambda: set_spin_l(var_spin_l.get()), width=6
)
spn_spin_l.pack(side='left')

# Tilt of rotation axis
frm_tilt = ttk.Labelframe(root, relief='ridge', text='Tilt', labelanchor='n')
frm_tilt.pack(side='left', fill=tk.Y)
lbl_tilt = tk.Label(frm_tilt, text='Angle(degree):')
lbl_tilt.pack(side='left')
var_tilt = tk.StringVar(root)  # variable for spinbox-value
var_tilt.set(tilt_angle_deg)  # Initial value
spn_tilt = tk.Spinbox(
    frm_tilt, textvariable=var_tilt, from_=0., to=180., increment=1,
    command=lambda: set_tilt(var_tilt.get()), width=6
)
spn_tilt.pack(side='left')

# Draw initial diagram
update_diagram()
draw_pass_spin()

# main loop
anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
root.mainloop()
