# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:54:34 2020

@author: NicholasHinds
"""

import cv2
import imutils

def cameraSource(source):
    return source

def lineCrossingPlacement(num, XorY):
    return num, XorY

def lineCoords(x, y):
    return x, y

def majority(x):
    map = {}
    max = ('', 0)
    
    for n in x:
        
        if n in map:
            map[n] += 1
        else:
            map[n] = 1
            
        if map[n] > max[1]:
            max = (n, map[n])
    
    return max

def process_video(video, values, motion, entry, exited, avg, entry_S, entry_E, exit_S, exit_E):
    
    while video.isOpened():
    
        ret, frame = video.read()
        flag = True
        # text = ""
            
        if ret == True:
            
            frame = imutils.resize(frame, width=500)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
                
            if avg is None:
                avg = gray.copy().astype("float")
                continue
                
            cv2.accumulateWeighted(gray, avg, 0.5)
            frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
            thresh = cv2.threshold(frameDelta, 5, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations = 2)
            count, height = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
            for c in count:
                    
                if cv2.contourArea(c) < 3000:
                    continue
                    
                (x, y, w, h) = cv2.boundingRect(c)
                values.append(x)
                t1 = x + w
                t2 = y + h
                cv2.rectangle(frame, (x, y), (t1, t2), (0, 0, 255), 2)
                flag = False
                    
            noX = len(values)
                
            if (noX > 1):
                    
                difference = values[noX - 1] - values[noX - 2]
                    
                if (difference > 0):
                        
                    motion.append(1)
                        
                else:
                        
                    motion.append(0)
                        
            if flag is True:
                    
                if (noX > 5):
                        
                    val, times = majority(motion)
                        
                    if val == 1 and times >= 15:
                            
                        entry += 1
                            
                    else:
                            
                        exited += 1
                            
                values = list()
                motion = list()
                    
            #cv2.line(frame, entry_S, entry_E, (0, 255, 0), 2) # Green - Entry
            #cv2.line(frame, exit_S, exit_E, (255, 0, 0), 2) # Blue - Exit
                
            cv2.putText(frame, "Enter: {}".format(entry), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 255), 2)
            cv2.putText(frame, "Exit: {}".format(exited), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
            cv2.imshow("Frame", frame)
            cv2.imshow("Gray", gray)
            cv2.imshow("FrameDelta", frameDelta)
                
        if cv2.waitKey(5) == ord('x'):
            break