import numpy as np
import sympy as sp
from sympy import *

# cari nilai tengah dari banyak matrix
def mean(matrix):       
    return np.mean(matrix, axis=0).astype(int)

# selisih tiap matrix dengan mean
def selisih(matrix, mean):          
    return np.int_(np.subtract(matrix, mean))

# hasil selisih yang negatif diubah ke positif
def ubahNegatif(matrix):            
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                if (matrix[i][j][k] < 0):
                    matrix[i][j][k] = matrix[i][j][k] * -1
    return matrix

# menggabungkan matrix selisih
# (masih bermasalah: kalau pakai 
# hasil matriks selisih bermasalah 
# tapi kalau pakai matriks contohSelisih berhasil di konkat)
# contohSelisih = [[[1, 0, 0], [1, 1, 0], [0, 0, 1]], [[0, 1, 0], [0, 0, 0], [1, 0, 1]]]
def concat(matrix):     
    for i in range(len(matrix)-1):
        matrix[0] = np.concatenate((matrix[0], matrix[i+1]), axis=1)
    return matrix[0]

# mencari covarian matrix yaitu A.A^T
def kovarian(matrix):      
    return np.dot(matrix, np.transpose(matrix))