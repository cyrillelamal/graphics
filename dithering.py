def fs_dithering(pixels):
    """Floyd-Steiner dithering. Affect passed pixels"""
    height = len(pixels) - 1

    for y in range(height):
        width = len(pixels[y]) - 1
        for x in range(width):
            old_pixel = pixels[x][y]
            new_pixel = similar_color(old_pixel)
            pixels[x][y] = new_pixel

            err = old_pixel - new_pixel

            pixels[x + 1][y] = pixels[x + 1][y] + err * 7 / 16
            pixels[x - 1][y + 1] = pixels[x - 1][y + 1] + err * 3 / 16
            pixels[x][y + 1] = pixels[x][y + 1] + err * 5 / 16
            pixels[x + 1][y + 1] = pixels[x + 1][y + 1] + err * 1 / 16

    return pixels


def similar_color(old_pixel):
    return round(old_pixel / 255, 2)


if __name__ == '__main__':
    m = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(fs_dithering(m))
