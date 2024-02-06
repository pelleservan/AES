import math as m
import numpy as np

import utile as U
import subBytes as B
import shiftRows as S
import mixColumns as M
import addRoundKey as A
import keyExtension as K
from config import *

def Cypher(nb_round=0, initial_msg='', chifrement_key='', mix=np.empty((1, 1), dtype='U4')):

    initial_msg = initial_msg.upper()
    chifrement_key = chifrement_key.upper()

    print('CYPHER (ENCRYPT) :')

    state = U.StrToMatrix(initial_msg)
    print(f'round[{0}].inout\t\t{U.PrintState(state=state, rpl='0X')}')

    matrix_key = U.StrToMatrix(chifrement_key)
    print(f'round[{0}].k_sch\t\t{U.PrintState(state=matrix_key, rpl='0X')}')

    keys = [matrix_key.copy()]

    for i in range(nb_round-1):

        state = A.AddRoundKey(state=state, key=matrix_key)
        print(f'round[{i+1}].start\t\t{U.PrintState(state=state, rpl='0X')}')
        
        state = B.SubBytes(state=state)
        print(f'round[{i+1}].s_box\t\t{U.PrintState(state=state, rpl='0X')}')

        state = S.ShiftRows(state=state)
        print(f'round[{i+1}].s_row\t\t{U.PrintState(state=state, rpl='0X')}')

        state = M.MixColumn(state=state, mix=mix)
        print(f'round[{i+1}].m_col\t\t{U.PrintState(state=state, rpl='0X')}')

        matrix_key = K.KeyExtension(key=matrix_key, round=i)
        keys.append(matrix_key)
        print(f'round[{i+1}].k_sch\t\t{U.PrintState(state=matrix_key, rpl='')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{i+2}].start\t\t{U.PrintState(state=state, rpl='0X')}')

    state = B.SubBytes(state=state)
    print(f'round[{i+2}].s_box\t\t{U.PrintState(state=state, rpl='0X')}')

    state = S.ShiftRows(state=state)
    print(f'round[{i+2}].s_row\t\t{U.PrintState(state=state, rpl='0X')}')

    matrix_key = K.KeyExtension(key=matrix_key, round=i+1)
    keys.append(matrix_key)
    print(f'round[{i+2}].k_sch\t\t{U.PrintState(state=matrix_key, rpl='')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{i+2}].output\t{U.PrintState(state=state, rpl='0X')}')

    state = U.PrintState(state=state, rpl='0X')
    matrix_key = U.PrintState(state=matrix_key, rpl='')

    return state, keys

def InverseCypher(nb_round=0, crypted_msg='', keys=[], imix=np.empty((1, 1), dtype='U4')):

    print('INVERSE CYPHER (DECRYPT) :')

    state = U.StrToMatrix(crypted_msg)
    print(f'round[{0}].iinout\t\t\t{U.PrintState(state=state, rpl='0X')}')

    matrix_key = keys[-1].copy()
    print(f'round[{0}].ik_sch\t\t\t{U.PrintState(state=matrix_key, rpl='0X')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{1}].istart\t\t\t{U.PrintState(state=state, rpl='0X')}')

    for i in range(nb_round-1):

        state = S.InverseShiftRows(state=state)
        print(f'round[{i+1}].is_row\t\t\t{U.PrintState(state=state, rpl='0X')}')

        state = B.InverseSubBytes(state=state)
        print(f'round[{i+1}].is_box\t\t\t{U.PrintState(state=state, rpl='0X')}')
        
        matrix_key = keys[-i-2].copy()
        print(f'round[{i+1}].ik_sch\t\t\t{U.PrintState(state=matrix_key, rpl='')}')

        state = A.AddRoundKey(state=state, key=matrix_key)
        print(f'round[{i+1}].ik_add\t\t\t{U.PrintState(state=state, rpl='0X')}')

        state = M.MixColumn(state=state, mix=imix)
        print(f'round[{i+2}].istart \t\t{U.PrintState(state=state, rpl='0X')}')

    state = S.InverseShiftRows(state=state)
    print(f'round[{i+2}].is_row\t\t{U.PrintState(state=state, rpl='0X')}')

    state = B.InverseSubBytes(state=state)
    print(f'round[{i+2}].is_box\t\t{U.PrintState(state=state, rpl='0X')}')

    matrix_key = keys[0].copy()
    print(f'round[{10}].ik_sch\t\t{U.PrintState(state=matrix_key, rpl='0X')}')

    state = A.AddRoundKey(state=state, key=matrix_key)
    print(f'round[{10}].output\t\t{U.PrintState(state=state, rpl='0X')}')

    state = U.PrintState(state=state, rpl='0X')

    return state

if __name__ == '__main__':

    initial_msg =    '00112233445566778899aabbccddeeff'
    chifrement_key = '000102030405060708090a0b0c0d0e0f'

    output = Cypher(nb_round=10, initial_msg=initial_msg, chifrement_key=chifrement_key, mix=mix)

    print(output)

    print('\n\n')

    InverseCypher(nb_round=10, crypted_msg=output[0], keys=output[1], imix=imix)