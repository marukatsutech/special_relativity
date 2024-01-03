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
    pass


def reset_arrows():
    pass


def update(f):
    update_plots()


# Global variables
# Parameters
num_of_pass1 = 16
time_event = 1.

range_x_min = -3.
range_x_max = 3.
range_y_min = -2.
range_y_max = 2.

# Generate figure and axes
title_ax0 = "Light arrows"
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
xx_line_spatial_virtual = [x_min, x_max]
yy_line_spatial_virtual = [time_event, time_event]
line_world_virtual, = ax0.plot(xx_line_spatial_virtual, yy_line_spatial_virtual, color='darkorange', linestyle="--")

# Arrow light passes
for k in range(num_of_pass1):
    theta = k * 2 * np.pi / num_of_pass1
    xy_pass1 = [np.cos(theta), np.sin(theta)]
    arrow_pass1 = ax0.annotate('', xy=xy_pass1, xytext=[0., 0.],
                               arrowprops=dict(width=1, headwidth=6, headlength=6,
                                               facecolor='darkorange', edgecolor='darkorange'))

# Event points on spatial line of observer
for k in range(num_of_pass1):
    theta = k * 2 * np.pi / num_of_pass1
    xy_pass1 = [np.cos(theta), np.sin(theta)]
    # Event points on spatial line and slop of arrows
    gradient_x_div_t_pass1 = 0.
    if np.abs(xy_pass1[1]) > 0.00001:
        gradient_x_div_t_pass1 = xy_pass1[0] / xy_pass1[1]
        slope = str(round(gradient_x_div_t_pass1, 2))
    else:
        gradient_x_div_t_pass1 = xy_pass1[0] / 0.00001
        slope = 'Infinity'
    ax0.text(xy_pass1[0], xy_pass1[1], slope, c='black')
    xy_event_space = [gradient_x_div_t_pass1 * time_event, time_event]
    circle_event_space = patches.Circle(xy=xy_event_space, radius=0.05, color='darkorange')
    ax0.add_patch(circle_event_space)
    # pass line
    xx_line_pass1 = [xy_event_space[0], xy_pass1[0]]
    yy_line_pass1 = [xy_event_space[1], xy_pass1[1]]
    line_pass1, = ax0.plot(xx_line_pass1, yy_line_pass1, color='darkorange', linestyle="-.", linewidth=0.5)


# Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Start main loop
# anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
