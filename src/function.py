import numpy as np

# cari nilai tengah dari banyak matrix
def mean(matrix):       
    return np.mean(matrix, axis=1).astype(int)

# selisih tiap matrix dengan mean
def selisih(matrix, mean):          
    return np.subtract(matrix, mean)

# mencari covarian matrix yaitu A.A^T
def kovarian(matrix):      
    return np.matmul(np.transpose(matrix), matrix)

# mencari nilai eigen vector dan eigen value dengan metode QR
def QRDecomposition(matrix):
    n, m = matrix.shape 
    matrixQ = np.empty((n, n)) 
    matrixU = np.empty((n, n)) 
    matrixU[:, 0] = matrix[:, 0]      
    matrixQ[:, 0] = matrixU[:, 0] / EuclideanDistance(matrixU[:, 0]) 
    for i in range(1, n):       
        matrixU[:, i] = matrix[:, i]  
        for j in range(i):    
            matrixU[:, i] -= np.matmul(matrix[:, i], matrixQ[:, j]) * matrixQ[:, j]
        matrixQ[:, i] = matrixU[:, i] / EuclideanDistance(matrixU[:, i])
    matrixR = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):   
            matrixR[i, j] = np.matmul(matrix[:, j], matrixQ[:, i]) 
    return matrixQ, matrixR 

def eigValVec(matrix):
    eigVector = np.eye(matrix.shape[0])
    X = np.copy(matrix)
    for i in range(1):
        Q, R = QRDecomposition(X)
        eigVector = np.matmul(eigVector, Q)
        X = np.matmul(R, Q)
    return np.diag(X), eigVector

# mencari euclidean distance
def EuclideanDistance(matrix):
    return np.sqrt(np.sum(np.square(matrix)))

