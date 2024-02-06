import numpy as np
from sympy import GF, Symbol

def galois_multiply(a, b):
    a_int = int(a, 16)  # Convertir en entier
    b_int = int(b, 16)  # Convertir en entier
    result = 0           # Initialisation de la variable result
    while b_int:
        if b_int & 1:
            result ^= a_int
        a_int <<= 1
        if a_int & 0x100:
            a_int ^= 0x11B
        b_int >>= 1
    return hex(result)

def MixColumn(state=np.empty((1, 1), dtype='U4'), mix=np.empty((1, 1), dtype='U4')):

    # for j in range(state.shape[1]):
    #     current_col = state[:, j]
    #     new_col = []
    #     for row in range(len(mix)):
    #         current_dig = []
    #         for i in range(len(current_col)): 
    #             word = current_col[i]
    #             word = bin(int(word[2:], 16)).replace('0b', '').zfill(8)
    #             coef = mix[row][i]
    #             if coef == '01':
    #                 current_dig.append(word)
    #             elif int(coef, 16) > 1:
    #                 word_computed = 0
    #                 if int(coef, 16)%2 == 1:
    #                     current_dig.append(word)
    #                 if word[0] == '1' and len(word) == 8:
    #                     filter = '100011011'
    #                     word += '0'
    #                     out = ''
    #                     for bit in range(len(word)):
    #                         out += str((int(word[bit])+int(filter[bit]))%2)
    #                     word_computed = out[1:]
    #                 elif word[0] == '0' and len(word) == 8:
    #                     word_computed = word[1:] + '0'
    #                 for _ in range(int(coef, 16)//2):
    #                     current_dig.append(word_computed)
    #             elif coef == '01':
    #                 current_dig.append(word)
    #         out_baud = ''
    #         for dig_i in range(len(current_dig[0])):
    #             cpt = 0
    #             for baud_i in range(len(current_dig)):
    #                 cpt += int(current_dig[baud_i][dig_i])
    #             out_baud += str(cpt%2)
    #         new_col.append('0X' + hex(int(out_baud, 2)).upper().replace('0X', '').zfill(2))
    #     state[:, j] = new_col

    result = np.empty_like(mix, dtype='U4')
    for i in range(4):
        for j in range(4):
            temp = 0
            for k in range(4):
                temp ^= int(galois_multiply(mix[i][k], state[k][j]), 16)
            result[i][j] = '0X{:02X}'.format(temp)

    return result