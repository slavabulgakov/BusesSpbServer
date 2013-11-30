DEBUG = True

path = ''
if DEBUG:
        path = ''
else:
        path = '/home/f/futbixru/list/'

def openFile(filename):
        data = ''
        try:
                f = open(path + filename, 'r')
        except Exception, e:
                pass
        else:
                data = f.read()
                f.close()
        return data

def saveFile(filename, data):
        f = open(path + filename, 'w')
        f.write(data)
        f.close()