#!/usr/bin/python
import os

class Pid():
    __path = ""
    __isvalid = False

    def __init__(self, path = "/var/run/nginx.pid"):
        self.__path = path
        self.__isvalid = self.__valid_path()
        return 

    def __valid_path(self):
        return os.path.exists(self.getPath())

    def getPath(self):
        return self.__path;
    
    def isValid(self):
        return self.__isvalid
    
    def reNew(self, path):
        self.__init__(path)
        return 
    
