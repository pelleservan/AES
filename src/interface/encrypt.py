import tkinter as tk

from interface.decrypt import DecryptFrame
from cypher.cypher import cypher
from config import mix

class EncryptFrame(tk.Frame):
    def __init__(self, root=None, initial_msg='', encryption_key='', front_color='#FFFFFF', bg_color='#FFFFFF', decrypt_frame=DecryptFrame()):
        super().__init__(root)

        self.front_color = front_color
        self.bg_color = bg_color

        self.configure(bg=self.front_color)
        
        self.initial_msg = initial_msg
        self.encryption_key = encryption_key
        self.cypher_output = []

        self.decrypt_frame = decrypt_frame

        self.generate_frame()


    def generate_frame(self):

        tk.Label(self, text=f'Encrypt a message :', bg=self.front_color, font=("Arial", 20)).grid(row=0, column=0, sticky='w')

        tk.Label(self, text=f'Initial message : ', bg=self.front_color, font=("Arial", 15)).grid(row=1, column=0, sticky='w')

        self.initial_msg_entry = tk.Entry(self, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.initial_msg_entry.insert(0, self.initial_msg)
        self.initial_msg_entry.grid(row=1, column=1, sticky='ew')

        tk.Label(self, text='Encryption key : ', bg=self.front_color, font=("Arial", 15)).grid(row=2, column=0, sticky='w')

        self.encryption_key_entry = tk.Entry(self, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.encryption_key_entry.insert(0, self.encryption_key)
        self.encryption_key_entry.grid(row=2, column=1, sticky='ew')

        tk.Button(self, text=f'Crypt message', command=lambda:self.run_cypher(), bg=self.front_color, highlightbackground=self.front_color).grid(row=1, column=2, rowspan=2, sticky='nsew')

        self.crypted_msg_label = tk.Label(self, text='Encrypted message : ', bg=self.front_color, font=("Arial", 15))
        self.crypted_msg_label.grid(row=3, column=0, columnspan=3, sticky='w')

    def run_cypher(self):

        self.initial_msg = self.initial_msg_entry.get()
        self.encryption_key = self.encryption_key_entry.get()

        if len(self.initial_msg) == 32 and len(self.encryption_key) == 32:

            self.cypher_output = cypher(nb_round=10, initial_msg=self.initial_msg, chifrement_key=self.encryption_key, mix=mix)

            self.crypted_msg_label["text"] = f'Encrypted message : {self.cypher_output[0]}'

            self.decrypt_frame.encrypted_msg_entry.delete(0, "end")
            self.decrypt_frame.encrypted_msg_entry.insert(0, self.cypher_output[0])

            self.keys_array = self.cypher_output[1]
            self.decrypt_frame.cypher_output = self.cypher_output
            self.decrypt_frame.keys_array = self.keys_array