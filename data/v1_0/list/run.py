import urllib
import urllib2

def load():
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
                'bSortable_9' : 'false',
                'bSortable_10' : 'false',
                # 'transport-type' : '1',
                # 'transport-type' : '46',
                # 'transport-type' : '2',
                # 'transport-type' : '0',
                })
        params = params + '&transport-type=0&transport-type=2&transport-type=1'
        url = urllib2.urlopen('http://transport.orgp.spb.ru/Portal/transport/routes/list', params)
        text = url.read()
        return text