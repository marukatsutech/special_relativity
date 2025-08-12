""" Spinor """
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

from matplotlib.colors import Normalize

""" Global variables """
vector_spin_axis_arrow_initial = np.array([0., 1., 0.])
vector_light_arrow_initial = np.array([0., 0., 1.])

theta_rad_spin_axis_arrow = 0.
theta_rad_light_arrow = 0.
theta_rad_spin_axis_arrow_anim = 0.
theta_rad_light_arrow_anim = 0.

rot_spin_axis_arrow = 1
rot_light_arrow = 1

tilt_angle_deg = - 70.

r_spin_axis_guide = 0.
h_spin_axis_guide = 0.

""" Animation control """
is_play = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Create figure and axes """
title_tk = "Spinor"
title_ax0 = title_tk

x_min = -2.
x_max = 2.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.

fig = Figure()
ax0 = fig.add_subplot(111, projection="3d")
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("y")
ax0.set_zlabel("z")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

# ax0.set_facecolor("black")
# ax0.axis('off')

x_min = -2.
x_max = 2.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.


""" Embed in Tkinter """
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill="both")

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

""" Global objects of Tkinter """
var_num_points = tk.StringVar(root)
var_theta_s2_deg = tk.StringVar(root)
var_turn = tk.StringVar(root)

""" Classes and functions """


class Counter:
    def __init__(self, is3d=None, ax=None, xy=None, z=None, label=""):
        self.is3d = is3d if is3d is not None else False
        self.ax = ax
        self.x, self.y = xy[0], xy[1]
        self.z = z if z is not None else 0
        self.label = label

        self.count = 0

        if not is3d:
            self.txt_step = self.ax.text(self.x, self.y, self.label + str(self.count))
        else:
            self.txt_step = self.ax.text2D(self.x, self.y, self.label + str(self.count))
            self.xz, self.yz, _ = proj3d.proj_transform(self.x, self.y, self.z, self.ax.get_proj())
            self.txt_step.set_position((self.xz, self.yz))

    def count_up(self):
        self.count += 1
        self.txt_step.set_text(self.label + str(self.count))

    def reset(self):
        self.count = 0
        self.txt_step.set_text(self.label + str(self.count))

    def get(self):
        return self.count


class Scatter3D:
    def __init__(self, ax, size_scat, cmap_scat, norm_vmin, norm_vmax):
        self.ax = ax
        self.size_scat = size_scat
        self.cmap_scat = cmap_scat
        self.norm = Normalize(vmin=norm_vmin, vmax=norm_vmax)

        self.points = [(0, 0, 0)]   # Dummy
        self.magnitude = [0]

        xs, ys, zs = zip(*self.points)
        self.scat_data = ax0.scatter(xs, ys, zs, c=self.magnitude, cmap=self.cmap_scat, s=self.size_scat, norm=self.norm)

    def append(self, x, y, z, value):
        self.points.append((x, y, z))
        self.magnitude.append(value)

        xs, ys, zs = zip(*self.points[1:])
        self.scat_data.remove()
        self.scat_data = ax0.scatter(xs, ys, zs, c=self.magnitude[1:], cmap=self.cmap_scat, s=self.size_scat, norm=self.norm)

    def clear_scatter(self):
        self.points = [(0, 0, 0)]  # Dummy
        self.magnitude = [0]

        xs, ys, zs = zip(*self.points)
        self.scat_data.remove()
        self.scat_data = ax0.scatter(xs, ys, zs, c=self.magnitude, cmap=self.cmap_scat, s=self.size_scat, norm=self.norm)

    def set_cmap(self, value):
        self.cmap_scat = value

    def set_size(self, value):
        self.size_scat = value


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
    rot_spin_axis_arrow = float(value)
    reset()
    update_diagram()
    draw_pass_spin()


def set_spin_l(value):
    global rot_light_arrow
    rot_light_arrow = float(value)
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
    (u0, v0, w0) = (vector_rotated_spin_axis_arrow_z[0], vector_rotated_spin_axis_arrow_z[1],
                    vector_rotated_spin_axis_arrow_z[2])
    qvr_spin_axis_arrow.remove()
    qvr_spin_axis_arrow = ax0.quiver(x0, y0, z0, u0, v0, w0, length=1, color='gray', normalize=True, label='Spin axis')
    # Rotate light arrow
    vector_rotated_light_arrow_z = rot_matrix_z.apply(vector_light_arrow_initial)
    rot_matrix_spin_axis_arrow_rotated = Rotation.from_rotvec(theta_rad_light_arrow_anim *
                                                              vector_rotated_spin_axis_arrow_z)
    vector_rotated_light_arrow = rot_matrix_spin_axis_arrow_rotated.apply(vector_rotated_light_arrow_z)
    qvr_light_arrow.remove()
    x1, y1, z1 = 0., 0., 0.
    u1, v1, w1 = vector_rotated_light_arrow[0], vector_rotated_light_arrow[1], vector_rotated_light_arrow[2]
    qvr_light_arrow = ax0.quiver(x1, y1, z1, u1, v1, w1, length=1, color='red', normalize=True,
                                 label='Light arrow)')

    magnitude_phase = (np.cos(theta_rad_spin_axis_arrow_anim) + 1) / 2.
    scatter_internal_phase.append(vector_rotated_light_arrow[0], vector_rotated_light_arrow[1],
                                  vector_rotated_light_arrow[2], magnitude_phase)


def create_parameter_setter():
    # Parameter setting
    # Rotation speed
    frm_spin = ttk.Labelframe(root, relief='ridge', text='Rotation speed', labelanchor='n')
    frm_spin.pack(side='left', fill=tk.Y)
    lbl_spin_s = tk.Label(frm_spin, text='Spin axis (blue arrow):')
    lbl_spin_s.pack(side='left')
    var_spin_s = tk.StringVar(root)  # variable for spinbox-value
    var_spin_s.set(str(rot_spin_axis_arrow))  # Initial value
    spn_spin_s = tk.Spinbox(
        frm_spin, textvariable=var_spin_s, from_=-8, to=8, increment=1,
        command=lambda: set_spin_s(var_spin_s.get()), width=6
    )
    spn_spin_s.pack(side='left')
    lbl_spin_l = tk.Label(frm_spin, text='Light arrow (Orange arrow):')
    lbl_spin_l.pack(side='left')
    var_spin_l = tk.StringVar(root)  # variable for spinbox-value
    var_spin_l.set(str(rot_light_arrow))  # Initial value
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
    var_tilt = tk.StringVar(root)
    var_tilt.set(str(tilt_angle_deg))
    spn_tilt = tk.Spinbox(
        frm_tilt, textvariable=var_tilt, from_=-180., to=180., increment=1,
        command=lambda: set_tilt(var_tilt.get()), width=6
    )
    spn_tilt.pack(side='left')


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")
    btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: scatter_internal_phase.clear_scatter())
    btn_clear.pack(side="left")


def create_center_lines():
    ln_axis_x = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_x)
    ln_axis_y = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_y)
    ln_axis_z = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_z)


def draw_static_diagrams():
    create_center_lines()


def reset():
    global is_play
    global theta_rad_spin_axis_arrow_anim, theta_rad_light_arrow_anim
    if is_play:
        is_play = not is_play
    cnt.reset()
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
    global theta_rad_spin_axis_arrow_anim, theta_rad_light_arrow_anim
    if is_play:
        cnt.count_up()
        update_diagram()
        # Change theta
        theta_rad_spin_axis_arrow_anim = theta_rad_spin_axis_arrow_anim - rot_spin_axis_arrow * ((2. * np.pi) / 360)
        theta_rad_light_arrow_anim = theta_rad_light_arrow_anim + rot_light_arrow * ((2. * np.pi) / 360)


""" main loop """
if __name__ == "__main__":
    cnt = Counter(ax=ax0, is3d=True, xy=np.array([x_min, y_max]), z=z_max, label="Step=")
    draw_static_diagrams()
    create_animation_control()
    create_parameter_setter()

    # Spin pass
    x_light_arrow_pass = []
    y_light_arrow_pass = []
    z_light_arrow_pass = []
    plt_light_arrow_pass, = ax0.plot(np.array(x_light_arrow_pass), np.array(y_light_arrow_pass),
                                     np.array(z_light_arrow_pass), color='gray', linewidth=1, linestyle='-')

    # Guide circle
    angle_light_circle = np.arange(0., 365., 6.)
    x_light_circle = np.cos(angle_light_circle * np.pi / 180.)
    z_light_circle = np.sin(angle_light_circle * np.pi / 180.)
    y_light_circle = angle_light_circle * 0.
    plt_light_circle, = ax0.plot(x_light_circle, y_light_circle, z_light_circle, linewidth=0.5, linestyle='--',
                                 c='red')

    # Guide circle spin arrow
    c_spin_axis_guide = Circle((0., 0.), 1., ec='gray', fill=False, linewidth=0.5, linestyle='--')
    ax0.add_patch(c_spin_axis_guide)
    art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=0., zdir='z')

    # Spin axis arrow
    x0_, y0_, z0_ = 0., 0., 0.
    u0_, v0_, w0_ = vector_spin_axis_arrow_initial[0], vector_spin_axis_arrow_initial[1], vector_spin_axis_arrow_initial[2]
    qvr_spin_axis_arrow = ax0.quiver(x0_, y0_, z0_, u0_, v0_, w0_, length=1, color='gray', normalize=True,
                                     label='Spin axis arrow')

    # Light arrow
    x1_, y1_, z1_ = 0., 0., 0.
    u1_, v1_, w1_ = vector_light_arrow_initial[0], vector_light_arrow_initial[1], vector_light_arrow_initial[2]
    qvr_light_arrow = ax0.quiver(x1_, y1_, z1_, u1_, v1_, w1_, length=1, color='orange', normalize=True,
                                 label='Light arrow)')

    scatter_internal_phase = Scatter3D(ax0, 8, "plasma", 0, 1)

    set_tilt(tilt_angle_deg)
    update_diagram()
    draw_pass_spin()

    # ax0.legend(loc='lower right', fontsize=8)

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
