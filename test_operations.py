import unittest
import numpy as np
from config import mix, imix
from addRoundKey import AddRoundKey
from mixColumns import MixColumn
from shiftRows import ShiftRows, InverseShiftRows
from subBytes import SubBytes, InverseSubBytes

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

class TestAddRoundKey(unittest.TestCase):

    def test_sub_bytes(self):
        """SubBytes function test."""
        result = SubBytes(state=sub_bytes_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], sub_bytes_output[i][j])

    def test_shift_rows(self):
        """ShiftRows function test."""
        result = ShiftRows(state=shift_rows_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], shift_rows_output[i][j])

    def test_mix_column(self):
        """MixColumn function test."""
        result = MixColumn(state=mix_column_input, mix=mix)
        print(result)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], mix_column_output[i][j])

    def test_add_round_key(self):
        """AddRoundKey function test."""
        result = AddRoundKey(state=add_round_key_input, key=key)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], add_round_key_output[i][j])

    def test_inverse_mix_column(self):
        """InverseMixColumn function test."""
        result = MixColumn(state=inverse_mix_column_input, mix=imix)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i,j], inverse_mix_column_output[i][j])

    def test_inverse_shift_rows(self):
        """InverseShiftRows function test."""
        result = InverseShiftRows(state=inverse_shift_rows_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i,j], inverse_shift_rows_output[i][j])

    def test_inverse_sub_bytes(self):
        """InverseSubBytes function test."""
        result = InverseSubBytes(state=inverse_sub_bytes_input)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i,j], inverse_sub_bytes_output[i][j])

if __name__ =='__main__':
    unittest.main()
