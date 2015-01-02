# http://trevorappleton.blogspot.de/2013/07/python-game-of-life.html

import pygame, sys, random
from pygame.locals import *

FPS = 10

WINDOWWIDTH = 640
WINDOWHEIGHT = 640
CELLSIZE = 10

assert WINDOWWIDTH % CELLSIZE == 0, "Windowwidth ERROR"
assert WINDOWHEIGHT % CELLSIZE == 0, "Windowheight ERROR"

CELLWIDTH = WINDOWWIDTH / CELLSIZE
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGRAY = (40,40,40)
GREEN = (0, 255,0)

def drawGrid():
    for x in range(0,WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range(0,WINDOWHEIGHT,CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y),(WINDOWWIDTH, y))

def blankGrid():
    gridDict = {}
    for y in range (CELLHEIGHT):
        for x in range (CELLWIDTH):
            gridDict[x,y] = 0
    return gridDict

def randomGrid(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

def getNeighbours(item, lifeDict):
    neighbours = 0
    for x in range (-1, 2):
        for y in range (-1, 2):
            checkCell = (item[0]+x, item[1]+y)
            if checkCell[0] < CELLWIDTH and checkCell[0] >= 0:
                if checkCell[1] < CELLHEIGHT and checkCell[1] >= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0:
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1:
            if numberNeighbours < 2:
                newTick[item] = 0
            elif numberNeighbours > 3:
                newTick[item] = 0
            else:
                newTick[item] = 1
        elif lifeDict[item] == 0:
            if numberNeighbours == 3:
                newTick[item] = 1
            else:
                newTick[item] = 0
    return newTick
        
            
    

def colorGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE
    x = x * CELLSIZE
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF,WHITE, (x,y,CELLSIZE,CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, GREEN, (x,y,CELLSIZE,CELLSIZE))
    return None

def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) 
    pygame.display.set_caption('Can you feel the gaaaame of life')
    DISPLAYSURF.fill(WHITE)

    lifeDict = blankGrid()
    lifeDict = randomGrid(lifeDict)
    for item in lifeDict:
        colorGrid(item, lifeDict)
    
    drawGrid()
    pygame.display.update()
    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        lifeDict = tick(lifeDict)
        for item in lifeDict:
            colorGrid(item, lifeDict)
        drawGrid()
        FPSCLOCK.tick(FPS)
        pygame.display.update()

if __name__ == '__main__':
    main()
