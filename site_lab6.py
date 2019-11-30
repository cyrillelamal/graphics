"""
Movements, transformations, etc.
"""
import math
import tkinter as tk

from converter import TRANSFORMATIONS
from figures import Shape


# ORDER IS IMPORTANT!
SHAPES = [
    # Background
    Shape('oval', [2.4, 11.4, 5, 13], '#edac7e', True),  # Hands
    Shape('oval', [5, 2, 8, 4], '#edac7e', True),  # Legs
    Shape('circle', [7.5, 21, 1.5], '#87cefa', True),  # Ears
    # Body
    Shape('oval', [4, 2, 16, 22], '#33ccff', False),  # Body
    Shape('oval', [8, 13, 12, 14.5], '#edac7e', False),  # Mouth
    Shape('oval', [9, 14, 11, 15], 'black', False),  # Nose
    # Premier plan
    Shape('circle', [7, 17, 1], 'white', True),  # Eyes
    Shape('circle', [6.5, 17, 0.2], 'black', True),  # Eyebrow
    Shape('oval', [9, 12, 10, 13.5], 'white', True),  # Teeth
]
CENTER = 10


CANVAS_SIZE = (720, 480)

# Counted constants
WIDTH, HEIGHT = CANVAS_SIZE


def draw_image():
    for shape in SHAPES:
        # Closure
        shape.canvas = canvas
        shape.canvas_size = CANVAS_SIZE
        # Drawing
        if shape.is_symmetric:
            shape.y_axis = CENTER
        shape.draw()


def transform_scenario():
    # Изменение масштаба
    t = [
        [2, 0],
        [0, 2]
    ]
    # Симметричное отражение
    t = TRANSFORMATIONS['rx']
    # Сдвиг
    t = [
        [1, 2],
        [0, 1]
    ]
    # Преобразование поворота
    t = [
        [lambda x: math.cos(x), lambda x: math.sin(x)],
        [lambda x: -math.sin(x), lambda x: math.cos(x)]
    ]
    # Масштаб + вращение: через интерфейс


def apply_transformation(event):
    pass


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

draw_image()


MASTER.after(1000, transform_scenario)
MASTER.mainloop()
