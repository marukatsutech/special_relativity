# Superposed wave

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
import tkinter as tk


def change_kn_min(value):
    global kn_min
    kn_min = float(value)


def change_kn_max(value):
    global kn_max
    kn_max = float(value)


def change_num_of_waves(value):
    global num_of_waves
    num_of_waves = int(float(value))


def change_kn_step():
    global kn_step, lbl_k_step
    kn_step = (kn_max - kn_min) / num_of_waves
    lbl_k_step['text'] = " Step of kn:" + str(kn_step)


def set_axis():
    global title_tk
    title_tk = "Superposed wave"
    root.title(title_tk)
    ax0.set_xlim(x_min, x_max)
    ax0.set_ylim(y_min, y_max)
    ax0.set_title('y=cos(2*pi*kn*x)')
    ax0.set_ylabel('y')
    ax0.grid()
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_title('')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid()


def update(f):
    ax0.cla()  # Clear ax
    ax1.cla()  # Clear ax
    set_axis()
    # Draw curve
    change_kn_step()
    y_superposed = x * 0.
    for i in range(num_of_waves):
        kn = kn_min + kn_step * i
        y = np.cos(2 * np.pi * (kn * x))
        y_superposed = y_superposed + y
        ax0.plot(x, y, linestyle='-', linewidth=0.5)
    y_superposed = y_superposed / num_of_waves
    ax1.plot(x, y_superposed, linestyle='-', label="Superposed wave")
    ax1.legend(prop={"size": 8}, loc="upper right")


# Global variables
# Data array
range_x_min = -4
range_x_max = 4.
range_y_min = -2.
range_y_max = 2.

# Generate figure and axes
title_ax0 = "Supervised wave"
title_tk = title_ax0
x_min = range_x_min
x_max = range_x_max
y_min = range_y_min
y_max = range_y_max

# Parameter of sine wave
num_of_waves = 1
kn_min = 1.
kn_max = 10.
kn_step = (kn_max - kn_min) / num_of_waves

# Generate line space
x = np.linspace(x_min, x_max, 2000)

# Generate tkinter
root = tk.Tk()

# Generate figure and axes
fig = Figure()
ax0 = fig.add_subplot(211)
ax1 = fig.add_subplot(212)

# Embed a figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

# Toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# kn min
label_kn_min = tk.Label(root, text="kn(min)")
label_kn_min.pack(side='left')
var_kn_min = tk.StringVar(root)  # variable for spinbox-value
var_kn_min.set(kn_min)  # Initial value
s_kn_min = tk.Spinbox(
    root, textvariable=var_kn_min, format="%.1f", from_=0, to=10, increment=0.1,
    command=lambda: change_kn_min(var_kn_min.get()), width=5
    )
s_kn_min.pack(side='left')

# kn max
label_kn_max = tk.Label(root, text="kn(max)")
label_kn_max.pack(side='left')
var_kn_max = tk.StringVar(root)  # variable for spinbox-value
var_kn_max.set(kn_max)  # Initial value
s_kn_max = tk.Spinbox(
    root, textvariable=var_kn_max, format="%.1f", from_=0, to=100, increment=1,
    command=lambda: change_kn_max(var_kn_max.get()), width=5
    )
s_kn_max.pack(side='left')

# Number of waves
label_nw = tk.Label(root, text="Number of waves")
label_nw.pack(side='left')
var_nw = tk.StringVar(root)  # variable for spinbox-value
var_nw.set(num_of_waves)  # Initial value
s_nw = tk.Spinbox(
    root, textvariable=var_nw, format="%.1f", from_=1, to=100, increment=1,
    command=lambda: change_num_of_waves(var_nw.get()), width=5
    )
s_nw.pack(side='left')


# Step of kn
text_k_step = " Step of kn:" + str(kn_step)
lbl_k_step = tk.Label(root, text=text_k_step)
lbl_k_step.pack(side='left')

# main loop
set_axis()

# Start main loop
anim = animation.FuncAnimation(fig, update, interval=100)
root.mainloop()

