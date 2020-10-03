# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:54:34 2020

@author: NicholasHinds
"""

import cv2
import Person
import mysql.connector
import numpy as np
import os

from datetime import datetime

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

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

def dbConnnect(host, user, password, db):
    
    mydb = mysql.connector.connect(
        host = host, 
        user = user, 
        password = password, 
        database = db,
        auth_plugin='mysql_native_password'
        )
    
    return mydb

def getTime():
    
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    eventTime = now.strftime('%H:%M:%S')

    return date, eventTime

def insertPeopleData(ete, pid, mid, dur, date, t, db):
    
    cursor = db.cursor()
    
    sql = 'INSERT INTO foottraffic (enterorexit, customerid, merchantid, dur, date, time) VALUES (%s, %s, %s, %s, %s, %s)'
    val = (ete, pid, mid, dur, date, t)

    cursor.execute(sql, val)
    
    db.commit()
    
# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)
    
# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']    

def process_video(video, lineStart, lineEnd, v_or_h, contourLimit, merchantid, db):
    
    ret, frame1 = video.read()
    ret, frame2 = video.read()
    
    video.set(3, 800)
    video.set(3, 600)
    
    peopleID = 0
    custID = 0
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
                                custID += 1
        
                                t = getTime()
                                
                                insertPeopleData('enter', custID, merchantid, 0.0, t[0], t[1], db)
                                
                            if i.exitingV(lineStart[1]) == True:
                                
                                exited += 1
                                custID += 1
                                
                                t = getTime()
                                
                                insertPeopleData('exit', custID, merchantid, 0.0, t[0], t[1], db)
                                
                        if v_or_h == 'h':
                            
                            if i.enteringH(lineEnd[0]) == True:
                                
                                entry += 1
                                custID
                                
                                t = getTime()
                                
                                insertPeopleData('enter', custID, merchantid, 0.0, t[0], t[1], db)
                                
                            if i.exitingH(lineStart[0]) == True:
                                
                                exited += 1
                                custID += 1
                                
                                t = getTime()
                                
                                insertPeopleData('exit', custID, merchantid, 0.0, t[0], t[1], db)
                            
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