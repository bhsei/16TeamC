#!/usr/bin/python
import os
import re

class ErrorLog():
    __path = ""
    __info_set = [ "debug", "info", "notice", "warn", "error","crit" ] 
    __info = "debug"
    __re = re.compile(r".*error_log (\S*) (\w*);",re.DOTALL)

    def __init__(self, path = "/var/log/nginx/error.log", info = "debug"):
        self.__path = path
        self.__info = info
        return 

    def __valid(self):
        flag = os.path.exists(self.getPath())
        flag = flag and (self.__info in self.__info_set)
        return flag

    def setUp(self,s):
        r = self.__re.match(s)
        if r != None:
            r = r.groups()
            self.setInfo(r[1])
            self.setPath(r[0]) 
            return True
        return False

    def setInfoSet(self,info_set):
        self.__info_set = info_set 
        return 
    def getInfoSet(self):
        return self.__info_set;

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
