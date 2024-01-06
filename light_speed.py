# Light speed

import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.patches as patches
import tkinter as tk
from tkinter import ttk
import matplotlib.ticker as ticker


def change_show_hide_status():
    global a1, a2, a3
    if var_w1.get():
        a1 = 1.
    else:
        a1 = 0.
    if var_w2.get():
        a2 = 1.
    else:
        a2 = 0.
    if var_w3.get():
        a3 = 1.
    else:
        a3 = 0.


def update_plots():
    global time_observer, xx_line_spatial, yy_line_spatial, line_spatial
    global line_pass_1, line_pass_2, line_pass_3, xx_guide, yy_guide
    global wave_curve_1, y_1, wave_curve_2, y_2, wave_curve_3, y_3, k, c
    global theta_light_pass_1, theta_light_pass_2, theta_light_pass_3
    global arrow_light_pass_1, arrow_light_pass_2, arrow_light_pass_3
    global slope_pass_1, slope_pass_2, slope_pass_3
    global xy_light_pass_1, xy_light_pass_2, xy_light_pass_3
    global circle_origin_1, circle_origin_2, circle_origin_3
    global lbl_lp1, lbl_lp2, lbl_lp3
    global wave_curve_supervised_3, wave_curve_supervised_multi
    time_observer = float(scl_ot_var.get()) / 10.
    # Spatial line of observer
    xx_line_spatial = [x_max, x_min]
    yy_line_spatial = [time_observer, time_observer]
    line_spatial.set_data(xx_line_spatial, yy_line_spatial)
    # Arrows of light passes
    theta_light_pass_1 = np.pi / 2. - float(scl_lp1_var.get()) * np.pi / 180.
    xy_light_pass_1 = [np.cos(theta_light_pass_1), np.sin(theta_light_pass_1)]
    arrow_light_pass_1.xy = xy_light_pass_1
    theta_light_pass_2 = np.pi / 2. - float(scl_lp2_var.get()) * np.pi / 180.
    xy_light_pass_2 = [np.cos(theta_light_pass_2), np.sin(theta_light_pass_2)]
    arrow_light_pass_2.xy = xy_light_pass_2
    theta_light_pass_3 = np.pi / 2. - float(scl_lp3_var.get()) * np.pi / 180.
    xy_light_pass_3 = [np.cos(theta_light_pass_3), np.sin(theta_light_pass_3)]
    arrow_light_pass_3.xy = xy_light_pass_3
    # Guide lines of light passes
    xx_guide = [0., np.cos(theta_light_pass_1) * x_max * 2.]
    yy_guide = [0., np.sin(theta_light_pass_1) * x_max * 2.]
    line_pass_1.set_data(xx_guide, yy_guide)
    xx_guide = [0., np.cos(theta_light_pass_2) * x_max * 2.]
    yy_guide = [0., np.sin(theta_light_pass_2) * x_max * 2.]
    line_pass_2.set_data(xx_guide, yy_guide)
    xx_guide = [0., np.cos(theta_light_pass_3) * x_max * 2.]
    yy_guide = [0., np.sin(theta_light_pass_3) * x_max * 2.]
    line_pass_3.set_data(xx_guide, yy_guide)
    # waves and markers
    if abs(xy_light_pass_1[1]) > 0.000001:
        slope_pass_1 = xy_light_pass_1[0] / xy_light_pass_1[1]
        if var_rd_k.get() == 1:
            k1 = 1.
        elif var_rd_k.get() == 2:
            k1 = 1. / slope_pass_1
        elif var_rd_k.get() == 3:
            k1 = slope_pass_1
        if var_rd_c.get() == 1:
            c1 = 1.
        elif var_rd_c.get() == 2:
            c1 = 1. / slope_pass_1
        elif var_rd_c.get() == 3:
            c1 = slope_pass_1
        y_1 = a1 * np.cos(2. * np.pi * (k1 * x - c1 * time_observer))
        wave_curve_1.set_ydata(y_1 + time_observer)
        # Origin markers
        circle_origin_1.set_center([c1 * time_observer, time_observer])
    if abs(xy_light_pass_2[1]) > 0.000001:
        slope_pass_2 = xy_light_pass_2[0] / xy_light_pass_2[1]
        if var_rd_k.get() == 1:
            k2 = 1.
        elif var_rd_k.get() == 2:
            k2 = 1. / slope_pass_2
        elif var_rd_k.get() == 3:
            k2 = slope_pass_2
        if var_rd_c.get() == 1:
            c2 = 1.
        elif var_rd_c.get() == 2:
            c2 = 1. / slope_pass_2
        elif var_rd_c.get() == 3:
            c2 = slope_pass_2
        y_2 = a2 * np.cos(2. * np.pi * (k2 * x - c2 * time_observer))
        wave_curve_2.set_ydata(y_2 + time_observer)
        # Origin markers
        circle_origin_2.set_center([c2 * time_observer, time_observer])
    if abs(xy_light_pass_3[1]) > 0.000001:
        slope_pass_3 = xy_light_pass_3[0] / xy_light_pass_3[1]
        if var_rd_k.get() == 1:
            k3 = 1.
        elif var_rd_k.get() == 2:
            k3 = 1. / slope_pass_3
        elif var_rd_k.get() == 3:
            k3 = slope_pass_3
        if var_rd_c.get() == 1:
            c3 = 1.
        elif var_rd_c.get() == 2:
            c3 = 1. / slope_pass_3
        elif var_rd_c.get() == 3:
            c3 = slope_pass_3
        y_3 = a3 * np.cos(2. * np.pi * (k3 * x - c3 * time_observer))
        wave_curve_3.set_ydata(y_3 + time_observer)
        # Origin markers
        circle_origin_3.set_center([c3 * time_observer, time_observer])
    # Supervised wave of 3 waves
    if var_ws3.get():
        wave_curve_supervised_3.set_ydata((y_1 + y_2 + y_3) / 3. + time_observer)
    else:
        wave_curve_supervised_3.set_ydata(x * 0. + time_observer)
    # Supervised wave of multi waves
    if var_wsm.get():
        y_multi = x * 0.
        for j in range(num_of_waves):
            # slope_n = j + 1.
            # cn = j + 1.
            slope_n = 0.1 * (j + 1)
            cn = 0.1 * (j + 1)
            if var_rd_k.get() == 1:
                kn = 1.
            elif var_rd_k.get() == 2:
                kn = 1. / slope_n
            elif var_rd_k.get() == 3:
                kn = slope_n
            if var_rd_c.get() == 1:
                cn = 1.
            elif var_rd_c.get() == 2:
                cn = 1. / slope_n
            elif var_rd_c.get() == 3:
                cn = slope_n
            y_n = np.cos(2. * np.pi * (kn * x - cn * time_observer))
            y_multi = y_multi + y_n
        wave_curve_supervised_multi.set_ydata(y_multi / num_of_waves / 1. + time_observer)
    else:
        wave_curve_supervised_multi.set_ydata(x * 0. + time_observer)
    # Slope info.
    lbl_lp1['text'] = "Light pass A (orange)(slope A=" + str(round(slope_pass_1, 2)) + "):"
    lbl_lp2['text'] = "Light pass B (green)(slope B=" + str(round(slope_pass_2, 2)) + "):"
    lbl_lp3['text'] = "Light pass C (blue)(slope C=" + str(round(slope_pass_3, 2)) + "):"


def update(f):
    update_plots()


# Global variables
# Parameters
time_observer = 0.
c = 1.
slope_pass_1 = 1.
slope_pass_2 = 2.
slope_pass_3 = 3.
theta_light_pass_1 = np.arctan2(1., 1.)
theta_light_pass_2 = np.arctan2(2., 1.)
theta_light_pass_3 = np.arctan2(3., 1.)
a1 = 1.
a2 = 1.
a3 = 1.
num_of_waves = 100

# Data array
range_x_min = -1.
range_x_max = 12.
range_y_min = -1.
range_y_max = 6.

# Generate figure and axes
title_ax0 = "Light speed"
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
xx_line_light = [0., y_max]
yy_line_light = [0., y_max]
line_light, = ax0.plot(xx_line_light, yy_line_light, color='gray', linestyle="-", linewidth=1)

for i in range(1, 13):
    circle_light = patches.Circle(xy=(0., 0.), radius=i, color='gray', fill=False, linestyle=":", linewidth=2)
    ax0.add_patch(circle_light)

# Spatial lines of observer
xx_line_spatial = [x_max, x_min]
yy_line_spatial = [time_observer, time_observer]
line_spatial, = ax0.plot(xx_line_spatial, yy_line_spatial, color='brown', linestyle="-", linewidth=2)

# Light passes Guide lines
xx_guide = [0., slope_pass_1 * y_max]
yy_guide = [0., y_max]
line_pass_1, = ax0.plot(xx_guide, yy_guide, color='darkorange', linewidth=1, linestyle="-")
xx_guide = [0., slope_pass_2 * y_max]
yy_guide = [0., y_max]
line_pass_2, = ax0.plot(xx_guide, yy_guide, color='green', linewidth=1, linestyle="-")
xx_guide = [0., slope_pass_3 * y_max]
yy_guide = [0., y_max]
line_pass_3, = ax0.plot(xx_guide, yy_guide, color='blue', linewidth=1, linestyle="-")

# Light passes
xy_light_pass_1 = [np.cos(theta_light_pass_1), np.sin(theta_light_pass_1)]
arrow_light_pass_1 = ax0.annotate('', xy=xy_light_pass_1, xytext=[0., 0.], arrowprops=dict(
    width=1, headwidth=4, headlength=4, facecolor='darkorange', edgecolor='orange'))
xy_light_pass_2 = [np.cos(theta_light_pass_2), np.sin(theta_light_pass_2)]
arrow_light_pass_2 = ax0.annotate('', xy=xy_light_pass_2, xytext=[0., 0.], arrowprops=dict(
    width=1, headwidth=4, headlength=4, facecolor='green', edgecolor='green'))
xy_light_pass_3 = [np.cos(theta_light_pass_3), np.sin(theta_light_pass_3)]
arrow_light_pass_3 = ax0.annotate('', xy=xy_light_pass_3, xytext=[0., 0.], arrowprops=dict(
    width=1, headwidth=4, headlength=4, facecolor='blue', edgecolor='blue'))

# Phase curve
x = np.linspace(x_min, x_max, 3000)
y_1 = x * 0.
wave_curve_1, = ax0.plot(x, y_1, linestyle='-', color="darkorange", linewidth=0.5, label='y=cos(2pi*(k_A*x-omega_A*t))')
y_2 = x * 0.
wave_curve_2, = ax0.plot(x, y_2, linestyle='-', color="green", linewidth=0.5, label='y=cos(2pi*(k_B*x-omega_B*t))')
y_3 = x * 0.
wave_curve_3, = ax0.plot(x, y_3, linestyle='-', color="blue", linewidth=0.5, label='y=cos(2pi*(k_C*x-omega_C*t))')
ax0.legend(loc='upper right')
y_3 = x * 0.
wave_curve_supervised_3, = ax0.plot(x, y_3, linestyle='-', color="brown",
                                    linewidth=2, label='Suppevised wave of 3 waves')
wave_curve_supervised_multi, = ax0.plot(x, y_3, linestyle='-', color="red",
                                        linewidth=3, label='Suppevised wave of 100 waves')
ax0.legend(loc='upper right')

# origin markers
circle_origin_1 = patches.Circle(xy=(0., 0.), radius=0.05, color='darkorange', linestyle="-", linewidth=1)
ax0.add_patch(circle_origin_1)
circle_origin_2 = patches.Circle(xy=(0., 0.), radius=0.05, color='green', linestyle="-", linewidth=1)
ax0.add_patch(circle_origin_2)
circle_origin_3 = patches.Circle(xy=(0., 0.), radius=0.05, color='blue', linestyle="-", linewidth=1)
ax0.add_patch(circle_origin_3)

# Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Parameter setting(k)
frm_parameter_k = ttk.Labelframe(root, relief="ridge", text="Parameter setting(k)", labelanchor="n")
frm_parameter_k.pack(side='left', fill=tk.Y)
# Radio button
var_rd_k = tk.IntVar(root)
# Radio button 1st
rd_k1 = tk.Radiobutton(frm_parameter_k, text="k(n) = 1", value=1, var=var_rd_k)
rd_k1.pack()
# Radio button 2nd
rd_k2 = tk.Radiobutton(frm_parameter_k, text="k(n) = 1 / slope(n)", value=2, var=var_rd_k)
rd_k2.pack()
# Radio button 3rd
rd_k3 = tk.Radiobutton(frm_parameter_k, text="k(n) = slope(n)", value=3, var=var_rd_k)
rd_k3.pack()
# Default
var_rd_k.set(1)  # set default

# Parameter setting(c)
frm_parameter_c = ttk.Labelframe(root, relief="ridge", text="Parameter setting(omega)", labelanchor="n")
frm_parameter_c.pack(side='left', fill=tk.Y)
# Radio button
var_rd_c = tk.IntVar(root)
# Radio button 1st
rd_c1 = tk.Radiobutton(frm_parameter_c, text="omega(n) = 1", value=1, var=var_rd_c)
rd_c1.pack()
# Radio button 2nd
rd_c2 = tk.Radiobutton(frm_parameter_c, text="omega(n) = 1 / slope(n)", value=2, var=var_rd_c)
rd_c2.pack()
# Radio button 3rd
rd_c3 = tk.Radiobutton(frm_parameter_c, text="omega(n) = slope(n))", value=3, var=var_rd_c)
rd_c3.pack()
# Default
var_rd_c.set(1)  # set default

# Checkbutton for show/hide waves
frm_cs = ttk.Labelframe(root, relief="ridge", text="Show/hide waves", labelanchor="n")
frm_cs.pack(side='left', fill=tk.Y)
var_w1 = tk.BooleanVar(root)    # Variable for checkbutton
check_w1 = tk.Checkbutton(frm_cs, text="wave A(Orange):", variable=var_w1, command=change_show_hide_status)
check_w1.pack()
var_w1.set(True)
var_w2 = tk.BooleanVar(root)    # Variable for checkbutton
check_w2 = tk.Checkbutton(frm_cs, text="wave B (Green):", variable=var_w2, command=change_show_hide_status)
check_w2.pack()
var_w2.set(True)
var_w3 = tk.BooleanVar(root)    # Variable for checkbutton
check_w3 = tk.Checkbutton(frm_cs, text="wave C (Blue):", variable=var_w3, command=change_show_hide_status)
check_w3.pack()
var_w3.set(True)
var_ws3 = tk.BooleanVar(root)    # Variable for checkbutton
check_ws3 = tk.Checkbutton(frm_cs, text="Supervised wave of 3 waves(Brown):",
                           variable=var_ws3, command=change_show_hide_status)
check_ws3.pack()
var_ws3.set(True)
var_wsm = tk.BooleanVar(root)    # Variable for checkbutton
check_wsm = tk.Checkbutton(frm_cs, text="Supervised wave of 100 waves(Red)",
                           variable=var_wsm, command=change_show_hide_status)
check_wsm.pack()
var_wsm.set(True)


# Light passes control
frm_lp = ttk.Labelframe(root, relief="ridge", text="Angle of light passes (degree)", labelanchor="n")
frm_lp.pack(side='left', fill=tk.Y)
lbl_lp1 = tk.Label(frm_lp, text="Light pass 1 (orange):")
lbl_lp1.pack()
scl_lp1_var = tk.StringVar(root)
scl_lp1 = tk.Scale(frm_lp, variable=scl_lp1_var, orient='horizontal', length=200, from_=-180, to=180)
scl_lp1.pack()
angle = int(theta_light_pass_1 * 180. / np.pi)
scl_lp1_var.set(angle)

lbl_lp2 = tk.Label(frm_lp, text="Light pass 2 (green):")
lbl_lp2.pack()
scl_lp2_var = tk.StringVar(root)
scl_lp2 = tk.Scale(frm_lp, variable=scl_lp2_var, orient='horizontal', length=200, from_=-180, to=180)
scl_lp2.pack()
angle = int(theta_light_pass_2 * 180. / np.pi)
scl_lp2_var.set(angle)

lbl_lp3 = tk.Label(frm_lp, text="Light pass 3 (blue):")
lbl_lp3.pack()
scl_lp3_var = tk.StringVar(root)
scl_lp3 = tk.Scale(frm_lp, variable=scl_lp3_var, orient='horizontal', length=200, from_=-180, to=180)
scl_lp3.pack()
angle = int(theta_light_pass_3 * 180. / np.pi)
scl_lp3_var.set(angle)

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
