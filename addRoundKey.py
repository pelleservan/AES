import numpy as np

def AddRoundKey(state=np.empty((1, 1), dtype='U4'), key=np.empty((1, 1), dtype='U4')):

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            key_baud = bin(int(key[i][j], 16)).replace('0b', '').zfill(8)
            key_baud = key_baud.zfill(8)

            state_baud = bin(int(state[i][j], 16)).replace('0b', '')
            state_baud = state_baud.zfill(8)

            out_baud = ''

            for bit_i in range(len(state_baud)):
                out_baud += str((int(state_baud[bit_i])+int(key_baud[bit_i]))%2)

            state[i][j] = '0X' + hex(int(out_baud, 2))[2:].zfill(2).upper()

    return state

