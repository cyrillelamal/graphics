"""
n-angles
"""
import math
import tkinter as tk

from converter import d2s


CANVAS_SIZE = (640, 480)
SCALE = (10, 10)
RADIUS = 10
PHI = 0


# Counted constants
WIDTH, HEIGHT = CANVAS_SIZE
X_OFFSET, Y_OFFSET = WIDTH // 2, HEIGHT // 2


def build_figure(event):
    canvas.delete('all')

    n = int(entry_n.get())

    angle = PHI
    x0 = RADIUS * math.cos(angle)
    y0 = RADIUS * math.sin(angle)
    p1 = d2s((x0, y0), CANVAS_SIZE, SCALE)
    for i in range(0, n+1):
        angle = PHI + 2*math.pi * i / n
        xi = round(RADIUS * math.cos(angle), 5)
        yi = round(RADIUS * math.sin(angle), 5)

        p2 = d2s((xi, yi), CANVAS_SIZE, SCALE)

        canvas.create_line(*p1, *p2)

        p1 = p2


MASTER = tk.Tk()
MASTER.title('ЛР №5. Косыгин К.С.')

# Frames
# Frame with enrty of number of angles and button
fe = tk.Frame(MASTER)
fe.pack()
# Frame with canvas
fc = tk.Frame(MASTER)
fc.pack()


# Inputs
tk.Label(fe, text='n:').grid(row=0, column=0)
entry_n = tk.Entry(fe)  # Entry for number of angles
entry_n.grid(row=0, column=1)
button_build = tk.Button(fe, text='Construire')  # Button commands redraw
button_build.grid(row=1, column=0, columnspan=2)
button_build.bind('<Button-1>', build_figure)

# Canvas
canvas = tk.Canvas(fc, width=WIDTH, height=HEIGHT)
canvas.pack()


MASTER.mainloop()
