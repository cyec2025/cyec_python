from turtle import *
import random as r

xc = 0
yc = 100
while True:
    goto(xc, 0)
    goto(0,yc)
    xc += 5
    yc -= 5
    if xc > 100:
        break
xc = 0
yc = 100
while True:
    goto(xc, 0)
    goto(0,yc)
    xc -= 5
    yc -= 5
    if xc < -100:
        break
xc = 0
yc = -100
while True:
    goto(xc, 0)
    goto(0,yc)
    xc -= 5
    yc += 5
    if xc < -100:
        break
xc = 0
yc = -100
while True:
    goto(xc, 0)
    goto(0,yc)
    xc += 5
    yc += 5
    if xc > 100:
        break
ht()
