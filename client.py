import socket
import threading
import sys
import os

def listen():
    print("Thread-1")
    while True:
        incoming = c.recv(1024)
        print ("\n"+"Friend: "+incoming.decode("utf-8")+"\n"+"Say: ")

def send():
    print("Thread-2")
    while True:
        message = input("Say: ")
        if(message == 'quit()'):
            os.exit()
        
        c.send(message.encode())
        


s = socket.socket()
host = socket.gethostname()
port = 6666
global c

s.bind((host,port))

s.listen(5)


c, addr = s.accept()
print ("Connection made")
first = threading.Thread(target=listen)
second = threading.Thread(target=send)
first.start()
second.start()
    
    







    
