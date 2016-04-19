# -*- coding: UTF-8 -*-

from Tkinter import *

def open():
    print 'open'

def save():
    print 'save'
    
def about():
    print 'about'

root = Tk()
menubar = Menu(root)
menubar.add_cascade(label="open", command=open)
menubar.add_cascade(label="save", command=save)
menubar.add_cascade(label="about", command=about)
root.config(menu=menubar)



root.mainloop()