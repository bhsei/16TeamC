#!/user/bin/python
import os
import re

class User():
    __user = ""
    __group = ""
    __re = re.compile(r".*user (\w*) (\w*)",re.DOTALL)
    def __init__(self, user = "nobody", group = "nogroup"):
        self.__user = user
        self.__group = group 
        return

    def __valid(self):
        result = os.popen("grep \"^" + self.getUser() + "\" /etc/passwd").read()
        if len(result) == 0:
            return False
        result = os.popen("grep \"^" + self.getGroup() + "\" /etc/group").read() 
        if len(result) == 0:
            return False
        return True

    def setUp(self,s):
        r = self.__re.match(s)
        if r != None:
            r = r.groups()
            self.setUser(r[0])
            self.setGroup(r[1])
            return True
        return False

    def isValid(self):
        return self.__valid()

    def setGroup(self, group):
        self.__group = group
        return 
    def getGroup(self):
        return self.__group

    def setUser(self, user):
        self.__user = user
        return 
    def getUser(self):
        return self.__user
    
    def __repr__(self):
        return "user %s %s;\n" % (self.getUser(),self.getGroup())
