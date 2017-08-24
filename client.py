import socket
from tkinter import *
from tkinter import ttk
import time

def goAhead(another):
    textbox.insert(END,entry.get()+"\n")
    entry.delete(0,END)

def runConnection(whatever):
    message = c.recv(1024).decode("utf-8")
    print (message)
    textbox.insert(END,message+"\n")
    textbox.update()
    
    

someNumber = 25
message = ''

global s
s = socket.socket()
host = socket.gethostname()
port = 6666

s.bind((host,port))
s.listen()
global c
c, addr = s.accept()

root = Tk()
textbox = Text(root)
textbox.pack()
entry = Entry(root)
entry.pack()


root.bind("<Return>",goAhead)
root.bind("<Button-2>",runConnection)
root.mainloop()

    
