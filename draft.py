import numpy as np

# Matrices A et B en hexadécimal
A = np.array([
    ['0X5F','0X57','0XF7','0X1D'],
    ['0X72','0XF5','0XBE','0XB9'],
    ['0X64','0XBC','0X3B','0XF9'],
    ['0X15','0X92','0X29','0X1A']
], dtype='U4')

B = np.array([
    ['0X0E', '0X0B', '0X0D', '0X09'],
    ['0X09', '0X0E', '0X0B', '0X0D'],
    ['0X0D', '0X09', '0X0E', '0X0B'],
    ['0X0B', '0X0D', '0X09', '0X0E']
], dtype='U4')

# Produit de deux matrices dans GF(2^8) avec polynôme irréductible 11B
def galois_multiply(a, b):
    a_int = int(a, 16)  # Convertir en entier
    b_int = int(b, 16)  # Convertir en entier
    result = 0           # Initialisation de la variable result
    while b_int:
        if b_int & 1:
            result ^= a_int
        a_int <<= 1
        if a_int & 0x100:
            a_int ^= 0x11B
        b_int >>= 1
    return hex(result)

# Produit matriciel de A et B
def matrix_multiply(A, B):
    result = np.empty_like(A, dtype='U4')  # Définir le type de données explicitement
    for i in range(4):
        for j in range(4):
            temp = 0
            for k in range(4):
                temp ^= int(galois_multiply(A[i][k], B[k][j]), 16)
            result[i][j] = '0x{:02X}'.format(temp)
    return result

# Afficher le résultat en hexadécimal
result_matrix = matrix_multiply(B, A)
print(result_matrix)
