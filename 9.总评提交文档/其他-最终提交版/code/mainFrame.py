#!/usr/bin/python
# -*- coding: UTF-8 -*-
from conf.conf import *
from Tkinter import *
from tkFileDialog import *
from status.getStatus import *
from multiprocessing import cpu_count
import os
import platform


class MainFrame:
    __root = Tk(":0")
    __conf = Conf()
    # 私有变量，保存各个属性的值
    __user = StringVar()
    __group = StringVar()
    __workerProcess = StringVar()
    __pidPath = StringVar()
    __logPath = StringVar()
    __logType = StringVar()
    __eventType = StringVar()
    __workerConnection = StringVar()

    # server
    __listen = StringVar()
    __server_name = StringVar()
    __index = StringVar()
    __rootFolder = StringVar()

    # 当前打开配置文件路径
    __conf_path = ''
    
    __logTypes = None

    # 系统用户组数组
    __users = None
    __groups = None

    # 获取系统支持的事件类型
    __eventTypes = None

    def get_conf(self):
        return self.__conf

    def open(self):
        self.__conf_path = askopenfilename()
        if self.__conf_path != '':
            conf = Conf(self.__conf_path)
            conf.setUpFromFile()
            self.__conf = conf
            self.__user.set(conf.getUser().getUser())
            self.__group.set(conf.getUser().getGroup())
            self.__workerProcess.set(conf.getWorkProcess().getProcess())
            self.__pidPath.set(conf.getPid().getPath())
            self.__logPath.set(conf.getErrorLog().getPath())
            self.__logType.set(conf.getErrorLog().getInfo())
            self.__eventType.set(conf.getEvents().getUse())
            self.__workerConnection.set(conf.getEvents().getWorkerConnections())
            self.__eventTypes = conf.getEvents().getUseSet()

    def save(self):
        if self.__conf_path == '':
            self.__conf_path = asksaveasfilename()
            if self.__conf_path == '':
                return

        conf = self.__conf
        conf.getUser().setUser(self.__user.get())
        conf.getUser().setGroup(self.__group.get())
        conf.getWorkProcess().setProcess(int(self.__workerProcess.get()))
        conf.getPid().setPath(self.__pidPath.get())
        conf.getErrorLog().setPath(self.__logPath.get())

        event = Events()
        event.setUse(self.__eventType.get())
        event.setWorkerConnections(int(self.__workerConnection.get()))
        conf.setEvents(event)

        conf.writeToFile()

    def test(self):
        print self.get_conf()

    def choose_pid_path(self):
        file_path = askdirectory()
        if file_path != '':
            self.__pidPath.set(file_path)

    def choose_log_path(self):
        file_path = askdirectory()
        if file_path != '':
            self.__logPath.set(file_path)

    def choose_root_path(self):
        file_path = askdirectory()
        if file_path != '':
            self.__rootFolder.set(file_path)

    def start(self):
        os.system('sudo /usr/local/nginx/sbin/nginx')

    def stop(self):
        os.system('sudo /usr/local/nginx/sbin/nginx -s start')

    def restart(self):
        os.system('sudo /usr/local/nginx/sbin/nginx -s reload')

    def suggest_process(self):
        self.__workerProcess.set(cpu_count())
        
    def suggest_event(self):
        sysstr = platform.system()
        print sysstr
        if(sysstr =="Windows"):
            self.__eventType.set("select")
        elif(sysstr == "Linux"):
            self.__eventType.set("epoll")
        else:
            self.__eventType.set("select")
        
        
    def __init__(self):
        # 通过工具类获取值
        self.__user.set("")
        self.__group.set("")
        self.__workerProcess.set("")
        self.__pidPath.set("")
        self.__logPath.set("")
        self.__eventType.set("")
        self.__workerConnection.set("")

        self.__listen.set("")
        self.__server_name.set("")
        self.__index.set("")
        self.__rootFolder.set("")

        # 需要通过工具获取
        self.__users = ['www', 'nobody']
        self.__groups = ['www', 'nogroup']
        self.__eventTypes = self.get_conf().getEvents().getUseSet()
        self.__logTypes = self.get_conf().getErrorLog().getInfoSet()

        # 图形界面
        self.__root.title("Nginx配置工具")
        self.__root.geometry("400x600")
        self.__root.resizable(width=True, height=True)

        menubar = Menu(self.__root)
        menubar.add_command(label="打开", command=self.open)
        menubar.add_command(label="保存", command=self.save)
        menubar.add_command(label="test", command=self.test)
        self.__root.config(menu=menubar)

        # 用户组
        user_group_label = Label(self.__root, text="用户组")
        user_group_label.grid(row=1, column=1)
        user_drop_list = OptionMenu(self.__root, self.__user, *self.__users)
        user_drop_list.grid(row=1, column=2)
        group_drop_list = OptionMenu(self.__root, self.__group, *self.__groups)
        group_drop_list.grid(row=1, column=3)

        worker_process_label = Label(self.__root, text="进程数")
        worker_process_label.grid(row=2, column=1)
        worker_process_spinbox = Spinbox(self.__root, from_=1, to=16, textvariable=self.__workerProcess)
        worker_process_spinbox.grid(row=2, column=2)
        worker_process_btn = Button(self.__root, text="建议值", command=self.suggest_process)
        worker_process_btn.grid(row=2, column=3)

        pid_path_label = Label(self.__root, text="PID存放路径")
        pid_path_label.grid(row=3, column=1)
        pid_path_show_label = Label(self.__root, textvariable=self.__pidPath)
        pid_path_show_label.grid(row=3, column=2)
        pid_path_button = Button(self.__root, text="更改", command=self.choose_pid_path)
        pid_path_button.grid(row=3, column=3)

        log_path_label = Label(self.__root, text="日志路径")
        log_path_label.grid(row=4, column=1)
        log_path_show_label = Label(self.__root, textvariable=self.__logPath)
        log_path_show_label.grid(row=4, column=2)
        log_path_button = Button(self.__root, text="更改", command=self.choose_log_path)
        log_path_button.grid(row=4, column=3)

        log_type_label = Label(self.__root, text="日志级别")
        log_type_label.grid(row=5, column=1)
        log_type_drop_list = OptionMenu(self.__root, self.__logType, *self.__logTypes)
        log_type_drop_list.grid(row=5, column=2)

        event_type_label = Label(self.__root, text="事件类型")
        event_type_label.grid(row=6, column=1)
        event_type_drop_list = OptionMenu(self.__root, self.__eventType, *self.__eventTypes)
        event_type_drop_list.grid(row=6, column=2)
        event_btn = Button(self.__root, text="建议值", command=self.suggest_event)
        event_btn.grid(row=6, column=3)

        worker_connection_label = Label(self.__root, text="最大连接数")
        worker_connection_label.grid(row=7, column=1)
        worker_connection_spinbox = Spinbox(self.__root, from_=1, to=65536, textvariable=self.__workerConnection)
        worker_connection_spinbox.grid(row=7, column=2)

        status = getstatus('192.168.103.201')

        status_label = Label(self.__root, text="系统状态：")
        status_label.grid(row=8, column=1)
        status_label2 = Label(self.__root, textvariable=status[7])
        status_label2.grid(row=8, column=2)

        start_button = Button(self.__root, text="开始", command=self.start)
        start_button.grid(row=9, column=1)
        stop_button = Button(self.__root, text="停止", command=self.stop)
        stop_button.grid(row=9, column=2)
        restart_button = Button(self.__root, text="重启", command=self.restart)
        restart_button.grid(row=9, column=3)

        active_connection_label1 = Label(self.__root, text="active connection")
        active_connection_label1.grid(row=10, column=1)
        active_connection_label2 = Label(self.__root, text=status[0])
        active_connection_label2.grid(row=10, column=2)

        accepts_label1 = Label(self.__root, text="accepts")
        accepts_label1.grid(row=11, column=1)
        accepts_label2 = Label(self.__root, text=status[1])
        accepts_label2.grid(row=11, column=2)

        handled_label1 = Label(self.__root, text="handled")
        handled_label1.grid(row=12, column=1)
        handled_label2 = Label(self.__root, text=status[2])
        handled_label2.grid(row=12, column=2)

        request_label1 = Label(self.__root, text="request")
        request_label1.grid(row=13, column=1)
        request_label2 = Label(self.__root, text=status[3])
        request_label2.grid(row=13, column=2)

        reading_label1 = Label(self.__root, text="reading")
        reading_label1.grid(row=14, column=1)
        reading_label2 = Label(self.__root, text=status[4])
        reading_label2.grid(row=14, column=2)

        writing_label1 = Label(self.__root, text="writing")
        writing_label1.grid(row=15, column=1)
        writing_label2 = Label(self.__root, text=status[5])
        writing_label2.grid(row=15, column=2)

        waiting_label1 = Label(self.__root, text="waiting")
        waiting_label1.grid(row=16, column=1)
        waiting_label2 = Label(self.__root, text=status[6])
        waiting_label2.grid(row=16, column=2)

        server_label = Label(self.__root, text="虚拟主机设置")
        server_label.grid(row=17, column=2)

        port_label = Label(self.__root, text="监听端口")
        port_label.grid(row=18, column=1)
        port_label_drop_list = Spinbox(self.__root, from_=1, to=65536, textvariable=self.__listen)
        port_label_drop_list.grid(row=18, column=2)

        name_label = Label(self.__root, text="名称")
        name_label.grid(row=19, column=1)
        name_entry = Entry(self.__root, textvariable=self.__server_name)
        name_entry.grid(row=19, column=2)

        index_label = Label(self.__root, text="主页")
        index_label.grid(row=20, column=1)
        index_entry = Entry(self.__root, textvariable=self.__index)
        index_entry.grid(row=20, column=2)

        root_path_label = Label(self.__root, text="根目录")
        root_path_label.grid(row=21, column=1)
        root_path_show_abel = Label(self.__root, textvariable=self.__rootFolder)
        root_path_show_abel.grid(row=21, column=2)
        root_path_button = Button(self.__root, text="更改", command=self.choose_root_path)
        root_path_button.grid(row=21, column=3)

    def show(self):
        self.__root.mainloop()
