from math import *

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addVectorMagAng(self, magnitude, angle):
        newPt = Point(self.x, self.y)
        newPt.x += magnitude*cos(radians(angle))
        newPt.y += magnitude*sin(radians(angle))

        return newPt

    def __repr__(self) -> str:
        return "(x: " + str(self.x) + ", y: " + str(self.y) + ")"




def hypotenuse(pt1: Point, pt2: Point):
    return sqrt(((pt1.x - pt2.x)**2) + ((pt1.y - pt2.y)**2))
