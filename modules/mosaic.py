import numpy as np
import cv2
import os

def pixelate(src, ratio):#モザイク処理
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def pixelate_area(src, x, y, width, height, ratio=1.1):#指定領域でモザイク処理
    dst = src.copy()
    dst[y:y + height, x:x + width] = pixelate(dst[y:y + height, x:x + width], ratio)
    return dst

def proccess(filename: str):

    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    
    filepath = "/Users/k21094kk/src/github/2022AIT-OOP2-G08/issue_11/modules/face.jpg"
    print("カレントパス", os.getcwd())
    print("filepath が指す絶対パス", os.path.abspath(filepath))
    print("ファイルが存在するかどうか", os.path.isfile(filepath))
    
    src_img : cv2.Mat = cv2.imread(filename)
    
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_img)

    for x,y,w,h in faces:
        dst_face = pixelate_area(src_img, x, y, w, h)
        #dst_img = cv2.rectangle(src_img, (x,y),(x+w,y+h),(255,0,0),2)


    if len(faces) > 0:
        cv2.imwrite('mosaic_face.jpg', dst_face)
    else:
        cv2.imwrite('mosaic_face.jpg')
    

if __name__=='__main__':
    input_file = 'face.jpg'
    proccess(input_file)

