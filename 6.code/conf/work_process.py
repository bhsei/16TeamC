#!/usr/bin/python
import os

class WorkProcess():
    __isvalid = False
    __process = 0
    
    def __init__(self, process = None):
        if(process == None):
            result = os.popen("grep 'nofileor' /proc/cpuinfo  | wc -l").read()
            process = int(result)
        self.__process = process
        self.__isvalid = self.__valid()
        return

    def __valid(self):
        return self.__process >= 0

    def isValid(self):
        return self.__isvalid   

    def getProcess(self):
        return self.__process

    def reNew(self, process):
        self.__init__(process)
