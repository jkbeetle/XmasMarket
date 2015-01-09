# -*- coding: utf-8 -*-
# ParticleSIM GRAPHICALs + PHYSICS
# JK // Immergrün // 02.01.14

import sys, numpy, pygame, copy, math
from pygame.locals import *

FPS = 10

WINDOWWIDTH = 640
WINDOWHEIGHT = 640

GREEN = (0,255,0)
RED = (255,0,0)
BACKGROUND = (0,0,0)

nDim=2
r=25
RepellConst=1000
RepellConst2=10
AttractorConst=10
nParticles=10


def CalculatePositions(x_veclist,v_veclist,F_veclist,dt,m):
    """Berechnung der neunen Positionen"""
    #print(str(x_veclist) + "  " +str(v_veclist)+ "  "+str(F_veclist))
    result = x_veclist+v_veclist*dt+1./(2*m)*F_veclist*dt*dt
    #print(result)
    return result
    
def CalculateVelocities(v_veclist,Fold_veclist,F_veclist,dt,m):
    """Berechnung der neuen Geschwindigkeiten"""
    print(" VELOCITIES: ", Fold_veclist,F_veclist)
    res=v_veclist+1./(2*m)*(Fold_veclist+F_veclist)*dt
    return res 

def AttractorForce(r1,r2):
    d=numpy.linalg.norm(r2-r1)
    if d==0:
        res=0
    else:
        res=1.*AttractorConst*(r2-r1)/d
    #print("Attractor: ",res)
    return res
    
def RepellingForce(r1,r2):
    d=numpy.linalg.norm(r2-r1)
    if d>=2*r:
        F=0
    else:
        #F=1.*RepellConst*(1./d-1./(2*r))
        F=RepellConst*(math.exp(RepellConst2/d)-math.exp(RepellConst2/(2*r)))
    res=-F*(r2-r1)/d
    return res
    
def CalculateForce(x_veclist,attractor_veclist):
    #Kraftberechnung
    F_veclist=numpy.zeros((len(x_veclist),2),float)
    #print(F_veclist)

    #RepellingForce
    for i in range(len(x_veclist)):
        r1=x_veclist[i]
        for j in range(i+1,len(x_veclist)):
            r2=x_veclist[j]
            Fij=RepellingForce(r1,r2)
            F_veclist[i]=F_veclist[i]+Fij
            F_veclist[j]=F_veclist[j]-Fij
    print("F: ",F_veclist)
    #AttractorForce
    for i in range(len(x_veclist)):
        r1=x_veclist[i]
        r2=attractor_veclist[i]
        Fi=AttractorForce(r1,r2)
        F_veclist[i]=F_veclist[i]+Fi
    print("F2: ",F_veclist)
    return F_veclist
    
    #return(numpy.array([[0,0]],float))
    



def drawParticle(particle,color):
    #print(particle)
    pygame.draw.circle(DISPLAYSURF, color,(int(particle[0]),int(particle[1])), 25, 1)
    #pygame.draw.line(DISPLAYSURF, GREEN, (particle[0],particle[1]-3),(particle[0],particle[1]+3))
    #pygame.draw.line(DISPLAYSURF, GREEN, (particle[0]-3,particle[1]),(particle[0]+3,particle[1]))

def drawAttractor(particle,attractor):
    pygame.draw.line(DISPLAYSURF,(150,150,150),(particle[0],particle[1]),(attractor[0],attractor[1]),1)

def main():
    #GRAPHICAL INIT
    pygame.init
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('ParticleSim')
    DISPLAYSURF.fill(BACKGROUND)

    #PHYSICS INIT
        
    x_veclist=numpy.array([[200,200],[400,400],[100,100]],float)
    v_veclist=numpy.array([[0,0],[0,0],[0,0]],float)
    attractor_veclist = numpy.array([[300,300],[300,300],[300,300]],float)

    zero_veclist=numpy.array([[0,0]],float)

    m=1
    dt=0.1
    nSteps=10

    colorlist = [RED, GREEN, (0,0,255)]

    F_veclist=CalculateForce(x_veclist,attractor_veclist)

    #SIMULATION LOOP
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #DRAW SHIT
        DISPLAYSURF.fill(BACKGROUND)
        #PHYSICS
        x_veclist=CalculatePositions(x_veclist,v_veclist,F_veclist,dt,m)
        Fold_veclist=copy.deepcopy(F_veclist)
        F_veclist=CalculateForce(x_veclist,attractor_veclist)
        v_veclist=CalculateVelocities(v_veclist,Fold_veclist,F_veclist,dt,m)
        print(x_veclist,v_veclist,F_veclist)
        for i in range(len(x_veclist)):
            drawParticle(x_veclist[i],colorlist[i])
            drawAttractor(x_veclist[i],attractor_veclist[i])
        #FPSCLOCK.tick(FPS)
        pygame.display.update()
    

if __name__ == '__main__':
    main()
