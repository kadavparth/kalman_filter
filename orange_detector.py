#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
import numpy as np
import cv2
from kalmanfilter import KalmanFilter


class OrangeDetector:
    
    def __init__(self):
        # Create mask for orange color
        self.low_orange = np.array([11, 128, 90])
        self.high_orange = np.array([179, 255, 255])

    def detect(self, frame):
        
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks with color ranges
        mask = cv2.inRange(hsv_img, self.low_orange, self.high_orange)

        # Find Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        box = (0, 0, 0, 0)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            box = (x, y, x + w, y + h)
            break

        return box
    
od = OrangeDetector()


kf = KalmanFilter()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    frame1 = cv2.imread('/home/parth/Desktop/kalman_filter/Pysource Kalman filter/blue_background.webp')
    
    if ret is False:
        break
    
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # detect = ora.detect(frame)
    
    # x,y,x2,y2 = detect    
    # 
    # cv2.rectangle(frame,(x,y),(x2,y2),color=(0,255,255))
    
    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)
    
    predicted = kf.predict(cx, cy)
    cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)
    
    cv2.circle(frame1, (cx, cy), 20, (0, 0, 255), 4)
    cv2.circle(frame1, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)
    
    cv2.imshow('blue',frame1)
    cv2.imshow("Frame", frame)
    cv2.imshow('HSV', hsv_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()