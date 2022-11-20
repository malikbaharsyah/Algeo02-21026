import cv2
import numpy as np
import os
from PIL import Image

def findBiggest(matrix):
    maxArea = 0
    biggest = matrix[0]
    for i in range(len(matrix)):
        area = matrix[i][2] * matrix[i][3]
        if area > maxArea:
            biggest = matrix[i]
            maxArea = area
    return biggest

def jarak(a,b):
    return np.sqrt(((b[0] - a[0]) * (b[0] - a[0])) + ((b[1] - a[1]) * (b[1] - a[1])))

def faceAlignment(img):

    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_frontalface_default.xml")
    eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "/haarcascade_eye.xml")
    face_coordinate = face_detector.detectMultiScale(img)
    eyes = eye_detector.detectMultiScale(img)

    # if (len(eyes) > 1):
    #     if (len(eyes) > 2):
    #         ab = abs(eyes[0][1] - eyes[1][1])
    #         bc = abs(eyes[1][1] - eyes[2][1])
    #         ac = abs(eyes[0][1] - eyes[2][1])
    #         if (ab < bc and ab < ac):
    #             eyes = np.delete(eyes, 2, 0)
    #         elif (bc < ab and bc < ac):
    #             eyes = np.delete(eyes, 0, 0)
    #         else:
    #             eyes = np.delete(eyes, 1, 0)
        
    #     eye_1 = eyes[0]
    #     eye_2 = eyes[1]

    #     if eye_1[0] < eye_2[0]:
    #         lEye = eye_1
    #         rEye = eye_2
    #     else:
    #         lEye = eye_2
    #         rEye = eye_1

    #     rEye_center = (rEye[0] + int(rEye[2] / 2), rEye[1] + int(rEye[3] / 2))
    #     lEye_center = (lEye[0] + int(lEye[2] / 2), lEye[1] + int(lEye[3] / 2))
    #     rEye_x = rEye_center[0]
    #     rEye_y = rEye_center[1]
    #     lEye_x = lEye_center[0]
    #     lEye_y = lEye_center[1]

    #     if lEye_y > rEye_y:
    #         proyeksi = (rEye_x, lEye_y)
    #         dir = -1 #rotate image clockwise
    #     else:
    #         proyeksi = (lEye_x, rEye_y)
    #         dir = 1 #rotate image counterclockwise

    #     a = jarak(lEye_center, proyeksi)
    #     b = jarak(rEye_center, lEye_center)
    #     c = jarak(rEye_center, proyeksi)
    #     cos = (b*b + c*c - a*a)/(2*b*c)
    #     sudut = (np.arccos(cos) *180) / np.pi

    #     if dir == -1:
    #         sudut = 90 - sudut
    #     else:
    #         angle = -(90-sudut)
    #     img = Image.fromarray(img)
    #     img = np.array(img.rotate(dir * sudut))

    # if len(face_coordinate) > 0:
    #     face_x, face_y, face_w, face_h = findBiggest(face_coordinate)
    #     img = img[face_y:face_y + face_h, face_x:face_x + face_w]


    img = cv2.resize(img, (256,256))

    return img
    