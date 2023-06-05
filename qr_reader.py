# pip install opencv-python

import cv2

d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("QR.jpg"))

print('\n' * 50)
print(val)
