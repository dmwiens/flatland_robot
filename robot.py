from ctypes import pointer
from math import sin, cos, pi, radians, degrees

import geometry as geo

LINK_A_LEN = 300
LINK_B_LEN = 200


def getPositionsFromTime(t):
    periodA = 1
    periodB = 1.8
    angleADEG = 20 + 10*sin(2*pi/periodA*t)
    angleBDEG = 60 + 30*sin(2*pi/periodB*t)

    # clockwise rotation
    # angleADEG = -90*t
    # angleBDEG = 90*t
    
    return (angleADEG, angleBDEG)


# If there are N links, there will be N+1 joint points
# Cartesian coordinates, not display coordinates
def getJointPoints(t):
    
    # Add origin
    points = []
    points.append(geo.Point(0, 0))
    current = points[-1]
    
    (angleADEG, angleBDEG) = getPositionsFromTime(t)

    # End of link A
    next = geo.Point()
    angle += angleADEG
    next.x = current.x + LINK_A_LEN*cos(radians(angle))
    next.y = current.y + LINK_A_LEN*sin(radians(angle))
    points.append(next)
    current = points[-1]

    # End of link B
    next = geo.Point()
    angle += angleBDEG
    next.x = current.x + LINK_B_LEN*cos(radians(angle))
    next.y = current.y + LINK_B_LEN*sin(radians(angle))
    points.append(next)
    current = points[-1]

    return points





