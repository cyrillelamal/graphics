import sys
import tkinter as tk

sys.path.insert(0, '..')
from converter import d2s


TRIANGLE = [
    (-10, 0),
    (0, 10),
    (5, -5)
]


MASTER = tk.Tk()
MASTER.title('СР №2. ВЗ №1. Косыгин К.С.')

# Frame with buttons
bf = tk.Frame(MASTER)
bf.pack()
# Frame with canvas
cf = tk.Frame(MASTER)
cf.pack()
