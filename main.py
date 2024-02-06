from cypher.cypher import cypher, inverse_cypher
from config import mix, imix

if __name__ == '__main__':

    initial_msg =    '00112233445566778899aabbccddeeff'
    chifrement_key = '000102030405060708090a0b0c0d0e0f'

    output = cypher(nb_round=10, initial_msg=initial_msg, chifrement_key=chifrement_key, mix=mix)

    print('\n\n')

    inverse_cypher(nb_round=10, crypted_msg=output[0], keys=output[1], imix=imix)