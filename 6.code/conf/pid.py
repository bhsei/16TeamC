#!/usr/bin/python
import os
import re

class Pid():
    __path = ""
    __re = re.compile(r".*pid (\S*);",re.DOTALL)

    def __init__(self, path = "/var/run/nginx.pid"):
        self.__path = path
        return 

    def __valid(self):
        return os.path.exists(self.getPath())

    def setUp(self, s):
        r = self.__re.match(s)
        if r!= None:
            r = r.groups()
            self.setPath(r[0])
            return True
        return False

    def setPath(self, path):
        self.__path = path
        return
    def getPath(self):
        return self.__path;
    
    def isValid(self):
        return self.__valid()
    
    def __repr__(self):
        return "pid %s;\n" % (self.getPath())
