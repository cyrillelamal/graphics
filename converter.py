import math

BASE_SCALE = (8, 8)

# Affine transformations matrices
TRANSFORMATIONS = {
    # Reflect at y
    'ry': [
        (-1, 0),
        (0, 1)
    ],
    # Reflect at x
    'rx': [
        (1, 0),
        (0, -1)
    ],
    'rotate': [
        [lambda thi: math.cos(thi), lambda thi: math.sin(thi)],
        [lambda thi: -math.sin(thi), lambda thi: math.cos(thi)],
    ],
    'y=x': [
        [0, 1],
        [1, 0]
    ],
    'y=0': [
        [1, 0],
        [1, 0]
    ]
}


def d2s(point: [tuple, list], window_size: tuple, scale: tuple = None):
    """Convert Descartes point to screen point."""
    if len(point) == 2:
        x, y = point
    elif len(point) == 3:
        x, y, z = point
    else:
        return point

    # TODO: z axis

    width, height = window_size
    xscale, yscale = BASE_SCALE if scale is None else scale

    x_mid = width // 2
    y_mid = height // 2
    x = x_mid + int(x * xscale)
    y = y_mid - int(y * yscale)

    return x, y


def fig2s(points: [list, tuple], window_size, scale=BASE_SCALE):
    """Transform list of points to raw integers acceptable by create* methods"""
    fig_points = []
    for p in points:
        fig_points += [*d2s(p, window_size, scale)]
    return fig_points


# def r2s(point):
#     """
#     Base:
#     x(s) = a*x(m) + b
#     y(s) = c*y(m) + d
#     x(min) <= x(m) <= x(max)
#     y(min) <= y(m) <= y(max)
#
#     Left-top point = (left, top)
#     Width and height of the area = (width, height)
#
#     x(s) = left + width/(x(max) - x(min) * (x(m) - x(min))
#     y(s) = top + height -  height/(y(max) - y(min)) * (y(m) - y(min))
#     """
#     if len(point) == 2:
#         x, y = point
#     elif len(point) == 3:
#         x, y, z = point
#     else:
#         return point
