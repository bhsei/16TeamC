#!/usr/bin/python
import os
from user import User
from work_process import WorkProcess
from pid import Pid
from error_log import ErrorLog
from worker_rlimit_nofile import WorkerRlimitNofile
from events import Events
class Conf():
    __path = ""
    __isvalid = False
    user = User()
    work_process = WorkProcess()
    pid = Pid()
    error_log = ErrorLog()
    worker_rlimit_nofile = WorkerRlimitNofile()
    events = Events() 
    http = None

    def __init__(self, path = "./nginx.conf"):
        self.__path = path
        self.__isvalid = self.__valid_path()
        return 

    def __valid_path(self):
        dirname = os.path.dirname(self.getPath())
        return os.path.exists(dirname)

    def getPath(self):
        return self.__path;
    
    def isValid(self):
        return self.__isvalid
    
    def reNew(self, path):
        self.__init__(path)
        return 
    
    def setUpFromFile(self):
        return 

    def writeToFile(self):
        if self.isValid():
            f = open(self.getPath(),"w")
            f.write(str(self.user))
            f.write(str(self.work_process))
            f.write(str(self.pid))
            f.write(str(self.error_log))
            f.write(str(self.worker_rlimit_nofile))
            f.write(str(self.events))
            f.close()
        else:
            pass
        return

if __name__ == "__main__":
    a = Conf()
    a.writeToFile() 
