import numpy as np

from operations.utile import str_to_matrix, print_state
from operations.shift_rows import shift_rows, inverse_shift_rows
from operations.mix_columns import mix_column
from cypher.add_round_key import add_round_key
from cypher.sub_bytes import sub_bytes, inverse_sub_bytes
from cypher.key_extension import key_extension


def cypher(nb_round=0, initial_msg='', chifrement_key='', mix=np.empty((1, 1), dtype='U4')):

    initial_msg = initial_msg.upper()
    chifrement_key = chifrement_key.upper()

    print('CYPHER (ENCRYPT) :')

    state = str_to_matrix(initial_msg)
    print(f'round[{0}].inout\t\t{print_state(state=state, rpl='0X')}')

    matrix_key = str_to_matrix(chifrement_key)
    print(f'round[{0}].k_sch\t\t{print_state(state=matrix_key, rpl='0X')}')

    keys = [matrix_key.copy()]

    for i in range(nb_round-1):

        state = add_round_key(state=state, key=matrix_key)
        print(f'round[{i+1}].start\t\t{print_state(state=state, rpl='0X')}')
        
        state = sub_bytes(state=state)
        print(f'round[{i+1}].s_box\t\t{print_state(state=state, rpl='0X')}')

        state = shift_rows(state=state)
        print(f'round[{i+1}].s_row\t\t{print_state(state=state, rpl='0X')}')

        state = mix_column(state=state, mix=mix)
        print(f'round[{i+1}].m_col\t\t{print_state(state=state, rpl='0X')}')

        matrix_key = key_extension(key=matrix_key, round=i)
        keys.append(matrix_key)
        print(f'round[{i+1}].k_sch\t\t{print_state(state=matrix_key, rpl='')}')

    state = add_round_key(state=state, key=matrix_key)
    print(f'round[{i+2}].start\t\t{print_state(state=state, rpl='0X')}')

    state = sub_bytes(state=state)
    print(f'round[{i+2}].s_box\t\t{print_state(state=state, rpl='0X')}')

    state = shift_rows(state=state)
    print(f'round[{i+2}].s_row\t\t{print_state(state=state, rpl='0X')}')

    matrix_key = key_extension(key=matrix_key, round=i+1)
    keys.append(matrix_key)
    print(f'round[{i+2}].k_sch\t\t{print_state(state=matrix_key, rpl='')}')

    state = add_round_key(state=state, key=matrix_key)
    print(f'round[{i+2}].output\t{print_state(state=state, rpl='0X')}')

    state = print_state(state=state, rpl='0X')
    matrix_key = print_state(state=matrix_key, rpl='')

    return state, keys

def inverse_cypher(nb_round=0, crypted_msg='', keys=[], imix=np.empty((1, 1), dtype='U4')):

    print('INVERSE CYPHER (DECRYPT) :')

    state = str_to_matrix(crypted_msg)
    print(f'round[{0}].iinout\t\t\t{print_state(state=state, rpl='0X')}')

    matrix_key = keys[-1].copy()
    print(f'round[{0}].ik_sch\t\t\t{print_state(state=matrix_key, rpl='0X')}')

    state = add_round_key(state=state, key=matrix_key)
    print(f'round[{1}].istart\t\t\t{print_state(state=state, rpl='0X')}')

    for i in range(nb_round-1):

        state = inverse_shift_rows(state=state)
        print(f'round[{i+1}].is_row\t\t\t{print_state(state=state, rpl='0X')}')

        state = inverse_sub_bytes(state=state)
        print(f'round[{i+1}].is_box\t\t\t{print_state(state=state, rpl='0X')}')
        
        matrix_key = keys[-i-2].copy()
        print(f'round[{i+1}].ik_sch\t\t\t{print_state(state=matrix_key, rpl='')}')

        state = add_round_key(state=state, key=matrix_key)
        print(f'round[{i+1}].ik_add\t\t\t{print_state(state=state, rpl='0X')}')

        state = mix_column(state=state, mix=imix)
        print(f'round[{i+2}].istart \t\t{print_state(state=state, rpl='0X')}')

    state = inverse_shift_rows(state=state)
    print(f'round[{i+2}].is_row\t\t{print_state(state=state, rpl='0X')}')

    state = inverse_sub_bytes(state=state)
    print(f'round[{i+2}].is_box\t\t{print_state(state=state, rpl='0X')}')

    matrix_key = keys[0].copy()
    print(f'round[{10}].ik_sch\t\t{print_state(state=matrix_key, rpl='0X')}')

    state = add_round_key(state=state, key=matrix_key)
    print(f'round[{10}].output\t\t{print_state(state=state, rpl='0X')}')

    state = print_state(state=state, rpl='0X')

    return state
