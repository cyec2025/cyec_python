#!/usr/bin/env python3

# Assignment 1: Tip Calculator
# Author: CYeC
# Date: 2022-02-11




print("Tip Calculator")
print()
print()

# user input

meal_cost = float(input("Cost of meal:\t"))
tip_percent = float(input("Tip percent:\t"))

# calculations

tip = meal_cost * (tip_percent/100)
total_cost = meal_cost + tip

# result

print()
print("Tip amount:\t$",round(tip,2))
print("Total amount:\t$",round(total_cost,2))





























