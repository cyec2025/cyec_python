import pygame as p
from pygame.locals import *
import sys
import random as r

keyhold = {"kw":False,"ks":False,"kd":False,"ka":False}
crobek_ai = False
# class

class Enemy:
    def __init__(self,spr,pos):
        self.spr = spr
        self.pos = pos
        
    def rend(self):
        screen.blit(self.spr,self.pos)

    def move(self,target):
        if self.pos[0] < target[0]:
            self.pos[0] += 5
        elif self.pos[0] > target[0]:
            self.pos[0] -= 5
        if self.pos[1] < target[1]:
            self.pos[1] += 5
        elif self.pos[1] > target[1]:
            self.pos[1] -= 5
            
# basic systems
p.init()
p.display.set_caption("Rouge II")
screen = p.display.set_mode((1440,860))
pos = [620,420]

# assets
rouge_s = p.image.load("Rouge2/assets/rouge_s.png")
clockwork_s = p.image.load("Rouge2/assets/clockworkmap.png")
crobek_s = p.image.load("Rouge2/assets/crobek_s.png")
clockwork_m = p.mixer.music.load("Rouge2/assets/clockwork_r2.wav")

# colors
white = p.Color(255,255,255)
grey = p.Color(150,150,150)
darkred = p.Color(200,0,0)

# random sit
rougebox = p.Rect(pos[0],pos[1],100,100)
crobek = Enemy(crobek_s,[400,400])

clockwork_m
p.mixer.music.play(-1)

game = True
# loop
while game == True:
    
    for event in p.event.get():
        if event.type == QUIT:
            game = False
        if event.type == KEYDOWN:
            if event.key == K_w:
                keyhold["kw"] = True
            if event.key == K_s:
                keyhold["ks"] = True
            if event.key == K_a:
                keyhold["ka"] = True
            if event.key == K_d:
                keyhold["kd"] = True
            if event.key == K_i:
                crobek_ai = True
        if event.type == KEYUP:
            if event.key == K_w:
                keyhold["kw"] = False
            if event.key == K_s:
                keyhold["ks"] = False
            if event.key == K_a:
                keyhold["ka"] = False
            if event.key == K_d:
                keyhold["kd"] = False

    if keyhold["ka"] == True:
        pos[0] -= 10
    if keyhold["kd"] == True:
        pos[0] += 10
    if keyhold["kw"] == True:
        pos[1] -= 10
    if keyhold["ks"] == True:
        pos[1] += 10
    if crobek_ai == True:
        crobek.move(pos)
    screen.fill(white)
    screen.blit(clockwork_s,[0,0])
    rougebox = p.Rect(pos[0],pos[1],100,100)
    screen.blit(rouge_s,pos)
    crobek.rend()
    p.time.delay(25)
    p.display.update()
