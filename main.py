import cv2
import mediapipe as mp
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

t = 0

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    glow_layer = np.zeros_like(frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            
            palm = hand_landmarks.landmark[9]
            cx = int(palm.x * w)
            cy = int(palm.y * h)

            
            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]

            x1 = int(thumb.x * w)
            y1 = int(thumb.y * h)

            x2 = int(index.x * w)
            y2 = int(index.y * h)

            distance = math.hypot(x2 - x1, y2 - y1)

            radius = int(distance)
            radius = max(40, min(radius,120))

            points = []


            for angle in range(0,360,8):

                rad = np.radians(angle)

                wave = math.sin(rad*6 + t) * 8

                r = radius + wave

                x = int(cx + r * math.cos(rad))
                y = int(cy + r * math.sin(rad))

                points.append((x,y))

            
            for i in range(len(points)-1):
                cv2.line(frame, points[i], points[i+1], (0,255,255),3)

            
            cv2.circle(glow_layer,(cx,cy),radius+50,(0,255,255),-1)

            
            cv2.circle(frame,(cx,cy),int(radius*0.6),(255,255,255),-1)

            
            cv2.circle(frame,(cx,cy),radius,(0,255,255),2)


    glow_layer = cv2.GaussianBlur(glow_layer,(0,0),35)

    frame = cv2.addWeighted(frame,1,glow_layer,0.7,0)

    cv2.imshow("Iron Man Energy Orb", frame)

    t += 0.15

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
