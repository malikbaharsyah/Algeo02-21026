import cv2
import numpy as np
import os
import faceAlignment

def folderToMatriks(path):
    matriks = np.matrix(faceAlignment.faceAlignment(cv2.imread(os.path.join(path, os.listdir(path)[0]), cv2.IMREAD_GRAYSCALE)).ravel())
    i = 1
    n = len(os.listdir(path))
    for file in os.listdir(path):
        print("Proses mendapatkan gambar menjadi matriks %d/%d" % (i,n), end='\r')
        grayscaled_img = cv2.imread(os.path.join(path, file), cv2.IMREAD_GRAYSCALE)
        aligned = faceAlignment.faceAlignment(grayscaled_img)
        flatten_img = aligned.ravel()
        facevector = np.matrix(flatten_img)
        matriks = np.r_[matriks, facevector]  
        i += 1
    matriks = np.delete(matriks, 0, axis=0)
    return matriks


def getImageFromPath(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = faceAlignment.faceAlignment(img)
    img = img.ravel()
    img = np.matrix(img)
    return img