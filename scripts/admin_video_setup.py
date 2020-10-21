"""
Created on Tue Sep  1 11:34:28 2020

@author: NicholasHinds
"""
import cv2
import sys
import tools

def main():
	print("Welcome to Traffic Tracer stream setup")
	video = input("Enter video file path:")
	x1 = input("Enter the starting x point:")
	y1 = input("Enter the starting y point:")
	x2 = input("Enter the ending x point:")
	y2 = input("Enter the ending y point:")
	v_or_h = input("Enter v or h value:")
	flipped = input("Flipped? true or false:")
	contourLimit = input("Enter the contour limit:")
	mid = input("Enter MID:")
	cameraFeed = tools.cameraSource(video)
	startPoint = tools.lineCoords(int(x1), int(y1))
	endPoint = tools.lineCoords(int(x2), int(y2))
	db = tools.dbConnnect("d1kb8x1fu8rhcnej.cbetxkdyhwsb.us-east-1.rds.amazonaws.com", "cg0qk6kstr07a5z4", "dw56x2swou8s05vw", "ljovr7av2qudtk53")
	video = cv2.VideoCapture(cameraFeed)
	tools.process_video(video, startPoint, endPoint, v_or_h, flipped, int(contourLimit), int(mid), db)

if __name__ == "__main__":
    main()