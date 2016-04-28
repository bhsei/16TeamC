#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
from tkFileDialog import *
#from conf.conf import Conf

root = Tk(":0")

root.title("Nginx配置工具")
root.geometry("300x200")
root.resizable(width=True, height= True)

filePath = StringVar(root)
fileObject = StringVar(root)
userGroup = StringVar(root)
eventType = StringVar(root)
workerProcess = StringVar(root)
workerConnection = StringVar(root)
pidPath = StringVar(root)
logPath = StringVar(root)
maxConn = StringVar(root)
rootPath = StringVar(root)
errorPage = StringVar(root)

#初始化变量
userGroup.set("nobody")
eventType.set("default")

def open():
    filePath = askopenfilename()
    if filePath == '' :
        print "file not open"
    else :
        conf = Conf()#解析没有实现
        
        # 伪造一些数据，应该在解析类实现
        userGroup.set("www www")
        workerProcess.set("2")
        pidPath.set("./")
        logPath.set("./")
        maxConn.set("65536")
        rootPath.set("./")
        errorPage.set("404.html")

def save():
    print "save"
    
def about():
    print "about"
    
def test():
    print "test code"

def choosePidPath():
    filePath = askdirectory()
    if filePath == '':
        print "path not choose"
    else:
        print filePath

def chooseLogPath():
    filePath = askdirectory()
    if filePath == '':
        print "path not choose"
    else:
        print filePath

menubar = Menu(root)
menubar.add_command(label="open", command=open)
menubar.add_command(label="save", command=save)
menubar.add_command(label="about", command=about)
menubar.add_command(label="test", command=test)
root.config(menu=menubar)

userGroupLabel = Label(root, text = "用户组")
userGroupLabel.grid(row=1, column=1)
userGroupChoice = ['root root', 'www www', 'user user1', 'user user2','nobody'] #获取用户组列表
userGroupList = OptionMenu(root, userGroup, *userGroupChoice)
userGroupList.grid(row=1, column=2)

workerProcessLabel = Label(root, text = "workerProcess")
workerProcessLabel.grid(row=2, column=1)
workerProcessEntry = Spinbox(root, from_ = 1, to = 16, textvariable = workerProcess)
workerProcessEntry.grid(row=2, column=2)

pidPathLabel = Label(root, text = "pidPath")
pidPathLabel.grid(row=3, column=1)
pidPathEntry = Button(root, text="choose path",command = choosePidPath)
pidPathEntry.grid(row=3, column=2)

logPathLabel = Label(root, text = "logPath")
logPathLabel.grid(row=4, column=1)
logPathEntry = Button(root, text="choose path",command = chooseLogPath)
logPathEntry.grid(row=4, column=2)

#网络连接序列化？？？
#接收多个网络连接？？？

eventLabel = Label(root, text = "event type")
eventLabel.grid(row=5, column=1)
eventTypes = ['kqueue', 'epoll', 'select', 'poll', 'default'] #获取用户组列表
userGroupList = OptionMenu(root, eventType, *eventTypes)
userGroupList.grid(row=5, column=2)

workerConnectionLabel = Label(root, text = "workerConnection")
workerConnectionLabel.grid(row=6, column=1)
workerConnectionEntry = Spinbox(root, from_ = 1, to = 65536, textvariable = workerConnection)
workerConnectionEntry.grid(row=6, column=2)



root.mainloop()
