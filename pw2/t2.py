"""
Sharp lines
"""
import tkinter as tk


BIAS = 0.2

SCALE = 50


MASTER = tk.Tk()
MASTER.title('СР №2. Задание №2. Косыгин К.С.')

canvas = tk.Canvas(MASTER, width=640, height=480)
canvas.pack()

x1, y1 = (1.0, 6.0)
x2, y2 = (1.0, 1.0)

canvas.create_line(x1, y1, x2, y2)

while y1 > 1.0:
    y1 -= round(BIAS, 1)
    x2 += round(BIAS, 1)
    canvas.create_line(x1*SCALE, y1*SCALE, x2*SCALE, y2*SCALE)


MASTER.mainloop()
