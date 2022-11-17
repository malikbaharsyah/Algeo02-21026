import numpy as np

def find_eig_qr(A):
    pQ = np.eye(A.shape[0])
    X = np.copy(A)
    for i in range(100):
            Q,R = np.linalg.qr(X)
            pQ = np.matmul(pQ, Q)
            X = np.matmul(R, Q)
    return np.diag(X), pQ
