# ==========================================
# Electron model with Hopf link rotation vector pairs
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
    def __init__(self, ax, color, radius, orbit_radius, initial_precession=0.0, initial_phase=0.0, scale=1.0):
        self.ax = ax
        self.color = color
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.precession_angle = initial_precession
        self.phase = initial_phase
        self.scale = scale

        # Deques for origin trajectory
        self.trail_orig_x = deque(maxlen=1000)
        self.trail_orig_y = deque(maxlen=1000)
        self.trail_orig_z = deque(maxlen=1000)
        self.plt_trail_orig, = self.ax.plot([], [], [], lw=1., color=color, alpha=0.8, visible=False)

        # Deques for marker trajectory
        self.trail_mark_x = deque(maxlen=1000)
        self.trail_mark_y = deque(maxlen=1000)
        self.trail_mark_z = deque(maxlen=1000)
        self.plt_trail_mark, = self.ax.plot([], [], [], lw=1., ls="--", color=color, alpha=0.8, visible=False)

        # Plot objects for visualization
        self.plt_circle, = self.ax.plot([], [], [], lw=1.2, color=color, alpha=0.6)
        self.plt_phase_line, = self.ax.plot([], [], [], lw=1.0, ls="--", color=color)
        self.plt_marker, = self.ax.plot([], [], [], marker="o", ms=4, color=color)
        self.quiver_obj = None
        self.origin = np.zeros(3)
        self.basis_x = np.array([0., 0., 1.])

    def reset_trails(self):
        """Clear all trajectory data"""
        self.trail_orig_x.clear()
        self.trail_orig_y.clear()
        self.trail_orig_z.clear()
        self.trail_mark_x.clear()
        self.trail_mark_y.clear()
        self.trail_mark_z.clear()
        self.plt_trail_orig.set_data_3d([], [], [])
        self.plt_trail_mark.set_data_3d([], [], [])

    def update_geometry(self, center_pos, rotation_axis, is_minor=False):
        # Calculate rotation axis
        norm = np.linalg.norm(rotation_axis)
        axis = rotation_axis / norm if norm > 1e-6 else np.array([0, 0, 1])

        # Determine reference vector for orbit
        if abs(axis[2]) < 0.9:
            ref = np.cross(axis, [0, 0, 1])
        else:
            ref = np.cross(axis, [0, 1, 0])
        ref /= np.linalg.norm(ref)

        # Calculate origin position (precession/orbit)
        rot_orbit = Rotation.from_rotvec(self.precession_angle * axis)
        rel_pos = rot_orbit.apply(ref) * self.orbit_radius
        self.origin = center_pos + rel_pos

        # Apply tilt based on the Left-Hand Rule
        if not is_minor:
            normal_axis = -rel_pos / np.linalg.norm(rel_pos) if np.linalg.norm(rel_pos) > 1e-6 else ref
            rot_tilt = Rotation.from_rotvec(-np.radians(45) * normal_axis)
            self.basis_x = rot_tilt.apply(axis)
            basis_y = normal_axis
        else:
            tilt_axis = rel_pos / np.linalg.norm(rel_pos) if np.linalg.norm(rel_pos) > 1e-6 else ref
            rot_tilt = Rotation.from_rotvec(np.radians(45) * tilt_axis)
            self.basis_x = rot_tilt.apply(axis)
            basis_y = tilt_axis

        basis_z = np.cross(self.basis_x, basis_y)

        # Update arrow (quiver)
        if self.quiver_obj: self.quiver_obj.remove()
        self.quiver_obj = self.ax.quiver(
            self.origin[0], self.origin[1], self.origin[2],
            self.basis_x[0], self.basis_x[1], self.basis_x[2],
            length=self.scale, color=self.color, linewidth=4, arrow_length_ratio=0.3
        )

        # Update rotation circle
        theta = np.linspace(0, 2 * np.pi, 40)
        c_pts = (np.cos(theta)[:, None] * basis_y + np.sin(theta)[:, None] * basis_z) * self.radius + self.origin
        self.plt_circle.set_data_3d(c_pts[:, 0], c_pts[:, 1], c_pts[:, 2])

        # Calculate marker position
        p_pos = self.origin + (np.cos(self.phase) * basis_y + np.sin(self.phase) * basis_z) * self.radius
        self.plt_phase_line.set_data_3d([self.origin[0], p_pos[0]], [self.origin[1], p_pos[1]],
                                        [self.origin[2], p_pos[2]])
        self.plt_marker.set_data_3d([p_pos[0]], [p_pos[1]], [p_pos[2]])

        # Update origin trail
        self.trail_orig_x.append(self.origin[0])
        self.trail_orig_y.append(self.origin[1])
        self.trail_orig_z.append(self.origin[2])
        self.plt_trail_orig.set_data_3d(list(self.trail_orig_x), list(self.trail_orig_y), list(self.trail_orig_z))

        # Update marker trail
        self.trail_mark_x.append(p_pos[0])
        self.trail_mark_y.append(p_pos[1])
        self.trail_mark_z.append(p_pos[2])
        self.plt_trail_mark.set_data_3d(list(self.trail_mark_x), list(self.trail_mark_y), list(self.trail_mark_z))


# ==========================================
# 2. RotationVectorPair Class
# ==========================================
class RotationVectorPair:
    def __init__(self, ax, color1, color2, radius, orbit_radius, scale=1.0, phase_offset=0.0):
        self.vec1 = RotationVector(ax, color1, radius, orbit_radius, 0.0 + phase_offset, np.pi, scale)
        self.vec2 = RotationVector(ax, color2, radius, orbit_radius, np.pi + phase_offset, np.pi, scale)

    def step(self, d_phase, d_orbit, center_pos, rotation_axis, is_minor=False):
        for v in [self.vec1, self.vec2]:
            v.phase = (v.phase + d_phase) % (2 * np.pi)
            v.precession_angle += d_orbit
            v.update_geometry(center_pos, rotation_axis, is_minor)

    def set_trace_visible(self, mode, visible):
        for v in [self.vec1, self.vec2]:
            if mode == "origin": v.plt_trail_orig.set_visible(visible)
            if mode == "marker": v.plt_trail_mark.set_visible(visible)

    def reset_all_trails(self):
        self.vec1.reset_trails()
        self.vec2.reset_trails()


# ==========================================
# 3. App
# ==========================================
class ElectronApp:
    def __init__(self, root):
        self.title = "Electron model with Hopf link rotation  vector pairs"
        self.root = root
        self.root.title(self.title)

        # High DPI support for Windows
        if platform.system() == "Windows":
            try:
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
            except:
                pass

        # --- STYLE & FONTS ---
        style = ttk.Style()
        style.configure("BigFont.TButton", font=("", 24, ""))

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

        # --- UI BUTTONS ---
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        ttk.Button(self.btn_frame, text="Play / Pause", style="BigFont.TButton",
                   command=self.toggle_play).pack(side=tk.LEFT, padx=5)

        self.trace_orig_enabled = False
        self.btn_orig = ttk.Button(self.btn_frame, text="Trace Origin: OFF", style="BigFont.TButton",
                                   command=lambda: self.toggle_trace("origin"))
        self.btn_orig.pack(side=tk.LEFT, padx=5)

        self.trace_mark_enabled = False
        self.btn_mark = ttk.Button(self.btn_frame, text="Trace Marker: OFF", style="BigFont.TButton",
                                   command=lambda: self.toggle_trace("marker"))
        self.btn_mark.pack(side=tk.LEFT, padx=5)

        ttk.Button(self.btn_frame, text="Reset Trace", style="BigFont.TButton",
                   command=self.reset_all_traces).pack(side=tk.LEFT, padx=5)

        # Matplotlib Figure Setup
        self.ax.set_box_aspect((1, 1, 1))
        lim = 2.5
        self.ax.set_xlim(-lim, lim)
        self.ax.set_ylim(-lim, lim)
        self.ax.set_zlim(-lim, lim)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.set_title(self.title, fontsize=30)

        # Create Vector Pairs
        self.pair_major = RotationVectorPair(self.ax, "blue", "gold", np.sqrt(2), np.sqrt(2) / 2.0, scale=np.sqrt(2))
        self.pair_minor = RotationVectorPair(self.ax, "red", "green", 1.0, 0.5, scale=1.0, phase_offset=np.pi / 2)

        self.update_all_vectors(0, 0, 0, 0)
        self.is_playing = False
        self.anim = animation.FuncAnimation(self.fig, self.loop, interval=40, cache_frame_data=False)

        # Draw center lines
        line_axis_x = art3d.Line3D([-lim, lim], [0., 0.], [0., 0.], color="gray", ls="-.", linewidth=1)
        self.ax.add_line(line_axis_x)
        line_axis_y = art3d.Line3D([0., 0.], [-lim, lim], [0., 0.], color="gray", ls="-.", linewidth=1)
        self.ax.add_line(line_axis_y)
        line_axis_z = art3d.Line3D([0., 0.], [0., 0.], [-lim, lim], color="gray", ls="-.", linewidth=1)
        self.ax.add_line(line_axis_z)

        # Draw circles
        # c00 = Circle((0, 0), np.sqrt(2)/2, ec='gray', ls=":", fill=False)
        # self.ax.add_patch(c00)
        # art3d.pathpatch_2d_to_3d(c00, z=0, zdir="x")
        # c01 = Circle((0, 0), np.sqrt(2)/2, ec='gray', ls=":", fill=False)
        # self.ax.add_patch(c01)
        # art3d.pathpatch_2d_to_3d(c01, z=0, zdir="y")
        c02 = Circle((0, 0), np.sqrt(2)/2, ec='gray', ls=":", fill=False)
        self.ax.add_patch(c02)
        art3d.pathpatch_2d_to_3d(c02, z=0, zdir="z")

    def toggle_play(self):
        self.is_playing = not self.is_playing

    def toggle_trace(self, mode):
        """Toggle visibility of origin or marker trails"""
        if mode == "origin":
            self.trace_orig_enabled = not self.trace_orig_enabled
            self.pair_major.set_trace_visible("origin", self.trace_orig_enabled)
            self.pair_minor.set_trace_visible("origin", self.trace_orig_enabled)
            self.btn_orig.config(text=f"Trace Origin: {'ON' if self.trace_orig_enabled else 'OFF'}")
        else:
            self.trace_mark_enabled = not self.trace_mark_enabled
            self.pair_major.set_trace_visible("marker", self.trace_mark_enabled)
            self.pair_minor.set_trace_visible("marker", self.trace_mark_enabled)
            self.btn_mark.config(text=f"Trace Marker: {'ON' if self.trace_mark_enabled else 'OFF'}")
        self.canvas.draw_idle()

    def reset_all_traces(self):
        """Reset all trajectory data"""
        self.pair_major.reset_all_trails()
        self.pair_minor.reset_all_trails()
        self.canvas.draw_idle()

    def update_all_vectors(self, d_p_maj, d_p_min, d_o_maj, d_o_min):
        """Update hierarchy of vectors"""
        self.pair_major.step(d_p_maj, d_o_maj, np.zeros(3), np.array([0, 0, 1]))
        y_origin = self.pair_major.vec2.origin
        y_axis = self.pair_major.vec2.basis_x
        self.pair_minor.step(d_p_min, d_o_min, y_origin, y_axis, is_minor=True)

    def loop(self, frame):
        if self.is_playing:
            # Mathematical speed ratios
            v_base = -0.05
            self.update_all_vectors(v_base, v_base, v_base * 2, v_base * np.sqrt(2))
            self.canvas.draw_idle()


if __name__ == "__main__":
    root = tk.Tk()
    app = ElectronApp(root)
    root.mainloop()