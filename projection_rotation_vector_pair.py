""" Projection of rotation vector pair """
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
phase_step_deg = 3.

""" Animation control """
is_play = False
is_tilt = False

""" Axis vectors """
vector_x_axis = np.array([1., 0., 0.])
vector_y_axis = np.array([0., 1., 0.])
vector_z_axis = np.array([0., 0., 1.])

""" Create figure and axes """
title_ax0 = "Projection of rotation vector pair"
title_tk = title_ax0

x_min = -5.
x_max = 5.
y_min = -5.
y_max = 5.
z_min = -5.
z_max = 5.

fig = Figure()
ax0 = fig.add_subplot(111, projection="3d")
ax0.set_box_aspect((4, 4, 4))
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("y")
ax0.set_zlabel("t")
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


class Line3d:
    def __init__(self, ax, x, y, z, u, v, w, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.u, self.v, self.w = u, v, w
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.label = label

        self.line_projection = art3d.Line3D([self.x, self.u], [self.y, self.v], [self.z, self.w],
                                            linewidth=self.line_width, color=self.color, linestyle=self.line_style,
                                            label=self.label)
        self.ax.add_line(self.line_projection)

    def set_xyz_uvw(self, x, y, z, u, v, w):
        self.x, self.y, self.z = x, y, z
        self.u, self.v, self.w = u, v, w
        self.line_projection.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])


class ProjectionLine3d:
    def __init__(self, ax, x, y, z, u, v, w, color, line_width, line_style, label):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.u, self.v, self.w = u, v, w
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.label = label

        self.line_projection = art3d.Line3D([self.x, self.u], [self.y, self.v], [self.z, self.w],
                                            linewidth=self.line_width, color=self.color, linestyle=self.line_style,
                                            label=self.label)
        self.ax.add_line(self.line_projection)
        self.end_marker, = self.ax.plot(self.u, self.v, self.w, marker="o", markersize=3, color=self.color)

    def set_uvw(self, u, v, w):
        self.u, self.v, self.w = u, v, w
        self.end_marker.set_data_3d([self.u], [self.v], [self.w])
        self.line_projection.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])

    def set_xyz_uvw(self, x, y, z, u, v, w):
        self.x, self.y, self.z = x, y, z
        self.u, self.v, self.w = u, v, w
        self.end_marker.set_data_3d([self.u], [self.v], [self.w])
        self.line_projection.set_data_3d([self.x, self.u], [self.y, self.v], [self.z, self.w])


class Circle3d:
    def __init__(self, ax, x, y, z, r, direction, line_width, line_style, color, alpha):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.r = r
        self.direction = direction
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.alpha = alpha

        self.angle_space = np.arange(0, 360)

        self.cos_data = self.r * np.cos(self.angle_space * np.pi / 180.) + self.x
        self.sin_data = self.r * np.sin(self.angle_space * np.pi / 180.) + self.y
        self.plain_data = self.angle_space * 0. + self.z

        if self.direction == "x":
            self.x_circle, self.y_circle, self.z_circle = self.plain_data, self.cos_data, self.sin_data
        elif self.direction == "y":
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.plain_data, self.sin_data
        else:  # "z"
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.sin_data, self.plain_data

        self.plt_circle, = self.ax.plot(self.x_circle, self.y_circle, self.z_circle,
                                        linewidth=self.line_width, linestyle=self.line_style,
                                        color=self.color, alpha=self.alpha)

    def rotate(self, angle, rotation_axis):
        rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        x_circle_rotated = []
        y_circle_rotated = []
        z_circle_rotated = []
        for i in range(len(self.angle_space)):
            vector_point = np.array(
                [self.x_circle[i], self.y_circle[i], self.z_circle[i]])
            point_rotated = rot_matrix.apply(vector_point)
            x_circle_rotated.append(point_rotated[0])
            y_circle_rotated.append(point_rotated[1])
            z_circle_rotated.append(point_rotated[2])
            self.x_circle[i] = point_rotated[0]
            self.y_circle[i] = point_rotated[1]
            self.z_circle[i] = point_rotated[2]
        self.plt_circle.set_xdata(np.array(x_circle_rotated))
        self.plt_circle.set_ydata(np.array(y_circle_rotated))
        self.plt_circle.set_3d_properties(np.array(z_circle_rotated))

    def reset(self):
        self.cos_data = self.r * np.cos(self.angle_space * np.pi / 180.) + self.x
        self.sin_data = self.r * np.sin(self.angle_space * np.pi / 180.) + self.y
        self.plain_data = self.angle_space * 0. + self.z

        if self.direction == "x":
            self.x_circle, self.y_circle, self.z_circle = self.plain_data, self.cos_data, self.sin_data
        elif self.direction == "y":
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.plain_data, self.sin_data
        else:  # "z"
            self.x_circle, self.y_circle, self.z_circle = self.cos_data, self.sin_data, self.plain_data

        self.plt_circle.set_xdata(self.x_circle)
        self.plt_circle.set_ydata(self.y_circle)
        self.plt_circle.set_3d_properties(self.z_circle)


class Arrow3d:
    def __init__(self, ax, x, y, z, u, v, w, scale, line_width, line_style, color, alpha):
        self.ax = ax
        self.x, self.y, self.z = x, y, z
        self.u, self.v, self.w = u, v, w
        self.scale = scale
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.alpha = alpha

        self.qvr = self.ax.quiver(self.x, self.y, self.z,
                                  self.u * self.scale, self.v * self.scale, self.w * self.scale,
                                  length=1, color=self.color, normalize=False,
                                  linewidth=self.line_width, linestyle=self.line_style)

        self.vector_init = np.array([self.u, self.v, self.w])

    def _update_quiver(self):
        self.qvr.remove()
        self.qvr = self.ax.quiver(self.x, self.y, self.z,
                                  self.u * self.scale, self.v * self.scale, self.w * self.scale,
                                  length=1, color=self.color, normalize=False,
                                  linewidth=self.line_width, linestyle=self.line_style)

    def rotate(self, angle, rotation_axis):
        rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
        rot_matrix = Rotation.from_rotvec(angle * rotation_axis)
        vector_rotated = rot_matrix.apply(self.vector_init)
        self.u, self.v, self.w = vector_rotated[0], vector_rotated[1], vector_rotated[2]
        self._update_quiver()
        self.vector_init = vector_rotated

    def set_vector(self, u, v, w):
        self.u, self.v, self.w = u, v, w
        self._update_quiver()

    def get_vector(self):
        return np.array([self.u, self.v, self.w])

    def set_scale(self, value):
        self.scale = value
        self._update_quiver()


class InternalPhase:
    def __init__(self, ax, phase_step):
        self.ax = ax
        self.phase_step = phase_step

        self.vector_spatial = np.array([0., 0., 1.])
        self.vector_time = np.array([0., 1., 0.])
        self.vector_phase_center_axis = np.array([0., 1., 0.])
        self.vector_phase = np.array([0., 0., 1.])

        self.vector_tilt_center_axis = np.array([1., 0., 0.])

        self.light_circle = Circle3d(self.ax, 0., 0., 0., 1., "y",
                                     1, "--", "darkorange", 1)
        self.rotation_vector_spacial = Arrow3d(self.ax, 0., 0., 0.,
                                               self.vector_spatial[0], self.vector_spatial[1], self.vector_spatial[2],
                                               1, 2, "-", "red", 1)
        self.rotation_vector_time = Arrow3d(self.ax, 0., 0., 0.,
                                            self.vector_time[0], self.vector_time[1], self.vector_time[2],
                                            1, 2, "-", "gray", 1)
        self.rotation_vector_phase = Arrow3d(self.ax, 0., 0., 0.,
                                             self.vector_phase[0], self.vector_phase[1], self.vector_phase[2],
                                             1, 2, "--", "darkorange", 1)

    def rotate_phase(self):
        rot_matrix = Rotation.from_rotvec(self.phase_step * self.vector_phase_center_axis)
        self.vector_phase = rot_matrix.apply(self.vector_phase)
        self.rotation_vector_phase.set_vector(self.vector_phase[0], self.vector_phase[1], self.vector_phase[2])

    def _rotate_all(self, angle, center_axis):
        rot_matrix = Rotation.from_rotvec(angle * center_axis)

        self.light_circle.rotate(angle, center_axis)

        self.vector_spatial = rot_matrix.apply(self.vector_spatial)
        self.vector_time = rot_matrix.apply(self.vector_time)
        self.vector_phase_center_axis = rot_matrix.apply(self.vector_phase_center_axis)
        self.vector_phase = rot_matrix.apply(self.vector_phase)

        self.rotation_vector_spacial.set_vector(self.vector_spatial[0], self.vector_spatial[1], self.vector_spatial[2])
        self.rotation_vector_time.set_vector(self.vector_time[0], self.vector_time[1], self.vector_time[2])
        self.rotation_vector_phase.set_vector(self.vector_phase[0], self.vector_phase[1], self.vector_phase[2])

    def tilt(self, angle_tilt):
        self._rotate_all(angle_tilt, self.vector_tilt_center_axis)

    def rotate_z(self):
        self._rotate_all(self.phase_step, vector_z_axis)

    def reset(self):
        self.light_circle.reset()

        self.vector_spatial = np.array([0., 0., 1.])
        self.vector_time = np.array([0., 1., 0.])
        self.vector_phase_center_axis = np.array([0., 1., 0.])
        self.vector_phase = np.array([0., 0., 1.])

        self.vector_tilt_center_axis = np.array([1., 0., 0.])

        self.rotation_vector_spacial.set_vector(self.vector_spatial[0], self.vector_spatial[1], self.vector_spatial[2])
        self.rotation_vector_time.set_vector(self.vector_time[0], self.vector_time[1], self.vector_time[2])
        self.rotation_vector_phase.set_vector(self.vector_phase[0], self.vector_phase[1], self.vector_phase[2])

    def show_rotation_vector_time(self):
        self.rotation_vector_time.set_scale(1)

    def hide_rotation_vector_time(self):
        self.rotation_vector_time.set_scale(0)

    def get_rotation_vector_spatial(self):
        vector = self.rotation_vector_phase.get_vector()
        return vector


class Line3D:
    def __init__(self, ax, x_start_init, x_end_init, y_start_init, y_end_init, z_start_init, z_end_init,
                 marker_size_start, marker_size_end, line_width, line_style, color, alpha):
        self.ax = ax
        self.line_width = line_width
        self.line_style = line_style
        self.marker_size_start = marker_size_start
        self.marker_size_end = marker_size_end
        self.color = color
        self.alpha = alpha

        self.x_start_init, self.x_end_init = x_start_init, x_end_init
        self.y_start_init, self.y_end_init = y_start_init, y_end_init
        self.z_start_init, self.z_end_init = z_start_init, z_end_init

        self.x_start, self.x_end = self.x_start_init, self.x_end_init
        self.y_start, self.y_end = self.y_start_init, self.y_end_init
        self.z_start, self.z_end = self.z_start_init, self.z_end_init

        self.plt_line, = self.ax.plot(np.array([self.x_start, self.x_end]),
                                      np.array([self.y_start, self.y_end]),
                                      np.array([self.z_start, self.z_end]),
                                      linewidth=self.line_width, linestyle=self.line_style,
                                      color=self.color, alpha=self.alpha)

        self.marker_start, = self.ax.plot(self.x_start, self.y_start, self.z_start,
                                          marker="o", markersize=self.marker_size_start, color=self.color)
        self.marker_end, = self.ax.plot(self.x_end, self.y_end, self.z_end,
                                        marker="o", markersize=self.marker_size_end, color=self.color)

    def reset(self):
        self.x_start, self.x_end = self.x_start_init, self.x_end_init
        self.y_start, self.y_end = self.y_start_init, self.y_end_init
        self.z_start, self.z_end = self.z_start_init, self.z_end_init

        self.update_line()

    def offset(self, x_value, y_value, z_value):
        self.x_start += x_value
        self.x_end += x_value
        self.y_start += y_value
        self.y_end += y_value
        self.z_start += z_value
        self.z_end += z_value

        self.update_line()

    def update_line(self):
        self.plt_line.set_xdata(np.array([self.x_start, self.x_end]))
        self.plt_line.set_ydata(np.array([self.y_start, self.y_end]))
        self.plt_line.set_3d_properties(np.array([self.z_start, self.z_end]))

        self.marker_start.set_data_3d([self.x_start], [self.y_start], [self.z_start])
        self.marker_end.set_data_3d([self.x_end], [self.y_end], [self.z_end])

    def rotate(self, angle, center_axis):
        line_start = np.array([self.x_start, self.y_start, self.z_start])
        line_end = np.array([self.x_end, self.y_end, self.z_end])

        rot_matrix = Rotation.from_rotvec(angle * center_axis)
        line_start_rotated = rot_matrix.apply(line_start)
        line_end_rotated = rot_matrix.apply(line_end)
        self.x_start, self.y_start, self.z_start = line_start_rotated[0], line_start_rotated[1], line_start_rotated[2]
        self.x_end, self.y_end, self.z_end = line_end_rotated[0], line_end_rotated[1], line_end_rotated[2]

        self.update_line()

    def get_start(self):
        return np.array([self.x_start, self.y_start, self.z_start])

    def get_end(self):
        return np.array([self.x_end, self.y_end, self.z_end])

    def set_start_end(self, x_start, y_start, z_start, x_end, y_end, z_end):
        self.x_start, self.x_end = x_start, x_end
        self.y_start, self.y_end = y_start, y_end
        self.z_start, self.z_end = z_start, z_end

        self.update_line()


class ProjectionPath:
    def __init__(self, ax, line_width, line_style, color, alpha):
        self.ax = ax
        self.line_width = line_width
        self.line_style = line_style
        self.color = color
        self.alpha = alpha

        self.x_path = []
        self.y_path = []
        self.z_path = []
        self.path, = self.ax.plot(np.array(self.x_path), np.array(self.y_path), np.array(self.z_path),
                                  linewidth=self.line_width, linestyle=self.line_style,
                                  color=self.color, alpha=self.alpha)

    def update_path(self, x, y, z):
        if z > 0:
            self.x_path.append(x)
            self.y_path.append(y)
            self.z_path.append(z)
        else:
            self.x_path.append(None)
            self.y_path.append(None)
            self.z_path.append(None)

        self.path.set_xdata(np.array(self.x_path, dtype=np.float64))
        self.path.set_ydata(np.array(self.y_path, dtype=np.float64))
        self.path.set_3d_properties(np.array(self.z_path, dtype=np.float64))

    def clear_path(self):
        self.x_path = []
        self.y_path = []
        self.z_path = []

        self.path.set_xdata(np.array(self.x_path))
        self.path.set_ydata(np.array(self.y_path))
        self.path.set_3d_properties(np.array(self.z_path))


def find_intersection(line1, line2):
    # Get parametric equations of the lines
    p1, d1 = line1  # Line 1: Origin p1 and direction vector d1
    p2, d2 = line2  # Line 2: Origin p2 and direction vector d2

    # Find the closest points using least squares method
    A = np.vstack([d1, -d2]).T
    b = p2 - p1
    t = np.linalg.lstsq(A, b, rcond=None)[0]  # Solve for parameters t

    # Calculate the closest points on each line
    point_on_line1 = p1 + t[0] * d1
    point_on_line2 = p2 + t[1] * d2

    # Check if the points are close enough to be considered an intersection
    if np.allclose(point_on_line1, point_on_line2, atol=1e-6):  # Adjust tolerance as needed
        return point_on_line1
    else:
        return None  # No intersection if points do not match


def switch_tilt():
    global is_tilt
    reset()
    internal_phase.hide_rotation_vector_time()
    projection_guide.reset()
    projection_guide.offset(0., 0., 1.)
    if is_tilt:
        pass
    else:
        internal_phase.tilt(np.deg2rad(45))
        internal_phase.show_rotation_vector_time()
        projection_guide.offset(0., -1., 0.)
    is_tilt = not is_tilt

    update_intersection()


def create_parameter_setter():
    frm_tilt = ttk.Labelframe(root, relief="ridge", text="Tilt (precession)", labelanchor="n")
    frm_tilt.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_tilt, text="On/off", command=switch_tilt)
    btn_play.pack(fill=tk.X)


def create_animation_control():
    frm_anim = ttk.Labelframe(root, relief="ridge", text="Animation", labelanchor="n")
    frm_anim.pack(side="left", fill=tk.Y)
    btn_play = tk.Button(frm_anim, text="Play/Pause", command=switch)
    btn_play.pack(fill=tk.X)
    btn_reset = tk.Button(frm_anim, text="Reset", command=reset)
    btn_reset.pack(fill=tk.X)
    btn_clear = tk.Button(frm_anim, text="Clear path", command=lambda: projection_path.clear_path())
    btn_clear.pack(fill=tk.X)


def create_center_lines():
    ln_axis_x = art3d.Line3D([x_min, x_max], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_x)
    ln_axis_y = art3d.Line3D([0., 0.], [y_min, y_max], [0., 0.], color="gray", ls="-.", linewidth=1)
    ax0.add_line(ln_axis_y)
    ln_axis_z = art3d.Line3D([0., 0.], [0., 0.], [z_min, z_max], color="blue", ls="-.", linewidth=1)
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


def update_intersection():
    # Check intersection
    line1 = (np.array([0, 0, 0]), internal_phase.get_rotation_vector_spatial())
    line2 = (projection_guide.get_start(), projection_guide.get_end() - projection_guide.get_start())

    intersection = find_intersection(line1, line2)

    if intersection is not None:
        projection_line.set_start_end(0., 0., 0,
                                      intersection[0], intersection[1], intersection[2])
        return intersection[0], intersection[1], intersection[2]
    else:
        print("No intersection exists.")
        return 0, 0, 0


def update_diagrams():
    internal_phase.rotate_phase()
    if is_tilt:
        internal_phase.rotate_z()
        projection_guide.rotate(np.deg2rad(phase_step_deg), vector_z_axis)

    x, y, z = update_intersection()
    projection_path.update_path(x, y, z)


def reset():
    global is_play
    cnt.reset()
    if is_play:
        is_play = not is_play
    internal_phase.reset()
    projection_guide.reset()
    projection_guide.offset(0., 0., 1.)
    update_intersection()


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

    internal_phase = InternalPhase(ax0, np.deg2rad(phase_step_deg))
    internal_phase.hide_rotation_vector_time()
    projection_guide = Line3D(ax0, -8., 8., 0., 0., 0., 0.,
                              0, 0, 1, "--", "green", 1)
    projection_guide.offset(0., 0., 1.)
    projection_line = Line3D(ax0, 0., 0., 0., 0., 0., 0.,
                             0, 3, 1, "--", "darkorange", 1)

    update_intersection()

    projection_path = ProjectionPath(ax0, 1, "-", "darkorange", 1)

    anim = animation.FuncAnimation(fig, update, interval=100, save_count=100)
    root.mainloop()