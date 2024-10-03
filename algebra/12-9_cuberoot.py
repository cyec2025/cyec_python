#12-9 Exercise 63 in Foerster's Algebra: Cube Roots by Trial and Error
#Flow chart given, solution presented in Basic.  CYeC wrote in python 3.6:

N = int(input("put the number you wanna get cube root of: "))
R = 1
D = 1
while True:
    print("this dont work:",R)
    if R*R*R > N:
        R -= D
        if D < 0.01:
            print("your cube root is",R,"oh and btw your original num is",N)
            break
        else: D *= 0.1
    else: R += D
