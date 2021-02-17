import numpy as np
import cv2
import pytesseract as r


# 미지로부터 텍스트를 추출하는 함수는 pytesseract.image_to_string() 이다.

r.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

print(r.pytesseract.image_to_string(r'C:\Users\calla\OneDrive\사진\이미지 3.png', lang='kor+eng' , config='--psm 1 -c preserve_interword_spaces=1'))
