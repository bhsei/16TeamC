#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
from tkFileDialog import *


class ServerFrame:
    __root = Tk(":0")
    # 私有变量，保存各个属性的值
    __listen = StringVar()
    __server_name = StringVar()
    __index = StringVar()
    __rootFolder = StringVar()

    def choose_root_path(self):
        file_path = askdirectory()
        if file_path != '':
            self.__rootFolder.set(file_path)

    def __init__(self):
        self.__listen.set("")
        self.__server_name.set("")
        self.__index.set("")
        self.__rootFolder.set("")

        # 图形界面
        self.__root.title("server编辑")
        self.__root.geometry("300x200")
        self.__root.resizable(width=True, height=True)

        port_label = Label(self.__root, text="监听端口")
        port_label.grid(row=1, column=1)
        port_label_drop_list = Spinbox(self.__root, from_=1, to=65536, textvariable=self.__listen)
        port_label_drop_list.grid(row=1, column=2)

        name_label = Label(self.__root, text="名称")
        name_label.grid(row=2, column=1)
        name_entry = Entry(self.__root, textvariable=self.__server_name)
        name_entry.grid(row=2, column=2)

        index_label = Label(self.__root, text="index")
        index_label.grid(row=3, column=1)
        index_entry = Entry(self.__root, textvariable=self.__index)
        index_entry.grid(row=3, column=2)

        root_path_label = Label(self.__root, text="根目录")
        root_path_label.grid(row=4, column=1)
        root_path_show_abel = Label(self.__root, textvariable=self.__rootFolder)
        root_path_show_abel.grid(row=4, column=2)
        root_path_button = Button(self.__root, text="更改", command=self.choose_root_path)
        root_path_button.grid(row=4, column=3)

    def show(self):
        self.__root.mainloop()

if __name__ == "__main__":
    frame = ServerFrame()
    frame.show()
