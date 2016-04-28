import urllib2
import re


def getstatus(server_name):
    response = urllib2.urlopen("http://"+server_name+"/ngx_status")
    message = response.read()
    matchObj = re.match(r'Active connections: (.*) \nserver accepts handled requests\n (\d*) (\d*) (\d*) \nReading: (\d*) Writing: (\d*) Waiting: (\d*)', message, re.I)
    active_connections = matchObj.group(1)
    accepts = matchObj.group(2)
    handled = matchObj.group(3)
    request = matchObj.group(4)
    reading = matchObj.group(5)
    writing = matchObj.group(6)
    waiting = matchObj.group(7)

    return [active_connections,accepts,handled,request,reading,writing,waiting]

