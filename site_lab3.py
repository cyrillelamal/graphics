import tkinter as tk


from converter import d2s
from axis import draw_axis


# Canvas parameters
CANVAS_SIZE = (320, 240)
AXIS_SCALE = (10, 10)  # Attention to d2s!!!

SERIF_SIZE = 4
AXIS_INDENT = 10
ARROW_INDENT = 3

NUM_OF_STEPS = 10**3  # For function


def func(x, a, b, c):
    """Parabola function"""
    return a * x**2 + b * x + c


# Counted constants
WIDTH, HEIGHT = CANVAS_SIZE
X_SCALE, Y_SCALE = AXIS_SCALE
SERIF_MID = SERIF_SIZE // 2
MID_X = WIDTH // 2
MID_Y = HEIGHT // 2


def get_users_input():
    params = {}
    try:
        params['a'] = float(entry_a.get())
        params['b'] = float(entry_b.get())
        params['c'] = float(entry_c.get())

        params['x_min'] = float(entry_x_min.get())
        params['x_max'] = float(entry_x_max.get())
    except ValueError:
        canvas.delete('all')
        canvas.create_text(MID_X, MID_Y, text='Некорректные значения')

    y_min = entry_y_min.get()
    y_max = entry_y_max.get()
    if y_min != '':
        params['y_min'] = y_min
    if y_max != '':
        params['y_max'] = y_max

    return params


def draw_graphic(params: dict):
    x_max = params.get('x_max')
    x_min = params.get('x_min')
    a = params.get('a')
    b = params.get('b')
    c = params.get('c')

    y_min = params.get('y_min')
    y_max = params.get('y_max')

    h = (x_max - x_min) / NUM_OF_STEPS  # literally dx

    # Functional point
    x = x_min
    y = func(x, a, b, c)

    # Graphical point
    point1 = d2s((x, y), CANVAS_SIZE)

    # Count points for function nad convert them
    x += h
    while x < x_max:
        y = func(x, a, b, c)

        # New screen point
        point2 = d2s((x, y), CANVAS_SIZE)

        # There is y(min) and the current f(x) is lower than that minimum
        # OR
        # There is y(max) and the current f(x) is bigger than that maximum
        if y_min is not None and y < float(y_min) or y_max is not None and y > float(y_max):
            pass

        # The graphic must be drawn
        else:
            canvas.create_line(*point1, *point2)

        point1 = point2
        x += h


def redraw(event):
    """Clear, Draw axis, Get user's input, Draw graphic"""
    # Clear
    canvas.delete('all')
    # Draw axis
    draw_axis(canvas, 2, CANVAS_SIZE, AXIS_INDENT, ARROW_INDENT, AXIS_SCALE)
    # Get user's input
    users_input = get_users_input()
    # Draw graphic
    if event is not None:
        draw_graphic(users_input)


MASTER = tk.Tk()
MASTER.title('ЛР №3. Косыгин К.С.')

fe = tk.Frame(MASTER)  # Frame with entries
fb = tk.Frame(MASTER)  # Frame with button
fc = tk.Frame(MASTER)  # Frame with canvas
fe.pack()
fb.pack()
fc.pack()


# Labels and entries
tk.Label(fe, text='a').grid(row=0, column=0, padx=3, pady=5)
entry_a = tk.Entry(fe)
entry_a.grid(row=0, column=1)
tk.Label(fe, text='b').grid(row=1, column=0, padx=3, pady=5)
entry_b = tk.Entry(fe)
entry_b.grid(row=1, column=1)
tk.Label(fe, text='c').grid(row=2, column=0, padx=3, pady=5)
entry_c = tk.Entry(fe)
entry_c.grid(row=2, column=1)

tk.Label(fe, text='x min').grid(row=3, column=0, padx=3, pady=5)
entry_x_min = tk.Entry(fe)
entry_x_min.grid(row=3, column=1)
tk.Label(fe, text='x max').grid(row=4, column=0, padx=3, pady=5)
entry_x_max = tk.Entry(fe)
entry_x_max.grid(row=4, column=1)
tk.Label(fe, text='y min').grid(row=5, column=0, padx=3, pady=5)
entry_y_min = tk.Entry(fe)
entry_y_min.grid(row=5, column=1)
tk.Label(fe, text='y max').grid(row=6, column=0, padx=3, pady=5)
entry_y_max = tk.Entry(fe)
entry_y_max.grid(row=6, column=1)


# Button
button = tk.Button(fb, text='Dessiner')
button.pack()
button.bind('<Button-1>', redraw)


# Canvas
canvas = tk.Canvas(fc, width=WIDTH, height=HEIGHT)
canvas.pack()
draw_axis(canvas, 2, CANVAS_SIZE, AXIS_INDENT, ARROW_INDENT, AXIS_SCALE)


MASTER.mainloop()
