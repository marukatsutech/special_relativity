# Over light speed

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.patches as patches
import tkinter as tk
from tkinter import ttk
import matplotlib.ticker as ticker


def update_sin_on_times(phase):
    global x_t1, y_t1, sin_on_time1, x_t2, y_t2, sin_on_time2
    x_t1 = angle * 0.
    y_t1 = angle * 0.
    x_t2 = angle * 0.
    y_t2 = angle * 0.
    for jj in range(num_of_points_angle):
        x_ = np.sin(angle[jj])
        y_ = np.cos(angle[jj])
        if np.abs(y_) > 0.00001:
            grad_t1 = x_ / y_
            y_t1[jj] = 1. + 0.1 * np.sin((angle[jj] - phase) * wave_number)
            x_t1[jj] = grad_t1 * 1.
            y_t2[jj] = 2. + 0.1 * np.sin((angle[jj] - phase) * wave_number)
            x_t2[jj] = grad_t1 * 2.
    sin_on_time1.set_xdata(x_t1)
    sin_on_time1.set_ydata(y_t1)
    sin_on_time2.set_xdata(x_t2)
    sin_on_time2.set_ydata(y_t2)


def update_sin_on_circles(phase):
    global sin_on_circle1, sin_on_circle2
    x_sin_update = (1. + 0.1 * np.sin((angle - phase) * wave_number)) * np.sin(angle)
    y_sin_update = (1. + 0.1 * np.sin((angle - phase) * wave_number)) * np.cos(angle)
    sin_on_circle1.set_xdata(x_sin_update)
    sin_on_circle1.set_ydata(y_sin_update)
    x_sin_update = 2. * (1. + 0.05 * np.sin((angle - phase) * wave_number)) * np.sin(angle)
    y_sin_update = 2. * (1. + 0.05 * np.sin((angle - phase) * wave_number)) * np.cos(angle)
    sin_on_circle2.set_xdata(x_sin_update)
    sin_on_circle2.set_ydata(y_sin_update)


def set_wave_number(value):
    global wave_number
    wave_number = float(value)
    update_plots()


def mouse_motion(event):
    global lbl_info_0
    if event.dblclick == 1:
        print("double click")
        pass
    elif event.button == 1:
        print("left click")
        if str(event.xdata) != "None" and str(event.ydata) != "None":
            print(event.xdata, event.ydata)
            lbl_info_0['text'] = "Mouse point x,y:" + str(event.xdata) + "," + str(event.ydata)
    elif event.button == 3:
        print("right click")
        pass


def update_plots():
    global xy_dot0, dot0, xx_line0, yy_line0, line0, gradient, xy_dot1, dot1, xx_line1, yy_line1, line1
    global xy_dot2, line2, xx_line2, yy_line2
    angle_dot0 = cnt / 100
    x_dot0 = np.sin(angle_dot0)
    y_dot0 = np.cos(angle_dot0)
    xy_dot0 = [x_dot0, y_dot0]
    dot0.set_center(xy_dot0)
    xx_line0 = [0., np.sin(angle_dot0)]
    yy_line0 = [0., np.cos(angle_dot0)]
    line0.set_data(xx_line0, yy_line0)
    if np.abs(y_dot0) > 0.00001:
        gradient = x_dot0 / y_dot0
        y_dot1 = 1.
        x_dot1 = gradient * y_dot1
        xy_dot1 = [x_dot1, y_dot1]
        dot1.set_center(xy_dot1)
        xx_line1 = [x_dot0, x_dot1]
        yy_line1 = [y_dot0, y_dot1]
        line1.set_data(xx_line1, yy_line1)
        y_dot2 = 2.
        x_dot2 = gradient * y_dot2
        xy_dot2 = [x_dot2, y_dot2]
        dot2.set_center(xy_dot2)
        xx_line2 = [x_dot1, x_dot2]
        yy_line2 = [y_dot1, y_dot2]
        line2.set_data(xx_line2, yy_line2)
    update_sin_on_circles(angle_dot0)
    update_sin_on_times(angle_dot0)


def reset_plots():
    global is_play, cnt, tx_step
    is_play = False
    cnt = 0
    tx_step.set_text("Step=" + str(cnt))
    update_plots()


def step():
    global cnt
    cnt += 1
    tx_step.set_text("Step=" + str(cnt))
    update_plots()


def switch():
    global is_play
    if is_play:
        is_play = False
    else:
        is_play = True
    tx_step.set_text("Step=" + str(cnt))


def update(f):
    global tx_step, cnt
    if is_play:
        tx_step.set_text("Step=" + str(cnt))
        tx_gradient.set_text("Gradient=" + str(round(gradient, 3)))
        update_plots()
        cnt += 1


# Global variables
gradient = 0.
wave_number = 16

# Animation control
cnt = 0
is_play = False

# Parameters

# Data array
num_of_points_angle = 1000
range_angle_min = 0.
range_angle_max = 2 * np.pi
range_x_min = -8.
range_x_max = 8.
range_y_min = -3.
range_y_max = 3.
angle = np.linspace(range_angle_min, range_angle_max, num_of_points_angle)
x = np.sin(angle)
y = np.cos(angle)
# circle1, = ax0.plot(x, y, linestyle='-', color='grey')

# Sine curve on circle1, 2 (Temporary setting. Update later by update_sin_on_circle0())
# x_sin = np.sin(angle * 0.25) * np.sin(angle)
# y_sin = np.sin(angle * 0.25) * np.cos(angle)
x_sin1 = np.sin(angle)
y_sin1 = np.cos(angle)
x_sin2 = 2. * np.sin(angle)
y_sin2 = 2. * np.cos(angle)

# Sine curve on time = 1, 2 (Temporary setting. Update later by update_sin_on_time1())
x_t1 = angle * 0.
y_t1 = angle * 0.
x_t2 = angle * 0.
y_t2 = angle * 0.

# Generate figure and axes
title_ax0 = "Over light speed"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max

fig = Figure()
ax0 = fig.add_subplot(111)
ax0.set_title(title_ax0)
ax0.set_xlabel("x")
ax0.set_ylabel("t")
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")
ax0.grid()
# ax0.invert_yaxis()

x_ticks = []
for ix in range(int(x_min), int(x_max)):
    x_ticks.append(ix)
ax0.xaxis.set_major_locator(ticker.FixedLocator(x_ticks))
y_ticks = []
for iy in range(int(y_min), int(y_max)):
    y_ticks.append(iy)
ax0.yaxis.set_major_locator(ticker.FixedLocator(y_ticks))
# ax0.set_xticklabels(x_ticks, fontsize=6)
# ax0.set_yticklabels(y_ticks, fontsize=6)

# Generate graphic items
# Counter text
tx_step = ax0.text(x_min, y_max * 0.9, "Step=" + str(0))
tx_gradient = ax0.text(x_min, y_max * 0.7, "Gradient=" + str(0))

# Guide circles and lines
circle1 = patches.Circle(xy=(0, 0.), radius=1., color='grey', fill=False)
ax0.add_patch(circle1)
circle2 = patches.Circle(xy=(0, 0.), radius=2., color='grey', fill=False)
ax0.add_patch(circle2)

for ii in range(- 100, 101):
    gradient_guide = ii * 0.5
    y_guide = 3.
    x_guide = gradient_guide * y_guide
    xx_guide = [-x_guide, x_guide]
    yy_guide = [-3., 3.]
    guide, = ax0.plot(xx_guide, yy_guide, color='grey', linewidth=1, linestyle=":")

xx_guide0 = [- 3., 3.]
yy_guide0 = [-3., 3.]
guide0, = ax0.plot(xx_guide0, yy_guide0, color='grey')
xx_guide1 = [3., - 3.]
yy_guide1 = [-3., 3.]
guide1, = ax0.plot(xx_guide1, yy_guide1, color='grey')

# Dots and lines
xy_dot0 = [0., 1.]
dot0 = patches.Circle(xy=xy_dot0, radius=0.05, color='red')
ax0.add_patch(dot0)
xx_line0 = [0., 0.]
yy_line0 = [0., 1.]
line0, = ax0.plot(xx_line0, yy_line0, color='red')

xy_dot1 = [0., 1.]
dot1 = patches.Circle(xy=xy_dot1, radius=0.05, color='blue')
ax0.add_patch(dot1)
xx_line1 = [0., 0.]
yy_line1 = [1., 1.]
line1, = ax0.plot(xx_line1, yy_line1, color='blue', linestyle="--")

xy_dot2 = [0., 2.]
dot2 = patches.Circle(xy=xy_dot2, radius=0.05, color='green')
ax0.add_patch(dot2)
xx_line2 = [0., 0.]
yy_line2 = [1., 2.]
line2, = ax0.plot(xx_line2, yy_line2, color='green', linestyle="--")

# Sine curves
sin_on_circle1, = ax0.plot(x_sin1, y_sin1, linestyle='-', color='red', linewidth=1)
sin_on_circle2, = ax0.plot(x_sin2, y_sin2, linestyle='-', color='orange', linewidth=1)
update_sin_on_circles(0.)
sin_on_time1, = ax0.plot(x_t1, y_t1, linestyle='-', color='blue', linewidth=1)
sin_on_time2, = ax0.plot(x_t2, y_t2, linestyle='-', color='green', linewidth=1)
update_sin_on_times(0.)

# Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')
canvas.mpl_connect('button_press_event', mouse_motion)

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Animation control
# Frame
frm_ac = ttk.Labelframe(root, relief="ridge", text="Animation control", labelanchor="n", width=100)
frm_ac.pack(side='left', fill=tk.Y)
# Play and pause button
btn_pp = tk.Button(frm_ac, text="Play/Pause", command=lambda: switch())
btn_pp.pack()
# Step button
btn_pp = tk.Button(frm_ac, text="Step", command=step)
btn_pp.pack()
# Clear button
btn_clr = tk.Button(frm_ac, text="Reset plots", command=lambda: reset_plots())
btn_clr.pack()

# Parameter setting
frm_parameter = ttk.Labelframe(root, relief="ridge", text="Parameter setting", labelanchor="n")
frm_parameter.pack(side='left', fill=tk.Y)
lbl_wave_number = tk.Label(frm_parameter, text="Wave number:")
lbl_wave_number.pack()
var_wave_number = tk.StringVar(root)  # variable for spinbox-value
var_wave_number.set(wave_number)  # Initial value
spn_aaa = tk.Spinbox(
    frm_parameter, textvariable=var_wave_number, format="%.1f", from_=1., to=100., increment=1.,
    command=lambda: set_wave_number(var_wave_number.get()), width=6
    )
spn_aaa.pack()

'''
# Option
# Frame
frm_cp = ttk.Labelframe(root, relief="ridge", text="Option", labelanchor="n")
frm_cp.pack(side='left', fill=tk.Y)
var_radio_click_option = tk.IntVar(root)
# Radio button 1st
rd_op0 = tk.Radiobutton(frm_cp, text="Option 0", value=0, var=var_radio_click_option)
rd_op0.pack()
# Radio button 2st
rd_op1 = tk.Radiobutton(frm_cp, text="Option 1", value=1, var=var_radio_click_option)
rd_op1.pack()
# Set default of radio buttons
var_radio_click_option.set(0)
'''

# Information of a cell clicked
# Frame
frm_info = ttk.Labelframe(root, relief="ridge", text="Information", labelanchor="n")
frm_info.pack(side='left', fill=tk.Y)
# Information label
lbl_info_0 = tk.Label(frm_info, text="Mouse point x,y:")
lbl_info_0.pack()

# Initialize data
update_plots()

# Draw animation
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()
