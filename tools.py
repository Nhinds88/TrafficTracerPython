# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:54:34 2020

@author: NicholasHinds
"""

import cv2
import time
import numpy
import Person

subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

Op = numpy.ones((3,3),numpy.uint8)
Cl = numpy.ones((11,11),numpy.uint8)

pid = 0
entry = 0
exited = 0

def cameraSource(source):
    return source

def lineCrossingPlacement(num, XorY):
    return num, XorY

def process_video(log, ret, frame, areaThreshold, entry_limit, entry_line, exit_limit, exit_line, line1, line2, line3, line4, persons):
    font = cv2.FONT_ITALIC
    max_p_age = 5
    
    global pid
    global entry
    global exited
    
    mask1 = subtractor.apply(frame)
    mask2 = subtractor.apply(frame)
    
    try:
        ret, imbin1 = cv2.threshold(mask1, 200, 255, cv2.THRESH_BINARY)
        ret, imbin2 = cv2.threshold(mask2, 200, 255, cv2.THRESH_BINARY)
         
        #Opening
        maskA = cv2.morphologyEx(imbin1, cv2.MORPH_OPEN, Op)
        maskB = cv2.morphologyEx(imbin2, cv2.MORPH_OPEN, Op)
         
        #Closing
        maskA = cv2.morphologyEx(maskA, cv2.MORPH_CLOSE, Cl)
        maskB = cv2.morphologyEx(maskB, cv2.MORPH_CLOSE, Cl)
    except :
        print('Enter: ', entry)
        print('Exited: ', exited)
        
    
    contours, hierarchy = cv2.findContours(maskB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for count in contours:
        area = cv2.contourArea(count)
        
        if area > areaThreshold:
            
            M = cv2.moments(count)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(count)
            
            new = True
            
            if cy in range(int(entry_limit[0]), int(exit_limit[0])):
                for i in persons:
                    if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                        
                        new = False
                        i.updateCoords(cx, cy)
                        if i.going_UP(exit_line[0], entry_line[0]) == True:
                            entry += 1
                            print('Entered ' + str(entry))
                            # print( "ID:",i.getId(),'crossed going up at',time.strftime("%c"))
                            log.write("ID: "+str(i.getId())+' crossed going Entry at ' + time.strftime("%c") + '\n')
                        elif i.going_DOWN(exit_line[0], entry_line[0]) == True:
                            exited += 1
                            print('Exited ' + str(exited))
                            # print( "ID:",i.getId(),'crossed going down at',time.strftime("%c"))
                            log.write("ID: " + str(i.getId()) + ' crossed going Exit at ' + time.strftime("%c") + '\n')
                        break
                    
                    if i.getState() == '1':
                        
                        if i.getDir() == 'exit' and i.getY() > exit_limit:
                            i.setDone()
                        elif i.getDir() == 'entry' and i.getY() < entry_limit:
                            i.setDone()
                    if i.timedOut():
                        
                        index = persons.index(i)
                        persons.pop(index)
                        del i
                
                if new == True:
                    p = Person.MyPerson(pid, cx, cy, max_p_age)
                    persons.append(p)
                    pid += 1
                    
            cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)
            
    for i in persons:
        cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)
        
    enter_str = 'Entered: ' + str(entry)
    exit_str = 'Exited: ' + str(exited)
    
    frame = cv2.polylines(frame, [line1], False, (255,0,0), thickness=2)
    frame = cv2.polylines(frame, [line2], False, (0,0,255), thickness=2)
    frame = cv2.polylines(frame, [line3], False, (0,255,0), thickness=1)
    frame = cv2.polylines(frame, [line4], False, (255,255,51), thickness=1)
    
    cv2.putText(frame, enter_str, (10,40), font, 0.5, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame, enter_str, (10,40), font, 0.5, (0,0,255), 1, cv2.LINE_AA)
    cv2.putText(frame, exit_str, (10,90), font, 0.5, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame, exit_str, (10,90), font, 0.5, (255,0,0), 1, cv2.LINE_AA)
    
    cv2.imshow('Frame', frame)
    #cv2.imshow('Mask', maskA)