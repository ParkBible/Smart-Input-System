import cv2 as cv
import mediapipe as mp
import time
import math
import numpy as np


hsv = 0
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0

# 키(10개)
key1 = []  # 첫째줄
for i in range(10):
    key1.append([0, 0, 0, 0, 0])  # 시작점x좌표, 시작점y좌표, 끝점x좌표, 끝점y좌표, 키값

# 첫째줄 키 범위
for i in range(10):
    key1[i][0] = 20 + i * 60  # 시작점 x
    key1[i][1] = 80 + i * 60  # 시작점 y
    key1[i][2] = 20  # 끝점 x
    key1[i][3] = 80  # 끝점 y
    key1[i][4] = i+1  # 키값(0~9)
    key1[9][4] = 0

key2 = []  # 첫째줄
for i in range(10):
    key2.append([0, 0, 0, 0, 0])  # 시작점x좌표, 시작점y좌표, 끝점x좌표, 끝점y좌표, 키값

# 두째줄 키 범위
for i in range(10):
    key2[i][0] = 20 + i * 60  # 시작점 x
    key2[i][1] = 80 + i * 60  # 시작점 y
    key2[i][2] = 80  # 끝점 x
    key2[i][3] = 140  # 끝점 y
key2[0][4] = "q"
key2[1][4] = "w"
key2[2][4] = "e"
key2[3][4] = "r"
key2[4][4] = "t"
key2[5][4] = "" \
             "y"
key2[6][4] = "u"
key2[7][4] = "i"
key2[8][4] = "o"
key2[9][4] = "p"

key3 = []  # 첫째줄
for i in range(9):
    key3.append([0, 0, 0, 0, 0])  # 시작점x좌표, 시작점y좌표, 끝점x좌표, 끝점y좌표, 키값

# 세째줄 키 범위
for i in range(9):
    key3[i][0] = 50 + i * 60  # 시작점 x
    key3[i][1] = 110 + i * 60  # 시작점 y
    key3[i][2] = 140  # 끝점 x
    key3[i][3] = 200  # 끝점 y
key3[0][4] = "a"
key3[1][4] = "s"
key3[2][4] = "d"
key3[3][4] = "f"
key3[4][4] = "g"
key3[5][4] = "h"
key3[6][4] = "j"
key3[7][4] = "k"
key3[8][4] = "l"

key4 = []  # 첫째줄

for i in range(7):
    key4.append([0, 0, 0, 0, 0])  # 시작점x좌표, 시작점y좌표, 끝점x좌표, 끝점y좌표, 키값

for i in range(7):
    key4[i][0] = 110 + i * 60  # 시작점 x
    key4[i][1] = 170 + i * 60  # 시작점 y
    key4[i][2] = 200  # 끝점 x
    key4[i][3] = 260  # 끝점 y

key4[0][4] = "z"
key4[1][4] = "x"
key4[2][4] = "c"
key4[3][4] = "v"
key4[4][4] = "b"
key4[5][4] = "n"
key4[6][4] = "m"

key5 = []  # 첫째줄
for i in range(5):
    key5.append([0, 0, 0, 0, 0])  # 시작점x좌표, 시작점y좌표, 끝점x좌표, 끝점y좌표, 키값

for i in range(5):
    key5[i][0] = 170 + i * 60  # 시작점 x
    key5[i][1] = 230 + i * 60  # 시작점 y
    key5[i][2] = 260  # 끝점 x
    key5[i][3] = 320  # 끝점 y
key5[0][4] = " "
key5[1][4] = " "
key5[2][4] = " "
key5[3][4] = " "
key5[4][4] = " "

def nothing(x):
    pass


cap = cv.VideoCapture(0)

img1 = np.zeros((200, 500, 3), np.uint8)  # 검은 바탕
count = 0
count_delay = 0
line=0
point = 0


def click(x):
    global count
    global count_delay
    global line
    global img
    global point
    count_delay = count_delay + 1
    if short > 15 and (count_delay % 5) == 0 :
        point = 0
    # count_delay가 20의 배수라면 출력
    if short < 15 and point == 0 :
        cv.putText(img1, str(key1[i][4]), (50 + count * 10, 60 + line*10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,
                   cv.LINE_AA)
        count = count + 1
        point = 1
        cv.rectangle(img, (key1[i][0], key1[i][2]), (key1[i][1], key1[i][3]), (255, 255, 255), -1)
    if (count>=35) :
        line = line + 1
        count = 0
def click1(x):
    global count
    global count_delay
    global line
    global img
    global point
    print(point)
    count_delay = count_delay + 1
    if short > 15 and (count_delay % 5) == 0 :
        point = 0
    # count_delay가 20의 배수라면 출력
    if short < 15 and point == 0 :
        cv.putText(img1, str(key2[j][4]), (50 + count * 10, 60 + line * 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                   1,
                   cv.LINE_AA)
        cv.rectangle(img, (key2[j][0], key2[j][2]), (key2[j][1], key2[j][3]), (255, 255, 255), -1)
        count = count + 1
        point = 1
    if (count >= 35):
        line = line + 1
        count = 0
def click2(x):
    global count
    global count_delay
    global line
    global img
    global point
    count_delay = count_delay + 1
    if short > 15 and (count_delay % 5) == 0 :
        point = 0
    # count_delay가 20의 배수라면 출력
    if short < 15 and point == 0 :
        cv.putText(img1, str(key3[i][4]), (50 + count * 10, 60 + line * 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                   1,
                   cv.LINE_AA)
        cv.rectangle(img, (key3[i][0], key3[i][2]), (key3[i][1], key3[i][3]), (255, 255, 255), -1)
        count = count + 1
        point = 1

    if (count >= 35):
        line = line + 1
        count = 0

def click3(x):
    global count
    global count_delay
    global line
    global img
    global point
    count_delay = count_delay + 1
    # count_delay가 20의 배수라면 출력
    if short > 15 and (count_delay % 5) == 0 :
        point = 0
    if short < 15 and point == 0 :
        cv.putText(img1, str(key4[i][4]), (50 + count * 10, 60 + line * 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                   1,
                   cv.LINE_AA)
        cv.rectangle(img, (key4[i][0], key4[i][2]), (key4[i][1], key4[i][3]), (255, 255, 255), -1)
        count = count + 1
        point = 1

    if (count >= 35):
        line = line + 1
        count = 0
def click4(x): #스페이스바
    global count
    global count_delay
    global line
    global img
    global point
    count_delay = count_delay + 1
    # count_delay가 20의 배수라면 출력
    if short > 15 and (count_delay % 5) == 0 :
        point = 0
    if short < 15 and point == 0 :
        cv.putText(img1, str(key5[i][4]), (50 + count * 10, 60 + line * 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                   1,
                   cv.LINE_AA)
        count = count + 1
        point = 1
        cv.rectangle(img, (170, 290), (470, 350), (255, 255, 255), -1)
    if (count >= 35):
        line = line + 1
        count = 0

def click5():  # enter키 입력, 혹은 문자 35개 이상 입력 시 호출
    global count_delay
    global line
    global count
    global img
    count_delay = count_delay + 1

    # count_delay가 20의 배수라면 출력
    if (count_delay % 60) == 0:
        line = line + 1
        count = 0
        cv.rectangle(img, (500, 290), (620, 350), (255, 255, 255), -1)


# centroid2 좌표가 특정 키 안에 1초동안 들어와 있으면 그 키를 입력.
# 자판(전체화면크기 640*480, 초기점 (20,20), 키 하나의 크기 60*60)


class handDetector():
    def __init__(self,mode=False,maxHands = 2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw= True ):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                #if id == 8:
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)
        return lmList

img = 0
i=0
j=0
cx_2=0
cy_2=0
cx_3=0
cy_3=0
cx_4=0
cy_4=0
cx_5=0
cy_5=0
length2=0
length3=0
length4=0
length5=0
x=0
y=0
short=0

def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = handDetector()
    centroid3 = [0, 0]
    global i
    global img
    global j
    global cx_2, cy_2, cx_3, cy_3, cx_4, cy_4, cx_5, cy_5
    global length2, length3, length4, length5
    global x,y,short

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if len(lmList) !=0:

            #검지
            x1_2, y1_2 = lmList[8][1:]
            x2_2, y2_2 = lmList[7][1], lmList[7][2]
            #중지
            x1_3, y1_3 = lmList[12][1:]
            x2_3, y2_3 = lmList[11][1], lmList[11][2]
            #약지
            x1_4, y1_4 = lmList[16][1:]
            x2_4, y2_4 = lmList[15][1], lmList[15][2]
            #새끼
            x1_5, y1_5 = lmList[20][1:]
            x2_5, y2_5 = lmList[19][1], lmList[19][2]

            #cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            length2 = math.hypot(x2_2 - x1_2, y2_2 - y1_2) #검지
            length3 = math.hypot(x2_3 - x1_3, y2_3 - y1_3) #중지
            length4 = math.hypot(x2_4 - x1_4, y2_4 - y1_4) #약지
            length5 = math.hypot(x2_5 - x1_5, y2_5 - y1_5) #새끼


            if length2 > length3:
                short = length3
                x = x1_3
                y = y1_3
            else:
                short = length2
                x = x1_2
                y = y1_2

            if length4 > short:
                short = short
            else:
                short = length4
                x = x1_4
                y = y1_4

            if length5 > short:
                short = short
                print(point)
                if short < 15:
                    cv.circle(img, (x, y), 10, (0, 255, 0), cv.FILLED)

            else:
                short = length5
                x = x1_5
                y = y1_5
                print(point)
                if short < 15:
                    cv.circle(img, (x, y), 10, (0, 255, 0), cv.FILLED)


        # 첫째줄 자판(눈으로 보이는 모양)
        for i in range(10):
            cv.rectangle(img, (key1[i][0], key1[i][2]), (key1[i][1], key1[i][3]), (0, 0, 0), 3)
            cv.putText(img, str(key1[i][4]), (40 + i * 60, 60), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
        # 둘째줄
        for i in range(10):
            cv.rectangle(img, (key2[i][0], key2[i][2]), (key2[i][1], key2[i][3]), (0, 0, 0), 3)
            cv.putText(img, str(key2[i][4]), (40 + i * 60, 120), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
        # 셋째줄
        for i in range(9):
            cv.rectangle(img, (key3[i][0], key3[i][2]), (key3[i][1], key3[i][3]), (0, 0, 0), 3)
            cv.putText(img, str(key3[i][4]), (70 + i * 60, 180), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
        # 넷째줄
        for i in range(7):
            cv.rectangle(img, (key4[i][0], key4[i][2]), (key4[i][1], key4[i][3]), (0, 0, 0), 3)
            cv.putText(img, str(key4[i][4]), (130 + i * 60, 240), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
        # 스페이스바
        cv.rectangle(img, (170, 290), (470, 350), (0, 0, 0), 3)
        cv.putText(img, "space", (280, 320), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
        # 엔터
        cv.rectangle(img, (500, 290), (620, 350), (0, 0, 0), 3)
        cv.putText(img, "enter", (510, 320), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))

        # 자판인식

        for i in range(10):
            if x > key1[i][0] and x < key1[i][1] and y > key1[i][2] and y < key1[i][3]:
                click(i)
        for j in range(10):
            if x > key2[j][0] and x < key2[j][1] and y > key2[j][2] and y < key2[j][3]:
                click1(j)
        for i in range(9):
            if x > key3[i][0] and x < key3[i][1] and y > key3[i][2] and y < key3[i][3]:
                click2(i)
        for i in range(7):
            if x > key4[i][0] and x < key4[i][1] and y > key4[i][2] and y < key4[i][3]:
                click3(i)
        for i in range(5):
            if x > key5[i][0] and x < key5[i][1] and y > key5[i][2] and y < key5[i][3]:
                click4(i)
        for i in range(5):
            if x > 500 and x < 620 and y > 290 and y < 350:
                click5()


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv.imshow('typing', img1)
        cv.imshow("Image", img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()