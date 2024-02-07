import math as m
import numpy as np

def str_to_matrix(str=''):
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

def print_state(state=np.empty((1, 1), dtype='U4'), rpl=''):

    print_state = ''

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            print_state += str(state[j][i])

    print_state = print_state.replace(rpl, '')

    return print_state