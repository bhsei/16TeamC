#!/usr/bin/python
import re
class Events():
    __use_set = ["kqueue","rtsig","epoll","/dev/poll","select","poll"]
    __use = "epoll" 
    __worker_connections = 1
    __re = re.compile(r".*events.*\{.*use (\w*).*worker_connections (\d*).*\}",re.DOTALL)
    
    def __init__(self, use = "epoll", worker_connections = 1):
        self.__use = use
        self.__worker_connections = worker_connections
        return

    def __valid(self):
        flag = self.getUse() in __use_set
        flat = flag and self.getWorkerConnections >= 1 
        return flag

    def setUp(self,s):
        r = self.__re.match(s)
        if r != None:
            r = r.groups()
            self.setUse(r[0])
            self.setWorkerConnections(int(r[1]))
            return True
        return False

    def isValid(self):
        return self.__valid()

    def getUse(self):
        return self.__use
    
    def setUse(self, use):
        self.__use = use 
        return 
    
    def getWorkerConnections(self):
        return self.__worker_connections

    def setWorkerConnections(self, worker_connections):
        self.__worker_connections = worker_connections
        return 

    def __repr__(self):
        ret = "events {\n"
        ret += "\tuse %s;\n" %(self.getUse() )
        ret += "\tworker_connections %s;\n" % (self.getWorkerConnections())
        ret += "}\n"
        return ret

     
    
        
