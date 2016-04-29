#!/usr/bin/python
# -*- coding: UTF-8 -*-
from conf.conf import *
from Tkinter import *
from tkFileDialog import *


class MainFrame:
    __root = Tk(":0")

    # 私有变量，保存各个属性的值
    __userGroup = StringVar()
    __workerProcess = StringVar()
    __pidPath = StringVar()
    __logPath = StringVar()
    __eventType = StringVar()
    __workerConnection = StringVar()

    # 当前打开配置文件路径
    __confPath = ''

    # 系统用户组数组
    __userGroups = None

    # 获取系统支持的事件类型
    __eventTypes = None

    def open(self):
        self.__confPath = askopenfilename()
        if self.__confPath != '':
            conf = Conf(self.__confPath)
            conf.setUpFromFile()
            self.__userGroup.set(conf.getUser().getUser() + " " + conf.getUser().getGroup())
            self.__workerProcess.set(conf.getWorkProcess().getProcess())
            self.__pidPath.set(conf.getPid().getPath())
            self.__logPath.set(conf.getErrorLog().getPath())
            self.__eventType.set(conf.getEvents().getUse())
            self.__workerConnection.set(conf.getEvents().getWorkerConnections())

    def save(self):
        if self.__confPath == '':
            self.__confPath = asksaveasfilename()
            if self.__confPath == '':
                return

        conf = Conf(self.__confPath)
        conf.setUser(self.__userGroup.get())
        conf.setWorkProcess(self.__workerProcess.get())
        conf.setPid(self.__pidPath.get())
        conf.setErrorLog(self.__logPath.get())

        event = Events()
        event.setUse(self.__eventType.get())
        event.setWorkerConnections(self.__workerConnection.get())
        conf.setEvents(event)

        conf.writeToFile()

    def about(self):
        print "about"

    def test(self):
        print self.__userGroup.get()
        print self.__workerProcess.get()
        print self.__pidPath.get()
        print self.__logPath.get()
        print self.__eventType.get()
        print self.__workerConnection.get()

    def choosePidPath(self):
        filePath = askdirectory()
        if filePath != '':
            self.__pidPath.set(filePath)

    def chooseLogPath(self):
        filePath = askdirectory()
        if filePath != '':
            self.__logPath.set(filePath)

    def __init__(self):
        # 通过工具类获取值
        self.__userGroup.set("")
        self.__workerProcess.set("")
        self.__pidPath.set("")
        self.__logPath.set("")
        self.__eventType.set("")
        self.__workerConnection.set("")

        # 需要通过工具获取
        self.__userGroups = ['root', 'admin']
        self.__eventTypes = ['kqueue', 'epoll', 'select', 'poll', 'default']

        # 图形界面
        self.__root.title("Nginx配置工具")
        self.__root.geometry("300x200")
        self.__root.resizable(width=True, height=True)

        menubar = Menu(self.__root)
        menubar.add_command(label="打开", command=self.open)
        menubar.add_command(label="保存", command=self.save)
        menubar.add_command(label="关于", command=self.about)
        menubar.add_command(label="test", command=self.test)
        self.__root.config(menu=menubar)

        # 用户组
        userGroupLabel = Label(self.__root, text="用户组")
        userGroupLabel.grid(row=1, column=1)
        userGroupDropList = OptionMenu(self.__root, self.__userGroup, *self.__userGroups)
        userGroupDropList.grid(row=1, column=2)

        workerProcessLabel = Label(self.__root, text="进程数")
        workerProcessLabel.grid(row=2, column=1)
        workerProcessSpinbox = Spinbox(self.__root, from_=1, to=16, textvariable=self.__workerProcess)
        workerProcessSpinbox.grid(row=2, column=2)

        pidPathLabel = Label(self.__root, text="PID存放路径")
        pidPathLabel.grid(row=3, column=1)
        pidPathShowLabel = Label(self.__root, textvariable=self.__pidPath)
        pidPathShowLabel.grid(row=3, column=2)
        pidPathButton = Button(self.__root, text="更改", command=self.choosePidPath)
        pidPathButton.grid(row=3, column=3)

        logPathLabel = Label(self.__root, text="日志路径")
        logPathLabel.grid(row=4, column=1)
        logPathShowLabel = Label(self.__root, textvariable=self.__logPath)
        logPathShowLabel.grid(row=4, column=2)
        logPathButton = Button(self.__root, text="更改", command=self.chooseLogPath)
        logPathButton.grid(row=4, column=3)

        eventTypeLabel = Label(self.__root, text="事件类型")
        eventTypeLabel.grid(row=5, column=1)
        eventTypeDropList = OptionMenu(self.__root, self.__eventType, *self.__eventTypes)
        eventTypeDropList.grid(row=5, column=2)

        workerConnectionLabel = Label(self.__root, text="最大连接数")
        workerConnectionLabel.grid(row=6, column=1)
        workerConnectionSpinbox = Spinbox(self.__root, from_=1, to=65536, textvariable=self.__workerConnection)
        workerConnectionSpinbox.grid(row=6, column=2)

    def show(self):
        self.__root.mainloop()
