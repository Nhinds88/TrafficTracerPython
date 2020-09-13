# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:36:27 2020

@author: NicholasHinds
"""

import numpy as np
import cv2 as cv

video = cv.VideoCapture('./vids/Pexels Videos 4698.mp4')

while(1):
    
    ret, frame = video.read()
    
    if ret == True:
        
        cv.imshow('Frame', frame)
        
        if cv.waitKey(5) == ord('x'):
            break
    
    else:
        break