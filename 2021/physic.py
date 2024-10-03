import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
x = height/2
y = width/2
xv = 5
yv = -5
max_yv = 50
screen = pygame.display.set_mode((width, height))

# Game loop.
while True:

    #physics 
    prev_x,prev_y = x,y
    xv = xv + (x - prev_x)
    yv = yv + (y - prev_y)
    if yv < max_yv or y < 500:
        yv += 1
    if y > 499:
        if yv > 0:
            yv = (yv * -1) / 2
        if yv < 1 and yv > -1:
            yv = 0
    if x > 625:
        if xv > 0:
            xv = (xv * -1) / 2
            x = 625
        else:
            x = 625
            xv = 0
    if x < 15:
        if xv < 0:
            xv = (xv * -1) / 2
            x = 0
        else:
            x = 15
    if yv == 0:
        if xv > 0:
            xv -= 1
        if xv < 0:
            xv += 1
    y += yv
    x += xv
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                xv += -10
                yv += -10
            if event.key == pygame.K_RIGHT:
                xv += 10
                yv += -10
            if event.key == pygame.K_UP:
                xv += -5
                yv += -20
            if event.key == pygame.K_DOWN:
                xv += 5
                yv += -20
  
    # Update.
  
    # Draw.
    pygame.draw.rect(screen,(100,100,100),pygame.Rect((0,515),(640,150)))
    pygame.draw.circle(screen,(255,0,0),(x,y),15)
    pygame.display.flip()
    fpsClock.tick(fps)
