import tkinter as tk

from interface.decrypt import DecryptFrame
from interface.encrypt import EncryptFrame
from interface.shell import Shell

class Window(tk.Tk):
    def __init__(self):
        
        super().__init__()

        self.title("AES")

        self.bg_color = '#3D3B40'
        self.front_color = '#525CEB'

        self.configure(bg=self.bg_color)

        self.initial_msg = '00112233445566778899aabbccddeeff'
        self.encryption_key = '000102030405060708090a0b0c0d0e0f'

        self.generate_container()

    def generate_container(self):

        tk.Label(self, text=f'AES algotihm', fg=self.front_color, bg=self.bg_color, font=("Arial", 30)).grid(row=0, column=0, sticky='ew')

        self.container = tk.Frame(self, bg=self.bg_color)
        self.container.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        ## Decrypt
        self.decrypt_frame = DecryptFrame(root=self.container, front_color=self.front_color, bg_color=self.bg_color)
        self.decrypt_frame.grid(row=1, column=0, sticky='nsew', pady=5)

        ## Encrypt
        self.crypt_frame = EncryptFrame(
            root=self.container,
            initial_msg=self.initial_msg, 
            encryption_key=self.encryption_key, 
            front_color=self.front_color, 
            bg_color=self.bg_color, 
            decrypt_frame=self.decrypt_frame
            )
        self.crypt_frame.grid(row=0, column=0, sticky='nsew')

        ## Shell
        self.shell = Shell(self.container)
        self.shell.grid(row=2, column=0, sticky='nsew')
