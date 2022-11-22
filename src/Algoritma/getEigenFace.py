import numpy as np
import os
import getFolder
import function
import time
import cv2
import faceAlignment

def getEigenFace(path):
    global mean_face
    global subtracted_face
    global start_time_training
    global end_time_training
    global evects
    start_time_training = time.time()
    nData = len(os.listdir(path))
    facematrix = getFolder.folderToMatriks(path)
    facematrix_t = np.transpose(facematrix)
    mean_face = function.mean(facematrix_t)
    subtracted_face = function.selisih(facematrix_t, mean_face)
    cov = function.kovarian(subtracted_face)
    cov = cov / nData
    evals = function.eigValVec(cov)[0]
    egvecs = function.eigValVec(cov)[1]
    idx = evals.argsort()[::-1]   
    evals = evals[idx]
    evects = egvecs[:,idx]
    evects = evects[:,0:nData-1]
    evects = np.matmul(subtracted_face, evects)
    norms = np.array([])
    for i in range(0, nData-1):
        norms = np.append(norms, function.EuclideanDistance(evects[:,i]))
    evects = evects / norms
    bobot = np.matmul(np.transpose(evects), subtracted_face)
    end_time_training = time.time()
    return bobot

def detectHasil(bobot, datapath, testpath):
    global start_time_detection
    global end_time_detection
    start_time_detection = time.time()
    testface = getFolder.getImageFromPath(testpath)
    testface = np.transpose(testface)
    testface = function.selisih(testface, mean_face)
    s = np.transpose(evects) * testface
    diff = bobot - s
    norms = np.array([])
    for i in range(0, len(os.listdir(datapath))):
        norms = np.append(norms, function.EuclideanDistance(diff[:,i]))
    min = np.amin(norms)
    max = np.amax(norms)
    idx = np.argmin(norms)
    nama = os.listdir(datapath)[idx]
    end_time_detection = time.time()
    return nama, min/max

def detectCam(bobot, datapath, img):
    testface = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    testface = faceAlignment.faceAlignment(testface)
    testface = testface.ravel()
    testface = np.matrix(testface)
    testface = np.transpose(testface)
    testface = function.selisih(testface, mean_face)
    s = np.transpose(evects) * testface
    diff = bobot - s
    norms = np.array([])
    for i in range(0, len(os.listdir(datapath))):
        norms = np.append(norms, function.EuclideanDistance(diff[:,i]))
    min = np.amin(norms)
    max = np.amax(norms)
    idx = np.argmin(norms)
    nama = os.listdir(datapath)[idx]
    return nama, min/max

def getElapsedTimeTraining():
    return end_time_training - start_time_training

def getElapsedTimeDetection():
    return end_time_detection - start_time_detection


