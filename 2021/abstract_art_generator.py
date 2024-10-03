from turtle import *
from random import randint

colormode(255)
color(randint(0,255),randint(0,255),randint(0,255))
fillcolor(randint(0,255),randint(0,255),randint(0,255))
begin_fill()
#startx = randint(-200,200)
#starty = randint(-200,200)
#goto(startx,starty)
force_armin = 1
if force_armin == 0:
    mikasa = input("armin form? (y/n):")
elif force_armin == 2:
    mikasa = "n"
else: mikasa = "y"
zimbabwe = randint(2,10)
for kenya in range(zimbabwe):
    if mikasa == "y":
        armin = randint(1,8)
        if armin == 8:
            end_fill()
            up()
            goto(randint(-200,200),randint(-200,200))
            down()
            begin_fill()
    if randint(0,5) == 1:
        erwin = randint(1,20)
        levi = randint(1,20)
        eren = randint(1,2)
        for india in range(randint(15,30)):
            if eren == 1:
                left(levi)
            else: right(levi)
            forward(erwin)
                           
    else: goto(randint(-200,200),randint(-200,200))
goto(0,0)
end_fill()
ht()
#goto(startx,starty)

