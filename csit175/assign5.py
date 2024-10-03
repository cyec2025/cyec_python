### Assignment 5: Imports
### Author: CYeC
### Date: 2022-03-13

import math as m
from turtle import *
import random as r

colors = ['#fce7e6','#f6c492','#fabab5','#b5d0d4','#a2c794']
width(3)

def main():
    petals(100,4,6.28)
    center()

def petals(a,n,end):
    t=0
    #draw the petals 
    begin_fill()
    while t<end:
         color(r.choice(colors))
         x=a*m.sin(t*n)*m.cos(t)
         y=a*m.sin(t*n)*m.sin(t)
         goto(x,y)
         t=t+0.02
    end_fill()

def center():
    #draw three circles for the middle of the flower 
    color(r.choice(colors))
    for i in range(3):
        circle(5+5*i)
        up()
        setpos(0,-(5+5*i))
        down()

main()
