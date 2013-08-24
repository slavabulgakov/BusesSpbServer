from django.http import HttpResponse
from django.utils import simplejson
import json
from models import UserProfile, User
import urllib2
import urllib
import settings

def _getRequest(url):
	response = urllib.urlopen(url)
	page = response.read()
	return page

def _updateUserInfo(vk_id, first_name, last_name, access_token, request):
	# user = auth.authenticate(username=vk_id, password=password)
	try:
		user = User.objects.get(username__exact=str(vk_id))
	except User.DoesNotExist:
		user = None

	# user = User.objects.get(username__exact=str(vk_id))
	if user is not None and user.is_active:
		user.backend='django.contrib.auth.backends.ModelBackend'
		auth.login(request, user)
	else:
		password = generatePassword()
		user = UserProfile.objects.create_user(username = vk_id, email = '', password=password)
		user.vk_id = vk_id
		user.first_name = first_name
		user.last_name = last_name
		user.save()

def auth(request):
	code = request.GET['code']
	request_url = vk.api_url + '/access_token?client_id=' + str(vk.app_id) + '&client_secret=' + vk.app_secret + '&code=' + code + 'redirect_url=http://brainshake.ru/auth'
	page = _getRequest(request_url)
	response = json.loads(page)
	try:
		vk_access_token = response['access_token']
		vk_user_id = response['user_id']
	except Exception, e:
		return HttpResponse('error')
	else:
		pass
	finally:
		pass

	vk_id = profiles['response'][0]['uid']
	first_name = profiles['response'][0]['first_name']
	last_name = profiles['response'][0]['last_name']
	_updateUserInfo(vk_id, first_name, last_name, vk_access_token, request)

	return HttpResponse('ok', content_type="text/plain")

def _isAuth(request):
	if request.user.is_authenticated():
		return HttpResponse(request.user.first_name + ' ' + request.user.last_name, content_type="text/plain")
	return HttpResponse("false", content_type="text/plain")

def addLike(request):
	bus_id = request.GET['bus_id']
	if _isAuth(request):
		user = UserProfile.objects.filter(user_id = request.user.id)[0]
		bus = Buses.objects.filter(bus_id = bus_id)
		likes = Likes.objects.filter(user = user, bus = bus)
		if likes.count() == 0:
			like = Likes(user = user, bus = bus)
			like.save()
			return HttpResponse('ok', content_type="text/plain")
		else:
			return HttpResponse('exist', content_type="text/plain")
	else:
		return HttpResponse('not auth', content_type="text/plain")

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

def root(request):
        return HttpResponse("", content_type="text/plain")
