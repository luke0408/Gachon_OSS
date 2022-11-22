import cv2

src = cv2.imread("./img/862227512_8de1721dea_o.jpg")

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 트랙바 함수 정의
def on_trackbar():
    # 트랙바 초기값 정보 받아오기
    rmin = cv2.getTrackbarPos('minRad ius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    # 받아온 정보를 cv2.HoughCircles에 입력
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=120, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()  # 복사한 입력영상 위에 원 그리기
    if circles is not None:
        for i in circles[0, :]:  # 검출된 원 갯수만큼 반복
            cv2.circle(dst, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 저장된 데이터를 이용해 원 그리기

    cv2.imshow('img', dst)


# 트랙바 생성
cv2.imshow('img', src)


# 트랙바 범위
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 200, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 300, on_trackbar)

# 트랙바 초깃값
cv2.setTrackbarPos('minRadius', 'img', 10)  # 초기값 10
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)


cv2.waitKey()