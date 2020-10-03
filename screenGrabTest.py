# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:02:21 2020

@author: NicholasHinds
"""
import cv2
import numpy as np
from PIL import ImageGrab

cv2.namedWindow('window', cv2.WINDOW_KEEPRATIO)

while(True):
    printscreen_pil = ImageGrab.grab()
    printscreen_numpy = np.array(printscreen_pil.getdata(), dtype = 
'uint8').reshape((printscreen_pil.size[1], printscreen_pil.size[0], 3))
    cv2.imshow('window', printscreen_numpy)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break