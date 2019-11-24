import tkinter as tk


COLORS = ['blue', 'red', 'green', 'yellow', 'white']

DEPTH = len(COLORS) - 1

WIDTH = 640
HEIGHT = 480

X_MID = WIDTH // 2
Y_MID = HEIGHT // 2

INITIAL_POINTS = [
    (X_MID-100, Y_MID+50),
    (X_MID, Y_MID-100),
    (X_MID+100, Y_MID+50)
]


def get_mid(p1, p2):
    """Return center point of two points"""
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return x, y


def sierpinski(points, depth):
    colors = COLORS

    p1, p2, p3 = points
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=colors[depth])

    if depth > 0:
        depth -= 1
        points1 = [
            points[0],
            get_mid(points[0], points[1]),
            get_mid(points[0], points[2])
        ]
        sierpinski(points1, depth)

        points2 = [
            points[1],
            get_mid(points[0], points[1]),
            get_mid(points[1], points[2])
        ]
        sierpinski(points2, depth)

        points3 = [
            points[2],
            get_mid(points[2], points[1]),
            get_mid(points[0], points[2])
        ]
        sierpinski(points3, depth)


MASTER = tk.Tk()
MASTER.title('СР №2. Задание №1. Косыгин К.С.')

canvas = tk.Canvas(MASTER, width=WIDTH, height=HEIGHT)
canvas.pack()

sierpinski(INITIAL_POINTS, DEPTH)

MASTER.mainloop()
