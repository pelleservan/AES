import numpy as np

def galois_multiply(a, b):
    a_int = int(a, 16)  
    b_int = int(b, 16)  
    result = 0          
    while b_int:
        if b_int & 1:
            result ^= a_int
        a_int <<= 1
        if a_int & 0x100:
            a_int ^= 0x11B
        b_int >>= 1
    return hex(result)

def mix_column(state=np.empty((1, 1), dtype='U4'), mix=np.empty((1, 1), dtype='U4')):

    result = np.empty_like(mix, dtype='U4')
    for i in range(4):
        for j in range(4):
            temp = 0
            for k in range(4):
                temp ^= int(galois_multiply(mix[i][k], state[k][j]), 16)
            result[i][j] = '0X{:02X}'.format(temp)

    return result