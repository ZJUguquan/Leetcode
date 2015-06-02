# coding: utf-8

from urllib import urlopen
from PIL import Image, ImageDraw


url = 'http://www.pythonchallenge.com/pc/def/integrity.html'

print urlopen(url).read()