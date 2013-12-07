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

def echo(request):
    data = _getData('list', 'data.dat')
    return HttpResponse(data, content_type="text/plain")
    
def version(request):
    data = _getData('list', 'version.dat')
    return HttpResponse(data, content_type="text/plain")