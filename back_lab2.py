from tkinter import *


DIGITS = '0123456789'

BLACK = '#000000'
RED = '#FF0000'
BLUE = '#0000FF'


class GUI:
    CANVAS_WIDTH = 200
    CANVAS_HEIGHT = 200
    BIAS = 10
    
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
        self._entry_points = Entry(self._frame_input)
        self._entry_points.pack()
        self._button_draw = Button(self._frame_input, text='Перерисовать')
        self._button_draw.pack()

        # Canvas for figures
        self._canvas = Canvas(
            self._frame_figure,
            width=GUI.CANVAS_WIDTH, height=GUI.CANVAS_HEIGHT
        )
        self._canvas.pack()

        self._draw_default_triangle()

    def _bind_defaults(self):
        self._button_draw.bind('<Button-1>', self.draw)

    def _draw_default_triangle(self):
        b = GUI.BIAS
        cw = GUI.CANVAS_WIDTH
        ch = GUI.CANVAS_HEIGHT
        self._canvas.create_line(b, b, cw, ch//2, fill=BLACK)
        self._canvas.create_line(b, ch, cw, ch//2, fill=RED)
        self._canvas.create_line(b, b, b, ch, fill=BLUE)

    def draw(self, event):
        self._canvas.delete('all')

        points = GUI.parse_points(self._entry_points.get())

        if len(points) != 6:
            self._canvas.create_text(
                GUI.CANVAS_WIDTH // 2,
                GUI.CANVAS_HEIGHT // 2,
                text='Le nombre est incorrect'
            )
            return

        self._canvas.create_polygon(points)

    @staticmethod
    def parse_points(string) -> list:
        points = []
        p = ''
        for ch in string:
            if ch in DIGITS:
                p += ch
            elif p != '':
                points.append(p)
                p = ''
        if p != '':
            points.append(int(p))
        return points

    def start_loop(self):
        self.__main_window.mainloop()
