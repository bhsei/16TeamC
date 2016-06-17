import urllib2
import re

def getstatus(server_name):

# check link connected
    try:
        urllib2.urlopen('http://'+server_name, timeout=5)
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            return [0, 0, 0, 0, 0, 0, 0, 'off']
        elif hasattr(e, 'reason'):
            return [0, 0, 0, 0, 0, 0, 0, 'off']

# crwal status information
    fa = re.findall('\d+', str(urllib2.urlopen('http://'+server_name+'/status').read()))
    fa .append('on')
    return fa

