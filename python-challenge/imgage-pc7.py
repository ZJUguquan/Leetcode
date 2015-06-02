
# coding: utf-8


# challenge 7 http://www.pythonchallenge.com/pc/def/oxygen.html
#
url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'

from PIL import Image
import glob


fpng = '/Users/jinyongyang/oxygen.png'
img = Image.open(fpng)
print img

w, h = img.size
print w, h

row = [img.getpixel((x, 45)) for x in range(0, w, 7)]

print ''.join([chr(i[1]) for i in row])

answers = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(i) for i in answers])

# integrity