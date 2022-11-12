import cv2
import numpy as np
import os
import faceAlignment

def folderToMatriks(path):
    matriks = np.matrix(faceAlignment.faceAlignment(cv2.imread(os.path.join(path, os.listdir(path)[0]), 0)).ravel())
    i = 0
    n = len(os.listdir(path))
    for file in os.listdir(path):
        grayscaled_img = cv2.imread(os.path.join(path, file), 0)
        aligned = faceAlignment.faceAlignment(grayscaled_img)
        flatten_img = aligned.ravel()
        facevector = np.matrix(flatten_img)
        matriks = np.r_[matriks, facevector]
        print("Proses mendapatkan gambar menjadi matriks %d/%d" % (i,n), end='\r')
        i += 1
    np.delete(matriks, 0)
    return matriks
