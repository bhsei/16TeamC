#!/usr/bin/python
import os

class WorkerRlimitNofile():
    __isvalid = False
    __nofile = 0
    
    def __init__(self, nofile = None):
        if(nofile == None):
            result = os.popen("ulimit -a | grep files").read().split(" ")[-1]
            nofile = int(result)
        self.__nofile = nofile
        self.__isvalid = self.__valid()
        return

    def __valid(self):
        return self.__nofile >= 0

    def isValid(self):
        return self.__isvalid   

    def getProcess(self):
        return self.__nofile

    def reNew(self, nofile):
        self.__init__(nofile)
