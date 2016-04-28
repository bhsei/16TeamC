#!/usr/bin/python
import os
import re

class WorkerRlimitNofile():
    __nofile = 0
    __re = re.compile(r".*worker_rlimit_nofile (\d*);",re.DOTALL)
    
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

    def setUp(self,s):
        r = self.__re.match(s)
        if r != None:
            r = r.groups()
            self.setNofile(int(r[0]))
            return True
        return False

    def setNofile(self, nofile):
        self.__nofile = nofile
        return
    def getNofile(self):
        return self.__nofile

    def __repr__(self):
        return "worker_rlimit_nofile %d;\n" %(self.getNofile())
