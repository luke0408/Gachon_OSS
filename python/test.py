import cv2

src = cv2.imread("./img/862227512_8de1721dea_o.jpg")
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient=True)

cv2.imshow("gray", gray)