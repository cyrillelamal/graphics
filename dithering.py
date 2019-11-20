from math import floor


def fs_dithering(pixels):
    """Floyd-Steiner dithering. Affect passed pixels"""
    height = len(pixels)
    width = len(pixels[0])

    for y in range(1, height):
        for x in range(1, width):
            old_pixel = pixels[x][y]
            new_pixel = map_threshold(old_pixel)

            errors = [
                old_color - new_color
                for old_color, new_color
                in zip(old_pixel, new_pixel)
            ]

            if x < width - 1:  # Pixel at East
                pixel = [
                    old_color + round(err * 7/16)
                    for old_color, err
                    in zip(pixels[x+1][y], errors)
                ]
                pixels[x+1][y] = pixel

            if x > 1 and y < height - 1:  # Pixel at South-West
                pixel = [
                    old_color + round(err * 3/16)
                    for old_color, err
                    in zip(pixels[x-1][y+1], errors)
                ]
                pixels[x-1][y+1] = pixel

            if y < height - 1:  # Pixel at South
                pixel = [
                    old_color + round(err * 5/16)
                    for old_color, err
                    in zip(pixels[x][y+1], errors)
                ]
                pixels[x][y+1] = pixel

            if x < width - 1 and y < height - 1:  # Pixel at South-East
                pixel = [
                    old_color + round(err / 16)
                    for old_color, err
                    in zip(pixels[x+1][y+1], errors)
                ]
                pixels[x+1][y+1] = pixel


def map_threshold(pixel):
    """Map to the closest colors"""
    return [255 * floor(color/128) for color in pixel]
