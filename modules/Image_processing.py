import cv2
import os

def mosaic(filename: str):

    face_cascade_path = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    
    #filepath = "/Users/k21094kk/src/github/2022AIT-OOP2-G08/issue_11/modules/face.jpg"
    #print("カレントパス", os.getcwd())
    #print("filepath が指す絶対パス", os.path.abspath(filepath))
    #print("ファイルが存在するかどうか", os.path.isfile(filepath))
    
    src_img : cv2.Mat = cv2.imread(filename)

    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_img, minSize=(150,150))

    print(faces)
    x=faces[0][0]
    y=faces[0][1]
    w=faces[0][2]
    h=faces[0][3]
    
    print("顔の座標(x,y,w,h):", x, y, w, h)
    
    #モザイク処理
    face= src_img[y:y+h, x:x+w]
    reduc = cv2.resize(face, (8,8))
    mosaic = cv2.resize(reduc,(w,h))
    src_img[y:y+h, x:x+w]=mosaic

    cv2.imwrite('/issue_11/images/mosaic/output_img.jpg', src_img)
    filepath = "output_img.jpg"
    print("カレントパス", os.getcwd())
    print("filepath が指す絶対パス", os.path.abspath(filepath))
    print("ファイルが存在するかどうか", os.path.isfile(filepath))
if __name__=='__main__':
    input_img = 'face.jpg'
    mosaic(input_img)

