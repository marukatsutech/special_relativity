# Double rotation
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
import matplotlib.patches as patches


def switch():
    global is_running
    if is_running:
        is_running = False
    else:
        is_running = True


def update(f):
    global cnt, line0, arrow1, l0_x, l0_y, l1_x, l1_y
    if is_running:
        tx_step.set_text(' Step=' + str(cnt))
        th0 = (theta0 + (2. * np.pi) / 360. * cnt) % (2. * np.pi)
        l0_x = r0 * np.cos(- th0 + np.pi / 2.)
        l0_y = r0 * np.sin(- th0 + np.pi / 2.)
        th1 = (theta0 + (2. * np.pi) / 360. * cnt * 2) % (2. * np.pi)
        l1_x = l0_x + r1 * np.cos(- th1 + np.pi / 2.)
        l1_y = l0_y + r1 * np.sin(- th1 + np.pi / 2.)
        line0.set_data([0., l0_x], [0., l0_y])
        arrow1.xy = [l1_x, l1_y]
        arrow1.set_position([l0_x, l0_y])
        cnt += 1
        tx_theta0.set_text(' Theta0=' + str(round(cnt % 360)) + "deg")
        tx_theta1.set_text(' Theta1=' + str(round((cnt * 2) % 720)) + "deg")


# Global variables
is_running = False

x_min = -4.
x_max = 4.
y_min = -4.
y_max = 4.

cnt = 0

num_of_points = 500

p0 = np.array([0., 0.])
r0 = 1.
theta0 = 0.
p1 = np.array([0., 2.])
r1 = 1.

# Generate figure and axes
title_ax0 = "Double rotation"
title_tk = title_ax0
fig = Figure()
ax0 = fig.add_subplot(111)
ax0.grid()
ax0.set_title(title_ax0)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_xlim(x_min, x_max)
ax0.set_ylim(y_min, y_max)
ax0.set_aspect("equal")

# Generate items
tx_step = ax0.text(x_min, y_max * 0.9, " Step=" + str(0))
tx_theta0 = ax0.text(x_min, y_max * 0.8, " Theta0=" + str(0) + "deg")
tx_theta1 = ax0.text(x_min, y_max * 0.7, " Theta1=" + str(0) + "deg")
circle = patches.Circle(xy=p0, radius=r0, fill=False, color='blue')
ax0.add_patch(circle)

x = np.linspace(x_min, x_max, num_of_points)

l0_x = r0 * np.cos(theta0 + np.pi / 2.)
l0_y = r0 * np.sin(theta0 + np.pi / 2.)
l1_x = l0_x + r1 * np.cos(theta0 * 2. + np.pi / 2.)
l1_y = l0_y + r1 * np.sin(theta0 * 2. + np.pi / 2.)
line0, = ax0.plot([0., l0_x], [0., l0_y], linewidth=2)
arrow1 = ax0.annotate('', xy=[l1_x, l1_y], xytext=[l0_x, l0_y],
                      arrowprops=dict(width=1, headwidth=6, headlength=6,
                                      facecolor='darkorange', edgecolor='darkorange'))
theta = np.linspace(0, 2 * np.pi, 100)
radius = 0.3

a0 = r0 * np.cos(- theta + np.pi / 2.)
b0 = r0 * np.sin(- theta + np.pi / 2.)
a1 = a0 + r1 * np.cos(- theta * 2. + np.pi / 2.)
b1 = b0 + r1 * np.sin(- theta * 2. + np.pi / 2.)
curve, = ax0.plot(a1, b1)

# Embed in Tkinter
root = tk.Tk()
root.title(title_tk)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

btn = tk.Button(root, text="Play/Pause", command=switch)
btn.pack()

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# main loop
anim = animation.FuncAnimation(fig, update, interval=50)
root.mainloop()

