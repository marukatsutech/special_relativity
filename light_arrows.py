# Light arrows

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.patches as patches
import tkinter as tk
from tkinter import ttk
import matplotlib.ticker as ticker


def update_plots():
    global secondary_circles, theta, xy_pass1
    global slopes, event_points, pass_lines, slope, xy_event_space, line_spatial
    # Secondary waves
    for i in range(num_of_pass1):
        if var_rd_sw.get() == 1:
            secondary_circles[i].set_center([out_of_range, out_of_range])
        elif var_rd_sw.get() == 2:
            theta = i * 2 * np.pi / num_of_pass1
            xy_pass1 = [np.cos(theta), np.sin(theta)]
            secondary_circles[i].set_center(xy_pass1)
        else:
            theta = i * 2 * np.pi / num_of_pass1
            xy_pass1 = [np.cos(theta), np.sin(theta)]
            if np.abs(xy_pass1[1]) > 0.00001:
                slp = xy_pass1[0] / xy_pass1[1]
                secondary_circles[i].set_center([slp, 1.])
            else:
                secondary_circles[i].set_center([out_of_range, out_of_range])
    # Event points on spatial line and slop of arrows
    for j in range(num_of_pass1):
        if var_rd_op.get() == 1:
            event_points[j].set_center([out_of_range, out_of_range])
            x_ = [out_of_range, out_of_range]
            y_ = [out_of_range, out_of_range]
            pass_lines[j].set_xdata(x_)
            pass_lines[j].set_ydata(y_)
            x_ = [out_of_range, out_of_range]
            y_ = [out_of_range, out_of_range]
            line_spatial.set_xdata(x_)
            line_spatial.set_ydata(y_)
        else:
            theta = j * 2 * np.pi / num_of_pass1
            xy_pass1 = [np.cos(theta), np.sin(theta)]
            slope = 0.
            if np.abs(xy_pass1[1]) > 0.00001:
                slope = xy_pass1[0] / xy_pass1[1]
            else:
                slope = xy_pass1[0] / 0.00001
            xy_event_space = [slope * time_event, time_event]
            event_points[j].set_center(xy_event_space)
            # pass line
            x_ = [xy_event_space[0], xy_pass1[0]]
            y_ = [xy_event_space[1], xy_pass1[1]]
            pass_lines[j].set_xdata(x_)
            pass_lines[j].set_ydata(y_)
            # Spatial line of observer
            x_ = [x_min, x_max]
            y_ = [time_event, time_event]
            line_spatial.set_xdata(x_)
            line_spatial.set_ydata(y_)
        if var_rd_sp.get() == 1:
            slopes[j].set_position([out_of_range, out_of_range])
        else:
            theta = j * 2 * np.pi / num_of_pass1
            xy_pass1 = [np.cos(theta), np.sin(theta)]
            slopes[j].set_position([xy_pass1[0], xy_pass1[1]])



def update(f):
    update_plots()


# Global variables
out_of_range = 100
# Parameters
num_of_pass1 = 16
time_event = 1.

range_x_min = -3.
range_x_max = 3.
range_y_min = -3.
range_y_max = 3.

# Generate figure and axes
title_ax0 = "Circular wave (light arrows) in Minkowski space"
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
ax0.set_xticklabels(x_ticks, fontsize=8)
ax0.set_yticklabels(y_ticks, fontsize=8)

# Generate graphic items

# Light circles and lines
circle_light1 = patches.Circle(xy=(0., 0.), radius=1., color='darkorange', fill=False, linestyle="--")
ax0.add_patch(circle_light1)

# World and space lines
xx_line_spatial = [out_of_range, out_of_range]
yy_line_spatial = [out_of_range, out_of_range]
line_spatial, = ax0.plot(xx_line_spatial, yy_line_spatial, color='darkorange', linestyle="--")

# Arrow light passes
for k in range(num_of_pass1):
    theta = k * 2 * np.pi / num_of_pass1
    xy_pass1 = [np.cos(theta), np.sin(theta)]
    arrow_pass1 = ax0.annotate('', xy=xy_pass1, xytext=[0., 0.],
                               arrowprops=dict(width=1, headwidth=6, headlength=6,
                                               facecolor='darkorange', edgecolor='darkorange'))

# Event points on spatial line of observer
event_points = []
pass_lines = []
slopes = []
for k in range(num_of_pass1):
    theta = k * 2 * np.pi / num_of_pass1
    xy_pass1 = [np.cos(theta), np.sin(theta)]
    # Event points on spatial line and slop of arrows
    slope = 0.
    if np.abs(xy_pass1[1]) > 0.00001:
        slope = xy_pass1[0] / xy_pass1[1]
        slope_str = str(round(slope, 2))
    else:
        slope = xy_pass1[0] / 0.00001
        slope_str = 'Infinity'
    txt_slope = ax0.text(out_of_range, out_of_range, slope_str, c='black')
    slopes.append(txt_slope)
    xy_event_space = [out_of_range, out_of_range ]
    circle_event_space = patches.Circle(xy=xy_event_space, radius=0.05, color='darkorange')
    ax0.add_patch(circle_event_space)
    event_points.append(circle_event_space)
    # pass line
    xx_line_pass1 = [out_of_range, out_of_range ]
    yy_line_pass1 = [out_of_range, out_of_range ]
    line_pass1, = ax0.plot(xx_line_pass1, yy_line_pass1, color='darkorange', linestyle="-.", linewidth=0.5)
    pass_lines.append(line_pass1)


# Secondary wave circles
secondary_circles = []
for m in range(num_of_pass1):
    circle_secondary = patches.Circle(xy=(out_of_range, out_of_range),
                                      radius=1., color='green', fill=False, linestyle="--")
    ax0.add_patch(circle_secondary)
    secondary_circles.append(circle_secondary)

# Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Parameter setting: Slopes
frm_parameter_sp = ttk.Labelframe(root, relief="ridge", text="Slope (=speed) of arrows", labelanchor="n")
frm_parameter_sp.pack(side='left', fill=tk.Y)
# Radio button
var_rd_sp = tk.IntVar(root)
# Radio button 1st
rd_sp_hide = tk.Radiobutton(frm_parameter_sp, text="Hide", value=1, var=var_rd_sp)
rd_sp_hide.pack()
# Radio button 2nd
rd_sp_show = tk.Radiobutton(frm_parameter_sp, text="Show", value=2, var=var_rd_sp)
rd_sp_show.pack()
# Default
var_rd_sp.set(1)  # set default

# Parameter setting: Event points on spatial line of observer
frm_parameter_op = ttk.Labelframe(root, relief="ridge", text="Observation points", labelanchor="n")
frm_parameter_op.pack(side='left', fill=tk.Y)
# Radio button
var_rd_op = tk.IntVar(root)
# Radio button 1st
rd_op_hide = tk.Radiobutton(frm_parameter_op, text="Hide", value=1, var=var_rd_op)
rd_op_hide.pack()
# Radio button 2nd
rd_op_show = tk.Radiobutton(frm_parameter_op, text="Show", value=2, var=var_rd_op)
rd_op_show.pack()
# Default
var_rd_op.set(1)  # set default

# Parameter setting: secondary waves
frm_parameter_sw = ttk.Labelframe(root, relief="ridge", text="Secondary waves", labelanchor="n")
frm_parameter_sw.pack(side='left', fill=tk.Y)
# Radio button
var_rd_sw = tk.IntVar(root)
# Radio button 1st
rd_sw_hide = tk.Radiobutton(frm_parameter_sw, text="Hide", value=1, var=var_rd_sw)
rd_sw_hide.pack()
# Radio button 2nd
rd_sw_on_circle = tk.Radiobutton(frm_parameter_sw, text="On light circle", value=2, var=var_rd_sw)
rd_sw_on_circle.pack()
# Radio button 3rd
rd_sw_on_spatial = tk.Radiobutton(frm_parameter_sw, text="On spatial line of observer", value=3, var=var_rd_sw)
rd_sw_on_spatial.pack()
# Default
var_rd_sw.set(1)  # set default

# Start main loop
anim = animation.FuncAnimation(fig, update, interval=out_of_range )
root.mainloop()
