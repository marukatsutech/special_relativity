# Projections of boson and fermion

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.patches as patches
import tkinter as tk
from tkinter import ttk
import matplotlib.ticker as ticker


def update(f):
    pass
    #  update_plots()


# Global variables
num_of_points_x = 100

# Parameters
range_x_min = -3.
range_x_max = 3.
range_y_min = -2.
range_y_max = 4.

# Data array
x = np.linspace(range_x_min, range_x_max, num_of_points_x)
y_line = x + 1.
y_parabola = x ** 2. + 1.

# Generate figure and axes
title_ax0 = "Boson"
title_ax1 = "Fermion"
title_tk = "Projections of boson and fermion"
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max

fig = Figure()
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)

ax0.set_title(title_ax0)
ax0.set_xlabel("x of observer")
ax0.set_ylabel("t of observer")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")
ax0.grid()

ax1.set_title(title_ax1)
ax1.set_xlabel("x of observer")
ax1.set_ylabel("t of observer")
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)
ax1.set_aspect("equal")
ax1.grid()

# Ticks
x_ticks = []
for ix in range(int(x_min), int(x_max)):
    x_ticks.append(ix)
ax0.xaxis.set_major_locator(ticker.FixedLocator(x_ticks))
ax1.xaxis.set_major_locator(ticker.FixedLocator(x_ticks))
y_ticks = []
for iy in range(int(y_min), int(y_max)):
    y_ticks.append(iy)
ax0.yaxis.set_major_locator(ticker.FixedLocator(y_ticks))
ax0.set_xticklabels(x_ticks, fontsize=8)
ax0.set_yticklabels(y_ticks, fontsize=8)
ax1.yaxis.set_major_locator(ticker.FixedLocator(y_ticks))
ax1.set_xticklabels(x_ticks, fontsize=8)
ax1.set_yticklabels(y_ticks, fontsize=8)

# Generate graphic items

# Light circles
circle_light0 = patches.Circle(xy=(0., 0.), radius=1., color='darkorange', fill=False, linestyle="--")
ax0.add_patch(circle_light0)
circle_light1 = patches.Circle(xy=(0., 0.), radius=1., color='darkorange', fill=False, linestyle="--")
ax1.add_patch(circle_light1)

# Spatial lines
xx_line_spatial = [x_min, x_max]
yy_line_spatial = [1., 1.]
line_spatial0, = ax0.plot(xx_line_spatial, yy_line_spatial, color='green', linestyle="-")
line_spatial1, = ax1.plot(xx_line_spatial, yy_line_spatial, color='green', linestyle="-")

# Line and Parabola
plot_line, = ax0.plot(x, y_line, color='blue', linewidth=1)
plot_parabola, = ax1.plot(x, y_parabola, color='blue', linewidth=1)

# Projection points
x_ = 0.
y_ = 0.
for i_ in range(1, 10):
    x_ = x_ + 0.5
    y_ = y_ + 0.5

    circle_dot0 = patches.Circle(xy=[x_, y_ + 1.], radius=0.05, color='blue')
    ax0.add_patch(circle_dot0)
    line_guide_h0, = ax0.plot([0., x_], [y_ + 1., y_ + 1.], color='blue', linewidth=0.5)
    line_guide_v0, = ax0.plot([x_, x_], [1., y_ + 1.], color='blue', linewidth=0.5)
    line_slope0, = ax0.plot([x_, 0.], [1., 0.], color='blue', linewidth=0.5)

    circle_dot1 = patches.Circle(xy=[np.sqrt(y_), y_ + 1.], radius=0.05, color='blue')
    ax1.add_patch(circle_dot1)
    line_guide_h1, = ax1.plot([0., np.sqrt(y_)], [y_ + 1., y_ + 1.], color='blue', linewidth=0.5)
    line_guide_v1, = ax1.plot([np.sqrt(y_), np.sqrt(y_)], [1., y_ + 1.], color='blue', linewidth=0.5)
    line_slope1, = ax1.plot([np.sqrt(y_), 0.], [1., - np.sqrt(y_) / y_ + 1.], color='blue', linewidth=0.5)

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
