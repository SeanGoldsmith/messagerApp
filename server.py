import socket

s = socket.socket()
host = '10.0.0.19'
port = 6666

s.connect((host,port))

while True:
    message = input("Send a message: ")
    s.send(message.encode())






    
    

    
    
    
    
    
    
    
    
    
    
