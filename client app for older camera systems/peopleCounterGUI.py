import cv2
import mysql.connector
import tkinter as tk

from datetime import datetime
from tkinter import filedialog
from PIL import ImageTk, Image

from random import randint
import time

# =============================================================================
# Adapted from
# https://github.com/Gupu25/PeopleCounter
# =============================================================================

#### Customer Object
class Customer:
    tracks = []
    def __init__(self, i, xi, yi):
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        self.done = False
        self.state = '0'
        self.dir = None
    def getTracks(self):
        return self.tracks
    def getId(self):
        return self.i
    def getState(self):
        return self.state
    def getDir(self):
        return self.dir
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getTime(self):
        return self.eventTime
    def updateCoords(self, xn, yn):
        self.age = 0
        self.tracks.append([self.x,self.y])
        self.x = xn
        self.y = yn
    def setDone(self):
        self.done = True
    def enteringV(self,point):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] < point and self.tracks[-2][1] >= point:
                    state = '1'
                    self.dir = 'entered'
                    
                    return True
            else:
                return False
        else:
            return False
    def exitingV(self,point):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] > point and self.tracks[-2][1] <= point: 
                    state = '1'
                    self.dir = 'exited'
                    
                    return True
            else:
                return False
        else:
            return False
    def enteringH(self,point):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][0] < point and self.tracks[-2][0] >= point: 
                    state = '1'
                    self.dir = 'entered'
                    
                    return True
            else:
                return False
        else:
            return False
    def exitingH(self,point):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][0] > point and self.tracks[-2][0] <= point: 
                    state = '1'
                    self.dir = 'exited'
                    
                    return True
            else:
                return False
        else:
            return False

def cameraSource(source):
    return source

def lineCoords(x, y):
    return x, y

def isVerticalORHorizontal(i):
    return i

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

def insertPeopleData(ete, pid, mid, dur, date, t, db):
    
    cursor = db.cursor()
    
    sql = 'INSERT INTO foottraffic (enterorexit, customerid, merchantid, dur, date, time) VALUES (%s, %s, %s, %s, %s, %s)'
    val = (ete, pid, mid, dur, date, t)

    cursor.execute(sql, val)
    
    db.commit()

    

def process_video(video, lineStart, lineEnd, v_or_h, contourLimit, merchantid, db, date, time):
    
    ret, frame1 = video.read()
    ret, frame2 = video.read()
    
    peopleID = 0
    custID = 0
    people = []
    
    st = time.split(":")

    hour = int(st[0])
    minutes = int(st[1])
    s = int(st[2])
    
    entry = 0
    exited = 0 
    
    while video.isOpened():
        
        check, _ = video.read()
        
        if check:
            
            milli = video.get(cv2.CAP_PROP_POS_MSEC)
            sec = milli / 1000 
            # print(round(sec))
            seconds = s + sec
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hour += 1
            if hour == 24:
                hour = 0
            
            currentVideoTime = str(hour) + ":" + str(minutes) + ":" + str(round(seconds))
            
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
                                
                                insertPeopleData('enter', custID, merchantid, 0.0, date, currentVideoTime, db)
                                
                            if i.exitingV(lineStart[1]) == True:
                                
                                exited += 1
                                custID += 1
                                
                                insertPeopleData('exit', custID, merchantid, 0.0, date, currentVideoTime, db)
                                
                        if v_or_h == 'h':
                            
                            if i.enteringH(lineEnd[0]) == True:
                                
                                entry += 1
                                custID
                                
                                insertPeopleData('enter', custID, merchantid, 0.0, date, currentVideoTime, db)
                                
                            if i.exitingH(lineStart[0]) == True:
                                
                                exited += 1
                                custID += 1
                                
                                insertPeopleData('exit', custID, merchantid, 0.0, date, currentVideoTime, db)
                            
                        break
                    
                if new == True:
                    p = Customer(peopleID, x, y)
                    people.append(p)
                    peopleID += 1
            ##################################################
                # used for finding camera specific parameters#
                ##############################################
                # cv2.rectangle(frame1, (x,y), (x + w, y + h), (0, 255, 0), 2)
                # 
                # cv2.putText(frame1, "Entered: {}".format(entry), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                # cv2.putText(frame1, "Exited: {}".format(exited), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
            #cv2.imshow('vid', frame1)
            ##################################################
            frame1 = frame2
            ret, frame2 = video.read()
            
        else:
            break
        
        if cv2.waitKey(5) == ord('x'):
            break
            
    cv2.destroyAllWindows()
    video.release()

db = dbConnnect("d1kb8x1fu8rhcnej.cbetxkdyhwsb.us-east-1.rds.amazonaws.com", "cg0qk6kstr07a5z4", "dw56x2swou8s05vw", "ljovr7av2qudtk53")
######## GUI #########################
root = tk.Tk()

root.title("Traffic Tracer")
root.minsize(400, 300)
root['background']='#2A3132'

vorh = tk.StringVar()

bg_image = Image.open("trafficTracerSmall.png")
background_image=ImageTk.PhotoImage(image=bg_image)
background_label = tk.Label(root, bg='#2A3132', image=background_image)
background_label.photo=background_image
background_label.grid(column = 0, row = 0)

date = tk.Label(root, fg='white', bg='#2A3132', text='Enter Date in Format YYYY-MM-DD: ').grid(row=1, column=0)
time = tk.Label(root, fg='white', bg='#2A3132', text='Enter Time in Format HH:MM:SS: ').grid(row=2, column=0)
dateEntry = tk.Entry(root)
timeEntry = tk.Entry(root)
dateEntry.grid(row=1, column=1)
timeEntry.grid(row=2, column=1)

def open_file(): 
    file = filedialog.askopenfilename(parent=root)
    print(file)
    video = cv2.VideoCapture(file)
    # Custom values are Client Specific and should not be changed unless camera is moved. 
    startPoint = lineCoords(0, 240)
    endPoint = lineCoords(640, 240)
    process_video(video, startPoint, endPoint, 'v', 4000, 2, db, dateEntry.get(), timeEntry.get())

labelFrame = tk.LabelFrame(root, fg='white', bg='#2A3132', text = "Open File")
labelFrame.grid(column = 0, row = 6, padx = 20, pady = 20)

button = tk.Button(labelFrame, fg='white', bg='#602c1f', text = "Browse A File",command = open_file)
button.grid(column = 1, row = 6)


root.mainloop()