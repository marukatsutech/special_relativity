""" Electric charges interaction model """
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk
from matplotlib.patches import Circle
from scipy.spatial.transform import Rotation
import mpl_toolkits.mplot3d.art3d as art3d

""" Global variables """
step_rotate = 2
counter_rotate_x = 0
counter_rotate_y = 0
counter_rotate_z = 0

""" Animation control """
is_play = True
is_rotate_x = False
is_rotate_y = False
is_rotate_z = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Other parameters """
theta_init_deg, phi_init_deg = 0., 0.
rot_velocity_x, rot_velocity_y, rot_velocity_z = 1., 1., 1.

""" Create figure and axes """
title_ax0 = "Electric charges interaction model"
title_tk = title_ax0

x_min = -2.
x_max = 2.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.

fig = Figure()
ax0 = fig.add_subplot(111, projection='3d')
ax0.set_box_aspect((1, 1, 1))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("A")
ax0.set_ylabel("B")
ax0.set_zlabel("C")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_zlim(z_min, z_max)

""" Embed in Tkinter """
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill="both")

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

""" Global objects of Tkinter """
var_turn_op = tk.IntVar()

""" Classes and functions """


def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi


def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z


class Arrow3d:
    def __init__(self, ax, x, y, z, is_normalize, length, theta, phi, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.is_normalize = is_normalize
        self.r = length
        self.theta_init = theta
        self.phi_init = phi
        self.color = color
        self.line_width = line_width
        self.line_style = line_style
        self.label = label

        self.u, self.v, self.w = spherical_to_cartesian(self.r, self.theta_init, self.phi_init)

        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize, linewidth=self.line_width,
                                      linestyle=self.line_style)

        self.vector_init = np.array([self.u, self.v, self.w])

    def _update_quiver(self):
        self.qvr.remove()
        if self.label != "":
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize,
                                      linewidth=self.line_width, linestyle=self.line_style, label=self.label)
        else:
            self.qvr = self.ax.quiver(self.x, self.y, self.z, self.u, self.v, self.w,
                                      length=1, color=self.color, normalize=self.is_normalize,
                                      linewidth=self.line_width,
                                      linestyle=self.line_style)

    def rotate(self, angle, rotation_axis):
        rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        vector_rotated = rot_matrix.apply(self.vector_init)
        self.u, self.v, self.w = vector_rotated[0], vector_rotated[1], vector_rotated[2]
        self._update_quiver()
        self.vector_init = vector_rotated

    def set_direction(self, theta, phi):
        self.u, self.v, self.w = spherical_to_cartesian(self.r, theta, phi)
        self._update_quiver()

    def set_vector(self, u, v, w):
        self.u, self.v, self.w = u, v, w
        self._update_quiver()

    def set_theta_initial(self, theta):
        self.theta_init = theta
        self.u, self.v, self.w = spherical_to_cartesian(self.r, self.theta_init, self.phi_init)
        self.vector_init = np.array([self.u, self.v, self.w])
        self._update_quiver()

    def set_phi_initial(self, phi):
        self.phi_init = phi
        self.u, self.v, self.w = spherical_to_cartesian(self.r, self.theta_init, self.phi_init)
        self.vector_init = np.array([self.u, self.v, self.w])
        self._update_quiver()

    def get_vector(self):
        return np.array([self.u, self.v, self.w])


def create_center_lines():
    line_axis_z = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="blue", ls="-.", linewidth=1)
    ax0.add_line(line_axis_z)
    line_axis_y = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="red", ls="-.", linewidth=1)
    ax0.add_line(line_axis_y)
    line_axis_z = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="green", ls="-.", linewidth=1)
    ax0.add_line(line_axis_z)


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")


def set_theta_initial(theta):
    arrow_init.set_theta_initial(np.deg2rad(theta))
    arrow.set_theta_initial(np.deg2rad(theta))


def set_phi_initial(phi):
    arrow_init.set_phi_initial(np.deg2rad(phi))
    arrow.set_phi_initial(np.deg2rad(phi))


def set_vx(velocity):
    global rot_velocity_x
    rot_velocity_x = velocity


def set_vy(velocity):
    global rot_velocity_y
    rot_velocity_y = velocity


def set_vz(velocity):
    global rot_velocity_z
    rot_velocity_z = velocity


def switch_is_rotate_x():
    global is_rotate_x
    is_rotate_x = not is_rotate_x


def switch_is_rotate_y():
    global is_rotate_y
    is_rotate_y = not is_rotate_y


def switch_is_rotate_z():
    global is_rotate_z
    is_rotate_z = not is_rotate_z


def create_parameter_setter():
    global var_turn_op
    frm_dir = ttk.Labelframe(root, relief="ridge", text="Initial direction", labelanchor='n')
    frm_dir.pack(side='left', fill=tk.Y)

    lbl_theta = tk.Label(frm_dir, text="Theta")
    lbl_theta.pack(side="left")

    var_theta = tk.StringVar(root)
    var_theta.set(str(theta_init_deg))
    spn_theta = tk.Spinbox(
        frm_dir, textvariable=var_theta, format="%.0f", from_=-360, to=360, increment=1,
        command=lambda: set_theta_initial(float(var_theta.get())), width=5
    )
    spn_theta.pack(side="left")

    lbl_phi = tk.Label(frm_dir, text="Phi")
    lbl_phi.pack(side="left")

    var_phi = tk.StringVar(root)
    var_phi.set(str(phi_init_deg))
    spn_phi = tk.Spinbox(
        frm_dir, textvariable=var_phi, format="%.0f", from_=-360, to=360, increment=1,
        command=lambda: set_phi_initial(float(var_phi.get())), width=5
    )
    spn_phi.pack(side="left")

    frm_rot = ttk.Labelframe(root, relief="ridge", text="Rotation", labelanchor='n')
    frm_rot.pack(side='left', fill=tk.Y)

    btn_rot_x_cw = tk.Button(frm_rot, text="A-axis (+180 deg)", command=lambda: switch_is_rotate_x())
    btn_rot_x_cw.pack(side='left')

    btn_rot_y_cw = tk.Button(frm_rot, text="B-axis (+180 deg)", command=lambda: switch_is_rotate_y())
    btn_rot_y_cw.pack(side='left')

    btn_rot_z_cw = tk.Button(frm_rot, text="C-axis (+180 deg)", command=lambda: switch_is_rotate_z())
    btn_rot_z_cw.pack(side='left')


def create_circle(ax, x, y, z, z_dir, edge_col, fill_flag, line_width, line_style, label):
    if label != "":
        c_spin_axis_guide = Circle((x, y), 1., ec=edge_col, fill=fill_flag,
                                   linewidth=line_width, linestyle=line_style, label=label)
    else:
        c_spin_axis_guide = Circle((x, y), 1., ec=edge_col, fill=fill_flag,
                                   linewidth=line_width, linestyle=line_style)
    ax.add_patch(c_spin_axis_guide)
    art3d.pathpatch_2d_to_3d(c_spin_axis_guide, z=z, zdir=z_dir)


def draw_static_diagrams():
    create_center_lines()
    """
    create_circle(ax0, 0., 0., 0., "x", "gray", False, 0.5,
                  "--", "Light-sphere")
    create_circle(ax0, 0., 0., 0., "y", "gray", False, 0.5,
                  "--", "")
    create_circle(ax0, 0., 0., 0., "z", "gray", False, 0.5,
                  "--", "")
    """


def update_arrow():
    global counter_rotate_x, counter_rotate_y, counter_rotate_z
    global is_rotate_x, is_rotate_y, is_rotate_z

    if is_rotate_x:
        arrow.rotate(np.deg2rad(step_rotate), vector_x_axis)
        counter_rotate_x += step_rotate
        if counter_rotate_x == 180:
            is_rotate_x = False
            counter_rotate_x = 0

    if is_rotate_y:
        arrow.rotate(np.deg2rad(step_rotate), vector_y_axis)
        counter_rotate_y += step_rotate
        if counter_rotate_y == 180:
            is_rotate_y = False
            counter_rotate_y = 0

    if is_rotate_z:
        arrow.rotate(np.deg2rad(step_rotate), vector_z_axis)
        counter_rotate_z += step_rotate
        if counter_rotate_z == 180:
            is_rotate_z = False
            counter_rotate_z = 0


def update_diagrams():
    global circle_x, circle_y, circle_z

    vector_arrow = arrow.get_vector()

    new_r_x = np.sqrt(float(vector_arrow[1]) ** 2 + float(vector_arrow[2]) ** 2)
    new_z_x = float(vector_arrow[0])
    circle_x.remove()
    circle_x = Circle((0., 0.), new_r_x, ec="red", fill=False, linewidth=0.5, linestyle="-")
    ax0.add_patch(circle_x)
    art3d.pathpatch_2d_to_3d(circle_x, z=new_z_x, zdir="x")

    new_r_y = np.sqrt(float(vector_arrow[0]) ** 2 + float(vector_arrow[2]) ** 2)
    new_z_y = float(vector_arrow[1])
    circle_y.remove()
    circle_y = Circle((0., 0.), new_r_y, ec="green", fill=False, linewidth=0.5, linestyle="-")
    ax0.add_patch(circle_y)
    art3d.pathpatch_2d_to_3d(circle_y, z=new_z_y, zdir="y")

    new_r_z = np.sqrt(float(vector_arrow[0]) ** 2 + float(vector_arrow[1]) ** 2)
    new_z_z = float(vector_arrow[2])
    circle_z.remove()
    circle_z = Circle((0., 0.), new_r_z, ec="blue", fill=False, linewidth=0.5, linestyle="-")
    ax0.add_patch(circle_z)
    art3d.pathpatch_2d_to_3d(circle_z, z=new_z_z, zdir="z")

    update_arrow()


def reset():
    global is_play
    is_play = False
    # cnt.reset()
    update_diagrams()


def switch():
    global is_play
    is_play = not is_play


def update(f):
    if is_play:
        # cnt.count_up()
        update_diagrams()


""" main loop """
if __name__ == "__main__":
    draw_static_diagrams()

    arrow_init = Arrow3d(ax0, 0., 0., 0., True, 1.,
                         np.deg2rad(theta_init_deg), np.deg2rad(phi_init_deg),
                         "gray", 2, "-", "Arrow")

    arrow = Arrow3d(ax0, 0., 0., 0., True, 1.,
                    np.deg2rad(theta_init_deg), np.deg2rad(phi_init_deg),
                    "black", 2, "-", "Arrow")

    circle_x = Circle((0., 0.), 0., ec="red", fill=False, linewidth=0.5, linestyle="-")
    ax0.add_patch(circle_x)
    art3d.pathpatch_2d_to_3d(circle_x, z=0, zdir="x")

    circle_y = Circle((0., 0.), 0., ec="green", fill=False, linewidth=0.5, linestyle="-")
    ax0.add_patch(circle_y)
    art3d.pathpatch_2d_to_3d(circle_y, z=0, zdir="y")

    circle_z = Circle((0., 0.), 0., ec="blue", fill=False, linewidth=0.5, linestyle="-")
    ax0.add_patch(circle_z)
    art3d.pathpatch_2d_to_3d(circle_z, z=0, zdir="z")

    # create_animation_control()
    create_parameter_setter()

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()
