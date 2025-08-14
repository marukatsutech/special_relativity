""" Rotation vector pair """
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

""" Global variables """
phase_step_deg = 1.
phase_init_a = 180.
phase_init_b = 0.
offset_scale = 0.5
size_phase_circle = 1.

""" Animation control """
is_play = False
is_rotation_by_resultant = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Create figure and axes """
title_ax0 = "Rotation vector pair"
title_tk = title_ax0

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

""" Embed in Tkinter """
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill="both")

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

""" Global objects of Tkinter """
var_phase_step = tk.StringVar(root)
var_path = tk.IntVar(root)
var_phase_init_a = tk.StringVar(root)
var_phase_init_b = tk.StringVar(root)
var_rot_a_by_d = tk.IntVar(root)
var_rot_d_by_a = tk.IntVar(root)
var_size_circle = tk.StringVar(root)

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


class RotationVector:
    def __init__(self, ax, color):
        self.ax = ax
        self.color = color

        self.origin = np.array([0., 0., 0.])
        self.scale = 1.
        self.center = vector_x_axis
        self.phase_base_a = vector_y_axis
        self.phase_base_b = vector_z_axis
        self.arrow = self.scale * self.center
        self.phase = 0.
        self.phase_vector = np.array([0., 1., 0.])
        self.size_circle = 1.

        self.quiver_vector = self.ax.quiver(*self.origin, *self.arrow, length=1, linewidth=2,
                                            color=self.color, normalize=False)
        line_a = zip(self.origin, self.phase_base_a)
        self.plt_phase_base_a, = self.ax.plot(*line_a, linewidth=0.5, linestyle=":", color=self.color)

        line_b = zip(self.origin, self.phase_base_b)
        self.plt_phase_base_b, = self.ax.plot(*line_b, linewidth=0.5, linestyle=":", color=self.color)

        self.num_points_circle = 100
        self.theta = np.linspace(0., 2. * np.pi, self.num_points_circle)
        circle_points = np.array([
            (np.cos(t) * self.phase_base_a + np.sin(t) * self.phase_base_b) * self.size_circle
            for t in self.theta
        ])

        self.circle, = self.ax.plot(circle_points[:, 0], circle_points[:, 1], circle_points[:, 2],
                                    linewidth=1, linestyle="-", color=self.color)

        circle_points_r1 = np.array([
            (np.cos(t) * self.phase_base_a + np.sin(t) * self.phase_base_b)
            for t in self.theta
        ])

        self.circle_r1, = self.ax.plot(circle_points_r1[:, 0], circle_points_r1[:, 1], circle_points_r1[:, 2],
                                       linewidth=0.5, linestyle="--", color=self.color)

        line_p = zip(self.origin, self.phase_vector)
        self.plt_phase, = self.ax.plot(*line_p, linewidth=1, linestyle="--", color=self.color)
        u, v, w = self.phase_vector[0], self.phase_vector[1], self.phase_vector[2]
        self.marker_end, = self.ax.plot(u, v, w, marker="o", markersize=3, color=self.color)

    def update_diagrams(self):
        # All
        self.arrow = self.scale * self.center
        self.quiver_vector.remove()
        self.quiver_vector = self.ax.quiver(*self.origin, *self.arrow, length=1, linewidth=2,
                                            color=self.color, normalize=False)
        circle_points = np.array([
            (np.cos(t) * self.phase_base_a + np.sin(t) * self.phase_base_b) * self.size_circle
            for t in self.theta
        ])
        self.circle.set_data_3d(circle_points[:, 0] + self.origin[0], circle_points[:, 1] + self.origin[1],
                                circle_points[:, 2] + self.origin[2],)

        circle_points_r1 = np.array([
            (np.cos(t) * self.phase_base_a + np.sin(t) * self.phase_base_b)
            for t in self.theta
        ])
        self.circle_r1.set_data_3d(circle_points_r1[:, 0] + self.origin[0], circle_points_r1[:, 1] + self.origin[1],
                                   circle_points_r1[:, 2] + self.origin[2], )

        # Phase
        self.phase_vector = ((np.cos(self.phase) * self.phase_base_a + np.sin(self.phase) * self.phase_base_b) *
                             self.size_circle + self.origin)
        line_p = zip(self.origin, self.phase_vector)
        self.plt_phase.set_data_3d(*line_p)
        u, v, w = self.phase_vector[0], self.phase_vector[1], self.phase_vector[2]
        self.marker_end.set_data_3d([u], [v], [w])

    def rotate_phase(self, angle):
        self.phase += angle
        self.update_diagrams()

    def set_phase(self, angle):
        self.phase = angle
        self.update_diagrams()

    def set_orign(self, origin):
        self.origin = origin
        self.update_diagrams()

    def set_circle_size(self, value):
        self.size_circle = value
        self.update_diagrams()

    def rotate_all(self, angle, vector):
        rot_matrix = Rotation.from_rotvec(angle * vector)
        self.center = rot_matrix.apply(self.center)
        self.phase_base_a = rot_matrix.apply(self.phase_base_a)
        self.phase_base_b = rot_matrix.apply(self.phase_base_b)
        self.update_diagrams()

    def get_phase_vector(self):
        return self.phase_vector

    def get_center_vector(self):
        return self.center

    def get_origin(self):
        return self.origin

    def reset(self):
        self.origin = np.array([0., 0., 0.])
        self.scale = 1.
        self.center = vector_x_axis
        self.phase_base_a = vector_y_axis
        self.phase_base_b = vector_z_axis
        self.arrow = self.scale * self.center
        self.update_diagrams()


class Path:
    def __init__(self, ax, line_width, color):
        self.ax = ax
        self.line_width = line_width
        self.color = color

        self.is_draw_path = False

        self.x_path = []
        self.y_path = []
        self.z_path = []
        self.path, = self.ax.plot(np.array(self.x_path), np.array(self.y_path), np.array(self.z_path),
                                  color=self.color, linewidth=self.line_width)

    def append_path(self, position):
        if self.is_draw_path:
            self.x_path.append(position[0])
            self.y_path.append(position[1])
            self.z_path.append(position[2])
            self.update_path()

    def update_path(self):
        self.path.set_data_3d(np.array(self.x_path), np.array(self.y_path), np.array(self.z_path))

    def clear_path(self):
        self.x_path = []
        self.y_path = []
        self.z_path = []
        self.update_path()

    def set_is_draw_path(self, value):
        self.is_draw_path = value


def set_phase_step_deg(value):
    global phase_step_deg
    phase_step_deg = value


def set_is_path(value):
    path_a.set_is_draw_path(value)
    path_b.set_is_draw_path(value)


def clear_path():
    path_a.clear_path()
    path_b.clear_path()


def set_size_phase_circle(value):
    global size_phase_circle
    size_phase_circle = value
    rotation_vector_a.set_circle_size(size_phase_circle)
    rotation_vector_b.set_circle_size(size_phase_circle)

    orthogonal_vector = np.cross(rotation_vector_a.get_center_vector(), rotation_vector_b.get_center_vector())
    offset_vector = orthogonal_vector / np.linalg.norm(orthogonal_vector) / 2.
    new_origin_a = np.array([offset_vector[0] * size_phase_circle, offset_vector[1] * size_phase_circle,
                             offset_vector[2]])
    new_origin_b = np.array([- offset_vector[0] * size_phase_circle, - offset_vector[1] * size_phase_circle,
                             offset_vector[2]])
    rotation_vector_a.set_orign(new_origin_a)
    rotation_vector_b.set_orign(new_origin_b)

    rotation_vector_a.update_diagrams()
    rotation_vector_b.update_diagrams()

    # rotation_vector_a.set_orign(rotation_vector_b.get_phase_vector())
    # rotation_vector_b.set_orign(rotation_vector_a.get_phase_vector())


def create_parameter_setter():
    # phase_step
    frm_step = ttk.Labelframe(root, relief="ridge", text="Phase per step", labelanchor='n')
    frm_step.pack(side="left", fill=tk.Y)

    # var_phase_step = tk.StringVar(root)
    var_phase_step.set(str(phase_step_deg))
    spn_step = tk.Spinbox(
        frm_step, textvariable=var_phase_step, format="%.0f", from_=-360, to=360, increment=1,
        command=lambda: set_phase_step_deg(float(var_phase_step.get())), width=5
    )
    spn_step.pack(side="left")

    frm_path = ttk.Labelframe(root, relief="ridge", text="Paths", labelanchor="n")
    frm_path.pack(side='left', fill=tk.Y)
    # var_path = tk.IntVar(root)

    chk_path = tk.Checkbutton(frm_path, text="On", variable=var_path,
                              command=lambda: set_is_path(var_path.get()))
    chk_path.pack()
    var_path.set(False)

    # Initial phases
    frm_phase_init = ttk.Labelframe(root, relief="ridge", text="Initial phases", labelanchor='n')
    frm_phase_init.pack(side="left", fill=tk.Y)

    lbl_a = tk.Label(frm_phase_init, text="A")
    lbl_a.pack(side='left')
    # var_phase_init_a = tk.StringVar(root)
    var_phase_init_a.set(str(phase_init_a))
    spn_phase_init_a = tk.Spinbox(
        frm_phase_init, textvariable=var_phase_init_a, format="%.0f", from_=-360, to=360, increment=1,
        command=lambda: rotation_vector_a.set_phase(np.deg2rad(float(var_phase_init_a.get()))), width=5
    )
    spn_phase_init_a.pack(side="left")

    lbl_b = tk.Label(frm_phase_init, text="B")
    lbl_b.pack(side='left')
    # var_phase_init_b = tk.StringVar(root)
    var_phase_init_b.set(str(phase_init_a))
    spn_phase_init_b = tk.Spinbox(
        frm_phase_init, textvariable=var_phase_init_b, format="%.0f", from_=-360, to=360, increment=1,
        command=lambda: rotation_vector_b.set_phase(np.deg2rad(float(var_phase_init_b.get()))), width=5
    )
    spn_phase_init_b.pack(side="left")

    # Option of rotation
    frm_rot = ttk.Labelframe(root, relief="ridge", text="Rotation", labelanchor="n")
    frm_rot.pack(side='left', fill=tk.Y)

    # var_rot_a_by_d = tk.IntVar(root)
    chk_rot_a_by_d = tk.Checkbutton(frm_rot, text="Rotate A by D", variable=var_rot_a_by_d)
    chk_rot_a_by_d.pack(side='left')
    var_rot_a_by_d.set(False)

    # var_rot_d_by_a = tk.IntVar(root)
    chk_rot_d_by_a = tk.Checkbutton(frm_rot, text="Rotate D by A", variable=var_rot_d_by_a)
    chk_rot_d_by_a.pack()
    var_rot_d_by_a.set(False)

    # Size of phase circle
    frm_size_circle = ttk.Labelframe(root, relief="ridge", text="Size of phase circles", labelanchor='n')
    frm_size_circle.pack(side="left", fill=tk.Y)

    # var_size_circle = tk.StringVar(root)
    var_size_circle.set(str(size_phase_circle))
    spn_size_circle = tk.Spinbox(
        frm_size_circle, textvariable=var_size_circle, format="%.1f", from_=0.0, to=2.0, increment=0.1,
        command=lambda: set_size_phase_circle(float(var_size_circle.get())), width=5
    )
    spn_size_circle.pack(side="left")


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(side="left")
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(side="left")
    btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: clear_path())
    btn_clear.pack(side="left")


def create_center_lines():
    ln_axis_x = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_x)
    ln_axis_y = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_y)
    ln_axis_z = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_z)


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


def update_diagrams():
    rotation_vector_a.rotate_phase(np.deg2rad(phase_step_deg))
    rotation_vector_b.rotate_phase(np.deg2rad(phase_step_deg))

    if var_rot_a_by_d.get():
        rotation_vector_a.rotate_all(np.deg2rad(phase_step_deg), rotation_vector_b.get_center_vector())
        rotation_vector_a.set_orign(rotation_vector_b.get_phase_vector())

    if var_rot_d_by_a.get():
        rotation_vector_b.rotate_all(np.deg2rad(phase_step_deg), rotation_vector_a.get_center_vector())
        rotation_vector_b.set_orign(rotation_vector_a.get_phase_vector())

    if var_path.get():
        path_a.append_path(rotation_vector_a.get_phase_vector())
        path_b.append_path(rotation_vector_b.get_phase_vector())


def reset():
    global is_play
    cnt.reset()
    if is_play:
        is_play = not is_play
    rotation_vector_a.reset()
    rotation_vector_b.reset()

    rotation_vector_a.rotate_all(np.deg2rad(-135), vector_y_axis)
    rotation_vector_a.set_phase(np.deg2rad(phase_init_a))

    rotation_vector_b.rotate_all(np.deg2rad(-45), vector_y_axis)
    rotation_vector_b.set_phase(np.deg2rad(phase_init_b))

    rotation_vector_a.set_orign(np.array([0., size_phase_circle / 2., 0.]))
    rotation_vector_b.set_orign(np.array([0., - size_phase_circle / 2., 0.]))

    rotation_vector_a.update_diagrams()
    rotation_vector_b.update_diagrams()


def switch():
    global is_play
    is_play = not is_play


def update(f):
    if is_play:
        cnt.count_up()
        update_diagrams()


""" main loop """
if __name__ == "__main__":
    cnt = Counter(ax=ax0, is3d=True, xy=np.array([x_min, y_max]), z=z_max, label="Step=")
    draw_static_diagrams()
    create_animation_control()
    create_parameter_setter()

    rotation_vector_a = RotationVector(ax0, "red")
    rotation_vector_b = RotationVector(ax0, "gray")

    rotation_vector_a.rotate_all(np.deg2rad(-135), vector_y_axis)
    rotation_vector_a.set_phase(np.deg2rad(phase_init_a))

    rotation_vector_b.rotate_all(np.deg2rad(-45), vector_y_axis)
    rotation_vector_b.set_phase(np.deg2rad(phase_init_b))

    rotation_vector_a.set_orign(np.array([0., offset_scale, 0.]))
    rotation_vector_b.set_orign(np.array([0., - offset_scale, 0.]))

    path_a = Path(ax0, 2, "pink")
    path_b = Path(ax0, 2, "silver")

    plt_dummy1 = ax0.plot(0, 0, 0, color="red", linewidth=2, label="Rotation vector A")
    plt_dummy2 = ax0.plot(0, 0, 0, color="gray", linewidth=2, label="Rotation vector D")
    ax0.legend(loc='lower right', fontsize=8)

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()