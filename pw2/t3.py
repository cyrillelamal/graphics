import sys
from math import sin, cos, degrees
from math import pi as PI
from tkinter import *

sys.path.insert(0, '..')
from converter import d2s

CS = (600, 600)
CW, CH = CS

R = 15  # Radius
NOA = 30  # Number of arrows
XB, YB = (1, 2)  # Arrow biases
AL = 3  # Arrow length


def main():
    for i in range(0, NOA+1):
        angle = 2 * PI * i / NOA
        xi = round(R * cos(angle), 5)
        yi = round(R * sin(angle), 5)

        arrow_point = d2s((xi, yi), CS)

        a1 = d2s((xi+XB, yi-YB), CS)
        a2 = d2s((xi-XB, yi-YB), CS)
        a3 = d2s((xi, yi-AL), CS)

        canvas.create_line(*arrow_point, *a1)
        canvas.create_line(*arrow_point, *a2)
        canvas.create_line(*arrow_point, *a3)


master = Tk()
master.title('ВСР №3. Косыгин К.С.')
canvas = Canvas(master, width=CW, height=CH)
canvas.pack()
master.after(0, main)
master.mainloop()
