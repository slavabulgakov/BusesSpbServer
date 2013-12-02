from django.http import HttpResponse
from django.utils import simplejson
import json
import urllib2
import urllib
import settings

def _getData(folder, filename):
	if settings.DEBUG:
		path = 'other/'
	else:
		path = '/home/f/futbixru/busesspb/public_html/busesspb/other/'
	f = open(path + folder + '/' + filename, 'r')
	text = f.read()
	return text

def listdata(request):
	try:
		data = _getData('list', 'data.dat')
	except Exception, e:
		data = ''
	return HttpResponse(data, content_type="text/plain")

def routesdata(request):
	try:
		data = _getData('feed/extract', 'routes.txt')
	except Exception, e:
		data = ''
	return HttpResponse(data, content_type="text/plain")

def version(request):
	try:
		data = _getData(request.path.split('/')[1], 'version.dat')
	except Exception, e:
		data = '1'
	return HttpResponse(data, content_type="text/plain")

def version_old(request):
	try:
		data = _getData('list', 'version.dat')
	except Exception, e:
		data = '1'
	return HttpResponse(data, content_type="text/plain")