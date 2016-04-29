#!/usr/bin/python
import os
import re
from user import User
from work_process import WorkProcess
from pid import Pid
from error_log import ErrorLog
from worker_rlimit_nofile import WorkerRlimitNofile
from events import Events
from http import Http
class Conf():
    __user = User()
    __work_process = WorkProcess()
    __pid = Pid()
    __error_log = ErrorLog()
    __worker_rlimit_nofile = WorkerRlimitNofile()
    __events = Events() 
    __http = Http()

    def __init__(self, path = "./nginx.conf"):
        self.__path = path
        return 

    def __valid(self):
        dirname = os.path.dirname(self.getPath())
        return os.path.exists(dirname)

    def getUser(self):
        return self.__user
    def setUser(self, user):
        self.__user = user
        return

    def getWorkProcess(self):
        return self.__work_process
    def setWorkProcess(self, work_process):
        self.__work_process = work_process
        return

    def getPid(self):
        return self.__pid
    def setPid(self, pid):
        self.__pid = pid
        return

    def getErrorLog(self):
        return self.__error_log
    def setErrorLog(self, error_log):
        self.__error_log = error_log
        return

    def getWorkerRlimitNofile(self):
        return self.__worker_rlimit_nofile
    def setWorkerRilimitNofile(self, worker_rlimit_nofile):
        self.__worker_rlimit_nofile = worker_rlimit_nofile
        return

    def getEvents(self):
        return self.__events
    def setEvents(self, events):
        self.__events = events
        return

    def getHttp(self):
        return self.__http
    def setHttp(self, http):
        self.__http = http
        return

    def setPath(self,path):
        self.__path = path
        return
    def getPath(self):
        return self.__path;
    
    def isValid(self):
        return self.__valid()
    
    def setUpFromFile(self):
        f = open(self.getPath())
        s = f.read()
        self.getUser().setUp(s)	
        self.getWorkProcess().setUp(s)
        self.getPid().setUp(s)
        self.getErrorLog().setUp(s)
        self.getWorkerRlimitNofile().setUp(s)
        self.getEvents().setUp(s)
        self.getHttp().setUp(s)
        return 

    def __repr__(self):
        s = ""
        s +=str(self.getUser())
        s +=str(self.getWorkProcess())
        s +=str(self.getPid())
        s +=str(self.getErrorLog())
        s +=str(self.getWorkerRlimitNofile())
        s +=str(self.getEvents())
        s +=str(self.getHttp())
        return s

    def writeToFile(self):
        if self.isValid():
            f = open(self.getPath(),"w")
            f.write(str(self))
            f.close()
        else:
            pass
        return

if __name__ == "__main__":
    a = Conf()
    a.writeToFile() 
