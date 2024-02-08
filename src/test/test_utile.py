import unittest
import numpy as np
import os
import sys

chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, chemin_parent)

from utile.str_to_matrix import str_to_matrix 
from utile.matrix_to_str import matrix_to_str

str_msg = '00102030405060708090A0B0C0D0E0F0'

matrix_msg = np.array([
    ['00', '40', '80', 'C0'],
    ['10', '50', '90', 'D0'],
    ['20', '60', 'A0', 'E0'],
    ['30', '70', 'B0', 'F0']
], dtype='U4')

class TestUtile(unittest.TestCase):

    def test_str_to_matrix(self):
        """str_to_matrix function test."""
        result = str_to_matrix(str=str_msg)
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.assertEqual(result[i, j], matrix_msg[i][j])

    def test_matrix_to_str(self):
        """matrix_to_str fucntion test."""
        result = matrix_to_str(state=matrix_msg)
        self.assertEqual(result, str_msg)

if __name__ =='__main__':
    unittest.main()
