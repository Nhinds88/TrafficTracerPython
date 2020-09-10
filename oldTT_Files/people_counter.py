# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:34:28 2020

@author: NicholasHinds
"""

import numpy
import cv2
import tools

try: 
    log = open('log.txt', 'w')
except:
    print('Cannot open log file')

#cameraFeed = tools.cameraSource(0)
#cameraFeed = tools.cameraSource('TestVideo.avi')
#cameraFeed = tools.cameraSource('https://r4---sn-a5mlrnez.googlevideo.com/videoplayback?expire=1599358291&ei=8_BTX6rlNIbakgaayoKQDw&ip=76.103.89.157&id=o-AK75r7WK7a2nSCa6muKbbTJAg3hG-4lu0iotr2nRCB4L&itag=18&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&gir=yes&clen=729683&ratebypass=yes&dur=16.021&lmt=1580854655287187&fvip=4&c=WEB&txp=1311222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgRUSTMoRdCCc0GsSN2FAgpqaHjU7_O6Qso6N2zJ5_yC4CICrlRdeAqppoyf2hKvgRnGCF_Toi8fTKB9nRpkaeigV3&redirect_counter=1&cm2rm=sn-n4vls7z&req_id=745e6a7fca55a3ee&cms_redirect=yes&mh=2R&mm=34&mn=sn-a5mlrnez&ms=ltu&mt=1599336628&mv=m&mvi=4&pl=23&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAKBhxlOlWeGHGAu0SBJSOtRrbbXCZ3Welkho91P7Kzd0AiEA0DE9S5OprKA1h8CTaVsRYNdYGz3nQyKsRopw09DyqWw%3D')
#cameraFeed = tools.cameraSource('Pexels Videos 4698.mp4')
cameraFeed = tools.cameraSource('Pexels Videos 4698.mp4')

video = cv2.VideoCapture(cameraFeed)

values = list()
motion = list()
avg = None
count1 = 0
count2 = 0

# =============================================================================
# height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
# width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
# frameArea = height * width
# areaThreshold = frameArea/250
# =============================================================================

#entry_line = tools.lineCrossingPlacement(int((2*(height/5))), 'y')
#exit_line = tools.lineCrossingPlacement(int(entry_line[0] + 100), 'y')
#entry_line_Limit = tools.lineCrossingPlacement(int((1*(height/5))), 'y')
#exit_line_Limit = tools.lineCrossingPlacement(int((4*(height/5))), 'y')

# =============================================================================
# entry_line = tools.lineCrossingPlacement(int(500), 'x') #Entry Start
# exit_line = tools.lineCrossingPlacement(int(150), 'x')
# entry_line_Limit = tools.lineCrossingPlacement(int(600), 'x')
# exit_line_Limit = tools.lineCrossingPlacement(int(50), 'x') #Entry End
# =============================================================================
                                        
# =============================================================================
# point1 = [0,0]
# point2 = [0,0]
# point3 = [0,0]
# point4 = [0,0]
# point5 = [0,0]
# point6 = [0,0]
# point7 = [0,0]
# point8 = [0,0]
#     
# if entry_line[1] == 'y':
#     point3 = [0, entry_line[0]]
#     point4 = [width, entry_line[0]]
#     print('Entry line Y')
# else:
#     point3 = [entry_line[0], 0]
#     point4 = [entry_line[0], height]
#     print('Entry line X')
# 
# if exit_line[1] == 'y':
#     point1 = [0, exit_line[0]]
#     point2 = [width, exit_line[0]]
#     print('Exit line Y')
# else:
#     point1 = [exit_line[0], 0]
#     point2 = [exit_line[0], height]
#     print('Exit line X')
#     
# if entry_line_Limit[1] == 'y':
#     point5 = [0, entry_line_Limit[0]]
#     point6 = [width, entry_line_Limit[0]]
#     print('Entry line Limit Y')
# else:
#     point5 = [entry_line_Limit[0], 0]
#     point6 = [entry_line_Limit[0], height]
#     print('Entry line Limit X')
#     
# if exit_line_Limit[1] == 'y':
#     point7 = [0, exit_line_Limit[0]]
#     point8 = [width, exit_line_Limit[0]]
#     print('Exit line Limit Y')
# else:
#     point7 = [exit_line_Limit[0], 0]
#     point8 = [exit_line_Limit[0], height]
#     print('Exit line Limit X')
# =============================================================================
    
# =============================================================================x
# line1_points = numpy.array([point1,point2], numpy.int32)
# line1_points = line1_points.reshape((-1,1,2))
# =============================================================================
# line2_points = numpy.array([point3,point4], numpy.int32)
# line2_points = line2_points.reshape((-1,1,2))
# =============================================================================
# line3_points = numpy.array([point5,point6], numpy.int32)
# line3_points = line3_points.reshape((-1,1,2))
# =============================================================================
# line4_points = numpy.array([point7,point8], numpy.int32)
# line4_points = line4_points.reshape((-1,1,2))
# =============================================================================

# persons = []

# while video.isOpened():
    
# =============================================================================
#     ret, frame = video.read()
#     
#     for i in persons:
#         i.age_one()
#         
#     if ret == True:
#         tools.process_video(log, ret, frame, areaThreshold, 
#                             entry_line_Limit, entry_line, 
#                             exit_line_Limit, exit_line, 
#                             line1_points, line2_points, 
#                             line3_points, line4_points, 
#                             persons)
# =============================================================================
    
tools.process_video(video, values, motion, count1, count2, avg)
    
# =============================================================================
#    if cv2.waitKey(5) == ord('x'):
#            break
# =============================================================================

log.flush()
log.close()
video.release()
cv2.destroyAllWindows()