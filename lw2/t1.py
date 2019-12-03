"""
50 squares
"""
import tkinter as tk
import sys

sys.path.insert(0, '..')
from converter import d2s


SIZE = (640, 640)
SCALE = (5, 5)

NOS = 50

POINTS = [
    [-52, 52],
    [52, -52]
]


WIDTH, HEIGHT = SIZE


def color_switcher(color='black'):
    return 'white' if color == 'black' else 'black'


def main(i=1, color='black'):
    if i == NOS:
        return

    POINTS[0][0] += 1
    POINTS[0][1] -= 1
    POINTS[1][0] -= 1
    POINTS[1][1] += 1

    p1 = d2s(POINTS[0], SIZE, SCALE)
    p2 = d2s(POINTS[1], SIZE, SCALE)

    canvas.create_rectangle(*p1, *p2, fill=color_switcher(color))

    canvas.after(200, main, i+1, color)


MASTER = tk.Tk()
MASTER.title('ЛР №2. Косыгин К.С.')

canvas = tk.Canvas(MASTER, width=WIDTH, height=HEIGHT)
canvas.pack()


MASTER.after(1000, main)
MASTER.mainloop()
