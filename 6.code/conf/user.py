#!/user/bin/python
import os

class User():
    __user = ""
    __group = ""
    __isvalid = False

    def __init__(self, user = "nobody", group = "nogroup"):
        self.__user = user
        self.__group = group 
        self.__isvalid =  self.__valid_all()
        return

    def __valid_all(self):
        result = os.popen("grep \"^" + self.getUser() + "\" /etc/passwd").read()
        if len(result) == 0:
            return False
        result = os.popen("grep \"^" + self.getGroup() + "\" /etc/group").read() 
        if len(result) == 0:
            return False
        return True

    def isValid(self):
        return self.__isvalid
    
    def getGroup(self):
        return self.__group

    def getUser(self):
        return self.__user
    
    def reNew(self, user, group):
        self.__init__(user,group)
        return

    def __repr__(self):
        return "user %s %s;\n" % (self.getUser(),self.getGroup())
