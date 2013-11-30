from filesIO import *
from list.run import load
from os import listdir
from os.path import isfile

for item in listdir:
	if !isfile(item):
		

text = load()
oldText = openFile('list/list')

if text != oldText:
        saveFile('list/list', text)
        v = openFile('version')
        version = 0
        if len(v) > 0:
                version = int(v)
        saveFile('list/version', str(version + 1))