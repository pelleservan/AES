import tkinter as tk

from cypher.cypher import inverse_cypher
from config import imix

class DecryptFrame(tk.Frame):
    def __init__(self, root=None, front_color='#FFFFFF', bg_color='#FFFFFF'):

        super().__init__(root)

        self.front_color = front_color
        self.bg_color = bg_color

        self.configure(bg=self.front_color)

        self.cypher_output = []
        self.keys_array = []

        self.generate_frame()

    def generate_frame(self):

        tk.Label(self, text=f'Decrypt a message :', bg=self.front_color, font=("Arial", 20)).grid(row=0, column=0, sticky='w')

        tk.Label(self, text=f'Encrypted message : ', bg=self.front_color, font=("Arial", 15)).grid(row=1, column=0, sticky='w')

        self.encrypted_msg_entry = tk.Entry(self, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.encrypted_msg_entry.grid(row=1, column=1, sticky='ew')

        tk.Label(self, text='Encryption key : ', bg=self.front_color, font=("Arial", 15)).grid(row=2, column=0, sticky='w')

        self.decryption_key_entry = tk.Entry(self, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.decryption_key_entry.insert(2, '000102030405060708090a0b0c0d0e0f')
        self.decryption_key_entry.grid(row=2, column=1, sticky='ew')

        tk.Button(self, text=f'Decrypt message', command=lambda:self.run_inverse_cypher(), bg=self.front_color, highlightbackground=self.front_color).grid(row=1, column=2, rowspan=2, sticky='nsew')

        self.decrypt_msg_lebel = tk.Label(self, text='Decrypted message : ', bg=self.front_color, font=("Arial", 15))
        self.decrypt_msg_lebel.grid(row=3, column=0, columnspan=3, sticky='w')

    def run_inverse_cypher(self):
        
        self.encrypted_msg = self.encrypted_msg_entry.get()
        self.encryption_key = self.decryption_key_entry.get()

        if len(self.encrypted_msg) == 32 and len(self.encryption_key) == 32:
            inverse_cypher_output = inverse_cypher(nb_round=10, crypted_msg=self.cypher_output[0], keys=self.keys_array, imix=imix)

            self.decrypt_msg_lebel["text"]= f'Decrypted message : {inverse_cypher_output}'