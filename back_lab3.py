from inspect import signature
import tkinter as tk


NUM_OF_STEPS = 100  # Function

SCALE = (10, 10)  # Pixels scale

EC_WIDTH = 320
EC_HEIGHT = 240


def example_parabola(x, a=1, b=0, c=0) -> float:
    """Return function value for passed"""
    return a * x**2 + b * x + c


class CanvasForGraphic:
    """Should be used as mixin"""
    def __init__(self, frame, width, height, func, scale=None, axis_bias=5):
        self.frame = frame

        self.width = width
        self.height = height

        self.scale = (1, 1) if scale is None else scale

        self.axis_bias = axis_bias
        self.axis_width = 2

        self._center_x = width // 2
        self._center_y = height // 2

        self.func = func

        self._append_canvas()

    def _append_canvas(self):
        c = tk.Canvas(self.frame, width=self.width, height=self.height)
        c.pack()
        self._canvas = c

    def draw_axis(self):
        """Draw x and y axis"""
        c = getattr(self, '_canvas')

        # X axis
        x_l = self.axis_bias
        x_r = self.width - self.axis_bias
        y = self._center_y
        c.create_line(x_l, y, x_r, y, width=self.axis_width)
        # Y axis
        x = self._center_x
        y_t = self.axis_bias
        y_b = self.height - self.axis_bias
        c.create_line(x, y_t, x, y_b, width=self.axis_width)

    def draw_graphic(self, x_min, x_max, y_min=None, y_max=None):
        """Draw the line forming graphic"""
        self._canvas.delete('all')
        self.draw_axis()

        # Function step
        h = (x_max - x_min) / NUM_OF_STEPS

        # Center of the canvas
        x_mid = self._center_x
        y_mid = self._center_y

        fx = x_min  # Functional x

        x_scale, y_scale = self.scale

        xp = x_mid + int(fx * x_scale)
        yp = y_mid - int(self.func(fx) * y_scale)

        while fx < x_max:
            fx += h
            xc = x_mid + int(fx * x_scale)
            yc = y_mid - int(self.func(fx) * y_scale)
            self._canvas.create_line(xp, yp, xc, yc, width=2)
            xp = xc
            yp = yc

    def enclose(self, *args):
        """Enclose the function bound to the instance with args"""
        def curry(old_func):
            sig = signature(old_func)
            if len(sig.parameters) == 1:
                return old_func

            def new_func(x):
                return old_func(x, *args)
            return new_func
        return curry(self.func)


class GUI:
    LABEL_NAMES = ['A', 'B', 'C', 'x min', 'y min', 'x max', 'y max']
    LABEL_PADDING = (3, 5)

    def __init__(self, title):
        m = tk.Tk()
        m.title(title)
        self.__master = m

        self._build_interface()
        self._bind_actions()

    def _build_interface(self):
        """Frames in the main window"""
        m = self.__master
        fe = tk.Frame(m)  # Frame with entries
        fe.pack()
        setattr(self, '_frame_entries', fe)
        fb = tk.Frame(m)  # Frame with button
        fb.pack()
        setattr(self, '_frame_button', fb)
        fc = tk.Frame(m)
        fc.pack()
        setattr(self, '_frame_canvas', fc)

        # Entries
        padx, pady = GUI.LABEL_PADDING  # Const padding
        ln = GUI.LABEL_NAMES
        for label, row in zip(ln, range(len(ln))):
            tk.Label(fe, text=label).grid(row=row, column=0, padx=padx, pady=pady)

            entry_name = '_entry_' + label.replace(' ', '_').lower()
            e = tk.Entry(fe)
            e.grid(row=row, column=1)
            setattr(self, entry_name, e)

        # Button
        self._button = tk.Button(fb, text='Dessiner')
        self._button.pack()

        # Canvas
        self._canvas = CanvasForGraphic(
            fc,
            EC_WIDTH, EC_HEIGHT,
            example_parabola,
            scale=SCALE
        )
        self._canvas.draw_axis()

    def _bind_actions(self):
        self._button.bind('<Button-1>', self._redraw)

    def _redraw(self, event):  # When 'redraw' button is pressed
        """Redraw"""
        user_input = self.get_user_input()
        canvas = self._canvas
        a = user_input.pop('a')
        b = user_input.pop('b')
        c = user_input.pop('c')

        # Make closure with default function
        canvas.enclose(a, b, c)
        canvas.draw_graphic(**user_input)

    def get_user_input(self) -> dict:
        """Read inputs"""
        return {
            'a': float(getattr(self, '_entry_a').get()),
            'b': float(getattr(self, '_entry_b').get()),
            'c': float(getattr(self, '_entry_c').get()),
            'x_min': float(getattr(self, '_entry_x_min').get()),
            'x_max': float(getattr(self, '_entry_x_max').get()),
            # y_max, y_min, etc
        }

    def start_loop(self):
        self.__master.mainloop()
