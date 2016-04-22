#!/usr/bin/python
import os

class WorkerRlimitNofile():
    __nofile = 0
    
    def __init__(self, nofile = None):
        if(nofile == None):
            result = os.popen("ulimit -a | grep files").read().split(" ")[-1]
            nofile = int(result)
        self.__nofile = nofile
        return

    def __valid(self):
        return self.__nofile >= 0

    def isValid(self):
        return self._valid()  

    def setNofile(self, nofile):
        self.__nofile = nofile
        return
    def getNofile(self):
        return self.__nofile

    def __repr__(self):
        return "worker_rlimit_nofile %d;\n" %(self.getNofile())
