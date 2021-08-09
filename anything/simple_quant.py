#!/user/bin/python
# -*-coding:UTF-8-*-

"""简单的图片量化算法"""
from PIL import Image


def simple_quant():
    im = Image.open("bubbles.jpg")
    w, h = im.size

    for row in range(h):
        for col in range(w):
            r, g, b = im.getpixel((col, row))
            r = r // 36 * 36
            g = g // 42 * 42
            b = b // 42 * 42

            im.putpixel((col, row), (r, g, b))

    im.save("bubbles_simple.jpg")


if __name__ == '__main__':
    simple_quant()
