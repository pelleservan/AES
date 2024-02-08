import tkinter as tk
import sys

class Shell(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.terminal = tk.Text(self, wrap="word")
        self.terminal.pack(expand=True, fill="both")
        
        sys.stdout = self
        
    def write(self, message):
        self.terminal.insert(tk.END, message)
        self.terminal.see(tk.END) 
