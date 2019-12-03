"""
Movements, transformations, etc.
"""
import math
import numpy as np
import tkinter as tk

from converter import TRANSFORMATIONS, d2s


# ORDER IS IMPORTANT!
POINTS = [
    (0, 2),
    (0, 20),
    (8, 20),
    (8, 17),
    (3, 17),
    (3, 14),
    (8, 14),
    (8, 11),
    (3, 11),
    (3, 2)
]
THI = 45


CANVAS_SIZE = (720, 480)
PERIOD = 700

# Counted constants
WIDTH, HEIGHT = CANVAS_SIZE
RAD_THI = math.radians(THI)


def draw_image(points=None):
    canvas.delete('all')

    points = POINTS if points is None else points
    num_of_points = len(points)

    for i in range(num_of_points):
        p1 = points[i]
        p2 = points[0] if i == num_of_points - 1 else points[i+1]
        p1 = d2s(p1, CANVAS_SIZE)
        p2 = d2s(p2, CANVAS_SIZE)
        canvas.create_line(*p1, *p2)


SCENARIO = [
    # Изменение масштаба
    [
        [1.5, 0],
        [0, 1.5]
    ],
    # Симметричное отражение
    TRANSFORMATIONS['rx'],
    # Сдвиг
    [
        [1, 2],
        [0, 1]
    ],
    # Преобразование поворота
    [
        [math.cos(RAD_THI), math.sin(RAD_THI)],
        [-math.sin(RAD_THI), math.cos(RAD_THI)],
    ],
]


def transform_scenario(i=0):
    """Main script"""
    if i == len(SCENARIO):
        return
    p = np.array(POINTS)
    t = np.array(SCENARIO[i])
    new_points = np.matmul(p, t).tolist()
    draw_image(new_points)
    canvas.after(PERIOD, transform_scenario, i+1)


def apply_transformation(event):
    p = np.array(POINTS)

    thi = entry_angle.get()
    if thi != '':
        thi = float(thi)
        t = [row.copy() for row in TRANSFORMATIONS.get('rotate')]

        for i in range(len(t)):
            for j in range(len(t[i])):
                t[i][j] = t[i][j](thi)

        t = np.array(t)

    else:
        t = np.array([
            [float(entry_a11.get()), float(entry_a12.get())],
            [float(entry_a21.get()), float(entry_a22.get())]
        ])

    points = np.matmul(p, t).tolist()

    draw_image(points)


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
# Button
button = tk.Button(fe, text='Appliquer')
button.grid(row=4, column=0, columnspan=2)
button.bind('<Button-1>', apply_transformation)

# Canvas
canvas = tk.Canvas(fc, width=WIDTH, height=HEIGHT)
canvas.pack()

draw_image()  # Default image


MASTER.after(PERIOD, transform_scenario)
MASTER.mainloop()
