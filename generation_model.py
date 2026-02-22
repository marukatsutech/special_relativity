# ==========================================
# Generation of Electron model with Hopf link rotation vector pairs
# ==========================================

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.spatial.transform import Rotation
from collections import deque
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

        # --- Local coordinate system bases ---
        self._basis_x = np.array([1., 0., 0.])  # Orbital plane base 1
        self._basis_y = np.array([0., 1., 0.])  # Orbital plane base 2
        self._basis_z = np.array([0., 0., 1.])  # Arrow direction

        # --- Quiver ---
        self.quiver_obj_base = None
        self.quiver_obj = None

        # --- Guide elements (Circles and Phase line) ---
        # Ensure these are initialized after the bases exist
        self.plt_circle, = self.ax.plot([], [], [], lw=1.2, color=color, alpha=1.)
        self.plt_phase_line, = self.ax.plot([], [], [], lw=1.0, ls="--", color=color)
        self.plt_marker, = self.ax.plot([], [], [], marker="o", ms=5, color=color)

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

        # --- Update Phase Marker ---
        p_vec = (np.cos(self.phase) * self._basis_x +
                 np.sin(self.phase) * self._basis_y) * self.radius + self.origin
        self.plt_phase_line.set_data_3d([self.origin[0], p_vec[0]],
                                        [self.origin[1], p_vec[1]],
                                        [self.origin[2], p_vec[2]])
        self.plt_marker.set_data_3d([p_vec[0]], [p_vec[1]], [p_vec[2]])

    def apply_rotation(self, angle_rad, axis_vector):
        rot = Rotation.from_rotvec(angle_rad * axis_vector)
        self._basis_x = rot.apply(self._basis_x)
        self._basis_y = rot.apply(self._basis_y)
        self._basis_z = rot.apply(self._basis_z)
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


# ==========================================
# 2. App
# ==========================================
class GenerationApp:
    def __init__(self, root):
        self.title = "Generation of Electron model"
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
        style.configure("Slider.TLabel", font=("", 24, ""))

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
        lim = 5.5
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
        c02 = Circle((0, 0), np.sqrt(2), ec='gray', ls=":", fill=False)
        self.ax.add_patch(c02)
        art3d.pathpatch_2d_to_3d(c02, z=0, zdir="z")

        # --- PARAMETERS ---
        self.blue_radius_scale = 1.
        self.yellow_radius_scale = 1.

        # --- SET ROTATION VELOCITY ---
        self.v_base = -0.05                       # Base velocity
        self.d_p_maj = self.v_base * np.sqrt(2)   # Phase of blue and yellow
        self.d_p_min = self.v_base * np.sqrt(2)   # Phase of red and green
        self.d_o_maj = self.v_base * np.sqrt(2)   # Orbit of yellow
        self.d_o_min = self.v_base * np.sqrt(2)   # Orbit of red and green

        # --- CREATE ROTATION VECTORS ---
        self.rotation_vector_blue = RotationVector(self.ax, "blue", length=np.sqrt(2), radius=np.sqrt(2), scale_arrow=1., scale_radius=1.)
        phase_point_blue = self.rotation_vector_blue.get_phase_point()
        self.rotation_vector_yellow = RotationVector(self.ax, "orange", length=np.sqrt(2), radius=np.sqrt(2), scale_arrow=1., scale_radius=1.,
                                                     origin=phase_point_blue)
        self.rotation_vector_yellow.apply_rotation(np.pi/2, np.array([1., 0., 0.]))

        # --- CREATE PHASE TRACE ---
        self.max_trace_pts = 1000  # Length of trace
        self.trace_x = deque(maxlen=self.max_trace_pts)
        self.trace_y = deque(maxlen=self.max_trace_pts)
        self.trace_z = deque(maxlen=self.max_trace_pts)

        self.plt_trace, = self.ax.plot([], [], [], color="orange", lw=1.5, alpha=0.6, label="Yellow Path")

        # --- UI - BUTTONS ---
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        ttk.Button(self.btn_frame, text="Play / Pause", style="BigFont.TButton",
                   command=self.toggle_play).pack(side=tk.LEFT, padx=5)

        ttk.Button(self.btn_frame, text="Reset", style="BigFont.TButton",
                   command=self.reset).pack(side=tk.LEFT, padx=5)

        # --- UI - SLIDER ---
        slider_frame = ttk.Frame(self.root)
        slider_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        ttk.Label(slider_frame, text="Blue Circle Radius Scale:").pack(side=tk.LEFT, padx=5)

        self.radius_val_var = tk.StringVar(value=f"{self.blue_radius_scale:.2f}")
        self.radius_val_label = ttk.Label(slider_frame, textvariable=self.radius_val_var, width=5)
        self.radius_val_label.pack(side=tk.LEFT, padx=5)

        self.radius_slider = ttk.Scale(
            slider_frame, from_=0.1, to=6.0, orient=tk.HORIZONTAL,
            command=self.update_blue_radius
        )
        self.radius_slider.set(self.blue_radius_scale)
        self.radius_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # --- UI - COUNTER LABEL ---
        self.counter_var = tk.StringVar(value="Step: 0")
        self.counter_label = ttk.Label(self.btn_frame, textvariable=self.counter_var, style="Counter.TLabel")
        self.counter_label.pack(side=tk.RIGHT, padx=20)

        # --- ANIMATION CONTROL ---
        self.is_playing = False
        self.anim = animation.FuncAnimation(self.fig, self.loop, interval=40, cache_frame_data=False)

    def reset(self):
        self.is_playing = False
        self.rotation_vector_blue.reset()
        self.rotation_vector_yellow.reset()
        self.rotation_vector_yellow.set_origin(self.rotation_vector_blue.get_phase_point())
        self.rotation_vector_yellow.apply_rotation(np.pi/2, np.array([1., 0., 0.]))

        self.trace_x.clear()
        self.trace_y.clear()
        self.trace_z.clear()
        self.plt_trace.set_data_3d([], [], [])
        self.canvas.draw_idle()

    def toggle_play(self):
        self.is_playing = not self.is_playing

    def update_diagrams(self, d_p_maj, d_p_min, d_o_maj, d_o_min):
        self.rotation_vector_blue.rotate_phase(d_p_maj)
        self.rotation_vector_yellow.rotate_phase(d_p_min)
        self.rotation_vector_yellow.set_origin(self.rotation_vector_blue.get_phase_point())
        self.rotation_vector_yellow.apply_rotation(d_p_maj, np.array([0., 0., 1.]))

    def loop(self, frame):
        if self.is_playing:
            # --- INCREMENT COUNTER ---
            self.frame_count += 1
            self.counter_var.set(f"Step: {self.frame_count}")

            self.update_diagrams(
                self.d_p_maj,
                self.d_p_min,
                self.d_o_maj,
                self.d_o_min
            )

            # --- UPDATE TRACE ---
            p = self.rotation_vector_yellow.get_phase_point()
            self.trace_x.append(p[0])
            self.trace_y.append(p[1])
            self.trace_z.append(p[2])

            self.plt_trace.set_data_3d(list(self.trace_x), list(self.trace_y), list(self.trace_z))

            self.canvas.draw_idle()

    def update_blue_radius(self, val):
        f_val = float(val)

        self.rotation_vector_blue.set_radius_scale(f_val)
        self.radius_val_var.set(f"{f_val:.2f}")

        self.rotation_vector_yellow.set_origin(self.rotation_vector_blue.get_phase_point())
        self.rotation_vector_yellow.set_length(np.sqrt(2) * f_val)
        self.d_p_min = self.v_base * np.sqrt(2) * f_val

        self.canvas.draw_idle()


if __name__ == "__main__":
    root = tk.Tk()
    app = GenerationApp(root)
    root.mainloop()