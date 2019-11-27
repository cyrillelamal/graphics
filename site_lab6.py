"""
Movements
"""
import tkinter as tk
import numpy

from converter import d2s, moved_axis
from transformations import TRANSFORMATIONS


FIGURES = [  # ORDER IS IMPORTANT !
    # [Symmetric, fig_type, color, *points]
    # Background
    [True, 'oval', '#edac7e', 2.4, 11.4, 5, 13],  # Hands
    [True, 'oval', '#edac7e', 5, 2, 8, 4],  # Legs
    [True, 'circle', '#87cefa', 7.5, 21, 1.5],  # Ears
    # Body
    [False, 'oval', '#33ccff', 4, 2, 16, 22],  # Body
    [False, 'oval', '#edac7e', 8, 13, 12, 14.5],  # Mouth
    [False, 'oval', 'black', 9, 14, 11, 15],  # Nose
    # Premier plan
    [True, 'circle', 'white', 7, 17, 1],  # Eyes
    [True, 'circle', 'black', 6.5, 17, 0.2],  # Eyebrow
    [True, 'oval', 'white', 9, 12, 10, 13.5],  # Teeth
]
# First quadrant => present as reflected at y
X_LINE = 0
Y_LINE = 10


CANVAS_SIZE = (720, 480)

# Counted constants
WIDTH, HEIGHT = CANVAS_SIZE


def create_circle(canvas: 'tk.Canvas', x, y, r, color='black'):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    p1 = d2s((x0, y0), CANVAS_SIZE)
    p2 = d2s((x1, y1), CANVAS_SIZE)
    canvas.create_oval(*p1, *p2, fill=color)


def draw_figure():
    for fig in FIGURES:
        is_symmetric = fig[0]
        figure_type = fig[1]
        color = fig[2]
        points = fig[3:]

        if figure_type == 'oval':
            x0, y0 = points[:2]
            x1, y1 = points[2:]
            p1 = d2s((x0, y0), CANVAS_SIZE)
            p2 = d2s((x1, y1), CANVAS_SIZE)
            canvas.create_oval(*p1, *p2, fill=color)
            if is_symmetric:
                x_moved0, y_moved0 = moved_axis(
                    (x0, y0), (Y_LINE, X_LINE)
                )
                x_moved1, y_moved1 = moved_axis(
                    (x1, y1), (Y_LINE, X_LINE)
                )
                moved_matrix = numpy.array(
                    [
                        (x_moved0, y_moved0),
                        (x_moved1, y_moved1)
                    ]
                )
                t = numpy.array(TRANSFORMATIONS['ry'])
                reflected_matrix = numpy.matmul(moved_matrix, t).tolist()
                p1, p2 = reflected_matrix
                p1 = d2s(p1, CANVAS_SIZE)
                p2 = d2s(p2, CANVAS_SIZE)
                canvas.create_oval(*p1, *p2, fill=color)

        if figure_type == 'circle':
            x, y, r = points
            create_circle(canvas, x, y, r, color)

        # TODO: other shapes


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

draw_figure()


MASTER.mainloop()
