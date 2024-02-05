import math as m
import numpy as np

import subBytes as B
import shiftRows as S
import mixColumns as M
import addRoundKey as A
import keyExtension as K
from config import *

initial_msg =    '00112233445566778899aabbccddeeff'
chifrement_key = '000102030405060708090a0b0c0d0e0f'

initial_msg = initial_msg.upper()
chifrement_key = chifrement_key.upper()

def StrToMatrix(str=''):
    split_str = []

    for i in range(0, len(str)-1, 2):
        pair = str[i:i+2] 
        split_str.append(pair)
        
    matrix_size  = int(m.sqrt(len(str)/2))

    state = np.empty((matrix_size, matrix_size), dtype='U4')

    cpt = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            state[j][i] = split_str[cpt]
            cpt += 1

    return state

def PrintState(state=np.empty((1, 1), dtype='U4'), rpl=''):

    print_state = ''

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            print_state += str(state[j][i])

    print_state = print_state.replace(rpl, '')

    return print_state

def Cypher(nb_round=0, initial_msg='', chifrement_key='', mix=np.empty((1, 1), dtype='U4')):

    print('CYPHER (ENCRYPT) :')

    state = StrToMatrix(initial_msg)
    print(f'round[{0}].inout\t\t{PrintState(state=state, rpl='0X')}')

    matrix_key = StrToMatrix(chifrement_key)
    print(f'round[{0}].k_sch\t\t{PrintState(state=matrix_key, rpl='0X')}')

    keys = []

    for i in range(nb_round-1):

        state = A.AddRoundKey(state=state, key=matrix_key)
        print(f'round[{i+1}].start\t\t{PrintState(state=state, rpl='0X')}')
        
        state = B.SubBytes(state=state)
        print(f'round[{i+1}].s_box\t\t{PrintState(state=state, rpl='0X')}')

        state = S.ShiftRows(state=state)
        print(f'round[{i+1}].s_row\t\t{PrintState(state=state, rpl='0X')}')

        state = M.MixColumn(state=state, mix=mix)
        print(f'round[{i+1}].m_col\t\t{PrintState(state=state, rpl='0X')}')

        matrix_key = K.KeyExtension(key=matrix_key, round=i)
        keys.append(matrix_key)
        print(f'round[{i+1}].k_sch\t\t{PrintState(state=matrix_key, rpl='')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{i+2}].start\t\t{PrintState(state=state, rpl='0X')}')

    state = B.SubBytes(state=state)
    print(f'round[{i+2}].s_box\t\t{PrintState(state=state, rpl='0X')}')

    state = S.ShiftRows(state=state)
    print(f'round[{i+2}].s_row\t\t{PrintState(state=state, rpl='0X')}')

    matrix_key = K.KeyExtension(key=matrix_key, round=i+1)
    keys.append(matrix_key)
    print(f'round[{i+2}].k_sch\t\t{PrintState(state=matrix_key, rpl='')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{i+2}].output\t{PrintState(state=state, rpl='0X')}')

    state = PrintState(state=state, rpl='0X')
    matrix_key = PrintState(state=matrix_key, rpl='')

    return state, keys

def InverseCypher(nb_round=0, crypted_msg='', keys=[], imix=np.empty((1, 1), dtype='U4')):

    print('INVERSE CYPHER (DECRYPT) :')

    state = StrToMatrix(crypted_msg)
    print(f'round[{0}].iinout\t\t{PrintState(state=state, rpl='0X')}')

    matrix_key = keys[-1]
    print(f'round[{0}].ik_sch\t\t{PrintState(state=matrix_key, rpl='0X')}')

    for i in range(nb_round-1):

        matrix_key = keys[-i-2]

        state = A.AddRoundKey(state=state, key=matrix_key)
        print(f'round[{i+1}].istart\t\t{PrintState(state=state, rpl='0X')}')

        state = S.InverseShiftRows(state=state)
        print(f'round[{i+1}].is_row\t\t{PrintState(state=state, rpl='0X')}')

        state = B.InverseSubBytes(state=state)
        print(f'round[{i+1}].is_box\t\t{PrintState(state=state, rpl='0X')}')

        # matrix_key = K.KeyExtension(key=matrix_key, round=i)
        print(f'round[{i+1}].ik_sch\t\t{PrintState(state=matrix_key, rpl='')}')

        # state = A.AddRoundKey(state=state, key=matrix_key)
        # print(f'round[{i+1}].ik_add\t\t{PrintState(state=state, rpl='0X')}')

        state = M.MixColumn(state=state, mix=imix)
        print(f'round[{i+1}].im_col\t\t{PrintState(state=state, rpl='0X')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{i+2}].istart\t{PrintState(state=state, rpl='0X')}')

    state = B.SubBytes(state=state)
    print(f'round[{i+2}].is_box\t{PrintState(state=state, rpl='0X')}')

    state = S.ShiftRows(state=state)
    print(f'round[{i+2}].is_row\t{PrintState(state=state, rpl='0X')}')

    matrix_key = K.KeyExtension(key=matrix_key, round=i+1)
    print(f'round[{i+2}].ik_sch\t{PrintState(state=matrix_key, rpl='')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{i+2}].ioutput\t{PrintState(state=state, rpl='0X')}')

    return state, matrix_key

if __name__ == '__main__':
    output = Cypher(nb_round=10, initial_msg=initial_msg, chifrement_key=chifrement_key, mix=mix)

    print('\n\n')

    InverseCypher(nb_round=10, crypted_msg=output[0], keys=output[1], imix=imix)