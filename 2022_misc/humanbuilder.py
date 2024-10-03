from random import *


fnames = ["gregory","winona","kevin","eren","armin","mikasa","levi","erwin","charlie","dan","ryan","aidan","ethan","tess","lila","owen","caitlin"]
lnames = ["harrison","middleton","jaeger","arlet","ackerman","hart","trimbleton","breightenbecher"]
colors = ["black","red","blue","yellow","orange","WHY???","NOOO!!!!","OH GOD!","grass..."]
jobs = ["carpenter","office worker","car washer","civil engineer","composer","garbage truck driver","salesperson","fisherperson"]

class human:
    def stats(self):
        print("NAME: ",self.fname,self.lname)
        print("FAVORITE COLOR: ",self.fcolor)
        print("AGE: ",self.age)
        print("JOB: ",self.job)
    def __init__(self,fname,lname,fcolor,age,job):
        self.fname = fname
        self.lname = lname
        self.fcolor = fcolor
        self.age = age
        self.job = job


def main():
    my_human = human(choice(fnames),choice(lnames),choice(colors),str(randint(17,75)),choice(jobs))
    my_human.stats()

main()

