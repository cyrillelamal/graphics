import tkinter as tk
import numpy as np


from converter import d2s, TRANSFORMATIONS


AXIS_NAMES = ['x', 'y', 'z']


DEFAULT_CANVAS_SIZE = (480, 320)

# Indent from the borders, in other words - padding
DEFAULT_AXIS_INDENT = 10
# Rise of arrows
DEFAULT_ARROW_INDENT = 3
# Descartes to screen
DEFAULT_AXIS_SCALE = (8, 8)


def draw_axis(
        canvas: 'tk.Canvas', num_of_axis: int,
        canvas_size=None,
        axis_indent=None,
        arrow_indent=None,
        axis_scale=None
):
    """Draw all stuff needed for axis"""
    canvas_size = DEFAULT_CANVAS_SIZE if canvas_size is None else canvas_size
    axis_indent = DEFAULT_AXIS_INDENT if axis_indent is None else axis_indent
    arrow_indent = DEFAULT_ARROW_INDENT if arrow_indent is None else arrow_indent
    axis_scale = DEFAULT_AXIS_SCALE if axis_scale is None else axis_scale

    draw_zero(canvas, canvas_size, axis_scale)
    draw_lines(canvas, num_of_axis, canvas_size, axis_indent)
    draw_arrows(canvas, num_of_axis, canvas_size, axis_indent, arrow_indent)
    draw_axis_names(canvas, num_of_axis, canvas_size, axis_indent)
    draw_serifs(canvas, num_of_axis, canvas_size, axis_indent, axis_scale)


def draw_zero(canvas: 'tk.Canvas', canvas_size: tuple, axis_scale: tuple):
    width, height = canvas_size
    x_offset, y_offset = width // 2, height // 2
    x_scale, y_scale = axis_scale
    x = x_offset + x_scale // 2
    y = y_offset - y_scale // 2
    # Text
    canvas.create_text(x, y, text='0')
    # Point
    r = x_scale // 5
    canvas.create_oval(
        x_offset - r, y_offset - r,
        x_offset + r, y_offset + r
    )


def draw_lines(
        canvas: 'tk.Canvas', num_of_axis: int,
        canvas_size=DEFAULT_CANVAS_SIZE, axis_indent=DEFAULT_AXIS_INDENT):
    """Draw lines forming axis"""
    width, height = canvas_size
    x_offset, y_offset = width // 2, height // 2

    if num_of_axis > 0:
        # X
        line = [
            axis_indent, y_offset,
            width - axis_indent, y_offset
        ]
        canvas.create_line(*line)
    if num_of_axis > 1:
        # Y
        line = [
            x_offset, axis_indent,
            x_offset, height - axis_indent
        ]
        canvas.create_line(*line)


def draw_arrows(
        canvas: 'tk.Canvas', num_of_axis: int,
        canvas_size=DEFAULT_CANVAS_SIZE,
        axis_indent=DEFAULT_AXIS_INDENT,
        arrow_indent=DEFAULT_ARROW_INDENT
):
    """Draw arrows indicating direction"""
    width, height = canvas_size
    x_offset, y_offset = width // 2, height // 2

    if num_of_axis > 0:
        # X
        line = [
            width - axis_indent, y_offset,
            width - 2*axis_indent, y_offset - arrow_indent
        ]
        canvas.create_line(*line)
        line[3] = y_offset + arrow_indent
        canvas.create_line(*line)

    if num_of_axis > 1:
        line = [
            x_offset, axis_indent,
            x_offset - arrow_indent, axis_indent * 2
        ]
        canvas.create_line(*line)
        line[2] = x_offset + arrow_indent
        canvas.create_line(*line)


def draw_axis_names(
        canvas: 'tk.Canvas', num_of_axis: int,
        canvas_size=DEFAULT_CANVAS_SIZE,
        axis_indent=DEFAULT_AXIS_INDENT,
):
    """Draw axis names"""
    width, height = canvas_size
    x_offset, y_offset = width // 2, height // 2

    axis_name = 'x'
    if num_of_axis > 0:
        # X
        x = width - int(1.5 * axis_indent)
        y = y_offset - axis_indent
        canvas.create_text(x, y, text=axis_name)
    axis_name = 'y'
    if num_of_axis > 1:
        # Y
        x = x_offset + axis_indent
        y = int(1.5 * axis_indent)
        canvas.create_text(x, y, text=axis_name)


def draw_serifs(
        canvas: 'tk.Canvas', num_of_axis: int,
        canvas_size=DEFAULT_CANVAS_SIZE,
        axis_indent=DEFAULT_AXIS_INDENT,
        axis_scale=DEFAULT_AXIS_SCALE
):
    """Draw serifs. Reflection_type in REFLECTIONS"""
    width, height = canvas_size
    x_offset, y_offset = width // 2, height // 2
    x_scale, y_scale = axis_scale

    def reflector(
            reflection_type: str,
            serif: list,
            offset: int, length: int, scale: int
    ):
        reflection_matrix = TRANSFORMATIONS[reflection_type]  # reflect at y

        p1 = d2s(tuple(serif[0]), canvas_size, axis_scale)
        p2 = d2s(tuple(serif[1]), canvas_size, axis_scale)

        axis_bias = offset + scale

        while axis_bias < length - 2*axis_indent:
            canvas.create_line(*p1, *p2)

            reflected_serif = np.matmul(
                np.array(serif), np.array(reflection_matrix)
            ).tolist()
            p1 = d2s(reflected_serif[0], canvas_size, axis_scale)
            p2 = d2s(reflected_serif[1], canvas_size, axis_scale)
            canvas.create_line(*p1, *p2)

            # Cycle parameters
            axis_bias += scale
            if reflection_type == 'ry':
                serif[0][0] += 1
                serif[1][0] += 1
            elif reflection_type == 'rx':
                serif[0][1] += 1
                serif[1][1] += 1

            p1 = d2s(tuple(serif[0]), canvas_size, axis_scale)
            p2 = d2s(tuple(serif[1]), canvas_size, axis_scale)

    if num_of_axis > 0:
        x_serif = [  # Descartes
            [1, 0.2],
            [1, -0.2]
        ]
        reflector('ry', x_serif, x_offset, width, x_scale)
    if num_of_axis > 1:
        y_serif = [  # Descartes
            [-0.2, 1],
            [0.2, 1]
        ]
        reflector('rx', y_serif, y_offset, height, y_scale)
