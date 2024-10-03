import pygame as p
from pygame.locals import *
import sys
p.init()

win = [800,800]
p.display.set_caption("Sock Game Version 2")
scream = p.display.set_mode(win)
font = p.font.Font('freesansbold.ttf', 32)
points = 0
blue = p.Color(0,0,255)
white = p.Color(255,255,255)
peri = p.Color(200,180,230)
purp = p.Color(220,120,220)
x = 200
y = 200
xv = 0
yv = 0
scream.fill(white)
p_img = p.image.load('my first pygame/silly pygame.png')
p_box = p.Rect(x,y,p_img.get_width()/2,p_img.get_height())
t_box = p.Rect(200,400,100,100)
friction = 0.5
speed = 1
jump_force = 25
max_xvel = 10
max_yvel = 40
while True:
    print(points)
    p.time.delay(25)
    p.display.update()
    scream.fill(white)
    scream.blit(p_img,(x-40,y))
    p_box.x = x
    p_box.y = y
    if p_box.colliderect(t_box):
        p.draw.rect(scream,peri,t_box)
        if pointing == 0:
            points += 1
            pointing = 1
            
    else:
        pointing = 0
        p.draw.rect(scream,purp,t_box)
    if xv < 0:
        xv += friction
    elif xv > 0:
        xv -= friction
    if yv < 0:
        yv += friction/2
    elif yv > 0:
        yv -= friction/2
    
    for event in p.event.get():
        if event.type == QUIT:
            p.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if y == win[1]-160:
                    yv += -jump_force
    keys = p.key.get_pressed()
    if keys[p.K_LEFT]:
        if xv >= -max_xvel:
            xv += -speed
    if keys[p.K_RIGHT]:
        if xv <= max_xvel:
            xv += speed

    x += xv
    y += yv

    if y < win[1]-160 and yv <= max_yvel:
        yv += 1
    elif y > win[1]-160:
        y = win[1]-160
        yv = 0

    #p.draw.circle(scream, blue, (x,y), 30)
