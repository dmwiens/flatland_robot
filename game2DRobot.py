# Ref: https://www.pygame.org/docs/tut/PygameIntro.html

import sys
import pygame
from math import *

import robot as rb
import geometry as geo

pygame.init()

FPS = 60
size = width, height = 1280, 960
speed = [1, 1]
black = 0, 0, 0
origin = geo.Point(500, 500)

surface = pygame.display.set_mode(size)
surface.convert

BLUE=(0,0,255)
BLUEG=(0,128,255)

def pause():
    programPause = input("Press the <ENTER> key to continue...")

# Gets the 6 points an elongated trapezoid, given the 2 "sword tips"
def getPointsOfTrapezoid2Pts(pt1: geo.Point, pt2: geo.Point):
	k = min(20, geo.hypotenuse(pt1, pt2)/2)
	angle1to2RAD = atan2(pt2.y-pt1.y, pt2.x-pt1.x)

	return [(pt1.x                                     , pt1.y                                 		),
			(pt1.x + k*cos(angle1to2RAD+radians(45))   , pt1.y + k*sin(angle1to2RAD+radians(45))  	),
			(pt2.x + k*cos(angle1to2RAD+radians(135))  , pt2.y + k*sin(angle1to2RAD+radians(135))	),
			(pt2.x                                     , pt2.y                                    	),
			(pt2.x + k*cos(angle1to2RAD-radians(135))  , pt2.y + k*sin(angle1to2RAD-radians(135)) 	),
			(pt1.x + k*cos(angle1to2RAD-radians(45))   , pt1.y + k*sin(angle1to2RAD-radians(45))  	),
			]



def getPointsOfRectAtAngle(left, top, width, height, angleDEG):
	angleRAD = radians(angleDEG)
	return [
		(left												, top                                                 ),
		(left + width*cos(angleRAD)                         , top + width*sin(angleRAD)                           ),
		(left + width*cos(angleRAD) + height*sin(angleRAD) 	, top + width*sin(angleRAD)    - height*cos(angleRAD) ),
		(left                    	+ height*sin(angleRAD) 	, top                          - height*cos(angleRAD) )
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
	(angleADEG, angleBDEG) = rb.getPositionsFromTime(t)

	# Draw
	surface.fill(black)
	linkA = pygame.draw.polygon(surface, BLUE, getPointsOfTrapezoid2Pts(origin, origin.addVectorMagAng(rb.LINK_A_LEN, angleADEG)))
	linkB = pygame.draw.polygon(surface, BLUEG, getPointsOfTrapezoid2Pts(origin.addVectorMagAng(rb.LINK_A_LEN, angleADEG), origin.addVectorMagAng(rb.LINK_A_LEN, angleADEG).addVectorMagAng(rb.LINK_B_LEN, angleBDEG)))
	surface.blit(ball, ballrect)
	# pygame.display.flip()

	pygame.display.update()

	# pause() 