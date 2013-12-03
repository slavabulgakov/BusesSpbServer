from filesIO import *
from os import listdir
from os.path import isdir, exists
from StringIO import StringIO
import zipfile

for item in listdir('.'):
	if isdir(item):
		run = __import__(item + '.run', fromlist=['load'])
		data = run.load()
		oldData = openFile(item + '/data.dat')
		version = 0
		v = openFile(item + '/version.dat')
		if len(v) > 0:
			version = int(v)
		if data != oldData:
			version = version + 1
			saveFile(item + '/data.dat', data)
			zippath = item + '/extract'
			if exists(zippath):
				zipData = StringIO()
				zipData.write(data)
				z = zipfile.ZipFile(zipData)
				z.extractall(zippath)
		saveFile(item + '/version.dat', str(version))