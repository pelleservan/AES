import numpy as np
from config import s_boX, is_boX

def sub_bytes(state=np.empty((1, 1), dtype='U4')) :

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            coord = [0, 0]
            current = state[i][j]
            if '0X' in current:
                current = current[2:]
            for k in range(2):
                if current[k].isalpha():
                    coord[k] = ord(current[k])-55
                else:
                    coord[k] = int(current[k])
            state[i][j] = s_boX[coord[0]][coord[1]]
            
    return state

def inverse_sub_bytes(state=np.empty((1, 1), dtype='U4')) :

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            coord = [0, 0]
            current = state[i][j]
            if '0X' in current:
                current = current[2:]
            for k in range(2):
                if current[k].isalpha():
                    coord[k] = ord(current[k])-55
                else:
                    coord[k] = int(current[k])
            state[i][j] = is_boX[coord[0]][coord[1]]
            
    return state