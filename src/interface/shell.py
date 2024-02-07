import tkinter as tk
import sys

class Shell(tk.Frame):
    def __init__(self):
        super().__init__()

        self.terminal = tk.Text(self, wrap="word")
        self.terminal.pack(expand=True, fill="both")
        
        sys.stdout = self
        
        # print("Bonjour le monde !")
        # print("Ceci est un test de terminal dans Tkinter.")
        
    def write(self, message):
        self.terminal.insert(tk.END, message)
        self.terminal.see(tk.END) 
