import filesIO
from os import listdir
from os.path import isdir, exists
from StringIO import StringIO
import zipfile

path = ''
if filesIO.DEBUG:
        path = '.'
else:
        path = '/home/f/futbixru/busesspb/public_html/busesspb/data/v1_0/'

for item in listdir(path):
	if isdir(item):
		run = __import__(item + '.run', fromlist=['load'])
		data = run.load()
		oldData = filesIO.openFile(item + '/data.dat')
		version = 0
		v = filesIO.openFile(item + '/version.dat')
		if len(v) > 0:
			version = int(v)
		if data != oldData:
			version = version + 1
			filesIO.saveFile(item + '/data.dat', data)
			zippath = item + '/extract'
			if exists(zippath):
				zipData = StringIO()
				zipData.write(data)
				z = zipfile.ZipFile(zipData)
				z.extractall(zippath)
		filesIO.saveFile(item + '/version.dat', str(version))