from tkinter import *


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'x': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


class GUI:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title('ЛР №1. Косыгин К.С.')
        self._build_base_interface()
        self._bind_defaults()

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

        # Labels and entries
        Label(self._frame_input, text='Le nombre a').pack()
        self._entry_num_a = Entry(self._frame_input)
        self._entry_num_a.pack()
        Label(self._frame_input, text='Le nombre b').pack()
        self._entry_num_b = Entry(self._frame_input)
        self._entry_num_b.pack()

        # Buttons with operations
        self._button_plus = Button(self._frame_button, text='+')
        self._button_plus.grid(row=1, column=1, sticky=NW)
        self._button_plus.pack()
        self._button_minus = Button(self._frame_button, text='-')
        self._button_minus.grid(row=1, column=2, sticky=NE)
        self._button_minus.pack()
        self._button_multiply = Button(self._frame_button, text='x')
        self._button_multiply.grid(row=2, column=1, sticky=SW)
        self._button_multiply.pack()
        self._button_divide = Button(self._frame_button, text='/')
        self._button_divide.grid(row=2, column=2, sticky=SE)
        self._button_divide.pack()

        # Result
        self._result_label = Label(self.__main_window, text='Le résultat')
        self._result_label.pack()

    def _bind_defaults(self):
        for k, v in self.__dict__.items():
            if k.startswith('_button_'):
                v.bind('<Button-1>', self.calculate)

    def calculate(self, event):
        """Calculate and display"""
        btn_txt = event.widget['text']
        a = float(self._entry_num_a.get())
        b = float(self._entry_num_b.get())

        result = OPERATIONS[btn_txt](a, b)

        self._result_label['text'] = result

    def start_loop(self):
        self.__main_window.mainloop()
