import socket
import threading
import sys

def listen():
    while True:
        incoming = s.recv(1024)
        print ("\n"+"Friend: "+incoming.decode("utf-8")+"\n"+"Say: ")

def send():
    while True:
        message = input("Say: ")
        if(message == 'quit()'):
            os.exit()
        s.send(message.encode())

s = socket.socket()
host = input("IP to connect to: ")
port = 6666

s.connect((host,port))


first = threading.Thread(target=listen)
second = threading.Thread(target=send)
first.start()
second.start()






    
    

    
    
    
    
    
    
    
    
    
    
