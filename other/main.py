from filesIO import *
from os import listdir
from os.path import isfile

for item in listdir('.'):
	if not isfile(item):
		run = __import__(item + '.run', fromlist=['load'])
		text = run.load()
		oldText = openFile(item + '/data')
		version = 0
		if text != oldText:
			saveFile(item + '/data', text)
			v = openFile('version')
			if len(v) > 0:
				version = int(v)
		saveFile(item + '/version', str(version + 1))