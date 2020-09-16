# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:54:34 2020

@author: NicholasHinds
"""

import cv2
import Person

def cameraSource(source):
    return source

def lineCoords(x, y):
    return x, y

def isVerticalORHorizontal(i):
    return i

def setResolution(video, height, width):
    video.set(3, height)
    video.set(4, width)
    
    return video

def contourLimit(c):
    return c

def process_video(video, lineStart, lineEnd, v_or_h, contourLimit):
    
    ret, frame1 = video.read()
    ret, frame2 = video.read()
    
    video.set(3, 800)
    video.set(3, 600)
    
    peopleID = 0
    people = []
    
    entry = 0
    exited = 0 
    
    while video.isOpened():
        
        check, _ = video.read()
        
        if check:
            
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations = 3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                
            cv2.line(frame1, (lineStart[0], lineStart[1]), (lineEnd[0], lineEnd[1]), (255, 0, 255), 2)
                
            
            for contour in contours:
                
                (x, y, w, h) = cv2.boundingRect(contour)
                
                if cv2.contourArea(contour) < contourLimit:
                    continue
                
                new = True
                
                for i in people:
                    
                    if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                        
                        new = False
                        i.updateCoords(x, y)
                        
                        if v_or_h == 'v':
                            
                            if i.enteringV(lineEnd[1]) == True:
                                
                                entry += 1
                                
                            if i.exitingV(lineStart[1]) == True:
                                
                                exited += 1
                                
                        if v_or_h == 'h':
                            
                            if i.enteringH(lineEnd[0]) == True:
                                
                                entry += 1
                                
                            if i.exitingH(lineStart[0]) == True:
                                
                                exited += 1
                            
                        break
                    
                if new == True:
                    p = Person.Customer(peopleID, x, y)
                    people.append(p)
                    peopleID += 1
                
                cv2.rectangle(frame1, (x,y), (x + w, y + h), (0, 255, 0), 2)
                
                cv2.putText(frame1, "Entered: {}".format(entry), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                cv2.putText(frame1, "Exited: {}".format(exited), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1) 
                
            cv2.imshow('vid', frame1)
            frame1 = frame2
            ret, frame2 = video.read()
            
        else:
            break
        
        if cv2.waitKey(5) == ord('x'):
                break
            
    cv2.destroyAllWindows()
    video.release()