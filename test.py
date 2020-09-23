# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:16:20 2020

@author: NicholasHinds
"""

import cv2

video = cv2.VideoCapture(0)

while True:
     
     ret, frame = video.read()
     
     if ret:
         
         cv2.imshow('desktop', frame)
         
         if cv2.waitKey(1)  == ord('x'):
             break
         
video.release()
cv2.destroyAllWindows()