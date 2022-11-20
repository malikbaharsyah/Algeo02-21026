import cv2
import numpy as np
import os
import getFolder
import function
import qr2

def getEigenFace(path):
    global mean_face
    global subtracted_face
    facematrix = getFolder.folderToMatriks(path)
    facematrix_t = np.transpose(facematrix)
    mean_face = function.mean(facematrix_t)
    subtracted_face = function.selisih(facematrix_t, mean_face)
    cov = function.kovarian(subtracted_face)
    evals = qr2.find_eig_qr(cov)[0]
    egvecs = qr2.find_eig_qr(cov)[1]
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
    list_jarak = np.square(proyeksi_data - proyeksi_test).sum(axis = 0)
    idx_terdekat = int(list_jarak.argsort()[::-1][:,0])
    file_terdekat = os.listdir(datapath)[idx_terdekat]
    return file_terdekat