#!/usr/bin/python


class Server():
    __listen = 80
    __server_name = []
    __index = []
    __root = ""
    __location = []
    
    def __init__(self,listen = 80, server_name = ["www.example.com"], index = ["index.html","index.htm"], root = "/var/www",location = []):
        self.__listen = listen
        self.__index = server_name
        self.__index = index
        self.__root = root
        self.__location = location
        return 

    def __valid(self):
        return self.getListen() in range(0,65536)

    def isValid(self):
        return self.__valid()

    def getListen(self):
        return self.__listen
    def setListen(self,listen):
        self.__listen = listen
        return

    def getServerName(self):
        return self.__server_name
    def setServerName(self,server_name):
        self.__server_name = server_name
        return

    def getIndex(self):
        return self.__index
    def setIndex(self, index):
        self.__index = index

    def getRoot(self):
        return self.__root
    def setRoot(self, root):
        self.__root = root
        return

    def getLocation(self):
        return self.__location
    def setLocation(self, location):
        self.__location = location
        return 

    def __repr__(self):
        ret = "server {\n"
        ret += "\tlisten %d;\n" %(self.getListen())
        ret += "\tserver_name "
        for i in self.getServerName():
            ret += i + " "
        ret += ";\n"
        ret += "\tindex "
        for i in self.getIndex():
            ret += i + " "
        ret += ";\n"
        ret += "\troot %s;\n" %(self.getRoot())
        ret += "}\n"
        return ret

    def _str__(self):
        return self.__repr__()
