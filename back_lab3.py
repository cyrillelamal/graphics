from tkinter import *


class GUI:
    LABELS = ['A', 'B', 'C', 'x min', 'y min', 'x max', 'y max']
    CANVAS_HEIGHT = 200
    CANVAS_WIDTH = 400

    H = 1

    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title('ЛР №3. Косыгин К.С.')
        self._build_base_interface()
        self._bind_defaults()

    def _build_base_interface(self):
        # User's input frame
        self._frame_input = Frame(self.__main_window)
        self._frame_input.pack()

        # Build user's input
        for label in GUI.LABELS:
            Label(self._frame_input, text=label).pack()

            field_name = '_entry_' + label.replace(' ', '_').lower()
            entry = Entry(self._frame_input)
            setattr(self, field_name, entry)
            entry.pack()

        # Button
        self._do_button = Button(self._frame_input, text='Dessiner')
        self._do_button.pack()

        # Output
        self._figure_frame = Frame(self.__main_window)
        self._figure_frame.pack()

        self._canvas = Canvas(self._figure_frame)
        self._canvas.pack()

        # X
        self._canvas.create_line(0, GUI.CANVAS_HEIGHT//2, GUI.CANVAS_WIDTH, GUI.CANVAS_HEIGHT//2)
        # Y
        self._canvas.create_line(GUI.CANVAS_WIDTH//2, 0, GUI.CANVAS_WIDTH//2, GUI.CANVAS_HEIGHT)

    def _bind_defaults(self):
        self._do_button.bind('<Button-1>', self.draw)

    @staticmethod
    def func(x, a, b, c):
        return a * x ** 2 + b * x + c

    def draw(self, event):
        values = {}
        for label in GUI.LABELS:
            key = label.replace(' ', '_').lower()
            attr = '_entry_' + key
            values[key] = float(getattr(self, attr).get())

        a = values['a']
        b = values['b']
        c = values['c']
        x_max = values['x_max']

        x = values['x_min']
        while x < x_max:
            y = GUI.func(x, a, b, c)
            x2 = x + GUI.H
            y2 = GUI.func(x2, a, b, c)
            self._canvas.create_line(x, y, x2, y2)
            x = x2

    def start_loop(self):
        self.__main_window.mainloop()
