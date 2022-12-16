#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 入力画像を読み込み
img = cv2.imread("/Users/k21031kk/Documents/GitHub/issue_11/images/nomal/irasuto.png")

import os

filepath = "/Users/k21031kk/Documents/GitHub/issue_11/images/nomal/irasuto.png"
print("カレントパス", os.getcwd())
print("filepath が指す絶対パス", os.path.abspath(filepath))
print("ファイルが存在するかどうか", os.path.isfile(filepath))

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 方法2(OpenCVで実装)
dst = cv2.Canny(gray, 100, 200)


# 結果を出力
#cv2.imshow(dst)
cv2.imwrite("../images/Canny/output.png", dst)
