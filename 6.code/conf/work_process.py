#!/usr/bin/python
import os
import re

class WorkProcess():
    __process = 0
    __re = re.compile(r".*worker_processes (\d*)",re.DOTALL)
    
    def __init__(self, process = None):
        if(process == None):
            result = os.popen("grep 'processor' /proc/cpuinfo  | wc -l").read()
            process = int(result)
        self.__process = process
        return

    def __valid(self):
        return self.__process >= 0
    
    def setUp(self,s):
        r = self.__re.match(s)
        if r != None:
            r = r.groups()
            self.setProcess(int(r[0]))
            return True
        return False


    def isValid(self):
        return self.__valid()

    def setProcess(self, process):
        self.__process = process
        return
    def getProcess(self):
        return self.__process

    def __repr__(self):
        return "worker_processes %d;\n" % (self.getProcess())
