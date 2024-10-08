#!usr\bin\env python3

# Assignment 4: Foot/Meter Converter
# Author: CYeC
# Date: 2022-03-07


feet = 0
meters = 0

def title():
    print("Foot and Meter Converter\n")

def main():
    title()
    menu()

def menu():
    
    menu = ""
    while menu.lower() != "a" or menu.lower() != "b":
        print("\nPick one.\n\nA. Feet to meters.\n\nB. Meters to feet.\n\n")
        menu = input("(a/b/quit):")
        if menu.lower() == "a":
            feet = float(input("\nInput feet: "))
            ftm(feet)
        elif menu.lower() == "b":
            meters = float(input("\nInput meters: "))
            mtf(meters)
        elif menu.lower() == "q" or menu.lower() == "quit":
            print("Closing...")
            menu = ""
            break
        else:
            print("please choice something better")

def mtf(meters):
    feet = meters / .3048
    print("Feet:",round(feet,2))
def ftm(feet):
    meters = feet * .3048
    print("Meters:",round(meters,2))


main()
