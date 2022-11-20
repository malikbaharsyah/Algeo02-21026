import numpy as np
import os
import getFolder
import function

def getEigenFace(path):
    global mean_face
    global subtracted_face
    facematrix = getFolder.folderToMatriks(path)
    facematrix_t = np.transpose(facematrix)
    mean_face = function.mean(facematrix_t)
    subtracted_face = function.selisih(facematrix_t, mean_face)
    cov = function.kovarian(subtracted_face)
    evals = function.eigValVec(cov)[0]
    egvecs = function.eigValVec(cov)[1]
    idx = evals.argsort()[::-1]   
    evals = evals[idx]
    evects = egvecs[:,idx]
    nData = len(os.listdir(path))
    eigenfaces = np.matmul(subtracted_face, evects[:,0:nData-1])
    return eigenfaces

def detectHasil(eigenfaces, datapath, testpath):
    testface = getFolder.getImageFromPath(testpath)
    testface = np.transpose(testface)
    testface = function.selisih(testface, mean_face)
    proyeksi_test = np.matmul(np.transpose(eigenfaces), testface)
    proyeksi_data = np.matmul(np.transpose(eigenfaces), subtracted_face)
    min = function.EuclideanDistance(proyeksi_test - proyeksi_data[:,0])
    nama = os.listdir(datapath)[0]
    persentase = np.mean(proyeksi_test / proyeksi_data[:,0])
    for i in range(1, len(os.listdir(datapath))):
        temp = function.EuclideanDistance(proyeksi_test - proyeksi_data[:,i])
        if temp < min:
            min = temp
            nama = os.listdir(datapath)[i]
            persentase = np.mean(proyeksi_test / proyeksi_data[:,i])
    return nama, persentase
