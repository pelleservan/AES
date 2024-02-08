import numpy as np

def matrix_to_str(state=np.empty((1, 1), dtype='U4'), rpl=''):

    print_state = ''

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            print_state += str(state[j][i])

    print_state = print_state.replace(rpl, '')

    return print_state