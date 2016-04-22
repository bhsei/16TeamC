#!/usr/bin/python
from server import Server
class Http():
    __upstream = None
    __server = [Server()]

    def __init__(self, upstream = None, server = [Server()]):
        self.__upstream = upstream
        self.__server = server
        return

    def __valid(self):
        return True
    
    def isValid(self):
        return self.__valid()

    def getUpstream(self):
        return self.__upstream
    def setUpstream(self, upstream):
        self.__upstream = upstream
        return

    def getServer(self):
        return self.__server
    def setServer(self, servers):
        self.__server = servers
        return
    def addServer(self, server):
        self.__server.append(server)
        return
    
    def __repr__(self):
        ret = "http {\n"
        tmp = self.getServer() 
        for i in tmp:
            ret += repr(i)
        ret += "}\n"
        return ret
        
