
# coding: utf-8

import requests

data = {'user': 'huge', 'password': 'file'}

url = 'http://www.pythonchallenge.com/pc/return/good.html'
r = requests.get(url, data)

print r.url
print r.text

