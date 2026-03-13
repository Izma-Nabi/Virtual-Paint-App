import cv2
import os
import htm as htm  # your hand tracking module
import numpy as np

# =========================
# Variables
# =========================
bthickness = 5           # brush thickness
ethickness = 50          # eraser thickness
xp, yp = 0, 0            # previous points
colordraw = (255, 192, 203)  # default color (pinkish)
myCanvas = np.zeros((720, 1280, 3), np.uint8)

# =========================
# Load header images
# =========================
path = r'C:\Users\DELL\OneDrive\Desktop\xx\xx\images'
img_list = os.listdir(path)
img_list.sort()

overlayList = []
for img_name in img_list:
    img_temp = cv2.imread(os.path.join(path, img_name))
    if img_temp is not None:
        img_temp = cv2.resize(img_temp, (1280, 125))
        overlayList.append(img_temp)

header = overlayList[0]

# =========================
# Camera setup
# =========================
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
print("Camera opened:", cap.isOpened())

# =========================
# Hand detector
# =========================
detector = htm.HandDetector(detectionCon=0.85)

# =========================
# Main loop
# =========================
while True:
    success, img = cap.read()
    if not success:
        print("Cannot read frame")
        break

    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # check which fingers are up
        fingers = detector.whichfingerup()

        # ----------------------
        # Selection mode (two fingers up)
        # ----------------------
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0  # reset previous points

            # only change color if finger is in header
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    colordraw = (222, 49, 99)   # pink
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    colordraw = (255, 0, 0)     # blue
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    colordraw = (0, 255, 0)     # green
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    colordraw = (0, 0, 0)       # eraser

            # show rectangle on selection
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25), colordraw, cv2.FILLED)

        # ----------------------
        # Drawing mode (index finger up, middle finger down)
        # ----------------------
        elif fingers[1] and not fingers[2]:
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            # eraser
            if colordraw == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), colordraw, bthickness)
                cv2.line(myCanvas, (xp, yp), (x1, y1), colordraw, ethickness)
            else:
                # normal drawing
                cv2.line(img, (xp, yp), (x1, y1), colordraw, bthickness)
                cv2.line(myCanvas, (xp, yp), (x1, y1), colordraw, ethickness)

            # update previous points
            xp, yp = x1, y1

    # =========================
    # Merge canvas with video
    # =========================
    imgGray = cv2.cvtColor(myCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, myCanvas)

    # overlay header
    img[0:125, 0:img.shape[1]] = header

    # show image
    cv2.imshow("Virtual Paint", img)

    # exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()