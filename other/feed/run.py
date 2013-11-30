import zipfile
import urllib2
from StringIO import StringIO

DEBUG = True

if DEBUG:
	path = ''
else:
	path = '/home/f/futbixru/feed/'

url = urllib2.urlopen('http://transport.orgp.spb.ru/Portal/transport/internalapi/gtfs/feed.zip')
data = url.read()

zipDataPath = path + 'data'
fdata = ''
try:
	f = open(zipDataPath, 'r')
except Exception, e:
	pass
else:
	fdata = f.read()
	f.close()
version = 0
oldText = ''
if '=>' in fdata:
        divider = fdata.find('=>')
        version = int(fdata[0 : divider])
        oldText = fdata[divider + 2 : ]
if data != oldText:
        f = open(zipDataPath, 'w')
        f.write(str(version + 1) + '=>' + data)
        f.close()

zipData = StringIO()
zipData.write(data)
z = zipfile.ZipFile(zipData)
zippath = path + 'feed'
z.extractall(zippath)