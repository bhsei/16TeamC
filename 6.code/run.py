# -*- coding: UTF-8 -*-

from Tkinter import *
from tkFileDialog import *

root = Tk()

root.title("Nginx配置工具")
root.geometry("249x200")
root.resizable(width=True, height= True)

filePath = StringVar()
fileObject = StringVar()
userGroup = StringVar()
workerProcess = StringVar()
pidPath = StringVar()
logPath = StringVar()
maxConn = StringVar()
rootPath = StringVar()
errorPage = StringVar()

def open():
    filePath = askopenfilename()
    if filePath == '' :
        print "file not open"
    else :
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
    
menubar = Menu(root)
menubar.add_cascade(label="open", command=open)
menubar.add_cascade(label="save", command=save)
menubar.add_cascade(label="about", command=about)
menubar.add_cascade(label="test", command=test)
root.config(menu=menubar)

userGroupLabel = Label(root, text = "用户组")
userGroupLabel.grid(row=1, column=1)
userGroupEntry = Entry(root, textvariable = userGroup)
userGroupEntry.grid(row=1, column=2)

workerProcessLabel = Label(root, text = "workerProcess")
workerProcessLabel.grid(row=2, column=1)
workerProcessEntry = Entry(root, textvariable = workerProcess)
workerProcessEntry.grid(row=2, column=2)

pidPathLabel = Label(root, text = "pidPath")
pidPathLabel.grid(row=3, column=1)
pidPathEntry = Entry(root, textvariable = pidPath)
pidPathEntry.grid(row=3, column=2)

rootPathLabel = Label(root, text = "rootPath")
rootPathLabel.grid(row=4, column=1)
rootPathEntry = Entry(root, textvariable = rootPath)
rootPathEntry.grid(row=4, column=2)

logPathLabel = Label(root, text = "logPath")
logPathLabel.grid(row=5, column=1)
logPathEntry = Entry(root, textvariable = logPath)
logPathEntry.grid(row=5, column=2)

maxConnLabel = Label(root, text = "maxConn")
maxConnLabel.grid(row=6, column=1)
maxConnEntry = Entry(root, textvariable = maxConn)
maxConnEntry.grid(row=6, column=2)

errorPageLabel = Label(root, text = "errorPage")
errorPageLabel.grid(row=7, column=1)
errorPageEntry = Entry(root, textvariable = errorPage)
errorPageEntry.grid(row=7, column=2)

root.mainloop()