# coding: utf-8


url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'

from urllib import urlopen
from PIL import Image, ImageDraw


if __name__ == '__main__':

    img = Image.open("oxygen.png")

    # mode of the picture
    print img.mode  # RGBA

    w, h = img.size
    print w, h  # 629 95
    row = [img.getpixel((x, 45)) for x in range(0, w, 7)]
    rs = [r for r, g, b, a in row if r == g == b]

    print ''.join([chr(i) for i in rs])


rs = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(i) for i in rs])