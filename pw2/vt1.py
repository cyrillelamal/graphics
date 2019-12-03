import sys
import tkinter as tk
import numpy as np

sys.path.insert(0, '..')
from converter import d2s, TRANSFORMATIONS as TR


CANVAS_SIZE = (640, 480)
SCALE = (22, 22)

PERIOD = 1000  # ms
SCENARIO = [
    TR.get('y=x'),
    TR.get('y=0'),
]


# Counted constants
CANVAS_WIDTH, CANVAS_HEIGHT = CANVAS_SIZE


TRIANGLE = [
    (8, 1),
    (7, 3),
    (6, 2)
]


def draw_triangle(points=None):
    canvas.delete('all')

    points = TRIANGLE if points is None else points
    num_of_points = len(points)

    for i in range(num_of_points):
        p1 = points[i]
        p2 = points[0] if i == num_of_points - 1 else points[i+1]

        p1 = d2s(p1, CANVAS_SIZE, SCALE)
        p2 = d2s(p2, CANVAS_SIZE, SCALE)
        canvas.create_line(*p1, *p2)


def transform(i=0):
    if i == len(SCENARIO):
        return
    m = np.array(TRIANGLE)
    t = np.array(SCENARIO[i])
    points = np.matmul(m, t).tolist()

    draw_triangle(points)

    canvas.after(PERIOD, transform, i+1)


MASTER = tk.Tk()
MASTER.title('СР №2. ВЗ №1. Косыгин К.С.')

# Frame with buttons
fb = tk.Frame(MASTER)
fb.pack()
# Frame with canvas
fc = tk.Frame(MASTER)
fc.pack()

# Canvas
canvas = tk.Canvas(fc, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

MASTER.after(0, transform)
MASTER.mainloop()
