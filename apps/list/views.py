from django.http import HttpResponse
from django.utils import simplejson
import json
import urllib2
import urllib
import settings

def _getData():
	if settings.DEBUG:
		path = 'other/data'
	else:
		path = '/home/f/futbixru/busesspb/public_html/busesspb/other/data'
	f = open(path, 'r')
	text = f.read()
	return text

def echo(request):
	data = _getData()
	divider = data.find('=>')
	text = data[divider + 2 : ]
	return HttpResponse(text, content_type="text/plain")

def version(request):
	data = _getData()
	divider = data.find('=>')
	version = data[0 : divider]
	return HttpResponse(version, content_type="text/plain")