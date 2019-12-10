"""
Animation with reflections
"""
import tkinter as tk
import numpy as np

from converter import d2s
from converter import TRANSFORMATIONS as TR

SCALE = (10, 10)
CS = (600, 600)  # Canvas size
W, H = CS  # Width and height


FIGURES = [  # ORDER IS IMPORTANT !
    # [Symmetric, fig_type, color, *points]
    # Background
    [True, 'oval', '#c48157', 1, -15.5, 13, -10],  # Legs
    [True, 'oval', '#c48157', 2.5, -2.5, 18, 4],  # Hands
    [True, 'oval', '#84d3db', 2, 18.5, 10, 11],  # Ears
    # Front
    [False, 'oval', '#84d3db', -10, -15, 10, 15],  # Body
    [True, 'oval', 'white', 0.5, 8, 2, 3],  # Teeth
    [False, 'oval', '#c9996c', -3, 8, 3, 5],  # Mouth
    [False, 'oval', 'black', -2, 9, 2, 7],  # Nose
    [True, 'oval', 'white', 0.5, 10, 4, 13.5],  # Eyes
    [True, 'oval', 'black', 1, 11, 1.5, 11.5],  # Eyebrows
]


# Main functions
def draw_figure():
    for fig in FIGURES:
        is_symmetric = fig[0]
        fig_type = fig[1]
        color = fig[2]
        points = fig[3:]

        if fig_type == 'oval':
            x0, y0 = points[:2]
            x1, y1 = points[2:]
            p1 = d2s((x0, y0), CS)
            p2 = d2s((x1, y1), CS)
            canvas.create_oval(*p1, *p2, fill=color)
            if is_symmetric:
                m = np.array([
                    [x0, y0],
                    [x1, y1]
                ])
                t = np.array(TR['ry'])
                reflected_matrix = np.matmul(m, t).tolist()
                p1, p2 = reflected_matrix
                p1 = d2s(p1, CS)
                p2 = d2s(p2, CS)
                canvas.create_oval(*p1, *p2, fill=color)


# Tkinter backend
master = tk.Tk()
master.title('Косыгин К.С.')
canvas = tk.Canvas(master, width=W, height=H)
canvas.pack()
master.after(0, draw_figure)
master.mainloop()
