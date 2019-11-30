import tkinter as tk
import numpy as np


from converter import d2s, TRANSFORMATIONS


DEFAULT_CANVAS_SIZE = (720, 480)


def create_circle(canvas: 'tk.Canvas', x, y, r, color='black', canvas_size=None):
    """Draw circle. Point must be in Descartes!"""
    canvas_size = DEFAULT_CANVAS_SIZE if canvas_size is None else canvas_size
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    p1 = d2s((x0, y0), canvas_size)
    p2 = d2s((x1, y1), canvas_size)
    canvas.create_oval(*p1, *p2, fill=color)


class Shape:
    def __init__(self, shape_type: str, parameters: list, color='black', is_symmetric=False,
                 canvas=None, canvas_size=DEFAULT_CANVAS_SIZE, y_axis=0
                 ):
        self._shape_type = shape_type
        self.parameters = parameters  # points and radius
        self.color = color
        self.is_symmetric = is_symmetric

        self.canvas = canvas
        self.canvas_size = canvas_size
        self.y_axis = y_axis

    def draw(self):
        """Switch according to the shape type"""
        if self._shape_type == 'oval':
            x0, y0 = self.parameters[:2]
            x1, y1 = self.parameters[2:]
            p1 = d2s((x0, y0), self.canvas_size)
            p2 = d2s((x1, y1), self.canvas_size)
            self.canvas.create_oval(*p1, *p2, fill=self.color)

            if self.is_symmetric:
                p1, p2 = self.reflect_where_y(self.y_axis)
                p1 = d2s(p1, self.canvas_size)
                p2 = d2s(p2, self.canvas_size)
                self.canvas.create_oval(*p1, *p2, fill=self.color)

        elif self._shape_type == 'circle':
            x, y, r = self.parameters
            create_circle(self.canvas, x, y, r, color=self.color)

            if self.is_symmetric:
                x, y = self.reflect_where_y(self.y_axis)
                create_circle(self.canvas, x, y, r, color=self.color)

        return self

    def reflect_where_y(self, y_axis=0):
        """
        Return point or list of points reflected as though y=const was another than 0.
        All calculations are in Descartes
        """
        st = self._shape_type

        if st == 'oval':
            # 2 points are concerned
            x0, y0 = self.parameters[:2]
            x1, y1 = self.parameters[2:]
            x0 -= y_axis
            x1 -= y_axis
            matrix = np.array([
                [x0, y0],
                [x1, y1]
            ])
            t = np.array(TRANSFORMATIONS['ry'])
            reflected_points = np.matmul(matrix, t).tolist()  # -x
            p1, p2 = reflected_points
            p1[0] += y_axis  # x
            p2[0] += y_axis  # x
            return [p1, p2]

        elif st == 'circle':
            x, y = self.parameters[:2]
            x -= y_axis
            matrix = np.array(
                [x, y]
            )
            t = np.array(TRANSFORMATIONS['ry'])
            reflected_point = np.matmul(matrix, t).tolist()
            x, y = reflected_point
            x += y_axis
            return [x, y]
