"""
Triangle
"""
import tkinter as tk


from converter import d2s


def draw_default_triangle():
    for line, color in zip(DEFAULT_TRIANGLE_LINES, COLORS):
        pd1, pd2 = line
        ps1 = d2s(pd1, WINDOW_SIZE)
        ps2 = d2s(pd2, WINDOW_SIZE)
        canvas.create_line(*ps1, *ps2, fill=color)


def draw(event):
    """Redraw content of the canvas. Display errors in the canvas"""
    canvas.delete('all')

    users_input = entry_points.get()
    points = parse_points(users_input)

    if len(points) != 6:
        canvas.create_text(X_MID, Y_MID, text='Некорректные вершины')
        return

    p1 = d2s(tuple(points[:2]), WINDOW_SIZE)
    p2 = d2s(tuple(points[2:4]), WINDOW_SIZE)
    p3 = d2s(tuple(points[4:]), WINDOW_SIZE)
    canvas.create_polygon(*p1, *p2, *p3)


def parse_points(string):
    points = []
    p = ''
    for ch in string:
        if ch in DIGITS:
            p += ch
        elif p != '':
            points.append(int(p))
            p = ''
    if p != '':
        points.append(int(p))
    return points


DIGITS = '0123456789'

DEFAULT_TRIANGLE_LINES = [
    ((-5, 0), (0, 5)),
    ((0, 5), (5, -5)),
    ((5, -5), (-5, 0))
]

COLORS = ['#000000', '#FF0000', '#0000FF']

WINDOW_SIZE = (400, 400)

WIDTH, HEIGHT = WINDOW_SIZE
X_MID, Y_MID = (p // 2 for p in WINDOW_SIZE)


MASTER = tk.Tk()
MASTER.title('ЛР №2. Косыгин К.С.')


# Frames
# Frame with user's input
fe = tk.Frame(MASTER)
fe.pack()
# Frame with canvas
fc = tk.Frame(MASTER)
fc.pack()


# Frame with entries
tk.Label(fe, text='Вершины').pack()
entry_points = tk.Entry(fe)
entry_points.pack()
# Button redraw
button = tk.Button(fe, text='Перерисовать')
button.pack()

# Canvas for the triangle
canvas = tk.Canvas(fc, width=WIDTH, height=HEIGHT)
canvas.pack()
draw_default_triangle()


# Bindings
button.bind('<Button-1>', draw)


MASTER.mainloop()
