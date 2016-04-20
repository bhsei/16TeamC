#!/usr/bin/python
import os
from user import User
from work_process import WorkProcess
from pid import Pid
from error_log import ErrorLog
from worker_rlimit_nofile import WorkerRlimitNofile

class Conf():
    __path = ""
    __isvalid = False
    user = User()
    work_process = WorkProcess()
    pid = Pid()
    error_log = ErrorLog()
    worker_rlimit_nofile = WorkerRlimitNofile()
    events = None
    http = None

    def __init__(self, path = "./nginx.conf"):
        self.__path = path
        self.__isvalid = self.__valid_path()
        return 

    def __valid_path(self):
        return os.path.exists(self.getPath())

    def getPath(self):
        return self.__path;
    
    def isValid(self):
        return self.__isvalid
    
    def reNew(self, path):
        self.__init__(path)
        return 
    
    def setUpFromFile(self):
        return 
