import unittest
import numpy as np
import os
import sys

chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, chemin_parent)

from config import mix, imix

from cypher.shift_rows import shift_rows, inverse_shift_rows
from cypher.mix_columns import mix_column
from cypher.add_round_key import add_round_key
from cypher.sub_bytes import sub_bytes, inverse_sub_bytes
from cypher.key_extension import key_extension
from cypher.cypher import cypher, inverse_cypher

sub_bytes_input = np.array([
    ['0X00', '0X40', '0X80', '0XC0'],
    ['0X10', '0X50', '0X90', '0XD0'],
    ['0X20', '0X60', '0XA0', '0XE0'],
    ['0X30', '0X70', '0XB0', '0XF0']
], dtype='U4')

sub_bytes_output = np.array([
    ['0X63', '0X09', '0XCD', '0XBA'],
    ['0XCA', '0X53', '0X60', '0X70'],
    ['0XB7', '0XD0', '0XE0', '0XE1'],
    ['0X04', '0X51', '0XE7', '0X8C']
], dtype='U4')

shift_rows_input = sub_bytes_output.copy()

shift_rows_output = np.array([
    ['0X63', '0X09', '0XCD', '0XBA'],
    ['0X53', '0X60', '0X70', '0XCA'],
    ['0XE0', '0XE1', '0XB7', '0XD0'],
    ['0X8C', '0X04', '0X51', '0XE7']
], dtype='U4')

mix_column_input = shift_rows_output.copy()

mix_column_output = np.array([
    ['0X5F','0X57','0XF7','0X1D'],
    ['0X72','0XF5','0XBE','0XB9'],
    ['0X64','0XBC','0X3B','0XF9'],
    ['0X15','0X92','0X29','0X1A']
], dtype='U4')

key = np.array([
    ['D6', 'D2', 'DA', 'D6'],
    ['AA', 'AF', 'A6', 'AB'],
    ['74', '72', '78', '76'],
    ['FD', 'FA', 'F1', 'FE']
], dtype='U2')

add_round_key_input = mix_column_output.copy()

add_round_key_output = np.array([
    ['0X89','0X85','0X2D','0XCB'],
    ['0XD8','0X5A','0X18','0X12'],
    ['0X10','0XCE','0X43','0X8F'],
    ['0XE8','0X68','0XD8','0XE4']
], dtype='U4')

inverse_mix_column_input = mix_column_output.copy()

inverse_mix_column_output = np.array([
    ['0X63', '0X09', '0XCD', '0XBA'],
    ['0X53', '0X60', '0X70', '0XCA'],
    ['0XE0', '0XE1', '0XB7', '0XD0'],
    ['0X8C', '0X04', '0X51', '0XE7']
], dtype='U4')

inverse_shift_rows_input = inverse_mix_column_output.copy()

inverse_shift_rows_output = np.array([
    ['0X63', '0X09', '0XCD', '0XBA'],
    ['0XCA', '0X53', '0X60', '0X70'],
    ['0XB7', '0XD0', '0XE0', '0XE1'],
    ['0X04', '0X51', '0XE7', '0X8C']
], dtype='U4')

inverse_sub_bytes_input = inverse_shift_rows_output.copy()

inverse_sub_bytes_output = np.array([
    ['0X00', '0X40', '0X80', '0XC0'],
    ['0X10', '0X50', '0X90', '0XD0'],
    ['0X20', '0X60', '0XA0', '0XE0'],
    ['0X30', '0X70', '0XB0', '0XF0']
], dtype='U4')

initial_msg =    '00112233445566778899aabbccddeeff'
chifrement_key = '000102030405060708090a0b0c0d0e0f'
crypted_msg = '69c4e0d86a7b0430d8cdb78070b4c55a'

key_extension_input = np.array([
    ['00', '04', '08', '0C'],
    ['01', '05', '09', '0D'],
    ['02', '06', '0A', '0E'],
    ['03', '07', '0B', '0F']
], dtype='U4')

key_extension_output = np.array([
    ['D6', 'D2', 'DA', 'D6'],
    ['AA', 'AF', 'A6', 'AB'],
    ['74', '72', '78', '76'],
    ['FD', 'FA', 'F1', 'FE']
], dtype='U4')

cypher_output = (
    '69C4E0D86A7B0430D8CDB78070B4C55A', 
    [   
        np.array([['00', '04', '08', '0C'],
                ['01', '05', '09', '0D'],
                ['02', '06', '0A', '0E'],
                ['03', '07', '0B', '0F']], dtype='<U4'),
        np.array([['D6', 'D2', 'DA', 'D6'],
                ['AA', 'AF', 'A6', 'AB'],
                ['74', '72', '78', '76'],
                ['FD', 'FA', 'F1', 'FE']], dtype='<U4'), 
        np.array([['B6', '64', 'BE', '68'],
                ['92', '3D', '9B', '30'],
                ['CF', 'BD', 'C5', 'B3'],
                ['0B', 'F1', '00', 'FE']], dtype='<U4'), 
        np.array([['B6', 'D2', '6C', '04'],
                ['FF', 'C2', '59', '69'],
                ['74', 'C9', '0C', 'BF'],
                ['4E', 'BF', 'BF', '41']], dtype='<U4'), 
        np.array([['47', '95', 'F9', 'FD'],
                ['F7', '35', '6C', '05'],
                ['F7', '3E', '32', '8D'],
                ['BC', '03', 'BC', 'FD']], dtype='<U4'), 
        np.array([['3C', 'A9', '50', 'AD'],
                ['AA', '9F', 'F3', 'F6'],
                ['A3', '9D', 'AF', '22'],
                ['E8', 'EB', '57', 'AA']], dtype='<U4'),
        np.array([['5E', 'F7', 'A7', '0A'],
                ['39', 'A6', '55', 'A3'],
                ['0F', '92', '3D', '1F'],
                ['7D', '96', 'C1', '6B']], dtype='<U4'), 
        np.array([['14', 'E3', '44', '4E'],
                ['F9', '5F', '0A', 'A9'],
                ['70', 'E2', 'DF', 'C0'],
                ['1A', '8C', '4D', '26']], dtype='<U4'), 
        np.array([['47', 'A4', 'E0', 'AE'],
                ['43', '1C', '16', 'BF'],
                ['87', '65', 'BA', '7A'],
                ['35', 'B9', 'F4', 'D2']], dtype='<U4'), 
        np.array([['54', 'F0', '10', 'BE'],
                ['99', '85', '93', '2C'],
                ['32', '57', 'ED', '97'],
                ['D1', '68', '9C', '4E']], dtype='<U4'), 
        np.array([['13', 'E3', 'F3', '4D'],
                ['11', '94', '07', '2B'],
                ['1D', '4A', 'A7', '30'],
                ['7F', '17', '8B', 'C5']], dtype='<U4')
    ]
)

class TestCypher(unittest.TestCase):

    def test_sub_bytes(self):
        """sub_bytes function test."""
        result = sub_bytes(state=sub_bytes_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], sub_bytes_output[i][j])

    def test_shift_rows(self):
        """shift_rows function test."""
        result = shift_rows(state=shift_rows_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], shift_rows_output[i][j])

    def test_mix_column(self):
        """mix_column function test."""
        result = mix_column(state=mix_column_input, mix=mix)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], mix_column_output[i][j])
                
    def test_key_extension(self):
        """key_extension function test."""
        result = key_extension(key=key_extension_input, round=0)
        print(result)
        print(key_extension_output)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], key_extension_output[i][j])

    def test_add_round_key(self):
        """add_roundKey function test."""
        result = add_round_key(state=add_round_key_input, key=key)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], add_round_key_output[i][j])

    def test_inverse_mix_column(self):
        """inverse_mix_column function test."""
        result = mix_column(state=inverse_mix_column_input, mix=imix)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i,j], inverse_mix_column_output[i][j])

    def test_inverse_shift_rows(self):
        """inverse_shift_rows function test."""
        result = inverse_shift_rows(state=inverse_shift_rows_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i,j], inverse_shift_rows_output[i][j])

    def test_inverse_sub_bytes(self):
        """inverse_sub_bytes function test."""
        result = inverse_sub_bytes(state=inverse_sub_bytes_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i,j], inverse_sub_bytes_output[i][j])

    def test_cypher(self):
        """cypher function test."""
        result = cypher(nb_round=10, initial_msg=initial_msg, chifrement_key=chifrement_key, mix=mix)[0].lower()
        self.assertEqual(result, crypted_msg)

    def test_inverse_cypher(self):
        """inverse_cypher function test."""
        result = inverse_cypher(nb_round=10, crypted_msg=cypher_output[0], keys=cypher_output[1], imix=imix).lower()
        self.assertEqual(result, initial_msg)

if __name__ =='__main__':
    unittest.main()
