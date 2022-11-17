import cv2
import numpy as np
import os
import getFolder
import function
import qr2

path = "E:/Kulyah/Semester 3/Aljabar Linier dan Geometri/Tubes/Algeo02-21026/src/dataset"

facematrix = getFolder.folderToMatriks(path)
facematrix_t = np.transpose(facematrix)


print("facematrix_t")
print(facematrix_t)
mean_face = function.mean(facematrix_t)

print("mean")
print(mean_face)
print(mean_face.shape)
temp = np.reshape(mean_face, (256, 256))
cv2.imwrite("test_mean.jpg", temp)

subtracted_face = function.selisih(facematrix_t, mean_face)

print("subtracted_face")
print(subtracted_face)
print(subtracted_face.shape)

print("kovarian")
cov = function.kovarian(np.transpose(subtracted_face))
print(cov)
print(cov.shape)

print("reduced eigen")
evals = qr2.find_eig_qr(cov)[0]
egvecs = qr2.find_eig_qr(cov)[1]
idx = evals.argsort()[::-1]   
evals = evals[idx]
evects = egvecs[:,idx]
print("evals")
print(evals)
print("eigvects")
print(egvecs)
print(egvecs.shape)

eigenfaces = np.matmul(subtracted_face, evects[:,0:25])


print("eigenfaces")

print(eigenfaces)
print(eigenfaces.shape)



testface = getFolder.getImageFromPath(("E:/Kulyah/Semester 3/Aljabar Linier dan Geometri/Tubes/Algeo02-21026/test/5.jpg"))
testface = np.transpose(testface)
print(testface.shape)

print("selisih baru")
testface = function.selisih(testface, mean_face)
print(testface)
print(testface.shape)


print("tes")
tes = np.matmul(np.transpose(eigenfaces), testface)
all_proj = np.matmul(np.transpose(eigenfaces), subtracted_face)
print(tes)
print(tes.shape)

print("all proj")
print(all_proj)
print(all_proj.shape)

distances = np.square(all_proj - tes).sum(axis = 0)
distance = int(distances.argsort()[::-1][:,0])
print("distance", distance)
closest_idx = int(distances.argsort()[::-1][:,0])
closest_path = os.listdir(path)[closest_idx]

# print nama file gambar yang mirip dengan testface
print(closest_path)


#for i in range(eigenfaces.shape[1]):
#    eigenface = eigenfaces[:,i].reshape((256, 256))
#    cv2.imwrite(str(i+1) +"_hasiltemp_cv2.jpg", eigenface)