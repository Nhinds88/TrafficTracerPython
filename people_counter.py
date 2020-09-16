# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:34:28 2020

@author: NicholasHinds
"""
import cv2
import tools

#cameraFeed = tools.cameraSource(0)
#cameraFeed = tools.cameraSource('TestVideo.avi')
#cameraFeed = tools.cameraSource('https://r4---sn-a5mlrnez.googlevideo.com/videoplayback?expire=1599358291&ei=8_BTX6rlNIbakgaayoKQDw&ip=76.103.89.157&id=o-AK75r7WK7a2nSCa6muKbbTJAg3hG-4lu0iotr2nRCB4L&itag=18&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&gir=yes&clen=729683&ratebypass=yes&dur=16.021&lmt=1580854655287187&fvip=4&c=WEB&txp=1311222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgRUSTMoRdCCc0GsSN2FAgpqaHjU7_O6Qso6N2zJ5_yC4CICrlRdeAqppoyf2hKvgRnGCF_Toi8fTKB9nRpkaeigV3&redirect_counter=1&cm2rm=sn-n4vls7z&req_id=745e6a7fca55a3ee&cms_redirect=yes&mh=2R&mm=34&mn=sn-a5mlrnez&ms=ltu&mt=1599336628&mv=m&mvi=4&pl=23&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAKBhxlOlWeGHGAu0SBJSOtRrbbXCZ3Welkho91P7Kzd0AiEA0DE9S5OprKA1h8CTaVsRYNdYGz3nQyKsRopw09DyqWw%3D')
cameraFeed = tools.cameraSource('./vids/videoplayback.mp4')
#cameraFeed = tools.cameraSource('videoplayback.mp4')
#cameraFeed = tools.cameraSource('./vids/videoplayback.mp4')

startPoint = tools.lineCoords(500, 0)
endPoint = tools.lineCoords(500, 800)

video = cv2.VideoCapture(cameraFeed)

#video = tools.setResolution(video, 800, 600)
    
tools.process_video(video, startPoint, endPoint, 'h', 1000)