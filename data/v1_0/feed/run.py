import urllib2

def load():
	url = urllib2.urlopen('http://transport.orgp.spb.ru/Portal/transport/internalapi/gtfs/feed.zip')
	data = url.read()
	return data