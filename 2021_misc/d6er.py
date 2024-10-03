import random as r
import turtle as t


ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
roll = 0
times_rolled = 0

while times_rolled < 30:
    roll = r.randint(1,6)
    if roll == 1:
        ones += 1
    elif roll == 2:
        twos += 1
    elif roll == 3:
        threes += 1
    elif roll == 4:
        fours += 1
    elif roll == 5:
        fives += 1
    elif roll == 6:
        sixes += 1
    times_rolled += 1
t.pensize(3)
t.ht()
t.left(90)
t.fd(10*ones)
t.bk(10*ones)
t.right(90)
t.forward(30)
t.left(90)
t.fd(10*twos)
t.bk(10*twos)
t.right(90)
t.forward(30)
t.left(90)
t.fd(10*threes)
t.bk(10*threes)
t.right(90)
t.forward(30)
t.left(90)
t.fd(10*fours)
t.bk(10*fours)
t.right(90)
t.forward(30)
t.left(90)
t.fd(10*fives)
t.bk(10*fives)
t.right(90)
t.forward(30)
t.left(90)
t.fd(10*sixes)
t.bk(10*sixes)
t.right(90)
t.forward(30)
t.left(90)

fgrefrgfdsw = 10

while fgrefrgfdsw > 0:
    t.color('red')
    t.forward(10)
    t.color('yellow')
    t.forward(10)
    fgrefrgfdsw -= 1
