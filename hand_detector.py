import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        landmarks = None

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    img, handLms, self.mpHands.HAND_CONNECTIONS
                )
                landmarks = handLms

        return img, landmarks

    def get_index_position(self, img, landmarks):

        if landmarks is None:
            return None

        h, w, _ = img.shape

        lm = landmarks.landmark[8]
        cx, cy = int(lm.x * w), int(lm.y * h)

        return cx, cy