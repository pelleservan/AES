import numpy as np

def shift_rows(state=np.empty((1, 1), dtype='U4')):

    shifted_state = np.empty(state.shape, dtype='U4')

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            shifted_state[i][j%state.shape[0]-i] = state[i][j]

    return shifted_state

def inverse_shift_rows(state=np.empty((1, 1), dtype='U4')):

    shifted_state = np.empty(state.shape, dtype='U4')

    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            shifted_state[i][j] = state[i][j-i]

    return shifted_state