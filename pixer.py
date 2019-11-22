import sys
from PIL import Image


def pixel_color(img_path, x, y):
    pixel = (int(x), int(y))
    im = Image.open(img_path)
    rgb_im = im.convert('RGB')
    return rgb_im.getpixel(pixel)


if __name__ == '__main__':
    img_path = sys.argv[1]
    x, y = sys.argv[2:4]

    r, g, b = pixel_color(img_path, x, y)

    print(r, g, b)
