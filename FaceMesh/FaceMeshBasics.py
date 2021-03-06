import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime=0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh  # 얼굴 망
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)  # 최대 인식 얼굴
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)  # 두께, 원의 반경

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:  # 얼굴 랜드마크가 감지 되면
        for faceLms in results.multi_face_landmarks:   # 여러 얼굴이 있을 수 있으니 for문
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec) # 랜드마크 출력
            for id, lm in enumerate(faceLms.landmark):
                #print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id, x, y)   # 랜드마크 아이디와 좌표 출력하기


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
