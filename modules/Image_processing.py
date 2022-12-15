import cv2

face_cascade_path = 'haarcascade_frontalface_default.xml'

def face_cascade(input, output):
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    src = cv2.imread(input)

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)


    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        

        
    cv2.imwrite(output, src)

#debug用コード
if __name__ == "__main__":
    input = 'sample.jpg'
    output = '/Users/k21013/Oop/Oop2/No.11/issue_11/images/face_check/output.jpg'
    face_cascade(input,output)
    #'/Users/k21013/Oop/Oop2/No.11/issue_11/images/face_check/output.jpg'