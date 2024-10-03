from turtle import *
from random import randint

colormode(255)
color(randint(0,255),randint(0,255),randint(0,255))
fillcolor(randint(0,255),randint(0,255),randint(0,255))
begin_fill()
#startx = randint(-200,200)
#starty = randint(-200,200)
#goto(startx,starty)

zimbabwe = randint(2,10)
for kenya in range(zimbabwe):
    goto(randint(-200,200),randint(-200,200))
goto(0,0)
end_fill()
#goto(startx,starty)

