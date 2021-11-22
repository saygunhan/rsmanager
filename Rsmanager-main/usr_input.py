import os
import pwd
import replace as r
import time


def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]
username = get_username()


def replacematik(path1,path2,ip,port):
    if (username=="root"):
        os.popen('cp /usr/bin/rsmanager/payloads/{}/{} /{}/Desktop/{}'.format(path1,path2,username,path2))
        path= "/{}/Desktop/{}".format(username,path2)
        i=2
        while True:
            time.sleep(1)
            print("Completed in ",i," seconds")
            i=i-1
            if i==0:
                break
            
        r.replace(path,ip,port)
    else:
        os.popen('cp /tmp/file1.txt /home/{}/Desktop/file1.txt'.format(username))
        path= "/home/{}/Desktop/{}".format(username,path2)
        i=2
        while True:
            time.sleep(1)
            print("Completed in ",i," seconds")
            i=i-1
            if i==0:
                break
        r.replace(path,ip,port)
