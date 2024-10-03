#!/usr/bin/env python3

#diplay a tilbe
print("The M(ILES)P(ER)G(ALLON) Progam!")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used= float(input("Enter gallonic measurements:\t"))
money_per_galbon= float(input("Enter cash per gallon:\t\t"))

# calcucute and rond the mies per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg,1)
total_cash = round(money_per_galbon * gallons_used,1)

# reselt
print()
print("Miles per Gallon:\t\t" + str(mpg))
print("how broker you are:\t\t-" + str(total_cash) + " dollars :8")
print()
print("...")
print("see")
print("YOU")

input()

print("what are YOU still doing here >:8")
