"""
Movements
"""
import math
import tkinter as tk
import numpy


CANVAS_SIZE = (640, 480)

# Counted constants
WIDTH, HEIGHT = CANVAS_SIZE

MASTER = tk.Tk()
MASTER.title('ЛР №6. Косыгин К.С.')

# Frame with entries
fe = tk.Frame(MASTER)
fe.pack()
# Frame with canvas
fc = tk.Frame(MASTER)
fc.pack()

# Inputs
tk.Label(fe, text='Угол:').grid(row=0, column=0)
entry_angle = tk.Entry(fe)
entry_angle.grid(row=0, column=1)  # Entry with angle
tk.Label(fe, text='Матрица преобразования').grid(row=1, column=0, columnspan=2)
entry_a11 = tk.Entry(fe)  # Entry 11
entry_a11.grid(row=2, column=0)
entry_a12 = tk.Entry(fe)  # Entry 12
entry_a12.grid(row=2, column=1)
entry_a21 = tk.Entry(fe)  # Entry 21
entry_a21.grid(row=3, column=0)
entry_a22 = tk.Entry(fe)  # Entry 22
entry_a22.grid(row=3, column=1)

# Canvas
canvas = tk.Canvas(fc, width=WIDTH, height=HEIGHT)
canvas.pack()


MASTER.mainloop()
