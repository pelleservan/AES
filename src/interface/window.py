import tkinter as tk

from cypher.cypher import cypher, inverse_cypher
from config import mix, imix
from interface.shell import Shell

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AES")

        self.bg_color = '#3D3B40'
        self.front_color = '#525CEB'


        self.configure(bg=self.bg_color)

        self.initial_msg = ''
        self.encryption_key = ''
        self.crypted_msg = tk.StringVar()
        self.crypted_msg.set("Encrypted message : ")
        self.decrypted_msg = tk.StringVar()
        self.decrypted_msg.set("Decrypted message : ")
        self.cypher_output = []
        self.keys_array = []

        self.generate_container()

    def generate_container(self):

        tk.Label(self, text=f'AES algotihm', fg=self.front_color, bg=self.bg_color, font=("Arial", 30)).grid(row=0, column=0, sticky='ew')

        self.container = tk.Frame(self, bg=self.bg_color)
        self.container.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        ### Encrypte
        self.encrypt_container = tk.Frame(self.container, bg=self.front_color)
        self.encrypt_container.grid(row=0, column=0, sticky='nsew')

        tk.Label(self.encrypt_container, text=f'Encrypt a message :', bg=self.front_color, font=("Arial", 20)).grid(row=0, column=0, sticky='w')

        tk.Label(self.encrypt_container, text=f'Initial message : ', bg=self.front_color, font=("Arial", 15)).grid(row=1, column=0, sticky='w')

        self.initial_msg_entry = tk.Entry(self.encrypt_container, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.initial_msg_entry.insert(0, '00112233445566778899aabbccddeeff')
        self.initial_msg_entry.grid(row=1, column=1, sticky='ew')

        tk.Label(self.encrypt_container, text='Encryption key : ', bg=self.front_color, font=("Arial", 15)).grid(row=2, column=0, sticky='w')

        self.encryption_key_entry = tk.Entry(self.encrypt_container, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.encryption_key_entry.insert(2, '000102030405060708090a0b0c0d0e0f')
        self.encryption_key_entry.grid(row=2, column=1, sticky='ew')

        tk.Button(self.encrypt_container, text=f'Crypt message', command=lambda:self.run_cypher(), bg=self.front_color, highlightbackground=self.front_color).grid(row=1, column=2, rowspan=2, sticky='nsew')

        tk.Label(self.encrypt_container, textvariable=self.crypted_msg, bg=self.front_color, font=("Arial", 15)).grid(row=3, column=0, columnspan=3, sticky='w')

        ### Decrypte
        self.decrypt_container = tk.Frame(self.container, bg=self.front_color)
        self.decrypt_container.grid(row=1, column=0, sticky='nsew', pady=10)

        tk.Label(self.decrypt_container, text=f'Decrypt a message :', bg=self.front_color, font=("Arial", 20)).grid(row=0, column=0, sticky='w')

        tk.Label(self.decrypt_container, text=f'Encrypted message : ', bg=self.front_color, font=("Arial", 15)).grid(row=1, column=0, sticky='w')

        self.encrypted_msg_entry = tk.Entry(self.decrypt_container, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.encrypted_msg_entry.grid(row=1, column=1, sticky='ew')

        tk.Label(self.decrypt_container, text='Encryption key : ', bg=self.front_color, font=("Arial", 15)).grid(row=2, column=0, sticky='w')

        self.decryption_key_entry = tk.Entry(self.decrypt_container, width=40, bg=self.bg_color, highlightbackground=self.front_color)
        self.decryption_key_entry.insert(2, '000102030405060708090a0b0c0d0e0f')
        self.decryption_key_entry.grid(row=2, column=1, sticky='ew')

        tk.Button(self.decrypt_container, text=f'Decrypt message', command=lambda:self.run_inverse_cypher(), bg=self.front_color, highlightbackground=self.front_color).grid(row=1, column=2, rowspan=2, sticky='nsew')

        tk.Label(self.decrypt_container, textvariable=self.decrypted_msg, bg=self.front_color, font=("Arial", 15)).grid(row=3, column=0, columnspan=3, sticky='w')

        ## Shell
        self.shell = Shell()
        self.shell.grid(row=2, column=0, sticky='nsew', padx=10)

    def run_cypher(self):
        self.initial_msg = self.initial_msg_entry.get()
        self.encryption_key = self.encryption_key_entry.get()

        if len(self.initial_msg) == 32 and len(self.encryption_key) == 32:
            self.cypher_output = cypher(nb_round=10, initial_msg=self.initial_msg, chifrement_key=self.encryption_key, mix=mix)
            self.crypted_msg.set(f'Encrypted message : {self.cypher_output[0]}')
            self.encrypted_msg_entry.delete(0, "end")
            self.encrypted_msg_entry.insert(0, self.cypher_output[0])
            self.keys_array = self.cypher_output[1]

    def run_inverse_cypher(self):
        self.encrypted_msg = self.encrypted_msg_entry.get()
        self.encryption_key = self.encryption_key_entry.get()

        if len(self.initial_msg) == 32 and len(self.encryption_key) == 32:
            inverse_cypher_output = inverse_cypher(nb_round=10, crypted_msg=self.cypher_output[0], keys=self.keys_array, imix=imix)
            self.decrypted_msg.set(f'Decrypted message : {inverse_cypher_output}')
