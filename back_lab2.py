from tkinter import *


DIGITS = '0123456789'

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
BIAS = 10

BLACK = '#000000'
RED = '#FF0000'
BLUE = '#0000FF'


class GUI:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title('ЛР №2. Косыгин К.С.')
        self._build_base_interface()
        self._bind_defaults()

    def _build_base_interface(self):
        # Frame with user's input
        self._frame_input = Frame(self.__main_window)
        self._frame_input.pack()
        # Frame with figure
        self._frame_figure = Frame(self.__main_window)
        self._frame_figure.pack()

        # User's input interface
        Label(self._frame_input, text='Вершины').pack()
        self._entry_peaks = Entry(self._frame_input)
        self._entry_peaks.pack()

        self._button_draw = Button(self._frame_input, text='Перерисовать')
        self._button_draw.pack()

        # Canvas for figures
        self._canvas = Canvas(self._frame_figure, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self._canvas.pack()

        self._draw_default_triangle()

    def _bind_defaults(self):
        self._button_draw.bind('<Button-1>', self.draw)

    def _draw_default_triangle(self):
        self._canvas.create_line(BIAS, BIAS, CANVAS_WIDTH, CANVAS_HEIGHT//2, fill=BLACK)
        self._canvas.create_line(BIAS, CANVAS_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT//2, fill=RED)
        self._canvas.create_line(BIAS, BIAS, BIAS, CANVAS_HEIGHT, fill=BLUE)

    def draw(self, event):
        self._canvas.delete('all')

        points = []
        p = ''
        for ch in self._entry_peaks.get():
            if ch in DIGITS:
                p += ch
            elif p != '':
                points.append(p)
                p = ''
        if p != '':
            points.append(p)

        points = [int(p) for p in points]

        if len(points) != 6:
            self._canvas.create_text(
                CANVAS_WIDTH // 2,
                CANVAS_HEIGHT // 2,
                text='Le nombre est incorrect'
            )
            return

        self._canvas.create_polygon(points)

    def start_loop(self):
        self.__main_window.mainloop()
