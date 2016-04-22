#!/usr/bin/python
import os

class ErrorLog():
    __path = ""
    __info_set = [ "debug", "info", "notice", "warn", "error","crit" ] 
    __info = "debug"

    def __init__(self, path = "/var/log/nginx/error.log", info = "debug"):
        self.__path = path
        self.__info = info
        return 

    def __valid(self):
        flag = os.path.exists(self.getPath())
        flag = flag and (self.__info in self.__info_set)
        return flag

    def setPath(self,path):
        self.__path = path 
        return 
    def getPath(self):
        return self.__path;
    
    def setInfo(self, info):
        self.__info = info
        return 
    def getInfo(self):
        return self.__info
    
    def isValid(self):
        return self.__valid()
    
    def __repr__(self):
        return "error_log %s %s;\n" %(self.getPath(),self.getInfo())
