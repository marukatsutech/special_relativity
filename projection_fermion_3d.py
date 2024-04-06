# Projection of fermion in 3D
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
    global theta0, qvr_phase0, theta1, qvr_phase1
    global c_upper0_guide, line_phase0_guide, line_phase1_guide
    global line_phase1_projection, line_phase1_projection_guide, projection_point
    global x0, y0, z0, u0, v0, w0
    global x1, y1, z1, u1, v1, w1
    # global x2, y2, z2, u2, v2, w2
    # global qvr_phase_composite
    # global x_phase_composite, y_phase_composite, z_phase_composite
    # global plt_composite_normalized, plt_composite_not_normalized, norm_phase_composite
    # Phase 0 (vertical)
    theta0_rad = theta0 * np.pi / 180.
    theta0_rad_offset = np.pi / 2 - theta0 * np.pi / 180.
    qvr_phase0.remove()
    x0, y0, z0 = 0., 0., 0.
    u0, v0, w0 = np.cos(theta0_rad_offset), 0., np.sin(theta0_rad_offset)
    qvr_phase0 = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='darkorange')
    line_phase0_guide.set_data_3d([np.cos(theta0_rad_offset), np.tan(theta0_rad)], [0., 0.],
                                  [np.sin(theta0_rad_offset), 1.])
    c_upper0_guide.remove()
    r = np.tan(theta0_rad)
    c_upper0_guide = Circle((0., 0.), r, ec='green', fill=False, linewidth=1, linestyle='--')
    ax0.add_patch(c_upper0_guide)
    art3d.pathpatch_2d_to_3d(c_upper0_guide, z=1, zdir='z')
    line_upper0_radius.set_data_3d([0., np.tan(theta0_rad)], [0., 0.], [1., 1.])
    # Phase 1 (horizontal)
    theta1 = theta0
    theta1_rad = theta1 * np.pi / 180.
    theta1_rad_offset = np.pi / 2 - theta1 * np.pi / 180.
    qvr_phase1.remove()
    x1, y1, z1 = 0., 0., 1.
    u1, v1, w1 = np.cos(theta1_rad_offset), np.sin(theta1_rad_offset), 0.
    qvr_phase1 = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='blue')
    projection_point = r * np.tan(theta1_rad)
    line_phase1_guide.set_data_3d([projection_point, 0.], [r, 0.],
                                  [1., 1.])
    line_phase1_projection.set_data_3d([x_min, x_max], [r, r], [1., 1.])
    line_phase1_projection_guide.set_data_3d([projection_point, projection_point], [r, 0.], [1., 1.])
    # Phase composite
    '''
    qvr_phase_composite.remove()
    x2, y2, z2 = 0., 0., 0.
    if var_composite.get():
        u2, v2, w2 = u0 + u1, v0 + v1, w0 + w1
        x_phase_composite = np.cos(np.pi / 2 - angle_phase_composite * np.pi / 180.) + \
                            np.cos(np.pi / 2 - angle_phase_composite * np.pi / 180.)
        y_phase_composite = np.sin(np.pi / 2 - angle_phase_composite * np.pi / 180.)
        z_phase_composite = np.sin(np.pi / 2 - angle_phase_composite * np.pi / 180.)
        norm_phase_composite = np.sqrt(x_phase_composite ** 2. + y_phase_composite ** 2. + y_phase_composite ** 2.)
    else:
        pass
        u2, v2, w2 = 0., 0., 0.
        x_phase_composite = angle_phase_composite * 0.
        y_phase_composite = angle_phase_composite * 0.
        z_phase_composite = angle_phase_composite * 0.
    qvr_phase_composite = ax0.quiver(x2, y2, z2, u2, v2, w2, length=1, color='darkorange', linewidths=0.5, normalize=True,
                                     label='composite vector(normalized)')
    plt_composite_normalized.set_xdata(x_phase_composite)
    plt_composite_normalized.set_ydata(y_phase_composite)
    plt_composite_normalized.set_3d_properties(z_phase_composite)
    plt_composite_not_normalized.set_xdata(x_phase_composite / norm_phase_composite)
    plt_composite_not_normalized.set_ydata(y_phase_composite / norm_phase_composite)
    plt_composite_not_normalized.set_3d_properties(z_phase_composite / norm_phase_composite)
    '''


def set_angle(value):
    global theta0
    theta0 = float(value)
    update_diagram()


def update(f):
    global txt_angle
    theta0_rad_offset = np.pi / 2 - theta0 * np.pi / 180.
    if np.sin(theta0_rad_offset) != 0:
        slope = np.cos(theta0_rad_offset) / np.sin(theta0_rad_offset)
        txt_angle.set_text('Angle(deg)=' + str(theta0) + ', slope=' + '{:.3f}'.format(slope) +
                           ', projection=' + '{:.3f}'.format(projection_point))
    else:
        txt_angle.set_text('Angle(deg)=' + str(theta0) + ', slope=infinity' + ', projection=infinity')


# Global variables

# Animation control

# Parameters
range_x_min = -5.
range_x_max = 5.
range_y_min = -5.
range_y_max = 5.
range_z_min = -2.
range_z_max = 4.

theta0 = 0.
theta1 = 0.
# step_rotation = 0.1

projection_point = 0.

# Generate figure and axes
title_ax0 = "Projection of double rotation in 3D"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max
z_min = range_z_min
z_max = range_z_max

fig = Figure()
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_box_aspect((10, 10, 6))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_zlabel('t')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

# Generate items
txt_angle = ax0.text2D(x_min, y_max, 'Angle(deg)=' + str(0) + ', slope=' + str(0) + ', projection=' + str(0))
xz, yz, _ = proj3d.proj_transform(x_min, y_max, z_max, ax0.get_proj())
txt_angle.set_position((xz, yz))

l_center_v = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color='gray', ls='-.', linewidth=0.5)
ax0.add_line(l_center_v)
l_center_h = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color='gray', ls='-.', linewidth=0.5)
ax0.add_line(l_center_h)
c_center = Circle((0., 0.), 1, ec='darkorange', fill=False)
ax0.add_patch(c_center)
art3d.pathpatch_2d_to_3d(c_center, z=0, zdir='y')

l_upper_y = art3d.Line3D([0., 0.], [y_min, y_max], [1., 1.], color='gray', ls='-.', linewidth=0.5)
ax0.add_line(l_upper_y)
l_upper_x = art3d.Line3D([x_min, x_max], [0., 0.], [1., 1.], color='gray', ls='-.', linewidth=0.5)
ax0.add_line(l_upper_x)
c_upper = Circle((0., 0.), 1, ec='blue', fill=False)
ax0.add_patch(c_upper)
art3d.pathpatch_2d_to_3d(c_upper, z=1, zdir='z')

# Phase 0 (vertical)
x0, y0, z0 = 0., 0., 0.
u0, v0, w0 = 0., 0., 1.
qvr_phase0 = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='darkorange')
line_phase0_guide = art3d.Line3D([0., 0.], [0., 0.], [1., 1.], linewidth=0.5, color='darkorange', ls='--')
ax0.add_line(line_phase0_guide)
# Projection of Phase 0 (vertical)
c_upper0_guide = Circle((0., 0.), 0, ec='green', fill=False, linewidth=0.5, linestyle='--')
ax0.add_patch(c_upper0_guide)
art3d.pathpatch_2d_to_3d(c_upper0_guide, z=1, zdir='z')
line_upper0_radius = art3d.Line3D([0., 0.], [0., 0.], [0., 0.], linewidth=0.5, color='green', ls='-.')
ax0.add_line(line_upper0_radius)

# Phase 1 (horizontal)
x1, y1, z1 = 0., 0., 1.
u1, v1, w1 = 0., 1., 0.
qvr_phase1 = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='blue')
line_phase1_guide = art3d.Line3D([0., 0.], [0., 0.], [0., 0.], linewidth=0.5, color='blue', ls='--')
ax0.add_line(line_phase1_guide)
line_phase1_projection = art3d.Line3D([x_min, x_max], [0., 0.], [1., 1.], linewidth=0.5, color='green', ls='--')
ax0.add_line(line_phase1_projection)

# Projection
line_phase1_projection_guide = art3d.Line3D([0., 0.], [0., 0.], [1., 1.], linewidth=1, color='magenta', ls='--')
ax0.add_line(line_phase1_projection_guide)

# Parabola
y_parabola = np.arange(x_min, x_max, 0.01)
z_parabola = y_parabola * 0. + 1.
x_parabola = y_parabola ** 2.
parabola = art3d.Line3D(x_parabola, y_parabola, z_parabola, color='magenta', ls='--', linewidth=1)
ax0.add_line(parabola)

# Phase composite
'''
x2, y2, z2 = 0., 0., 0.
u2, v2, w2 = u0 + u1, v0 + v1, w0 + w1
qvr_phase_composite = ax0.quiver(x2, y2, z2, u2, v2, w2, length=1, color='darkorange', linewidths=1, normalize=True,
                                 label='composite vector(normalized)')
angle_phase_composite = np.arange(0., 360., 0.01)
x_phase_composite = np.cos(np.pi / 2 - angle_phase_composite * np.pi / 180.) + \
                   np.cos(np.pi / 2 - angle_phase_composite * np.pi / 180.)
y_phase_composite = np.sin(np.pi / 2 - angle_phase_composite * np.pi / 180.)
z_phase_composite = np.sin(np.pi / 2 - angle_phase_composite * np.pi / 180.)
norm_phase_composite = np.sqrt(x_phase_composite ** 2. + y_phase_composite ** 2. + y_phase_composite ** 2.)
plt_composite_normalized, = ax0.plot(x_phase_composite, y_phase_composite, z_phase_composite, linewidth=1,
                                     linestyle=':', c='darkorange', label='Normalized')
plt_composite_not_normalized, = ax0.plot(x_phase_composite / norm_phase_composite,
                                         y_phase_composite / norm_phase_composite,
                                         z_phase_composite / norm_phase_composite, linewidth=1, linestyle='--',
                                         c='darkorange', label='Not normalized')

ax0.legend(loc='lower right')
'''
# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Parameter setting
frm_parameter = ttk.Labelframe(root, relief='ridge', text='Angle(degree)', labelanchor='n')
frm_parameter.pack(side='left', fill=tk.Y)
lbl_angle = tk.Label(frm_parameter, text='Theta0(blue):')
lbl_angle.pack()
var_angle = tk.StringVar(root)  # variable for spinbox-value
var_angle.set(0)  # Initial value
spn_angle = tk.Spinbox(
    frm_parameter, textvariable=var_angle, format='%.1f', from_=0., to=360., increment=1.,
    command=lambda: set_angle(var_angle.get()), width=6
    )
spn_angle.pack()

# Composite vector on/off
'''
frm_composite = ttk.Labelframe(root, relief='ridge', text='Composite vector', labelanchor='n')
frm_composite.pack(side='left', fill=tk.Y)
var_composite = tk.BooleanVar(root)    # Variable for checkbutton
var_composite.set(True)
chk_composite = tk.Checkbutton(frm_composite, text='Show', variable=var_composite, command=update_diagram)
chk_composite.pack()
'''
# main loop
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
