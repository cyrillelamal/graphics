"""
Calculator
"""
import tkinter as tk


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'x': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def calculate(event):
    """Calculate and display"""
    btn_txt = event.widget['text']

    a = float(entry_a.get())
    b = float(entry_b.get())

    res = OPERATIONS[btn_txt](a, b)

    result_entry.configure(state='normal')
    result_entry.delete(first=0, last=tk.END)
    result_entry.insert(tk.END, res)
    result_entry.configure(state='disabled')


WIDTH = 230
HEIGHT = 200


MASTER = tk.Tk()
MASTER.title('ЛР №1. Косыгин К.С.')
MASTER.geometry(f'{WIDTH}x{HEIGHT}')
MASTER.resizable(0, 0)

# Frame
# Frame with entries
fe = tk.Frame(MASTER)
fe.pack()
# Frame with buttons
fb = tk.Frame(MASTER)
fb.pack()
# Frame with output
fo = tk.Frame(MASTER)
fo.pack()


# Labels and entries
# Input zone
tk.Label(fe, text='Le nombre a:').grid(row=0, column=0, padx=4, pady=5)
entry_a = tk.Entry(fe)
entry_a.grid(row=0, column=1)
tk.Label(fe, text='Le nombre b:').grid(row=1, column=0, padx=4, pady=5)
entry_b = tk.Entry(fe)
entry_b.grid(row=1, column=1)
# Buttons
plus_button = tk.Button(fb, text='+')
plus_button.grid(row=0, column=0, padx=10, pady=10)
minus_button = tk.Button(fb, text='-')
minus_button.grid(row=0, column=1, padx=10, pady=10)
multiply_button = tk.Button(fb, text='x')
multiply_button.grid(row=1, column=0, padx=10, pady=10)
divide_button = tk.Button(fb, text='/')
divide_button.grid(row=1, column=1, padx=10, pady=10)
# Result
result_entry = tk.Entry(fo)
result_entry.pack()
result_entry.configure(state='disabled')
# Copyright
tk.Label(MASTER, text='Косыгин К.С. ИВТ 1.2').pack()


# Bindings
plus_button.bind('<Button-1>', calculate)
minus_button.bind('<Button-1>', calculate)
multiply_button.bind('<Button-1>', calculate)
divide_button.bind('<Button-1>', calculate)


MASTER.mainloop()
