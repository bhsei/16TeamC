#!/usr/bin/python
import os

class ErrorLog():
    __path = ""
    __isvalid = False
    __info_set = [ "debug", "info", "notice", "warn", "error","crit" ] 
    __info = "debug"

    def __init__(self, path = "/var/log/nginx/error.log", info = "debug"):
        self.__path = path
        self.__info = info
        self.__isvalid = self.__valid_path()
        return 

    def __valid_path(self):
        flag = os.path.exists(self.getPath())
        flag = flag and (self.__info in self.__info_set)
        return flag

    def getPath(self):
        return self.__path;
    
    def getInfo(self):
        return self.__info
    
    def isValid(self):
        return self.__isvalid
    
    def reNew(self, path):
        self.__init__(path)
        return 
 
