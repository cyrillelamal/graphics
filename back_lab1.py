from tkinter import *


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'x': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


class GUI:
    WIDTH = 220
    HEIGHT = 250

    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title('ЛР №1. Косыгин К.С.')
        self.__main_window.geometry(f'{GUI.WIDTH}x{GUI.HEIGHT}')
        self._build_base_interface()
        self._bind_defaults()
        self._add_copyright()

    def _build_base_interface(self):
        # Frame with input fields
        self._frame_input = Frame(self.__main_window)
        self._frame_input.pack()
        # Frame with input buttons
        self._frame_button = Frame(self.__main_window)
        self._frame_button.pack()
        # Frame with output
        self._frame_output = Frame(self.__main_window)
        self._frame_output.pack()

        # Labels and entries :: Frame with input fields
        Label(self._frame_input, text='Le nombre a:').grid(row=0)
        self._entry_num_a = Entry(self._frame_input)
        self._entry_num_a.grid(row=0, column=1, padx=5, pady=5)
        Label(self._frame_input, text='Le nombre b:').grid(row=1)
        self._entry_num_b = Entry(self._frame_input)
        self._entry_num_b.grid(row=1, column=1, padx=5, pady=5)

        # Buttons with operations :: Frame with input buttons
        self._button_plus = Button(self._frame_button, text='+')
        self._button_plus.grid(row=0, column=0, padx=10, pady=10)
        self._button_minus = Button(self._frame_button, text='-')
        self._button_minus.grid(row=0, column=1, padx=10, pady=10)
        self._button_multiply = Button(self._frame_button, text='x')
        self._button_multiply.grid(row=1, column=0, padx=10, pady=10)
        self._button_divide = Button(self._frame_button, text='/')
        self._button_divide.grid(row=1, column=1, padx=10, pady=10)

        # Result
        self._result_label = Label(self.__main_window, text='Le résultat')
        self._result_label.pack()

    def _add_copyright(self):
        Label(self.__main_window, text='Косыгин К.С. ИВТ 1.2').pack()

    def _bind_defaults(self):
        for prop, item in self.__dict__.items():
            if prop.startswith('_button_'):
                item.bind('<Button-1>', self.calculate)

    def calculate(self, event):
        """Calculate and display"""
        btn_txt = event.widget['text']
        a = float(self._entry_num_a.get())
        b = float(self._entry_num_b.get())

        result = OPERATIONS[btn_txt](a, b)

        self._result_label['text'] = result

    def start_loop(self):
        self.__main_window.mainloop()
