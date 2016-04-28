#!/usr/bin/python
import re

class Server():
    __listen = 80
    __server_name = []
    __index = []
    __root = ""
    __location = []
    __re = re.compile(r".*server\s*\{\s*listen\s*(\d*);\s*server_name\s*(.*);\s*index\s*(.*);\s*root\s*(\S*);\s*\}",re.DOTALL)
    
    def __init__(self,listen = 80, server_name = ["www.example.com"], index = ["index.html","index.htm"], root = "/var/www",location = []):
        self.__listen = listen
        self.__server_name = server_name
        self.__index = index
        self.__root = root
        self.__location = location
        return 

    def __valid(self):
        return self.getListen() in range(0,65536)

    def setUp(self,s):
        r = self.__re.match(s)
        if r!=None:
            r = r.groups() 
            self.setListen(int(r[0]))
            self.setServerName(r[1].split(" "))
            self.setIndex(r[2].split(" "))
            self.setRoot(r[3])
            return True
        return False

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
        ret = "\tserver {\n"
        ret += "\t\tlisten %d;\n" %(self.getListen())
        ret += "\t\tserver_name "
        for i in self.getServerName():
            ret += i + " "
        ret += ";\n"
        ret += "\t\tindex "
        for i in self.getIndex():
            ret += i + " "
        ret += ";\n"
        ret += "\t\troot %s;\n" %(self.getRoot())
        ret += "\t}\n"
        return ret

