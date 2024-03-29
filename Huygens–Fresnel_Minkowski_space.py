# Huygens–Fresnel principle in Minkowski space

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.patches as patches
import tkinter as tk
from tkinter import ttk
import matplotlib.ticker as ticker


def change_show_hide_status():
    global a1
    if var_w1.get():
        a1 = 1.
    else:
        a1 = 0.


def update_plots():
    global theta_light_pass_1, xy_light_pass_1, circles_marker, circles_light_marker, arrows_light_marker
    global lines_connection, time_observer, y_1
    # Arrow of light pass 1
    theta_light_pass_1 = np.pi / 2. - float(scl_lp1_var.get()) * np.pi / 180.
    xy_light_pass_1 = [np.cos(theta_light_pass_1), np.sin(theta_light_pass_1)]
    arrow_light_pass_1.xy = xy_light_pass_1
    # Markers, light circles , light arrows on spatial line
    if abs(xy_light_pass_1[1]) > 0.000001:
        slope1 = xy_light_pass_1[0] / xy_light_pass_1[1]
        for n in range(5):
            xy_maker = [slope1 * (n + 1), n + 1]
            circles_marker[n].set_center(xy_maker)
            circles_light_marker[n].set_center(xy_maker)
            arrows_light_marker[n].set_position(xy_maker)
            arrows_light_marker[n].xy = [xy_maker[0] + xy_light_pass_1[0], xy_maker[1] + xy_light_pass_1[1]]
        for m in range(5):
            if m == 0:
                xy1 = circles_marker[m].get_center()
                xx_connection = [xy_light_pass_1[0], xy1[0]]
                yy_connection = [xy_light_pass_1[1], xy1[1]]
            else:
                xy0 = arrows_light_marker[m - 1].xy
                xy1 = circles_marker[m].get_center()
                xx_connection = [xy0[0], xy1[0]]
                yy_connection = [xy0[1], xy1[1]]
            lines_connection[m].set_data(xx_connection, yy_connection)
    time_observer = float(scl_ot_var.get()) / 10.
    # Spatial line of observer
    xx = [x_max, x_min]
    yy = [time_observer, time_observer]
    line_spatial.set_data(xx, yy)
    # Wave curve
    if abs(xy_light_pass_1[1]) > 0.000001:
        slope1 = xy_light_pass_1[0] / xy_light_pass_1[1]
        if var_rd_k.get() == 1:
            k = 1.
        elif var_rd_k.get() == 2:
            k = 1. / slope1
        elif var_rd_k.get() == 3:
            k = slope1
        if var_rd_c.get() == 1:
            omega = 1.
        elif var_rd_c.get() == 2:
            omega = 1. / slope1
        elif var_rd_c.get() == 3:
            omega = slope1
        # y_1 = a1 * np.cos(2. * np.pi * (k * (x - omega1 * time_observer)))
        # y_1 = a1 * np.cos(2. * np.pi * (k * x - k * omega1 * time_observer))
        y_1 = a1 * np.cos(2. * np.pi * (k * x - omega * time_observer))
        wave_curve_1.set_ydata(y_1 + time_observer)


def update(f):
    update_plots()


# Global variables
colors = ['red', 'orange', 'gold', 'green', 'blue', 'indigo', 'violet', 'purple']

# Parameters
start_guide = -12
end_guide = 12
num_of_guide = end_guide - start_guide + 1
time_observer = 0.
theta_light_pass_1 = np.arctan2(1., 1.)
a1 = 1.

# Data array
range_x_min = -1.
range_x_max = 12.
range_y_min = -1.
range_y_max = 6.

# Generate figure and axes
title_ax0 = "Huygens–Fresnel principle in Minkowski space"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max

fig = Figure()
ax0 = fig.add_subplot(111)
ax0.set_title(title_ax0)
ax0.set_xlabel("x of observer")
ax0.set_ylabel("t of observer")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")
ax0.grid()
# Ticks
x_ticks = []
for ix in range(int(x_min), int(x_max)):
    x_ticks.append(ix)
ax0.xaxis.set_major_locator(ticker.FixedLocator(x_ticks))
y_ticks = []
for iy in range(int(y_min), int(y_max)):
    y_ticks.append(iy)
ax0.yaxis.set_major_locator(ticker.FixedLocator(y_ticks))
ax0.set_xticklabels(x_ticks, fontsize=6)
ax0.set_yticklabels(y_ticks, fontsize=6)

# Generate graphic items
# Guide lines and circles
color_idx = 0
for i in range(1, 13):
    circle_light = patches.Circle(xy=(0., 0.), radius=i, color=colors[color_idx],
                                  fill=False, linestyle=":", linewidth=2)
    ax0.add_patch(circle_light)
    color_idx += 1
    if color_idx >= len(colors):
        color_idx = 0

# Secondary waves
for i in range(num_of_guide):
    xx_guide = [0., start_guide + i]
    yy_guide = [0., 1.]
    guide, = ax0.plot(xx_guide, yy_guide, color=colors[0], linewidth=0.5, linestyle="-")
    color_idx = 1
    for j in range(5):
        xy_circle = [xx_guide[1], yy_guide[1] + j]
        circle_light1 = patches.Circle(xy=xy_circle, radius=1, color=colors[color_idx],
                                       fill=False, linestyle=":", linewidth=1)
        ax0.add_patch(circle_light1)
        color_idx += 1
        if color_idx >= len(colors):
            color_idx = 0

color_idx = 0
for i in range(1, 6):
    xx_guide = [x_min, x_max]
    yy_guide = [i, i]
    guide_spatial, = ax0.plot(xx_guide, yy_guide, color=colors[color_idx], linewidth=1, linestyle="-")
    color_idx += 1
    if color_idx >= len(colors):
        color_idx = 0

xy_light_pass_1 = [np.cos(theta_light_pass_1), np.sin(theta_light_pass_1)]
arrow_light_pass_1 = ax0.annotate('', xy=xy_light_pass_1, xytext=[0., 0.], arrowprops=dict(
    width=1, headwidth=6, headlength=6, facecolor='red', edgecolor='red'))

# Markers on spatial line
circles_marker = []
for i in range(5):
    circle_spatial_1 = patches.Circle(xy=(0., 0.), radius=0.05, color=colors[i], linestyle="-", linewidth=1)
    ax0.add_patch(circle_spatial_1)
    circles_marker.append(circle_spatial_1)

# Light circles markers
circles_light_marker = []
arrows_light_marker = []
for i in range(5):
    circle_light_marker = patches.Circle(xy=(0., 0.), radius=1, color=colors[i + 1],
                                         fill=False, linestyle=":", linewidth=1.5)
    ax0.add_patch(circle_light_marker)
    circles_light_marker.append(circle_light_marker)

# Light arrows at markers
arrows_light_marker = []
for i in range(5):
    arrow_light_marker = ax0.annotate('', xy=(0., 0.), xytext=[0., 0.], arrowprops=dict(
        width=1, headwidth=6, headlength=6, facecolor=colors[i + 1], edgecolor=colors[i + 1]))
    arrows_light_marker.append(arrow_light_marker)

# Connection line Light arrows to markers
lines_connection = []
for i in range(5):
    line_connection, = ax0.plot((0., 0.), (0., 0.), color=colors[i], linewidth=1, linestyle="--")
    lines_connection.append(line_connection)

# Spatial lines of observer
xx_line_spatial = [x_max, x_min]
yy_line_spatial = [time_observer, time_observer]
line_spatial, = ax0.plot(xx_line_spatial, yy_line_spatial, color='brown', linestyle="-", linewidth=2)

# Phase curve
x = np.linspace(x_min, x_max, 1000)
y_1 = x * 0.
wave_curve_1, = ax0.plot(x, y_1, linestyle='-', color="red", linewidth=1,
                         label='y=cos(2pi*(k*x-omega*t)')
ax0.legend(loc='upper right')

# Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Checkbutton for show/hide a wave
frm_cs = ttk.Labelframe(root, relief="ridge", text="Show/hide wave", labelanchor="n")
frm_cs.pack(side='left', fill=tk.Y)
var_w1 = tk.BooleanVar(root)    # Variable for checkbutton
check_w1 = tk.Checkbutton(frm_cs, text="wave:", variable=var_w1, command=change_show_hide_status)
check_w1.pack()
var_w1.set(True)

# Parameter setting(k)
frm_parameter_k = ttk.Labelframe(root, relief="ridge", text="Parameter setting(k)", labelanchor="n")
frm_parameter_k.pack(side='left', fill=tk.Y)
# Radio button
var_rd_k = tk.IntVar(root)
# Radio button 1st
rd_k1 = tk.Radiobutton(frm_parameter_k, text="k = 1", value=1, var=var_rd_k)
rd_k1.pack()
# Radio button 2nd
rd_k2 = tk.Radiobutton(frm_parameter_k, text="k = 1 / slope", value=2, var=var_rd_k)
rd_k2.pack()
# Radio button 3rd
rd_k3 = tk.Radiobutton(frm_parameter_k, text="k = slope", value=3, var=var_rd_k)
rd_k3.pack()
# Default
var_rd_k.set(1)  # set default

# Parameter setting(c)
frm_parameter_c = ttk.Labelframe(root, relief="ridge", text="Parameter setting(omega)", labelanchor="n")
frm_parameter_c.pack(side='left', fill=tk.Y)
# Radio button
var_rd_c = tk.IntVar(root)
# Radio button 1st
rd_c1 = tk.Radiobutton(frm_parameter_c, text="omega = 1", value=1, var=var_rd_c)
rd_c1.pack()
# Radio button 2nd
rd_c2 = tk.Radiobutton(frm_parameter_c, text="omega = 1 / slope", value=2, var=var_rd_c)
rd_c2.pack()
# Radio button 3rd
rd_c3 = tk.Radiobutton(frm_parameter_c, text="omega = slope", value=3, var=var_rd_c)
rd_c3.pack()
# Default
var_rd_c.set(1)  # set default

# Light passes control
frm_lp = ttk.Labelframe(root, relief="ridge", text="Angle of light passes (degree)", labelanchor="n")
frm_lp.pack(side='left', fill=tk.Y)
scl_lp1_var = tk.StringVar(root)
scl_lp1 = tk.Scale(frm_lp, variable=scl_lp1_var, orient='horizontal', length=200, from_=-180, to=180)
scl_lp1.pack()
angle = int(theta_light_pass_1 * 180. / np.pi)
scl_lp1_var.set(angle)

# Observer time control
frm_ot = ttk.Labelframe(root, relief="ridge", text="Time of observer ( / 10)", labelanchor="n")
frm_ot.pack(side='left', fill=tk.Y)
scl_ot_var = tk.StringVar(root)
scl_ot = tk.Scale(frm_ot, variable=scl_ot_var, orient='horizontal', length=200, from_=0, to=50)
scl_ot.pack(side='left')
scl_ot_var.set(0)


# Start main loop
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
