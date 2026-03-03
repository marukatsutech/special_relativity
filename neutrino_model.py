# ==========================================
# Neutrino model
# ==========================================

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from scipy.spatial.transform import Rotation
import ctypes
import platform
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.patches import Circle


# ==========================================
# 1. RotationVector Class
# ==========================================
class RotationVector:
    def __init__(self, ax, color, length=1.0, radius=1.0, scale_arrow=1.0, scale_radius=1.0, origin=np.zeros(3)):
        self.ax = ax
        self.color = color
        self.length_origin = length
        self.radius_origin = radius
        self.scale_arrow = scale_arrow
        self.scale_radius = scale_radius
        self.origin = origin

        self.radius = self.radius_origin * self.scale_radius
        self.phase = 0.

        # --- Local coordinate system bases (initial) ---
        self._basis_x_init = np.array([1., 0., 0.])  # Orbital plane base 1
        self._basis_y_init = np.array([0., 1., 0.])  # Orbital plane base 2
        self._basis_z_init = np.array([0., 0., 1.])  # Arrow direction

        # --- Local coordinate system bases ---
        self._basis_x = np.array([1., 0., 0.])  # Orbital plane base 1
        self._basis_y = np.array([0., 1., 0.])  # Orbital plane base 2
        self._basis_z = np.array([0., 0., 1.])  # Arrow direction

        # --- Quiver ---
        self.quiver_obj_base = None
        self.quiver_obj = None

        # --- Guide elements (Circles and Phase line) ---
        # Ensure these are initialized after the bases exist
        self.plt_circle, = self.ax.plot([], [], [], lw=2, color=color, alpha=1.)
        # self.plt_phase_line, = self.ax.plot([], [], [], lw=1.0, ls="--", color=color)
        # self.plt_marker, = self.ax.plot([], [], [], marker="o", ms=5, color=color)

        self.update_diagrams()

    def update_diagrams(self):
        # --- Update Quiver (The Arrow) ---

        if self.quiver_obj_base:
            self.quiver_obj_base.remove()

        self.quiver_obj_base = self.ax.quiver(
            self.origin[0], self.origin[1], self.origin[2],
            self._basis_z[0], self._basis_z[1], self._basis_z[2],
            length=self.length_origin, color=self.color, linewidth=3,
            arrow_length_ratio=0.2, normalize=True, ls="-"
        )

        if self.quiver_obj:
            self.quiver_obj.remove()

        arrow_length = self.length_origin * self.scale_arrow * self.scale_radius
        self.quiver_obj = self.ax.quiver(
             self.origin[0], self.origin[1], self.origin[2],
             self._basis_z[0], self._basis_z[1], self._basis_z[2],
             length=arrow_length, color=self.color, linewidth=3,
             arrow_length_ratio=0.2, normalize=True, ls="--"
        )

        # --- Update Orbital Circle ---
        theta = np.linspace(0, 2 * np.pi, 64)
        # Circle points on the x-y local plane
        c_pts = (np.cos(theta)[:, None] * self._basis_x +
                 np.sin(theta)[:, None] * self._basis_y) * self.radius + self.origin
        self.plt_circle.set_data_3d(c_pts[:, 0], c_pts[:, 1], c_pts[:, 2])

        """
        # --- Update Phase Marker ---
        p_vec = (np.cos(self.phase) * self._basis_x +
                 np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        self.plt_phase_line.set_data_3d([self.origin[0], p_vec[0]],
                                        [self.origin[1], p_vec[1]],
                                        [self.origin[2], p_vec[2]])
        self.plt_marker.set_data_3d([p_vec[0]], [p_vec[1]], [p_vec[2]])
        """

    def apply_rotation(self, angle_rad, axis_vector):
        rot = Rotation.from_rotvec(angle_rad * axis_vector)
        self._basis_x = rot.apply(self._basis_x)
        self._basis_y = rot.apply(self._basis_y)
        self._basis_z = rot.apply(self._basis_z)
        self.update_diagrams()

    def set_tilt(self, angle_rad, axis_vector):
        rot = Rotation.from_rotvec(angle_rad * axis_vector)
        self._basis_x = rot.apply(self._basis_x_init)
        self._basis_y = rot.apply(self._basis_y_init)
        self._basis_z = rot.apply(self._basis_z_init)
        self.update_diagrams()

    def rotate_phase(self, angle_rad):
        self.phase = (self.phase + angle_rad) % (2 * np.pi)
        self.update_diagrams()

    def reset(self):
        self.phase = 0.
        self._basis_x = np.array([1., 0., 0.])  # Orbital plane base 1
        self._basis_y = np.array([0., 1., 0.])  # Orbital plane base 2
        self._basis_z = np.array([0., 0., 1.])  # Arrow direction
        self.update_diagrams()

    def set_origin(self, origin):
        self.origin = origin
        self.update_diagrams()

    def set_radius_scale(self, scale_radius):
        self.scale_radius = scale_radius
        self.radius = self.radius_origin * self.scale_radius
        self.update_diagrams()

    def set_length(self, length):
        self.length_origin = length
        self.update_diagrams()

    def get_phase_point(self):
        p_vec = (np.cos(self.phase) * self._basis_x +
                 np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        return p_vec

    def get_vector(self):
        arrow_length = self.length_origin * self.scale_arrow # * self.scale_radius
        return self._basis_z * arrow_length


# ==========================================
# 2. PrecessionBase Class
# ==========================================
class PrecessionBase:
    def __init__(self, ax, color, length=1.0, radius=1.0, scale_arrow=1.0, scale_radius=1.0, origin=np.zeros(3)):
        self.ax = ax
        self.color = color
        self.length_origin = length
        self.radius_origin = radius
        self.scale_arrow = scale_arrow
        self.scale_radius = scale_radius
        self.origin = origin

        self.radius = self.radius_origin * self.scale_radius
        self.phase = 0.

        # --- Local coordinate system bases ---
        self._basis_x = np.array([1., 0., 0.])  # Orbital plane base 1
        self._basis_y = np.array([0., 1., 0.])  # Orbital plane base 2
        self._basis_z = np.array([0., 0., 1.])  # Arrow direction

        # --- Quiver ---
        # self.quiver_obj_base = None
        self.quiver_obj = None

        # --- Guide elements (Circles and Phase line) ---
        # Ensure these are initialized after the bases exist
        self.plt_circle, = self.ax.plot([], [], [], lw=1.2, color=color, ls="--", alpha=1.)
        self.plt_phase_line1, = self.ax.plot([], [], [], lw=1.0, ls="--", color=color)
        self.plt_phase_line2, = self.ax.plot([], [], [], lw=1.0, ls="--", color=color)
        self.plt_marker1, = self.ax.plot([], [], [], marker="o", ms=5, color=color)
        self.plt_marker2, = self.ax.plot([], [], [], marker="o", ms=5, color=color)

        self.update_diagrams()

    def update_diagrams(self):
        # --- Update Quiver (The Arrow) ---

        """
        if self.quiver_obj_base:
            self.quiver_obj_base.remove()

        self.quiver_obj_base = self.ax.quiver(
            self.origin[0], self.origin[1], self.origin[2],
            self._basis_z[0], self._basis_z[1], self._basis_z[2],
            length=self.length_origin, color=self.color, linewidth=3,
            arrow_length_ratio=0.2, normalize=True, ls="-"
        )
        """

        if self.quiver_obj:
            self.quiver_obj.remove()

        # arrow_length = self.length_origin * self.scale_arrow * self.scale_radius
        arrow_length = self.length_origin * self.scale_arrow
        self.quiver_obj = self.ax.quiver(
             self.origin[0], self.origin[1], self.origin[2],
             self._basis_z[0], self._basis_z[1], self._basis_z[2],
             length=arrow_length, color=self.color, linewidth=3,
             arrow_length_ratio=0.2, normalize=True, ls="--"
        )

        # --- Update Orbital Circle ---
        theta = np.linspace(0, 2 * np.pi, 64)
        # Circle points on the x-y local plane
        c_pts = (np.cos(theta)[:, None] * self._basis_x +
                 np.sin(theta)[:, None] * self._basis_y) * self.radius + self.origin
        self.plt_circle.set_data_3d(c_pts[:, 0], c_pts[:, 1], c_pts[:, 2])

        # --- Update Phase Marker ---
        p_vec1 = (np.cos(self.phase) * self._basis_x +
                  np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        self.plt_phase_line1.set_data_3d([self.origin[0], p_vec1[0]],
                                         [self.origin[1], p_vec1[1]],
                                         [self.origin[2], p_vec1[2]])
        self.plt_marker1.set_data_3d([p_vec1[0]], [p_vec1[1]], [p_vec1[2]])

        p_vec2 = (-np.cos(self.phase) * self._basis_x +
                  -np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        self.plt_phase_line2.set_data_3d([self.origin[0], p_vec2[0]],
                                         [self.origin[1], p_vec2[1]],
                                         [self.origin[2], p_vec2[2]])
        self.plt_marker2.set_data_3d([p_vec2[0]], [p_vec2[1]], [p_vec2[2]])

    def apply_rotation(self, angle_rad, axis_vector):
        rot = Rotation.from_rotvec(angle_rad * axis_vector)
        self._basis_x = rot.apply(self._basis_x)
        self._basis_y = rot.apply(self._basis_y)
        self._basis_z = rot.apply(self._basis_z)
        self.update_diagrams()

    def rotate_phase(self, angle_rad):
        self.phase = (self.phase + angle_rad) % (2 * np.pi)
        self.update_diagrams()

    def set_phase(self, angle_rad):
        self.phase = angle_rad
        self.update_diagrams()

    def reset(self):
        self.phase = 0.
        self._basis_x = np.array([1., 0., 0.])  # Orbital plane base 1
        self._basis_y = np.array([0., 1., 0.])  # Orbital plane base 2
        self._basis_z = np.array([0., 0., 1.])  # Arrow direction
        self.update_diagrams()

    def set_origin(self, origin):
        self.origin = origin
        self.update_diagrams()

    def set_radius_scale(self, scale_radius):
        self.scale_radius = scale_radius
        self.radius = self.radius_origin * self.scale_radius
        self.update_diagrams()

    def set_length(self, length):
        self.length_origin = length
        self.update_diagrams()

    def set_arrow_scale(self, scale_arrow):
        self.scale_arrow = scale_arrow
        self.update_diagrams()

    def get_phase_point1(self):
        p_vec1 = (np.cos(self.phase) * self._basis_x +
                  np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        return p_vec1

    def get_phase_point2(self):
        p_vec2 = (-np.cos(self.phase) * self._basis_x +
                  -np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        return p_vec2


# ==========================================
# 3. App
# ==========================================
class GenerationApp:
    def __init__(self, root):
        self.title = "Neutrino model"
        self.root = root
        self.root.title(self.title)

        # --- COUNTER VARIABLE ---
        self.frame_count = 0

        # --- HIGH DPI SUPPORT FOR WINDOWS ---
        if platform.system() == "Windows":
            try:
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
            except:
                pass

        # --- STYLE & FONTS ---
        style = ttk.Style()
        style.configure("BigFont.TButton", font=("", 24, ""))
        style.configure("Counter.TLabel", font=("Consolas", 24, "bold"), foreground="blue")

        # --- PLOT SETUP ---
        self.fig = Figure(figsize=(8, 8), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # --- ADDING THE TOOLBAR ---
        self.toolbar_frame = ttk.Frame(self.root)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()

        # --- MATPLOTLIB FIGURE SETUP ---
        self.ax.set_box_aspect((1, 1, 1))
        lim = 2.5
        self.ax.set_xlim(-lim, lim)
        self.ax.set_ylim(-lim, lim)
        self.ax.set_zlim(-lim, lim)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.set_title(self.title, fontsize=30)

        # --- CREATE STATIC DIAGRAMS - CENTER LINES ---
        line_axis_x = art3d.Line3D([-lim, lim], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
        self.ax.add_line(line_axis_x)
        line_axis_y = art3d.Line3D([0., 0.], [-lim, lim], [0., 0.], color="gray", ls="-.", linewidth=1)
        self.ax.add_line(line_axis_y)
        line_axis_z = art3d.Line3D([0., 0.], [0., 0.], [-lim, lim], color="gray", ls="-.", linewidth=1)
        self.ax.add_line(line_axis_z)

        # --- CREATE STATIC DIAGRAMS - ADDITIONAL CIRCLES ---
        # c00 = Circle((0, 0), np.sqrt(2)/2, ec='gray', ls=":", fill=False)
        # self.ax.add_patch(c00)
        # art3d.pathpatch_2d_to_3d(c00, z=0, zdir="x")
        # c01 = Circle((0, 0), np.sqrt(2)/2, ec='gray', ls=":", fill=False)
        # self.ax.add_patch(c01)
        # art3d.pathpatch_2d_to_3d(c01, z=0, zdir="y")
        c02 = Circle((0, 0), np.sqrt(2)/2, ec='gray', ls=":", fill=False)
        self.ax.add_patch(c02)
        art3d.pathpatch_2d_to_3d(c02, z=0, zdir="z")

        # --- PARAMETERS ---
        self.blue_radius_scale = 1.
        self.yellow_radius_scale = 1.

        # --- SET ROTATION VELOCITY ---
        self.v_base = -0.05                 # Base velocity
        self.d_precess_phase = self.v_base * np.sqrt(2)   # Phase of precession
        self.d_p_min = self.v_base * np.sqrt(2)     # Phase of red and green
        self.d_o_maj = self.v_base * np.sqrt(2)     # Orbit of yellow
        self.d_o_min = self.v_base * np.sqrt(2)     # Orbit of red and green

        self.v_precess_base = 1.                    # Base velocity of precession angle
        self.d_precess_angle = self.v_precess_base  # Velocity of precession angle

        self.precess_angle = 0.

        # --- CREATE PRECESSION BASE ---
        self.precession_base = PrecessionBase(self.ax, "gray", length=1., radius=np.sqrt(2)/2,
                                              scale_arrow=np.sqrt(2)*2, scale_radius=1.)

        # --- CREATE ROTATION VECTORS ---
        precess_point_1 = self.precession_base.get_phase_point1()
        self.rotation_vector_blue = RotationVector(self.ax, "blue", length=np.sqrt(2), radius=np.sqrt(2),
                                                   scale_arrow=1., scale_radius=1.,
                                                   origin=precess_point_1)

        precess_point_2 = self.precession_base.get_phase_point2()
        self.rotation_vector_yellow = RotationVector(self.ax, "orange", length=np.sqrt(2), radius=np.sqrt(2),
                                                     scale_arrow=1., scale_radius=1.,
                                                     origin=precess_point_2)

        # self.rotation_vector_blue.apply_rotation(np.pi/2, np.array([1, 0, 0]))
        # self.rotation_vector_yellow.apply_rotation(np.pi / 2, np.array([-1, 0, 0]))

        # --- CREATE PHASE TRACE ---

        # --- UI - BUTTONS ---
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        ttk.Button(self.btn_frame, text="Play / Pause", style="BigFont.TButton",
                   command=self.toggle_play).pack(side=tk.LEFT, padx=5)

        ttk.Button(self.btn_frame, text="Reset", style="BigFont.TButton",
                   command=self.reset).pack(side=tk.LEFT, padx=5)

        # --- UI - COUNTER LABEL ---
        self.counter_var = tk.StringVar(value="Step: 0")
        self.counter_label = ttk.Label(self.btn_frame, textvariable=self.counter_var, style="Counter.TLabel")
        self.counter_label.pack(side=tk.RIGHT, padx=20)

        # --- ANIMATION CONTROL ---
        self.is_playing = False
        self.anim = animation.FuncAnimation(self.fig, self.loop, interval=40, cache_frame_data=False)

        self.is_oscillate = False
        self.btn_osc = ttk.Button(self.btn_frame, text="Oscillation: OFF", style="BigFont.TButton",
                                  command=lambda: self.toggle_oscillation())
        self.btn_osc.pack(side=tk.LEFT, padx=5)

    def toggle_oscillation(self):
        self.is_oscillate = not self.is_oscillate
        self.btn_osc.config(text=f"Oscillation: {'ON' if self.is_oscillate else 'OFF'}")
        self.canvas.draw_idle()

    def reset(self):
        self.is_playing = False
        self.canvas.draw_idle()

    def toggle_play(self):
        self.is_playing = not self.is_playing

    def update_diagrams(self, phase_pr, angle_pr, length, radius):

        self.precession_base.set_radius_scale(radius)
        self.precession_base.set_phase(phase_pr)

        precess_point_1 = self.precession_base.get_phase_point1()
        self.rotation_vector_blue.set_origin(precess_point_1)
        if np.linalg.norm(precess_point_1) != 0:
            precess_point_1 = precess_point_1 / np.linalg.norm(precess_point_1)
        self.rotation_vector_blue.set_tilt(angle_pr, precess_point_1)

        precess_point_2 = self.precession_base.get_phase_point2()
        self.rotation_vector_yellow.set_origin(precess_point_2)
        if np.linalg.norm(precess_point_2) != 0:
            precess_point_2 = precess_point_2 / np.linalg.norm(precess_point_2)
        self.rotation_vector_yellow.set_tilt(angle_pr, precess_point_2)

        self.precession_base.set_arrow_scale(length)

        self.rotation_vector_blue.set_radius_scale(radius)
        self.rotation_vector_yellow.set_radius_scale(radius)

    def loop(self, frame):
        if self.is_playing:
            # --- INCREMENT COUNTER ---
            self.frame_count += 1
            self.counter_var.set(f"Step: {self.frame_count}")

            # --- UPDATE DIAGRAMS ---
            precess_phase_osc = np.pi * np.cos(np.pi * self.frame_count / 180. * 2)
            precess_angle_osc = np.pi / 4 * np.cos(np.pi * self.frame_count / 180. * 2)

            arrow_blue = self.rotation_vector_blue.get_vector()
            arrow_yellow = self.rotation_vector_yellow.get_vector()
            precess_length = arrow_blue[2] + arrow_yellow[2]

            if self.is_oscillate:
                precess_radius_scale_osc = precess_length - np.sqrt(2)
            else:
                precess_radius_scale_osc = 1

            self.update_diagrams(
                precess_phase_osc,
                precess_angle_osc,
                precess_length,
                precess_radius_scale_osc
            )

            # --- UPDATE TRACE ---
            pass

            self.canvas.draw_idle()


if __name__ == "__main__":
    root = tk.Tk()
    app = GenerationApp(root)
    root.mainloop()