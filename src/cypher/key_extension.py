import numpy as np
from config import s_box

def rot_word(w=[]):
    
    first_element = w[0]
    
    w_without_first = w[1:]
    
    w_with_first_at_end = np.append(w_without_first, first_element)

    return w_with_first_at_end

def sub_word(w=''):

    for i in range(len(w)):
        coord = [0, 0]
        current = w[i]
        for k in range(2):
            if current[k].isalpha():
                coord[k] = ord(current[k])-55
            else:
                coord[k] = int(current[k])
        w[i] = s_box[coord[0]][coord[1]]

    return w

def round_constant(w=[], round=0):
    r = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']
    R = [f'{r[round]}', '00', '00', '00'] 

    r_bin = []
    for i in  range(len(R)):
        r_bin.append(bin(int(R[i], 16)).replace('0b', '').zfill(8))

    word_bin = []
    for i in range(len(w)):
        word_bin.append(bin(int(w[i], 16)).replace('0b', '').zfill(8))

    w = []
    for i in range(len(word_bin)):
        w.append('')
        for j in range(len(word_bin[i])):
            w[i] += str((int(word_bin[i][j]) + int(r_bin[i][j]))%2)
    
    for i in range(len(w)):
        w[i] = hex(int(w[i], 2))[2:].zfill(2).upper()

    return w

def g_func(w3='', round=0):

    w3 = rot_word(w=w3)

    w3 = sub_word(w=w3)

    w3 = round_constant(w=w3, round=round)

    return w3

def xor(w1=[], w2=[]):

    exit_w = []

    w1_bin = []
    w2_bin = []
    for i in range(len(w1)):
        w1_bin.append(bin(int(w1[i], 16)).replace('0b', '').zfill(8))
        w2_bin.append(bin(int(w2[i], 16)).replace('0b', '').zfill(8))

    exit_w = []
    for i in range(len(w1_bin)):
        exit_w.append('')
        for j in range(len(w1_bin[i])):
            exit_w[i] += str((int(w1_bin[i][j]) + int(w2_bin[i][j])) % 2)

    for i in range(len(exit_w)):
        exit_w[i] = hex(int(exit_w[i], 2)).upper().replace('0X', '').zfill(2)

    return exit_w

def key_extension(key=np.empty((1, 1), dtype='U4'), round=0):

    exit_key = np.empty(key.shape, dtype='U4')

    for j in range(key.shape[1]):

        word = key[:, j]

        if j == 0:

            w = g_func(w3=key[:, -1].copy(), round=round)
        
        else:
            w = exit_key[:, j-1]

        word = xor(w1=word, w2=w)

        exit_key[:, j] = word

    return exit_key
