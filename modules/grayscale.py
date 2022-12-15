import cv2

def gray_scale(input_img):
    img_bgr = cv2.imread('input_img/' + input_img)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("images/gs/" + input_img ,img_gray)
