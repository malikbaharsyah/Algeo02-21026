import numpy as np
import os
import getFolder
import function
import time

def getEigenFace(path):
    global mean_face
    global subtracted_face
    global start_time_training
    global end_time_training
    start_time_training = time.time()
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
    end_time_training = time.time()
    return eigenfaces

def detectHasil(eigenfaces, datapath, testpath):
    global start_time_detection
    global end_time_detection
    start_time_detection = time.time()
    testface = getFolder.getImageFromPath(testpath)
    testface = np.transpose(testface)
    testface = function.selisih(testface, mean_face)
    proyeksi_test = np.matmul(np.transpose(eigenfaces), testface)
    proyeksi_data = np.matmul(np.transpose(eigenfaces), subtracted_face)
    min = function.EuclideanDistance(proyeksi_test - proyeksi_data[:,0])
    nama = os.listdir(datapath)[0]
    persentase = np.sum(proyeksi_test)/np.sum(proyeksi_data[:,0]) * 100
    for i in range(1, len(os.listdir(datapath))):
        temp = function.EuclideanDistance(proyeksi_test - proyeksi_data[:,i])
        if temp < min:
            min = temp
            nama = os.listdir(datapath)[i]
            persentase = np.sum(proyeksi_test)/np.sum(proyeksi_data[:,i]) * 100
    end_time_detection = time.time()
    return nama, persentase

def getElapsedTimeTraining():
    return end_time_training - start_time_training

def getElapsedTimeDetection():
    return end_time_detection - start_time_detection
