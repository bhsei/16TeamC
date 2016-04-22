#!/usr/bin/python
import os

class WorkProcess():
    __process = 0
    
    def __init__(self, process = None):
        if(process == None):
            result = os.popen("grep 'processor' /proc/cpuinfo  | wc -l").read()
            process = int(result)
        self.__process = process
        return

    def __valid(self):
        return self.__process >= 0

    def isValid(self):
        return self.__valid()

    def setProcess(self, process):
        self.__process = process
        return
    def getProcess(self):
        return self.__process

    def __repr__(self):
        return "worker_processes %d;\n" % (self.getProcess())
