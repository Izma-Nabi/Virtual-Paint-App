# import cv2
# import mediapipe as mp
# import time

# class HandDetector:
#     def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#         self.tipids=[4,8,12,16,20]
#         self.lmList=[]

#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(
#             static_image_mode=self.mode,
#             max_num_hands=self.maxHands,
#             min_detection_confidence=self.detectionCon,
#             min_tracking_confidence=self.trackCon
#         )
#         self.mpDraw = mp.solutions.drawing_utils

#     def findHands(self, img, draw=True):
#         """Detects hands and optionally draws landmarks"""
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)

#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
#         return img

#     def findPosition(self, img, handNo=0, draw=True):
#         """Returns landmark positions [(id, cx, cy), ...] for a hand"""

#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#             h, w, c = img.shape
#             for id, lm in enumerate(myHand.landmark):
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 self.lmList.append((id, cx, cy))

#                 # Draw specific landmarks with colors
#                 if draw:
#                     if id == 0:        # wrist
#                         cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
#                     # elif id == 4:      # thumb tip
#                     #     cv2.circle(img, (cx, cy), 7, (0, 255, 0), cv2.FILLED)
#                     # elif id == 8:      # index tip
#                     #     cv2.circle(img, (cx, cy), 7, (0, 0, 255), cv2.FILLED)
#                     # elif id == 12:     # middle tip
#                     #     cv2.circle(img, (cx, cy), 7, (255, 255, 0), cv2.FILLED)
#                     # elif id == 16:     # ring tip
#                     #     cv2.circle(img, (cx, cy), 7, (0, 255, 255), cv2.FILLED)
#                     # elif id == 20:     # pinky tip
#                     #     cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
#         return self.lmList
    
#     def whichfingerup(self):
#         fingers=[]
#         if len(self.lmList)!=0:
#             # Thumb: tip y < ip y
#             if(self.lmList[self.tipids[0]][2] < self.lmList[self.tipids[0]-1][2]):
#                 fingers.append(1)
#             else:
#                 fingers.append(0)
#             for id in range(1,5):
#                 if(self.lmList[self.tipids[id]][2] < self.lmList[self.tipids[id]-2][2]):
#                     fingers.append(1)
#                 else:
#                     fingers.append(0)
#         return fingers

# # ----------------------------------------------------
# # Standalone main function
# # ----------------------------------------------------
# def main():
#     cap = cv2.VideoCapture(0)  
#     detector = HandDetector()
#     pTime = 0

#     while True:
#         success, img = cap.read()
#         if not success:
#             print("Video ended or cannot read frame")
#             break

#         img = detector.findHands(img)
#         lmList = detector.findPosition(img, handNo=0, draw=True)

#         # Example: print first landmark
#         if lmList:
#             print(lmList[0])

#         # FPS calculation
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, str(int(fps)), (10, 70),
#                     cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

#         cv2.imshow("Image", img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # ----------------------------------------------------
# # Run main if module is executed directly
# # ----------------------------------------------------
# if __name__ == "__main__":
#     main()
import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.tipids=[4,8,12,16,20]
        self.lmList=[]

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """Detects hands and optionally draws landmarks"""
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        """Returns landmark positions [(id, cx, cy), ...] for a hand"""
        self.lmList = [] 
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            h, w, c = img.shape
            for id, lm in enumerate(myHand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append((id, cx, cy))

                # Draw specific landmarks with colors
                if draw:
                    if id == 0:        # wrist
                        cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
                    # elif id == 4:      # thumb tip
                    #     cv2.circle(img, (cx, cy), 7, (0, 255, 0), cv2.FILLED)
                    # elif id == 8:      # index tip
                    #     cv2.circle(img, (cx, cy), 7, (0, 0, 255), cv2.FILLED)
                    # elif id == 12:     # middle tip
                    #     cv2.circle(img, (cx, cy), 7, (255, 255, 0), cv2.FILLED)
                    # elif id == 16:     # ring tip
                    #     cv2.circle(img, (cx, cy), 7, (0, 255, 255), cv2.FILLED)
                    # elif id == 20:     # pinky tip
                    #     cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return self.lmList
    
    def whichfingerup(self):
        fingers=[]
        if len(self.lmList)!=0:
            if(self.lmList[self.tipids[0]][1] < self.lmList[self.tipids[0]-1][1]):
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if(self.lmList[self.tipids[id]][2] < self.lmList[self.tipids[id]-2][2]):
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers



# ----------------------------------------------------
# Standalone main function
# ----------------------------------------------------
def main():
    cap = cv2.VideoCapture(0)  
    detector = HandDetector()
    pTime = 0

    while True:
        success, img = cap.read()
        if not success:
            print("Video ended or cannot read frame")
            break

        img = detector.findHands(img)
        lmList = detector.findPosition(img, handNo=0, draw=True)

        # Example: print first landmark
        if lmList:
            print(lmList[0])

        # FPS calculation
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ----------------------------------------------------
# Run main if module is executed directly
# ----------------------------------------------------
if __name__ == "__main__":
    main()
