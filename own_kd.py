# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:07:48 2022

@author: parth
"""

from kalmanfilter import KalmanFilter
import cv2

kf = KalmanFilter()

img = cv2.imread("blue_background.webp")

ball_pos = [(50,100), (100,100), (150,100), (200,100), (250,100), (300,100)]

for pt in ball_pos:
    cv2.circle(img, pt, 15, (0,255,0), -1)
    
    predicted = kf.predict(pt[0], pt[1])
    cv2.circle(img, (predicted[0], predicted[1]), 20, (0,0,255))


for i in range(10):
    predicted = kf.predict(predicted[0], predicted[1])
    cv2.circle(img, (predicted[0], predicted[1]), 20, (0,0,255))

cv2.imshow('win', img)


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()