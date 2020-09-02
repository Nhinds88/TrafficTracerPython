# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:34:28 2020

@author: NicholasHinds
"""

import numpy
import cv2
#import Person
#import time
import tools

try: 
    log = open('log.txt', 'w')
except:
    print('Cannot open log file')
    
enterCount = 0
exitCount = 0

cameraFeed = tools.cameraSource(0)


video = cv2.VideoCapture(cameraFeed)

height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frameArea = height * width
areaThreshold = frameArea/250

entry_line = tools.lineCrossingPlacement((2*(height/5)), 'y')
exit_line = tools.lineCrossingPlacement((3*(height/5)), 'y')
entry_line_Limit = tools.lineCrossingPlacement((1*(height/5)), 'y')
exit_line_Limit = tools.lineCrossingPlacement((4*(height/5)), 'y')
                                        
point1 = [0,0]
point2 = [0,0]
point3 = [0,0]
point4 = [0,0]
point5 = [0,0]
point6 = [0,0]
point7 = [0,0]
point8 = [0,0]

if entry_line[1] == 'y':
    point3 = [0, entry_line[0]]
    point4 = [width, entry_line[0]]
else:
    point3 = [0, entry_line[0]]
    point4 = [height, entry_line[0]]

if exit_line[1] == 'y':
    point1 = [0, exit_line[0]]
    point2 = [width, exit_line[0]]
else:
    point1 = [0, exit_line[0]]
    point2 = [height, exit_line[0]]
    
if entry_line_Limit[1] == 'y':
    point5 = [0, entry_line_Limit[0]]
    point6 = [width, entry_line_Limit[0]]
else:
    point5 = [0, entry_line_Limit[0]]
    point6 = [height, entry_line_Limit[0]]
    
if exit_line_Limit[1] == 'y':
    point7 = [0, exit_line_Limit[0]]
    point8 = [width, exit_line_Limit[0]]
else:
    point7 = [0, exit_line_Limit[0]]
    point8 = [height, exit_line_Limit[0]]
    
# =============================================================================
line1_points = numpy.array([point1,point2], numpy.int32)
line1_points = line1_points.reshape((-1,1,2))
# =============================================================================
line2_points = numpy.array([point3,point4], numpy.int32)
line2_points = line1_points.reshape((-1,1,2))
# =============================================================================
line3_points = numpy.array([point5,point6], numpy.int32)
line3_points = line1_points.reshape((-1,1,2))
# =============================================================================
line4_points = numpy.array([point7,point8], numpy.int32)
line4_points = line1_points.reshape((-1,1,2))
# =============================================================================

persons = []

while video.isOpened():
    
    ret, frame = video.read()
    
    for i in persons:
        i.age_one()
        
    tools.process_video(log, ret, frame, enterCount, exitCount, areaThreshold, entry_line_Limit, entry_line, exit_line_Limit, exit_line, line1_points, line2_points, line3_points, line4_points, persons)
    
    if cv2.waitKey(5) == ord('x'):
            break

log.flush()
log.close()
video.release()
cv2.destroyAllWindows()