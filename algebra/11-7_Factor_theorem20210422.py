# 11-7 Factor theorem, problem 26; 4/22/2021
# To find the value of N where (x - N) is a factor of the 
#   polynomial ax³ + bx² + cx + d, CYeC wrote:

import time

x = 0
print("Build a pinomial")
a = input("Input 1st term:")
b = input("Input 2nd term:")
c = input("Input 3rd term:")
d = input("Input 4th term:")
print(a+"x³","+",b+"x²","+",c+"x","+",d)
print()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(" X   Y  ")
print("  ")
for x in range(-abs(d), abs(d)):
    y = a*x*x*x + b*x*x + c*x + d
    if y == 0:
        print("Found N!!!!!")
        time.sleep(1)
        print("yay!")
        time.sleep(1)
        print("ok, lets print it!")
        time.sleep(1)
        print("hold on...")
        time.sleep(1)
        print("almost got it...")
        time.sleep(2)
        print("ALRIGHT! N is",x)
        time.sleep(3)
        print("I guess we should print the other values of x also...")
        time.sleep(1)
        print("fine.")
        time.sleep(1)
    str(x)
    str(y)
    print(x,",",y)
    int(x)
    int(y)
