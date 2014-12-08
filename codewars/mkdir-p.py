import os

def mkdirp(*directories):
	try:
		os.makedirs(os.path.join(*directories))
	except OSError:
		pass


mkdirp('/Steve/Users/','staticor','/Dropbox/Python/','howareyou')