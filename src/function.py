import numpy as np

# cari nilai tengah dari banyak matrix
def mean(matrix):       
    return np.mean(matrix, axis=1).astype(int)

# selisih tiap matrix dengan mean
def selisih(matrix, mean):          
    return np.subtract(matrix, mean)

# mencari covarian matrix yaitu A.A^T
def kovarian(matrix):      
    #result = []
    #for i in range(0, len(matrix),1):
    #    result.append(np.dot(np.transpose(matrix[i]), matrix[i]))
    #return np.array(result)
    return np.matmul(np.transpose(matrix), matrix)

def QRDecomposition(matrix):
    n, m = matrix.shape 
    matrixQ = np.empty((n, n)) 
    matrixU = np.empty((n, n)) 
    matrixU[:, 0] = matrix[:, 0]      
    matrixQ[:, 0] = matrixU[:, 0] / np.linalg.norm(matrixU[:, 0]) 
    for i in range(1, n):       
        matrixU[:, i] = matrix[:, i]  
        for j in range(i):    
            matrixU[:, i] -= (matrix[:, i] @ matrixQ[:, j]) * matrixQ[:, j]
        matrixQ[:, i] = matrixU[:, i] / np.linalg.norm(matrixU[:, i])
    matrixR = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):   
            matrixR[i, j] = matrix[:, j] @ matrixQ[:, i]    
    return matrixQ, matrixR 

def eigVec(matrix):
    eigVector = np.eye(matrix.shape[0])
    X = np.copy(matrix)
    for i in range(1):
        matrixQ, matrixR = QRDecomposition(X)
        eigVector = eigVector @ matrixQ
        X = matrixR @ matrixQ
    return np.array(eigVector)

def eigVecList(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(eigVec(matrix[i]))
    return np.array(result)

def eigFace(selisih, eigVector):
    result = []
    for i in range(len(selisih)):
        result.append(np.dot(eigVector[i], selisih[i]))
    return np.array(result)