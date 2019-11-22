import tkinter as tk


# Canvas parameters
CANVAS_WIDTH = 320
CANVAS_HEIGHT = 240

X_SCALE = 8
Y_SCALE = 8

AXIS_BIAS = 5

NUM_OF_STEPS = 10**3  # For function


# Counted constants
MID_X = CANVAS_WIDTH // 2
MID_Y = CANVAS_HEIGHT // 2


def func(x, a, b, c):
    """Parabola function"""
    return a * x**2 + b * x + c


def clear(canvas: 'tk.Canvas'):
    """Delete the content of the passed canvas"""
    canvas.delete('all')


def draw_axis(canvas: 'tk.Canvas'):
    """Draw axis on the passed canvas"""
    center_x = CANVAS_WIDTH // 2
    center_y = CANVAS_HEIGHT // 2
    # X axis
    xl = AXIS_BIAS
    xr = CANVAS_WIDTH - AXIS_BIAS
    y = center_y
    canvas.create_line(xl, y, xr, y)
    # Y axis
    x = center_x
    yt = AXIS_BIAS
    yb = CANVAS_HEIGHT - AXIS_BIAS
    canvas.create_line(x, yt, x, yb)


def get_users_input():
    params = {}
    try:
        params['a'] = float(entry_a.get())
        params['b'] = float(entry_b.get())
        params['c'] = float(entry_c.get())

        params['x_min'] = float(entry_x_min.get())
        params['x_max'] = float(entry_x_max.get())
    except ValueError:
        show_errors(canvas, 'Некорректные значения')

    y_min = entry_y_min.get()
    y_max = entry_y_max.get()
    if y_min != '':
        params['y_min'] = y_min
    if y_max != '':
        params['y_max'] = y_max

    return params


def show_errors(canvas: 'tk.Canvas', msg: str):
    canvas.delete('all')
    canvas.create_text(MID_X, MID_Y, text=msg)


def draw_graphic(params: dict):
    x_max = params.get('x_max')
    x_min = params.get('x_min')
    a = params.get('a')
    b = params.get('b')
    c = params.get('c')

    y_min = params.get('y_min')
    y_max = params.get('y_max')

    h = (x_max - x_min) / NUM_OF_STEPS  # literally dx

    # Functional x
    x = x_min

    # Points
    xp = MID_X + int(x * X_SCALE)
    yp = MID_Y - int(func(x, a, b, c) * Y_SCALE)

    x += h
    while x < x_max:
        y = func(x, a, b, c)

        # Points
        xc = MID_X + int(x * X_SCALE)
        yc = MID_Y - int(y * Y_SCALE)

        # There is y(min) and the current f(x) is lower than that minimum
        # OR
        # There is y(max) and the current f(x) is bigger than that maximum
        if y_min is not None and y < float(y_min) or y_max is not None and y > float(y_max):
            pass

        else:  # No importance
            canvas.create_line(xp, yp, xc, yc)

        xp, yp = xc, yc
        x += h


def redraw(event):
    """Clear, Draw axis, Get user's input, Draw graphic"""
    # Clear
    clear(canvas)
    # Draw axis
    draw_axis(canvas)
    # Get user's input
    users_input = get_users_input()
    # Draw graphic
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
canvas = tk.Canvas(fc, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

draw_axis(canvas)
