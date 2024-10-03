import math

while True:
    print("Note: if you get a 'math domain error', you've probably got a non-real number")
    a = float(input("A:"))
    b = float(input("B:"))
    c = float(input("C:"))


    yea = input("want the positive x? (yes, no):")
    if yea == "yes":
        x = (-b + (math.sqrt((b**2) - (4*a*c)))) / 2*a

        print("positive x:",x)

    yea = input("want the negative x? (yes, no):")
    if yea == "yes":
        x = (-b - (math.sqrt((b**2) - (4*a*c)))) / 2*a

        print("negative x:",x)
    print()
    input("next")
