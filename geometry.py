from math import *

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y



def hypotenuse(pt1: Point, pt2: Point):
    return sqrt(((pt1.x - pt2.x)**2) + ((pt1.y - pt2.y)**2))
