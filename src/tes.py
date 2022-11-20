import cv2
import numpy as np
import os
import getFolder
import function
import qr2
import getEigenFace

dataset = "E:/Kulyah/Semester 3/Aljabar Linier dan Geometri/Tubes/Algeo02-21026/src/dataset"

eigenfaces = getEigenFace.getEigenFace(dataset)
print(eigenfaces)


print("BERHASIL MELAKUKAN TRAINING")

pathtest = "E:/Kulyah/Semester 3/Aljabar Linier dan Geometri/Tubes/Algeo02-21026/test"



lanjut = True
found = False

while (lanjut):
    inputGambar = str(input("Masukkan nama file gambar untuk test: "))
    while(not found):
        if inputGambar in os.listdir(pathtest):
            found = True
        else:
            inputGambar = str(input("File tidak ditemukan, masukkan nama file gambar: "))

    testpath = os.path.join(pathtest, inputGambar)

    print("Gambar yang terdeteksi adalah: ", getEigenFace.detectHasil(eigenfaces, datapath=dataset, testpath=testpath))

    inputy = str(input("Apakah anda ingin mencoba lagi? (y/n): "))
    valid = False
    while (not valid):
        if inputy == "y":
            valid = True
            found = False
        elif inputy == "n":
            valid = True
            lanjut = False
        else:
            inputy = str(input("Input tidak valid, masukkan kembali: "))

#for i in range(eigenfaces.shape[1]):
#    eigenface = eigenfaces[:,i].reshape((256, 256))
#    cv2.imwrite(str(i+1) +"_hasiltemp_cv2.jpg", eigenface)

# for file in os.listdir(path):
#     print("Proses mengolah folder %d/%d" % (i,nData), end='\r')
#     if i != 1:
#         temp = getFolder.folderToMatriks(os.path.join(path, file))
#         temp = np.transpose(temp)
#         mean_temp = function.mean(temp)
#         mean_temp = mean_temp.ravel()
#         mean_temp = np.matrix(mean_temp)
#         facematrix = np.r_[facematrix, mean_temp]
#     else:
#         facematrix = getFolder.folderToMatriks(os.path.join(path, os.listdir(path)[0]))
#         facematrix = np.transpose(facematrix)
#         mean_temp = function.mean(facematrix)
#         mean_temp = mean_temp.ravel()
#         mean_temp = np.matrix(mean_temp)
#         facematrix = mean_temp
#     i += 1