"""
Body launched under the horizon angle
"""
import math
import tkinter as tk

from converter import d2s
from axis import draw_axis


# Number of frames
N = 50

V0 = 100  # Начальная скорость
alpha = 80  # Угол
g = 9.8  # Ускорение свободного падения


CANVAS_SIZE = (680, 360)
SCALE = (0.35, 0.35)


# Counted constants
CANVAS_WIDTH, CANVAS_HEIGHT = CANVAS_SIZE

T_START = 0  # Start time
T_FINAL = 2*V0 * math.sin(math.radians(alpha)) / g  # Fly time

# Period between frames
PERIOD = int(round(T_FINAL / N, 5) * 1000)

RAD = math.radians(alpha)


def trajectory(t):
    """Return Descartes point at time"""
    x = V0 * t * math.cos(RAD)
    y = V0 * t * math.sin(RAD) - g*t*t/2
    return x, y


def draw_trajectory(t, xp, yp):
    xc, yc = d2s(trajectory(t), CANVAS_SIZE, SCALE)

    if yc < CANVAS_HEIGHT // 2:

        canvas.create_line(xp, yp, xc, yc)

        canvas.after(PERIOD, lambda: draw_trajectory(t+1, xc, yc))


MASTER = tk.Tk()
MASTER.title('ЛР №4. Косыгин К.С.')
canvas = tk.Canvas(MASTER, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

draw_axis(canvas, 2, CANVAS_SIZE)

x0, y0 = d2s(trajectory(T_START), CANVAS_SIZE, SCALE)  # x(0), y(0)

MASTER.after(1, lambda: draw_trajectory(1, x0, y0))

MASTER.mainloop()
