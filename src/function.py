import numpy as np
import sympy as sp
from sympy import *

# cari nilai tengah dari banyak matrix
def mean(matrix):       
    return np.mean(matrix, axis=0).astype(int)

# selisih tiap matrix dengan mean
def selisih(matrix, mean):          
    return np.abs(np.int_(np.subtract(matrix, mean)))

# menggabungkan matrix selisih
def concat(matrix):
    result = []
    for i in range(len(matrix)):
        if (i == 0):
            result = matrix[i]
        else:
            result = np.concatenate((result, matrix[i]), axis=1)
    return result

# mencari covarian matrix yaitu A.A^T
def kovarian(matrix):      
    return np.dot(matrix, np.transpose(matrix))