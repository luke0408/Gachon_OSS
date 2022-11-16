import cv2
import math
import numpy as np

src = cv2.imread("../img/862227512_8de1721dea_o.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient=True)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200,
                          param1=300, param2=80, minRadius=100, maxRadius=300)
circles = np.uint16(np.around(circles))

lines = cv2.HoughLinesP(canny, 0.8, math.pi / 180, 90, 
                        minLineLength = 10, maxLineGap = 100)

for i in circles[0, :]:
  cv2.circle(dst, (i[0],i[1]), i[2], (0,255,0), 2)

for i in lines:
  cv2.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), 
          (0, 0, 255), 2)
  
cv2.imshow("Detected Cicles and Line", dst)
cv2.waitKey(0)
cv2.destoryAllWindows()