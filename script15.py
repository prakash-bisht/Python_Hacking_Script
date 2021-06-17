import string
import random

key = "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0,1024))

print(key)
print("\nThe length of key: ",len(key))

message = "wireshark"
print("\nMessage is: ",message)

def str_xor(s1,s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])


encryption = str_xor(message,key)
print("\nencrypted message is: ",encryption)

decryption = str_xor(encryption,key)
print("\ndecrypted message is: ",decryption)
