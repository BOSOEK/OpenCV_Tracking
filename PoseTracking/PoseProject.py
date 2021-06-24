import cv2
import mediapipe as mp
import time
import PoseModule as pm

cap = cv2.VideoCapture('./Videos/TheRack.mp4')
pTime = 0
detector = pm.poseDetector()  # 동작 감지기
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)  # 프레임 구하기
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)  # 프레임 좌측 상단에 출력

    cv2.imshow('Image', img)
    cv2.waitKey(1)