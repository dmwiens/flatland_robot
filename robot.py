from math import sin, cos, pi, radians, degrees

LINK_A_LEN = 300
LINK_B_LEN = 200



def getPositionsFromTime(t):
    pA = 1
    pB = 1.8
    angleADEG = 20 + 10*sin(2*pi/pA*t)
    angleBDEG = 60 + 30*sin(2*pi/pB*t)
    
    return (angleADEG, angleBDEG)




