"""
Rotate at x in 3D
"""
from math import sin, cos, radians
from tkinter import *
import numpy as np
import sys

sys.path.insert(0, '..')
from converter import d2s


PERIOD = 80  # ms
CS = (200, 200)
CW, CH = CS

FIG = [(-10, -10, 0), (10, 10, 0),]


def transform(a=0):
    a = 0 if a == 360 else a
    a_r = radians(a)
    m = np.array(FIG)
    t = np.array([
        [1, 0, 0],
        [0, cos(a_r), -sin(a_r)],
        [0, sin(a_r), cos(a_r)]
    ])
    rotated = np.matmul(m, t).tolist()
    points = []
    for rp in rotated:
        dp = list(d2s(rp, CS))
        points += dp
    print(a, points)
    canvas.delete('all')
    canvas.create_rectangle(*points)
    canvas.after(PERIOD, transform, a+1)


# Backend
master = Tk()
master.title('СЗ №2. ВСР №3')
canvas = Canvas(master, width=CW, height=CH)
canvas.pack()
master.after(PERIOD, transform)
master.mainloop()
