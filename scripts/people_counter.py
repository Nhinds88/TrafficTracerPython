# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:34:28 2020

@author: NicholasHinds
"""
import cv2
import tools
import numpy as np
import os

#cameraFeed = tools.cameraSource(0)
#cameraFeed = tools.cameraSource('TestVideo.avi')
#cameraFeed = tools.cameraSource('https://r4---sn-a5mlrnez.googlevideo.com/videoplayback?expire=1599358291&ei=8_BTX6rlNIbakgaayoKQDw&ip=76.103.89.157&id=o-AK75r7WK7a2nSCa6muKbbTJAg3hG-4lu0iotr2nRCB4L&itag=18&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&gir=yes&clen=729683&ratebypass=yes&dur=16.021&lmt=1580854655287187&fvip=4&c=WEB&txp=1311222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgRUSTMoRdCCc0GsSN2FAgpqaHjU7_O6Qso6N2zJ5_yC4CICrlRdeAqppoyf2hKvgRnGCF_Toi8fTKB9nRpkaeigV3&redirect_counter=1&cm2rm=sn-n4vls7z&req_id=745e6a7fca55a3ee&cms_redirect=yes&mh=2R&mm=34&mn=sn-a5mlrnez&ms=ltu&mt=1599336628&mv=m&mvi=4&pl=23&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAKBhxlOlWeGHGAu0SBJSOtRrbbXCZ3Welkho91P7Kzd0AiEA0DE9S5OprKA1h8CTaVsRYNdYGz3nQyKsRopw09DyqWw%3D')
#cameraFeed = tools.cameraSource('./vids/TestVideo.avi')
#cameraFeed = tools.cameraSource('videoplayback.mp4')
#cameraFeed = tools.cameraSource('./vids/videoplayback.mp4')
#cameraFeed = tools.cameraSource('http://192.168.0.162:5000/')
cameraFeed = tools.cameraSource('https://r4---sn-n4v7sn7y.googlevideo.com/videoplayback?expire=1602737451&ei=y4CHX6feKtuJ2_gP34atyAU&ip=76.103.89.157&id=o-ADFDXzMt00hRpP_FZse1JybvNGeKpz7iw6c3ohD7EQR9&itag=18&source=youtube&requiressl=yes&mh=TQ&mm=31%2C26&mn=sn-n4v7sn7y%2Csn-a5meknel&ms=au%2Conr&mv=m&mvi=4&pl=23&initcwndbps=2316250&vprv=1&mime=video%2Fmp4&gir=yes&clen=1729413&ratebypass=yes&dur=30.766&lmt=1523285753586330&mt=1602715711&fvip=4&fexp=23915654&c=WEB&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgeBJSLrD8LY-INmfnjNT8pIKjHFM86wJy1WkT0NIbI8ICIQDSl8y522vDHSrpJY3NylUMjEfqtKzSVteWh_Cp_B2ykg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAKjM1_obNUngOf6GJaYlqkvrhi2cFD_2Di-3E8nOlPYOAiEAu9VvnbgePGOEkrZiYbBgdYRebHUC7INVkcnKuu02GwY%3D')

startPoint = tools.lineCoords(0, 130)
endPoint = tools.lineCoords(640, 130)

db = tools.dbConnnect("localhost", "root", "Delonh88", "traffictracer")

video = cv2.VideoCapture(cameraFeed)
    
tools.process_video(video, startPoint, endPoint, 'v', False, 8000, 2, db)