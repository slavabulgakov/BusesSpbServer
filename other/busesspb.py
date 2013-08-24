import urllib
import urllib2

DEBUG = True

params = urllib.urlencode({
                'sEcho' : '10',
                'iColumns' : '11',
                'sColumns' : 'id,transportType,routeNumber,name,urban,poiStart,poiFinish,cost,forDisabled,scheduleLinkColumn,mapLinkColumn',
                'iDisplayStart' : '0',
                'iDisplayLength' : '1000',
                'sNames' : 'id,transportType,routeNumber,name,urban,poiStart,poiFinish,cost,forDisabled,scheduleLinkColumn,mapLinkColumn',
                'iSortingCols' : '1',
                'iSortCol_0' : '2',
                'sSortDir_0' : 'asc',
                'bSortable_0' : 'true',
                'bSortable_1' : 'true',
                'bSortable_2' : 'true',
                'bSortable_3' : 'true',
                'bSortable_4' : 'true',
                'bSortable_5' : 'true',
                'bSortable_6' : 'true',
                'bSortable_7' : 'true',
                'bSortable_8' : 'true',
                'bSortable_9' : 'true',
                'bSortable_10' : 'true',
                'transport-type' : '1',
                'transport-type' : '46',
                'transport-type' : '2',
                'transport-type' : '0'
                })
url = urllib2.urlopen('http://transport.orgp.spb.ru/Portal/transport/routes/list', params)
text = url.read()
if DEBUG:
        path = 'data'
else:
        path = '/home/f/futbixru/data'
data = ''
try:
        f = open(path, 'r')
except Exception, e:
        pass
else:
        data = f.read()
        f.close()
version = 0
oldText = ''
if '=>' in data:
        divider = data.find('=>')
        version = int(data[0 : divider])
        oldText = data[divider + 2 : ]
if text != oldText:
        f = open(path, 'w')
        f.write(str(version + 1) + '=>' + text)
        f.close()