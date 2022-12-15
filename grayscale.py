import sys
import cv2

class grayscale():
    _, infile, outfile = sys.argv
    img_bgr = cv2.imread(infile)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(outfile, img_gray)