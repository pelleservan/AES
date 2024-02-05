import numpy as np
from config import s_box

def RotWord(w=[]):
    
    first_element = w[0]
    
    w_without_first = w[1:]
    
    w_with_first_at_end = np.append(w_without_first, first_element)

    return w_with_first_at_end

def SubWord(w=''):

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

def RoundConstant(w=[], round=0):
    r = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']
    R = [f'{r[round]}', '00', '00', '00'] 

  # print(R)

    R_bin = []
    for i in  range(len(R)):
        R_bin.append(bin(int(R[i], 16)).replace('0b', '').zfill(8))

    word_bin = []
    for i in range(len(w)):
        word_bin.append(bin(int(w[i], 16)).replace('0b', '').zfill(8))

    w = []
    for i in range(len(word_bin)):
        w.append('')
        for j in range(len(word_bin[i])):
            w[i] += str((int(word_bin[i][j]) + int(R_bin[i][j]))%2)
    
    for i in range(len(w)):
        w[i] = hex(int(w[i], 2))[2:].zfill(2).upper()

    return w

def gFunc(w3='', round=0):

  # print(f'w3 : \t{w3}')

    w3 = RotWord(w=w3)
  # print(f'rot word : \t{w3}')

    w3 = SubWord(w=w3)
  # print(f'sub word : \t{w3}')

    w3 = RoundConstant(w=w3, round=round)
  # print(f'round const : \t{w3}')

    return w3

def XOR(w1=[], w2=[]):

    exit_w = []

    w1_bin = []
    w2_bin = []
    for i in range(len(w1)):
        w1_bin.append(bin(int(w1[i], 16)).replace('0b', '').zfill(8))
        w2_bin.append(bin(int(w2[i], 16)).replace('0b', '').zfill(8))

  # print(w1_bin)
  # print(w2_bin)

    exit_w = []
    for i in range(len(w1_bin)):
        exit_w.append('')
        for j in range(len(w1_bin[i])):
            exit_w[i] += str((int(w1_bin[i][j]) + int(w2_bin[i][j])) % 2)

    for i in range(len(exit_w)):
        exit_w[i] = hex(int(exit_w[i], 2)).upper().replace('0X', '').zfill(2)

    return exit_w

def KeyExtension(key=np.empty((1, 1), dtype='U4'), round=0):

    exit_key = np.empty(key.shape, dtype='U4')

    for j in range(key.shape[1]):

        word = key[:, j]
      # print(f'w{j} : \t{word}')

        if j == 0:

            w = gFunc(w3=key[:, -1].copy(), round=round)
          # print(f'g(w3) : {w}')
        
        else:
            w = exit_key[:, j-1]
          # print(f'w{key.shape[0]-1+j} : \t{w}')

        word = XOR(w1=word, w2=w)
      # print(f'key : \t{word}')

        exit_key[:, j] = word
      # print(f'key : \n{exit_key}')

      # print('\n')

    return exit_key
