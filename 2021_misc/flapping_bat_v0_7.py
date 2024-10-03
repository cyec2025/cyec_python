import pygame as p
from pygame.locals import *
import sys
import random as r
import time
import os

# basic
p.init()
p.display.set_caption("Flapping Bat Version 0.7")
screan = p.display.set_mode((600,600))
pos = [50,300]
velocity = -20
max_vel = 20
flap_anim = 0
menu_anim = 0
clock = p.time.Clock()
living = 2
bg_scroll = 0
moon_scroll = 300
spacing = 300
min_size = 50
startery = 1
score = 0
levi = 0
music = 1
with open("Flapping Bat/secrets/highscore.txt", 'r') as hs_g:
    if os.stat("Flapping Bat/secrets/highscore.txt").st_size == 0:
        highscore = 0
    else:
        highscore = (hs_g.read())
# colors

white = p.Color(255,255,255)
hitbox = p.Color(200,200,200)
red = p.Color(120,0,0)
night = p.Color(50,55,80)
black = p.Color(0,0,0)
ob_color = p.Color(r.randint(0,255),r.randint(0,255),r.randint(0,255))

# objects

font = p.font.SysFont("monospace", 40)
scoring = font.render("zam", 1, (255,255,100))
p_f1 = p.image.load("Flapping Bat/assets/flapbat1.png")
p_f2 = p.image.load("Flapping Bat/assets/flapbat2.png")
bg = p.image.load("Flapping Bat/assets/flappingbatground.png")
menu1 = p.image.load("Flapping Bat/assets/menu1.png")
menu2 = p.image.load("Flapping Bat/assets/menu2.png")
moon = p.image.load("Flapping Bat/assets/moon.png")
ob_bg = p.image.load("Flapping Bat/assets/ob_bg.png")
ob_fg = p.image.load("Flapping Bat/assets/ob_fg.png")
death_sound = p.mixer.Sound("Flapping Bat/assets/death.wav")
score_sound = p.mixer.Sound("Flapping Bat/assets/points.wav")
p.mixer.music.load("Flapping Bat/assets/menu_theme.wav")
p_box = p.Rect(pos[0],pos[1],24,24)
ob_box1 = p.Rect(0,0,96,600)
ob_box2 = p.Rect(0,0,96,600)
ob_x = 600
ob_y1 = r.randint(-600,-100)
ob_y2 = ob_y1 + r.randint(600+min_size+int((spacing/2)),600+min_size+spacing)
# on start
screan.fill(white)
p.mixer.music.play(-1)
# full loop
while True:
    p.time.delay(25)
    p.display.update()
    # events
    for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    living = 1
                    pos = [50,300]
                    velocity = -20
                    bg_scroll = 0
                    moon_scroll = 300
                    spacing = 300
                    min_size = 50
                    startery = 1
                    score = 0
                    ob_box1 = p.Rect(0,0,96,600)
                    ob_box2 = p.Rect(0,0,96,600)
                    ob_x = 600
                    ob_y1 = r.randint(-600,-100)
                    ob_y2 = ob_y1 + r.randint(600+min_size+int((spacing/2)),600+min_size+spacing)
                    levi = 0
                if event.key == K_MINUS:
                    p.mixer.music.fadeout(500)
                if event.key == K_EQUALS:
                    p.mixer.music.play(-1)
    #rendring
    if menu_anim == 1:
        screan.blit(menu1,(0,0))
        menu_anim = 0
    elif menu_anim == 0:
        screan.blit(menu2,(0,0))
        menu_anim = 1
    
    # main loope

    while living == 1:
        if startery == 1:
            startery = 0
            p.mixer.music.fadeout(500)
            p.mixer.music.load("Flapping Bat/assets/game_forest.wav")
            p.mixer.music.play(-1)
        # events
        for event in p.event.get():
            if event.type == QUIT:
                p.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    velocity = -10
                    flap_anim = 5
                if event.key == K_MINUS:
                    p.mixer.music.fadeout(500)
                if event.key == K_EQUALS:
                    p.mixer.music.play(-1)
        # basic loop stuff
        clock.tick(60)
        p.time.delay(25)
        ob_x -= 10
        ob_box1.x = ob_x
        ob_box2.x = ob_x
        ob_box1.y = ob_y1
        ob_box2.y = ob_y2
        p.display.update()
        velocity += 1
        p_box.x = pos[0]+8
        p_box.y = pos[1]+8
        bg_scroll -= 1
        moon_scroll -= 0.25
        # collisions
        if p_box.colliderect(ob_box1) or p_box.colliderect(ob_box2):
            living = 0
        if ob_box1.x == 50:
            score += 1
            score_sound.play()
        # rendering
        screan.fill(night)
        screan.blit(bg,(bg_scroll,0))
        screan.blit(bg,(bg_scroll+600,0))
        screan.blit(moon,(moon_scroll,80))
        screan.blit(ob_bg,(ob_x,0))
        if flap_anim > 0:
            screan.blit(p_f2,pos)
        else: screan.blit(p_f1,pos)
        p.draw.rect(screan,ob_color,ob_box1)
        p.draw.rect(screan,ob_color,ob_box2)
        screan.blit(ob_fg,(ob_x,ob_y1))
        screan.blit(ob_fg,(ob_x,ob_y2))
        scoring = font.render(str(score), 1, (255,255,100))
        screan.blit(scoring,(20,20))
        # end of loop stuff
        pos[1] += velocity
        flap_anim -= 1
        if ob_x < -300:
            if spacing > 0:
                spacing -= r.randint(1,10)
            ob_box1 = p.Rect(0,0,96,600)
            ob_box2 = p.Rect(0,0,96,600)
            ob_x = 600
            ob_y1 = r.randint(-600,-100)
            ob_y2 = ob_y1 + r.randint(600+min_size+int((spacing/2)),600+min_size+spacing)
        if bg_scroll < -600:
            bg_scroll = 0
        if moon_scroll < -24:
            moon_scroll = 600
        if pos[1] > 650 or pos[1] < -24:
            living = 0
        if living == 0:
            p.mixer.music.fadeout(500)
            time.sleep(1)
            velocity = -20
            while pos[1] < 1000 or levi == 0:
                for event in p.event.get():
                    if event.type == QUIT:
                        p.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            if pos[1] > 1000:
                                levi = 1
                screan.fill(black)
                screan.blit(p_f2,pos)
                font = p.font.SysFont("monospace", 80)
                scoring = font.render(str(score), 1, (255,255,100))
                screan.blit(scoring,(260,260))
                font = p.font.SysFont("monospace", 40)
                screan.blit(font.render("Final Score",1,(255,255,100)),(150,200))
                screan.blit(font.render("High Score",1,(255,255,100)),(150,400))
                font = p.font.SysFont("monospace", 80)
                if int(highscore) < score:
                    highscore = score
                    with open("Flapping Bat/secrets/highscore.txt", 'w') as hs_c:
                        hs_c.write(str(highscore))
                scoring = font.render(str(highscore), 1, (255,255,100))
                screan.blit(scoring,(260,450))
                font = p.font.SysFont("monospace", 40)
                velocity += 1
                pos[1] += velocity
                p.time.delay(25)
                p.display.update()
            living = 2
            break

    
    
