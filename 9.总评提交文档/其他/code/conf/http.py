#!/usr/bin/python
import re
from server import Server
class Http():
    __upstream = None
    __server = Server()
    __re = re.compile(r".*http\s*\{(.*)\}",re.DOTALL)

    def __init__(self, upstream = None, server = Server()):
        self.__upstream = upstream
        self.__server = server
        return

    def __valid(self):
        return True
    
    def setUp(self,s):
        r = self.__re.match(s) 
        if r != None:
            r = r.groups()
            return self.getServer().setUp(r[0])
        return False
    
    def isValid(self):
        return self.__valid()

    def getUpstream(self):
        return self.__upstream
    def setUpstream(self, upstream):
        self.__upstream = upstream
        return

    def getServer(self):
        return self.__server
    def setServer(self, server):
        self.__server = server
        return
    
    def __repr__(self):
        ret = "http {\n"
        ret += repr(self.getServer())
        ret += "}\n"
        return ret
        
