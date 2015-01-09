# -*- coding: utf-8 -*-
# ParticleSIM GRAPHICALs
# JK // Immergrün // 02.01.14

import sys, numpy, pygame
from pygame.locals import *

FPS = 10

WINDOWWIDTH = 640
WINDOWHEIGHT = 640

GREEN = (0,255,0)
BACKGROUND = (0,0,0)

particles = numpy.array([[200,200],[255,290],[360,299]])

def drawParticle(particle):
    #print(particle)
    pygame.draw.circle(DISPLAYSURF, GREEN, particle, 10, 1)
    pygame.draw.line(DISPLAYSURF, GREEN, (particle[0],particle[1]-3),(particle[0],particle[1]+3))
    pygame.draw.line(DISPLAYSURF, GREEN, (particle[0]-3,particle[1]),(particle[0]+3,particle[1]))
    

def main():
    #GRAPHICAL INIT
    pygame.init
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('ParticleSim')
    DISPLAYSURF.fill(BACKGROUND)

    #SIMULATION LOOP
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #DRAW SHIT
        DISPLAYSURF.fill(BACKGROUND)        
        for item in particles:
            drawParticle(item)
        #FPSCLOCK.tick(FPS)
        pygame.display.update()
    

if __name__ == '__main__':
    main()
