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

#memasukan lambda ke matrix
def subsLamda(matrix): 
    var = symbols('λ')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == j):
                matrix[i][j] = (var - matrix[i][j])
            else:
                matrix[i][j] = -matrix[i][j]
    return matrix

def eigenValues(matrix):     
    return solve(Matrix(subsLamda(matrix)).det())

#memasukan nilai lambda ke matrix
def setLamda(matrix, x):    
    var = symbols('λ')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == j):
                matrix[i][j] = (var - matrix[i][j]).subs(var, x)
            else:
                matrix[i][j] = -matrix[i][j]
    return matrix

def eigenVectors(matrix): 
    eig = solve(Matrix(subsLamda(matrix)).det())
    result = []
    for i in range(0, len(eig)):
        setLamda(matrix, eig[i])
        temp = Matrix(matrix)
    result.append(temp.nullspace())
    return result