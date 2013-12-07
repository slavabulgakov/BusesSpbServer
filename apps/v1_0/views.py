from django.http import HttpResponse
import settings

def _getData(folder, filename):
	if settings.DEBUG:
		path = 'data/v1_0/'
	else:
		path = '/home/f/futbixru/busesspb/public_html/busesspb/data/v1_0/'
	f = open(path + folder + '/' + filename, 'r')
	text = f.read()
	f.close()
	return text

def listdata(request):
	data = _getData('list', 'data.dat')
	return HttpResponse(data, content_type="text/plain")

def routesdata(request):
	data = _getData('feed/extract', 'routes.txt')
	return HttpResponse(data, content_type="text/plain")

def version(request):
	bits = request.path.split('/')
	data = ''
	if settings.DEBUG:
		index = 2
		count = 5
	else:
		index = 3
		count = 6
	if len(bits) == count:
		data = _getData(request.path.split('/')[index], 'version.dat')
	return HttpResponse(data, content_type="text/plain")