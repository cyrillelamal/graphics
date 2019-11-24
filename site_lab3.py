import tkinter as tk


from converter import d2s


# Canvas parameters
WINDOW_SIZE = (320, 240)
AXIS_SCALE = (10, 10)  # Attention to d2s!!!

SERIF_SIZE = 4
AXIS_BIAS = 10
ARROW_BIAS = 3

NUM_OF_STEPS = 10**3  # For function


def func(x, a, b, c):
    """Parabola function"""
    return a * x**2 + b * x + c


# REFLECTION MATRICES
REFLECTIONS = {
    'ry': [  # At y
        (-1, 0),
        (0, 1)
    ],
    'rx': [  # At x
        (1, 0),
        (0, -1)
    ]
}


# Counted constants
WIDTH, HEIGHT = WINDOW_SIZE
X_SCALE, Y_SCALE = AXIS_SCALE
SERIF_MID = SERIF_SIZE // 2
MID_X = WIDTH // 2
MID_Y = HEIGHT // 2


def matrix_mult2(m1, m2):
    """Serif * matrix"""
    a, b = m1[0]
    c, d = m1[1]

    e, f = m2[0]
    g, h = m2[1]

    return [
        (a*e + b*g, a*f + b*h),
        (c*e + d*g, c*f + d*h)
    ]


def draw_arrows():
    """Draw arrows"""
    x_line = [
        WIDTH - AXIS_BIAS, MID_Y,
        WIDTH - 2*AXIS_BIAS, MID_Y - ARROW_BIAS
    ]
    canvas.create_line(*x_line)
    x_line[3] = MID_Y + ARROW_BIAS
    canvas.create_line(*x_line)

    y_line = [
        MID_X, AXIS_BIAS,
        MID_X - ARROW_BIAS, AXIS_BIAS*2
    ]
    canvas.create_line(*y_line)
    y_line[2] = MID_X + ARROW_BIAS
    canvas.create_line(*y_line)


def draw_axis_names():
    """Draw axis names"""
    # X
    x = WIDTH - int(1.5*AXIS_BIAS)
    y = MID_Y - AXIS_BIAS
    canvas.create_text(x, y, text='X')
    # Y
    x = MID_X + AXIS_BIAS
    y = int(1.5*AXIS_BIAS)
    canvas.create_text(x, y, text='Y')


def draw_serifs(base_serif, reflection_type: str):
    """Draw serifs. Reflection_type in REFLECTIONS"""
    reflection_type = reflection_type.lower()
    reflection_matrix = REFLECTIONS[reflection_type]

    p1 = d2s(base_serif[0], WINDOW_SIZE, AXIS_SCALE)
    p2 = d2s(base_serif[1], WINDOW_SIZE, AXIS_SCALE)

    axis_bias = MID_X + X_SCALE  # Just loop parameter
    while axis_bias < WIDTH - AXIS_BIAS * 2:
        canvas.create_line(*p1, *p2)  # Draw first right serif

        reflected_serif = matrix_mult2(base_serif, reflection_matrix)  # Left serif in Descartes
        p1 = d2s(reflected_serif[0], WINDOW_SIZE, AXIS_SCALE)
        p2 = d2s(reflected_serif[1], WINDOW_SIZE, AXIS_SCALE)
        canvas.create_line(*p1, *p2)

        # Cycle parameters
        if reflection_type == 'ry':
            axis_bias += X_SCALE
            base_serif[0][0] += 1
            base_serif[1][0] += 1
        else:
            axis_bias += Y_SCALE
            base_serif[0][1] += 1
            base_serif[1][1] += 1

        p1 = d2s(base_serif[0], WINDOW_SIZE, AXIS_SCALE)
        p2 = d2s(base_serif[1], WINDOW_SIZE, AXIS_SCALE)


def draw_axis():
    """Draw axis"""
    draw_arrows()
    draw_axis_names()
    # X
    xl = AXIS_BIAS
    xr = WIDTH - AXIS_BIAS
    y = MID_Y
    canvas.create_line(xl, y, xr, y)
    x_serif = [
        [1, +0.2],  # First point
        [1, -0.2]  # Second point
    ]
    draw_serifs(x_serif, 'ry')
    # Y
    x = MID_X
    yt = AXIS_BIAS
    yb = HEIGHT - AXIS_BIAS
    canvas.create_line(x, yt, x, yb)
    y_serif = [
        [-0.2, 1],
        [0.2, 1]
    ]
    draw_serifs(y_serif, 'rx')


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
    point1 = d2s((x, y), WINDOW_SIZE)

    # Count points for function nad convert them
    x += h
    while x < x_max:
        y = func(x, a, b, c)

        # New screen point
        point2 = d2s((x, y), WINDOW_SIZE)

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
    draw_axis()
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
canvas = tk.Canvas(fc, width=WIDTH, height=HEIGHT)
canvas.pack()
draw_axis()


MASTER.mainloop()
