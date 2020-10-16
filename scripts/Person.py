# =============================================================================
# https://github.com/Gupu25/PeopleCounter
# =============================================================================

from random import randint
import time

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
        self.eventTime = ''
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
                    self.eventTime = time.asctime(time.localtime())
                    
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
                    self.eventTime = time.asctime(time.localtime())
                    
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
                    self.eventTime = time.asctime(time.localtime())
                    
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
                    self.eventTime = time.asctime(time.localtime())
                    
                    return True
            else:
                return False
        else:
            return False
class MultiPerson:
    def __init__(self, persons, xi, yi):
        self.persons = persons
        self.x = xi
        self.y = yi
        self.tracks = []
        self.done = False
        
