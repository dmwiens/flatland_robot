# Ref: https://www.pygame.org/docs/tut/PygameIntro.html

import sys
import pygame
import math

import robot as rb

pygame.init()

FPS = 60
size = width, height = 1280, 960
speed = [1, 1]
black = 0, 0, 0
origin = {'x': 500, 'y':500}

surface = pygame.display.set_mode(size)
surface.convert

BLUE=(0,0,255)
BLUEG=(0,128,255)


def getPointsOfRectAtAngle(left, top, width, height, angleDEG):
    angleRAD = math.radians(angleDEG)
    return [
        (left                                                       , top                                                           ),
        (left + width*math.cos(angleRAD)                            , top + width*math.sin(angleRAD)                                ),
        (left + width*math.cos(angleRAD)+ height*math.sin(angleRAD) , top + width*math.sin(angleRAD)    - height*math.cos(angleRAD) ),
        (left                           + height*math.sin(angleRAD) , top                               - height*math.cos(angleRAD) )
    ]

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


clk = pygame.time.Clock()
t = 0

while clk.tick(FPS):
    
    #increment time
    t += 1/FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    # New angles
    (angleADEG, angleBDEG) = rb.getPositionFromTime(t)

    surface.fill(black)
    linkA = pygame.draw.polygon(surface, BLUE,  getPointsOfRectAtAngle(origin['x'], origin['y'], rb.LINK_A_LEN, 20, angleADEG))
    linkB = pygame.draw.polygon(surface, BLUEG, getPointsOfRectAtAngle(origin['x'] + rb.LINK_A_LEN*math.cos(math.radians(angleADEG)), origin['y'] + rb.LINK_A_LEN*math.sin(math.radians(angleADEG)), rb.LINK_B_LEN, 20, angleBDEG))
    surface.blit(ball, ballrect)

    
    # pygame.display.flip()

    pygame.display.update()