#!/usr/bin/python
import os

class Pid():
    __path = ""

    def __init__(self, path = "/var/run/nginx.pid"):
        self.__path = path
        return 

    def __valid(self):
        return os.path.exists(self.getPath())


    def setPath(self, path):
        self.__path = path
        return
    def getPath(self):
        return self.__path;
    
    def isValid(self):
        return self.__valid()
    
    def __repr__(self):
        return "pid %s;\n" % (self.getPath())
