import sys
import tkinter as tk


sys.path.insert(0, '..')
from converter import d2s

NUM_OF_ARROWS = 30

WIDTH = 640
HEIGHT = 480

X_MID = WIDTH // 2
Y_MID = HEIGHT // 2


def create_circle(x, y, r):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1)


def redraw(event):
    canvas.delete('all')

    users_input = get_users_input()
    x = users_input.get('x')
    y = users_input.get('y')
    r = users_input.get('radius')

    circle_center = d2s((x, y), (WIDTH, HEIGHT))
    x, y = circle_center  # Screen points
    create_circle(x, y, r)

    # Draw arrows
    xt = x
    yt = y - r
    angle = 360 / NUM_OF_ARROWS


def get_users_input():
    re = radius_entry.get()
    radius = re if re != '' else HEIGHT // 4

    xe = x_entry.get()
    x = xe if xe != '' else X_MID
    ye = y_entry.get()
    y = ye if ye != '' else Y_MID

    return {
        'x': int(x), 'y': int(y),
        'radius': int(radius)
    }


MASTER = tk.Tk()
MASTER.title('СР №1. Задание №3. Косыгин К.С.')

# Entries frame
fe = tk.Frame(MASTER)
fe.pack()
# Canvas frame
cf = tk.Frame(MASTER)
cf.pack()

# User's input
tk.Label(fe, text='Radius').grid(row=0, column=0, columnspan=2, padx=3, pady=5)
radius_entry = tk.Entry(fe)
radius_entry.grid(row=0, column=2, columnspan=2, padx=3, pady=5)

tk.Label(fe, text='x').grid(row=1, column=0, padx=3, pady=5)
x_entry = tk.Entry(fe)
x_entry.grid(row=1, column=1, padx=3, pady=5)

tk.Label(fe, text='y').grid(row=1, column=2, padx=3, pady=5)
y_entry = tk.Entry(fe)
y_entry.grid(row=1, column=3, padx=3, pady=5)

button_redraw = tk.Button(fe, text='Dessiner')
button_redraw.grid(row=2, column=1, columnspan=2)
button_redraw.bind('<Button-1>', redraw)

# Canvas
cf = tk.Frame(MASTER)
cf.pack()
canvas = tk.Canvas(cf, width=WIDTH, height=HEIGHT)
canvas.pack()

MASTER.mainloop()
